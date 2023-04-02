import tkinter as tk
import cv2
import PIL.Image
import PIL.ImageTk
from string import ascii_uppercase
from keras.models import model_from_json
import operator


class App:
    def __init__(self, window):
        self.is_on = True
        # load the trained convolutional neural network and the label binarizer
        self.directory = "model/"
        self.vid = cv2.VideoCapture(0)
        self.current_image = None  # current image from the camera
        self.current_image2 = None  # current image from the camera

        # load json and create model

        self.json_file = open(self.directory+"model-bw-alpha.json", "r")
        self.model_json = self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.model_json)
        self.loaded_model.load_weights(self.directory+"model-bw-alpha.h5")

        self.json_file_num = open(self.directory+"model-bw-digit.json", "r")
        self.model_json_num = self.json_file_num.read()
        self.json_file_num.close()
        self.loaded_model_num = model_from_json(self.model_json_num)
        self.loaded_model_num.load_weights(self.directory+"model-bw-digit.h5")

        self.ct = {}  # dictionary to store the count of each gesture
        self.ct['blank'] = 0  # count of the blank gesture
        self.blank_flag = 0  # flag to check if the blank gesture has been detected
        for i in range(10):
            self.ct[str(i)] = 0
        for i in ascii_uppercase:
            self.ct[i] = 0
        print("Loaded model from disk")

        self.root = window
        self.root.title("Sign language to Text Converter")

        # close the window
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("800x700")  # set window size
        root.configure(background='#26242f')

        # create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT), bg="#26242f")
        self.canvas.pack()

        self.T1 = tk.Label(self.root)
        self.T1.place(x=10, y=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)+20)
        self.T1.config(text="Character :", font=(
            "Courier", 20, "bold"), bg="#26242f", fg="white")

        self.panel = tk.Label(self.root)  # Current SYmbol
        self.panel.place(x=220, y=self.vid.get(
            cv2.CAP_PROP_FRAME_HEIGHT)+20)

        self.T2 = tk.Label(self.root)
        self.T2.place(x=10, y=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)+60)
        self.T2.config(text="Word :", font=(
            "Courier", 20, "bold"), bg="#26242f", fg="white")

        self.panel2 = tk.Label(self.root)  # Word in text
        self.panel2.place(x=120, y=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)+60)

        self.T3 = tk.Label(self.root)
        self.T3.place(x=10, y=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)+100)
        self.T3.config(text="Sentence :", font=(
            "Courier", 20, "bold"), bg="#26242f", fg="white")

        self.panel3 = tk.Label(self.root)  # Sentence in text
        self.panel3.place(x=220, y=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)+100)

        self.btcall = tk.Button(
            self.root, command=self.switch, height=0, width=0)
        self.btcall.config(text="Alphabets Recoginition", font=(
            "Courier", 14), bg="#26242f", fg="white")
        self.btcall.place(x=10, y=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)+150)

        self.btn = tk.Button(
            self.root, command=lambda: AboutPage(root), height=0, width=0)
        self.btn.config(text="About", font=(
            "Courier", 14), bg="#26242f", fg="white")
        self.btn.place(x=300, y=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)+150)

        self.str = ""
        self.word = ""
        self.current_symbol = "Empty"
        self.photo = "Empty"
        # start the video playback process
        self.video()

        # bind key events
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def video(self):
        # get a frame from the video source
        ret, frame = self.vid.read()

        if ret:
            # convert the frame to a PIL ImageTk format and display it on the canvas
            cv2image = cv2.flip(frame, 1)
            x1 = int(0.5*frame.shape[1])
            y1 = 10
            x2 = frame.shape[1]-10
            y2 = int(0.5*frame.shape[1])
            cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255, 0, 0), 1)
            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
            self.current_image = PIL.Image.fromarray(cv2image)
            self.imgtk = PIL.ImageTk.PhotoImage(image=self.current_image)

            cv2image = cv2image[y1:y2, x1:x2]
            gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 2)
            th3 = cv2.adaptiveThreshold(
                blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            res = cv2.threshold(
                th3, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            if self.is_on:
                self.predicting_alpha(res)
            else:
                self.predicting_num(res)

            self.current_image2 = PIL.Image.fromarray(res)
            self.imgtk1 = PIL.ImageTk.PhotoImage(image=self.current_image2)

            self.panel.config(text=self.current_symbol, font=(
                "Ariel", 20), bg="#26242f", fg="white")
            self.panel2.config(text=self.word, font=(
                "Courier", 20), bg="#26242f", fg="white")
            self.panel3.config(text=self.str, font=(
                "Courier", 20), bg="#26242f", fg="white")

            self.canvas.create_image(0, 0, image=self.imgtk, anchor=tk.NW)
            self.canvas.create_image(x1, y1, image=self.imgtk1, anchor=tk.NW)
            self.canvas.create_rectangle(
                x1, y1, x2, y2, outline='#26242f', width=4)

        # call the same function after 30 milliseconds
        self.root.after(30, self.video)

    def predicting_alpha(self, test_image):
        test_image = cv2.resize(test_image, (128, 128))
        result = self.loaded_model.predict(test_image.reshape(1, 128, 128, 1))
        prediction = {}
        prediction['blank'] = result[0][0]
        inde = 1
        for i in ascii_uppercase:
            prediction[i] = result[0][inde]
            inde += 1
        # LAYER 1
        prediction = sorted(prediction.items(),
                            key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]

        if (self.current_symbol == 'blank'):
            for i in ascii_uppercase:
                self.ct[i] = 0
        self.ct[self.current_symbol] += 1
        if (self.ct[self.current_symbol] > 60):
            for i in ascii_uppercase:
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 20:
                    self.ct['blank'] = 0
                    for i in ascii_uppercase:
                        self.ct[i] = 0
                    return
            self.ct['blank'] = 0
            for i in ascii_uppercase:
                self.ct[i] = 0
            if self.current_symbol == 'blank':
                if self.blank_flag == 0:
                    self.blank_flag = 1
                    if len(self.str) > 0:
                        self.str += " "
                    self.str += self.word
                    self.word = ""
            else:
                if (len(self.str) > 16):
                    self.str = ""
                self.blank_flag = 0
                self.word += self.current_symbol

    def predicting_num(self, test_image):
        test_image = cv2.resize(test_image, (128, 128))
        result = self.loaded_model.predict(test_image.reshape(1, 128, 128, 1))
        prediction = {}
        prediction['blank'] = result[0][10]
        inde = 0
        for i in range(10):
            prediction[str(i)] = result[0][inde]
            inde += 1
        # LAYER 1
        prediction = sorted(prediction.items(),
                            key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]

        if (self.current_symbol == 'blank'):
            for i in range(10):
                self.ct[str(i)] = 0
        self.ct[self.current_symbol] += 1
        if (self.ct[self.current_symbol] > 60):
            for i in ascii_uppercase:
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 20:
                    self.ct['blank'] = 0
                    for i in range(10):
                        self.ct[str(i)] = 0
                    return
            self.ct['blank'] = 0
            for i in range(10):
                self.ct[str(i)] = 0
            if self.current_symbol == 'blank':
                if self.blank_flag == 0:
                    self.blank_flag = 1
                    if len(self.str) > 0:
                        self.str += " "
                    self.str += self.word
                    self.word = ""
            else:
                if (len(self.str) > 16):
                    self.str = ""
                self.blank_flag = 0
                self.word += self.current_symbol

    def switch(self):
        if (self.is_on):
            self.is_on = False
            self.btcall.config(text="Number Recognition")

        else:
            self.is_on = True
            self.btcall.config(text="Alphabet Recognition")

    def destructor(self):
        print("Closing Application...")
        self.root.destroy()
        self.vid.release()
        cv2.destroyAllWindows()


class AboutPage:
    def __init__(self, master):
        self.master = master

        # Create a new window for the about page
        self.top = tk.Toplevel(master)
        self.top.title("About")
        self.top.protocol('WM_DELETE_WINDOW', self.destructor1)
        self.top.geometry("800x750")
        self.top.configure(background="#26242f")

        self.tx = tk.Label(self.top)

        self.tx.config(text="Efforts By",
                       font=("Courier", 30, "bold"), bg="#26242f", fg="white")

        self.tx.grid(row=0, column=1, padx=25, pady=10)

        # # Create a list of team member names and image file paths
        team_members = [
            {'name': 'Mayank\nRA201100303002',
                'photo': "Sign Language Recognition/About/test.png"},
            {'name': 'Mohit\nRA201100303019',
                'photo': "Sign Language Recognition/About/test.png"},
            {'name': 'Muskan\nRA201100303002',
                'photo': "Sign Language Recognition/About/test.png"}
        ]

        # # Load the images and create a list of photo objects
        self.photos = []
        for member in team_members:
            img = PIL.Image.open(member['photo'])
            img = img.resize((200, 200))
            photo = PIL.ImageTk.PhotoImage(img)
            self.photos.append(photo)

        # # Create a grid to place the team members in
        for i, member in enumerate(team_members):
            # Create a canvas for the photo
            canvas = tk.Canvas(self.top, width=200, height=200)
            canvas.create_image(0, 0, anchor='nw', image=self.photos[i])
            canvas.grid(row=1, column=i, padx=25, pady=10)

            # Create a label for the name
            self.name_label = tk.Label(
                self.top, text=member['name'], font=('Arial', 14), bg="#26242f", fg="white")
            self.name_label.grid(row=2, column=i, padx=25, pady=10)

        self.mentor = tk.Label(self.top)
        self.mentor.config(text="Under the supervision of", font=(
            "Courier", 30, "bold"), bg="#26242f", fg="white")
        self.mentor.grid(row=3, column=0, padx=25, pady=10, columnspan=3)

        img1 = PIL.Image.open("Sign Language Recognition/About/test.png")
        img1 = img1.resize((200, 200))
        self.mentor = PIL.ImageTk.PhotoImage(img1)

        canvas = tk.Canvas(self.top, width=200, height=200)
        canvas.create_image(0, 0, anchor='nw', image=self.mentor)
        canvas.grid(row=4, column=1, padx=25, pady=10)

        self.mentor_label = tk.Label(
            self.top, text="Shivani Tyagi", font=('Arial', 14), bg="#26242f", fg="white")
        self.mentor_label.grid(row=5, column=1, padx=25, pady=10)

    def destructor1(self):
        # Destroy the about page
        self.top.destroy()


# create the GUI window and start the app
print("Starting Application...")
root = tk.Tk()
app = App(root)
root.mainloop()
