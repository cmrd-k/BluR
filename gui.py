import tkinter as tk
import tkinter.filedialog as filedialog
import os

# Define the functions for handling drag and drop events
def on_drag_enter(event):
    file_frame.configure(bg='light blue')

def on_drag_leave(event):
    file_frame.configure(bg='white')

def on_drag_over(event):
    file_frame.configure(bg='light blue')

def on_drop(event):
    file_path = event.data['text']
    if os.path.isfile(file_path):
        print("Selected file:", file_path)
    else:
        print("Not a valid file")

def on_click(event):
    file_path = filedialog.askopenfilename()
    if os.path.isfile(file_path):
        print("Selected file:", file_path)
    else:
        print("Not a valid file")

# Create the GUI window
root = tk.Tk()
root.title("File Selector")

# Create a select input and a button to execute a test function
select_label = tk.Label(root, text="Select an option:")
select_label.grid(row=0, column=0, padx=10, pady=10)

select_input = tk.Entry(root)
select_input.grid(row=0, column=1, padx=10, pady=10)

test_button = tk.Button(root, text="Test", command=lambda: print("Test function executed"))
test_button.grid(row=0, column=2, padx=10, pady=10)

# Create a drag and drop area for selecting a file
file_frame = tk.Frame(root, width=300, height=200, bd=2, relief=tk.SUNKEN)
file_frame.grid(row=2, column=0, padx=10, pady=10)
file_frame.grid_propagate(False)

file_text = tk.Label(file_frame, text="Drop files here")
file_text.pack(expand=True)

# Bind the drag and drop events
file_frame.bind("<<Enter>>", on_drag_enter)
file_frame.bind("<<Leave>>", on_drag_leave)
file_frame.bind("<<Motion>>", on_drag_over)
file_frame.bind("<<Drop>>", on_drop)
file_frame.bind("<<Button-1>>", on_click)

# Enable drag and drop on the window
root.attributes('-type', 'dock')
root.tk.call('tk', 'windowingsystem')


# Run the main loop
root.mainloop()