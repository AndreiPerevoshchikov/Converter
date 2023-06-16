import json  # Importing the JSON module for working with JSON data
from customtkinter import *  # Importing customtkinter library for customized Tkinter widgets
from customtkinter import filedialog as fd  # Importing the filedialog module from customtkinter library
import pathlib  # Importing the pathlib module for working with file paths
from PIL import Image, ImageTk  # Importing the Image and ImageTk modules from PIL (Python Imaging Library)
from itertools import count, cycle  # Importing count and cycle functions from itertools module
import os  # Importing the os module for interacting with the operating system
import pandas as pd  # Importing the pandas library for working with data in CSV format

# Defining a custom class ImageLabel that inherits from CTkLabel (customized Label widget)
class ImageLabel(CTkLabel):
    def load(self, im):
        """
        Loads and displays an animated image in the Label widget.

        Parameters:
            im (str): The path to the image.
        """
        im = Image.open(im)  # Open the image using PIL
        frames = []  # List to store individual frames of the animated image

        try:
            # Iterate over the frames of the animated image
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))  # Append each frame to the frames list
                im.seek(i)
        except EOFError:
            pass

        self.frames = cycle(frames)  # Create an iterator that cycles through the frames
        self.delay = im.info['duration']  # Get the delay between frames from image metadata

        if len(frames) == 1:
            self.configure(image=next(self.frames))  # Display the first frame if only one frame exists
        else:
            self.next_frame()  # Display the next frame

    def next_frame(self):
        """
        Displays the next frame of the animated image.
        """
        if self.frames:
            self.configure(image=next(self.frames))  # Display the next frame
            self.after(self.delay, self.next_frame)  # Schedule the next frame to be displayed

# Function that handles the event of clicking the "Choose json file" button
def callback():
    """
    Event handler for the "Choose json file" button.
    Opens a file dialog to select a file and writes the file path to the input field.
    """
    name = fd.askopenfilename()  # Open a file dialog and get the selected file path
    ePath.configure(state='normal')  # Enable the input field for editing
    ePath.delete('1', 'end')  # Clear the input field
    ePath.insert('1', name)  # Insert the selected file path into the input field
    ePath.configure(state='readonly')  # Set the input field to read-only mode

# Function that converts a JSON file to CSV format
def convert():
    """
    Converts the JSON file to CSV format.
    Reads the data from the JSON file, forms a CSV string, and saves it to a new CSV file.
    """
    json_file = ePath.get()  # Get the path to the JSON file from the input field
    csv_file = pathlib.Path(json_file)  # Create a Path object from the JSON file path
    csv_file = csv_file.stem + '.csv'  # Get the file name without extension and add ".csv" extension
    try:
        with open(json_file, 'r') as f:
            data = json.loads(f.read())  # Read the JSON data from the file and parse it
        output = ','.join([*data[0]])  # Form the CSV header row using the keys of the first object
        print(output)
        for obj in data:
            output += f'\n{obj["id"]},{obj["first_name"]},{obj["last_name"]}'  # Append CSV rows with values from JSON objects
        print(output)
        with open(csv_file, 'w') as f:
            f.write(output)  # Write the CSV string to the new CSV file
    except Exception as ex:
        print(f'Error: {str(ex)}')

    CTkLabel(root, text='Conversion completed', font=('Arial', 15)).pack(pady=10)

# Function that opens the selected CSV file in Excel
def open_csv_file():
    """
    Opens the selected CSV file in Excel.
    """
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])  # Open a file dialog to select a CSV file
    if file_path:
        df = pd.read_csv(file_path)  # Read the CSV file into a pandas DataFrame
        excel_file_path = os.path.splitext(file_path)[0] + ".xlsx"  # Create the path for the corresponding Excel file
        df.to_excel(excel_file_path, index=False)  # Convert the DataFrame to Excel format and save it
        os.startfile(excel_file_path)  # Open the XLSX file in Excel

if __name__ == '__main__':
    # Initialize the custom library
    set_appearance_mode("dark")  # Set the appearance mode to dark
    set_default_color_theme("dark-blue")  # Set the default color theme

    root = CTk()  # Create the root window using customized Tkinter
    lb = ImageLabel(root, text="")  # Create an instance of ImageLabel widget
    lb.pack()
    lb.load('test.gif')  # Load and display an animated image in the widget

    root.title('JSON to CSV Converter')  # Set the window title
    root.geometry('600x600+400+400')  # Set the window size and position
    root.resizable(width=False, height=False)  # Disable window resizing

    CTkButton(root, text='Choose json file', font=('Arial', 15), command=callback).pack(pady=10)  # Create and place a button for choosing the JSON file

    lbPath = CTkLabel(root, text='File path:', font=('Arial', 15))  # Create a label for the file path
    lbPath.pack()  # Place the label in the window

    ePath = CTkEntry(root, width=400, state='readonly')  # Create an input field for displaying the file path
    ePath.pack(pady=10)  # Place the input field in the window

    btnConvert = CTkButton(root, text='Convert', font=('Arial', 15), command=convert).pack(pady=10)  # Create and place a button for conversion
    open_button = CTkButton(root, text="Open CSV file", command=open_csv_file)  # Create a button for opening the CSV file
    open_button.pack()  # Place the button in the window

    root.mainloop()  # Start the main event loop
