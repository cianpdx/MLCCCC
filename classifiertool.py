# previews each image in directory, user presses button, image is copied into the sub folder

root = Tk()
root.title("Image Classifier")
root.geometry("700x700")

def choose_0():


    directory0 = r"chicken_photos_sub\0\zero"
    os.rename(os.path.join(directory, photo_file), directory0 + photo_file)
    label.grid_forget()
    showing_image()
    return

def choose_1():


    directory1 = r"chicken_photos_sub\1\one"
    os.rename(os.path.join(directory, photo_file), directory1 + photo_file)
    label.grid_forget()
    showing_image()
    return

def choose_2():


    directory2 = r"""chicken_photos_sub\2\two"""
    os.rename(os.path.join(directory, photo_file), directory2 + photo_file)
    label.grid_forget()
    showing_image()
    return

def choose_3():


    directory3 = r"""chicken_photos_sub\3\three"""
    os.rename(os.path.join(directory, photo_file), directory3 + photo_file)
    label.grid_forget()
    showing_image()
    return

directory = "chicken_photos_sub"

def showing_image():
    global label
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") and filename.startswith("2020"):
            global photo_file
            photo_file = filename
            image_no_1 = ImageTk.PhotoImage(Image.open(os.path.join(directory, filename)))
            label = Label(image=image_no_1)
            label.grid(row=3, column=0, columnspan=4)
            button_0 = Button(root, text="0", command=choose_0)
            button_0.grid(row=5, column=0)
            button_1 = Button(root, text="1", command=choose_1)
            button_1.grid(row=5, column=1)
            button_2 = Button(root, text="2", command=choose_2)
            button_2.grid(row=5, column=2)
            button_3 = Button(root, text="3", command=choose_3)
            button_3.grid(row=5, column=3)
            root.mainloop()
            continue
        else:
            continue

showing_image()