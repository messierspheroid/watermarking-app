from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, asksaveasfilename

# initialize application
root = Tk()
root.geometry('+%d+%d' % (450, 800))


class App:

    def __init__(self):
        pass

    def canvas(self):
        # set up canvas
        self.content = Canvas(root, width=150, height=100, bg="#EEEEEE")
        self.content.grid(row=0, padx=15, pady=15)

    def start(self):
        self.canvas()
        # row 0
        start_button_text = StringVar()
        self.start_button = Button(root, textvariable=start_button_text, command=self.open)
        start_button_text.set("Start")
        self.start_button.grid(row=0, column=0)

        intro_text = "Personalize images by adding your own overlays and/or text.\n\n" \
                     "Upload your own images.\nSave your new overlayed image " \
                     "straight to your computer!\n\n" \
                     "Select the Start!"
        self.intro_textbox_obj = Label(root, text=intro_text, padx=10, pady=10)
        self.intro_textbox_obj.grid(row=0, column=1)

    def image_ratio_calculator(self):
        pass

    def open(self):
        self.canvas()

        img = Image.open(askopenfile(parent=root, mode="rb", title="Choose a file",
                                     filetype=[('png images', '*.png'),
                                               ('jpeg images', '*.jpeg'),
                                               ('jpg images', '*.jpg')]))

        if img:
            self.start_button.destroy()
            self.intro_textbox_obj.destroy()

            img_resize = img.resize(size=(600, 381))
            background = ImageTk.PhotoImage(img_resize)
            background_img_label = Label(root, padx=15, pady=15, image=background)
            background_img_label.image = background
            background_img_label.grid(columnspan=1, row=0, column=1)

            # Change Image button
            change_image_button_text = StringVar()
            change_image_button = Button(root, textvariable=change_image_button_text, command=self.start)
            change_image_button_text.set("Change Image")
            change_image_button.grid(row=0, column=0, sticky=N)

            # Add Customizations button
            add_customization_button_text = StringVar()
            add_customization_button = Button(root, textvariable=add_customization_button_text)
            add_customization_button_text.set("Add Customizations")
            add_customization_button.grid(row=0, column=0)

            # Download Image button
            download_image_button_text = StringVar()
            download_image_button = Button(root, textvariable=download_image_button_text)
            download_image_button_text.set("Download Image")
            download_image_button.grid(row=0, column=0, sticky=S)

    def save(self):
        asksaveasfilename(root, )


App().start()
root.mainloop()
