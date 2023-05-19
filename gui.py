import main
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
filepath = None

def browseFiles():
    print("abc")
    global filepath
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=[("Supported Files",
                                                      "*.mp4"), ("Supported Files",
                                                      "*.avi"),
                                                     ("experimental",
                                                      "*")])
    filepath = filename
    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


def trackProgress(percent):
    print(f'Dies ist das Percent: {percent}')
    print(f'Dies ist das pBar: {pBar["value"]}')
    if pBar['value'] < 100:
        #print("Hello")
        pBar['value'] = float(percent)
        pLabel['text'] = f'{percent}% processed'
        window.update()


def startBlur():
    main.blurVideo("./input/video.mp4")


# Create the root window
window = Tk()
window.title('File Explorer')
window.geometry("500x500")
window.config(background="#121212")

window.option_add("*Background", "#1e1e1e")

label_file_explorer = Label(window,
                            text="Select a File to blur",
                            width=50, height=4,
                            fg="white")

button_browse = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_blur = Button(window,
                     text="Blur Video",
                     command=lambda: startBlur())

button_exit = Button(window,
                     text="Exit",
                     command=exit)

pLabel = Label(window,
                text="",
                fg="white")
pBar = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='determinate',
    length=280
)

label_file_explorer.grid(column=0, row=1)

button_browse.grid(column=0, row=2)

button_blur.grid(column=0, row=3)

button_exit.grid(column=0, row=4)

pBar.grid(column=0, row=5, columnspan=2, padx=10, pady=20)

pLabel.grid(column=1, row=5, columnspan=2, padx=10, pady=20)


# Let the window wait for any events
window.mainloop()