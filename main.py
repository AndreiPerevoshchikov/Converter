import json
import customtkinter
from customtkinter import filedialog as fd
import pathlib


def callback():
    name = fd.askopenfilename()
    ePath.configure(state='normal')
    ePath.delete('1', 'end')
    ePath.insert('1', name)
    ePath.configure(state='readonly')


def convert():
    json_file = ePath.get()
    csv_file = pathlib.Path(json_file)
    csv_file = csv_file.stem + '.csv'
    try:
        with open(json_file, 'r') as f:
            data = json.loads(f.read())
        output = ','.join([*data[0]])
        print(output)
        for obj in data:
            output += f'\n{obj["id"]},{obj["first_name"]},{obj["last_name"]}'
        print(output)
        with open(csv_file, 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')

    customtkinter.CTkLabel(root, text='Конвертация завершена', font=('Arial', 15)).pack(pady=10)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title('Конвертер json в csv')
root.geometry('800x400+400+400')
root.resizable(width=False, height=False)


customtkinter.CTkButton(root, text='Выбрать json файл', font=('Arial', 15), command=callback).pack(pady=10)

lbPath = customtkinter.CTkLabel(root, text='Путь к файлу:', font=('Arial', 15))
lbPath.pack()

ePath = customtkinter.CTkEntry(root, width=400, state='readonly')
ePath.pack(pady=10)

btnConvert = customtkinter.CTkButton(root, text='Конвертировать', font=('Arial', 15), command=convert).pack(pady=10)


root.mainloop()


# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
#
# app = customtkinter.CTk()
# app.geometry("400x780")
# app.title("SuperPuperDuperConverter3000")
#
# def button_callback():
#     print("Button click", combobox_1.get())
#
#
# def slider_callback(value):
#     progressbar_1.set(value)
#
#
# frame_1 = customtkinter.CTkFrame(master=app)
# frame_1.pack(pady=20, padx=60, fill="both", expand=True)
#
# label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
# label_1.pack(pady=10, padx=10)
#
# progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
# progressbar_1.pack(pady=10, padx=10)
#
# button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
# button_1.pack(pady=10, padx=10)
#
# slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
# slider_1.pack(pady=10, padx=10)
# slider_1.set(0.5)
#
# entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
# entry_1.pack(pady=10, padx=10)
#
# optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# optionmenu_1.pack(pady=10, padx=10)
# optionmenu_1.set("CTkOptionMenu")
#
# combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# combobox_1.pack(pady=10, padx=10)
# combobox_1.set("CTkComboBox")
#
# checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
# checkbox_1.pack(pady=10, padx=10)
#
# radiobutton_var = customtkinter.IntVar(value=1)
#
# radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
# radiobutton_1.pack(pady=10, padx=10)
#
# radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
# radiobutton_2.pack(pady=10, padx=10)
#
# switch_1 = customtkinter.CTkSwitch(master=frame_1)
# switch_1.pack(pady=10, padx=10)
#
# text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
# text_1.pack(pady=10, padx=10)
# text_1.insert("0.0", "CTkTextbox\n\n\n\n")
#
# segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
# segmented_button_1.pack(pady=10, padx=10)
#
# tabview_1 = customtkinter.CTkTabview(master=frame_1, width=200, height=70)
# tabview_1.pack(pady=10, padx=10)
# tabview_1.add("CTkTabview")
# tabview_1.add("Tab 2")
#
# app.mainloop()
