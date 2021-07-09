import json
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, SaveAs

# initialize application
root = Tk()
root.geometry('+%d+%d' % (450, 800))


class App:
    def __init__(self, content, start_button, intro_textbox_obj, img):
        self.content = content
        self.start_button = start_button
        self.intro_textbox_obj = intro_textbox_obj
        self.img = img

    def canvas(self):
        # set up canvas
        content = Canvas(root, width=150, height=100, bg="#EEEEEE")
        content.grid(padx=15, pady=15)

    def start(self):
        self.canvas()

        # row 0
        start_button_text = StringVar()
        start_button = Button(root, textvariable=start_button_text, command=self.open)
        start_button_text.set("Start")
        start_button.grid(row=0, column=0)

        intro_text = "Personalize images by adding your own overlays and/or text.\n\n" \
                     "Upload your own images.\nSave your new overlayed image " \
                     "straight to your computer!\n\n" \
                     "Select the Start!"
        intro_textbox_obj = Label(root, text=intro_text, padx=10, pady=10)
        intro_textbox_obj.grid(row=0, column=1)

    def image_ratio_calculator(self):
        pass

    def open(self):
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
            background_img_label.grid(rowspan=3, row=0, column=1)

            # Change Image button
            change_image_button_text = StringVar()
            change_image_button = Button(root, textvariable=change_image_button_text)
            change_image_button_text.set("Change Image")
            change_image_button.grid(row=0, column=0)

            # Add Customizations button
            add_customization_button_text = StringVar()
            add_customization_button = Button(root, textvariable=add_customization_button_text)
            add_customization_button_text.set("Add Customizations")
            add_customization_button.grid(row=1, column=0)

            # Download Image button
            download_image_button_text = StringVar()
            download_image_button = Button(root, textvariable=download_image_button_text)
            download_image_button_text.set("Download Image")
            download_image_button.grid(row=2, column=0)

    # def resize_image(self):
    #     width, height = int(self.img.size[0]), int(self.img.size[1])
    #     if width > height:
    #         height = int((height * 600) / width)
    #         width = 600
    #     elif height > width:
    #         height = int((height * 550) / width)
    #         width = 550
    #     else:
    #         width, height = 550, 550
    #
    #     img = self.img.resize((width, height))
    #     return img


    # def save(self):
    #     filename = SaveAs(parent=root, filetypes=[('png images', '*.png'),
    #                                                 ('jpeg images', '*.jpeg'),
    #                                                 ('jpg images', '*.jpg')])
    #
    #     saved_file = filename.show()
    #     saved_file()



App().start()
root.mainloop()
