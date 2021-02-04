from tkinter import *
from tkinter import filedialog
import webbrowser
import time
import pyautogui as gui
import csv
from tkinter import messagebox
from io import BytesIO
import win32clipboard
from PIL import Image
import urllib.parse

global path
global success
global numentry
global imagepath
global image_success
global message
global instruct

imagepath = ""
path = ""
root = Tk()
root.title("Whatsapp messages")
root.configure(background="snow", height=700, width=1000)


def closeinstruct():
    global instruct
    instruct.place_forget()


# def video():
#     webbrowser.open("https://youtu.be/Gi4Thoai26s")


# def instructionss():
#     global instruct
#     backg = "gray7"
#     frontg = "white smoke"
#     instruct = Frame(root, bg=backg, bd=5)
#     instruct.place(x=0, y=0, relheight=1, relwidth=1)
#
#     close_button = Button(instruct, text="X", font="courier 16", bg="red", fg="white", command=closeinstruct)
#     close_button.place(relx=0.93, rely=0.02, relwidth=0.05, relheight=0.05)
#
#     heading = Label(instruct, text="INSTRUCTIONS!", font="impact 26 bold", bg=backg, fg="deep pink")
#     heading.place(relx=0.3, rely=0.05)
#
#     point1 = Label(instruct, text="1.Connect your whatsapp to whatsapp web before starting.", font="courier 14 bold",
#                    bg=backg, fg=frontg)
#     point1.place(relx=0.02, rely=0.2)
#
#     point2 = Label(instruct, text="2.Use your system default browser and keep it on while starting.",
#                    font="courier 14 bold", bg=backg, fg=frontg)
#     point2.place(relx=0.02, rely=0.28)
#
#     point3 = Label(instruct, text="3.Provide numbers with country code without '+' before number.",
#                    font="courier 14 bold", bg=backg, fg=frontg)
#     point3.place(relx=0.02, rely=0.36)
#
#     point4 = Label(instruct, text="4.Dont use emojis in message field.", font="courier 14 bold", bg=backg, fg=frontg)
#     point4.place(relx=0.02, rely=0.44)
#
#     point5 = Label(instruct, text="5.Do not try to minimize or close the browser.", font="courier 14 bold", bg=backg,
#                    fg=frontg)
#     point5.place(relx=0.02, rely=0.52)
#
#     point6 = Label(instruct, text="6.Keep browser open until the process is done.", font="courier 14 bold", bg=backg,
#                    fg=frontg)
#     point6.place(relx=0.02, rely=0.6)
#
#     point7 = Label(instruct, text="7.If Your browser creates additional dilogues please look into them.",
#                    font="courier 14 bold", bg=backg, fg=frontg)
#     point7.place(relx=0.02, rely=0.68)
#
#     point8 = Label(instruct, text="8.Try to provide .csv file which contains only phone numbers.",
#                    font="courier 14 bold", bg=backg, fg=frontg)
#     point8.place(relx=0.02, rely=0.76)
#
#     point9 = Label(instruct, text="9.For detailed instructions click below button.", font="courier 14 bold", bg=backg,
#                    fg=frontg)
#     point9.place(relx=0.02, rely=0.84)
#
#     youtube = Button(instruct, text="Click here!!", font="impact 16", fg="red", bg="snow3", command=video)
#     youtube.place(relx=0.27, rely=0.9, relwidth=0.4)


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def selectimage():
    global imagepath
    global image_success

    root.imagename = filedialog.askopenfilename(initialdir="d:", title="select a file"
                                                , filetype=(("JPEG Files", "*.jpg"), ("PNG files", "*.png")))
    imagepath = root.imagename
    if imagepath != "":
        image_success = Label(root, text="Image received", fg="red", bg="snow", font="times 14")
        image_success.place(relx=0.72, rely=0.72)


def selectfile():
    global path
    global success
    root.filename = filedialog.askopenfilename(initialdir="d:", title="select a file"
                                               , filetype=(("CSV Files", "*.csv"), ("all files", "*.*")))
    path = root.filename
    if path != "":
        success = Label(root, text="File has been received", fg="red", bg="snow", font="times 14")
        success.place(relx=0.47, rely=0.54)


def submitt():
    global path
    global imagepath
    global numentry
    global success
    global image_success
    global message
    numbers = []
    if path != "":
        success.place_forget()
        with open(path, 'rt') as f:
            data = csv.reader(f)
            for row in data:
                for ele in row:
                    if len(ele) > 5:
                        if ele[0] == "+" or ele.isnumeric():
                            q = ele.strip()
                            q = q.rstrip()
                            numbers.append(q)
    else:
        st = numentry.get()
        if st == "" or st == "Enter Numbers with their country code...":
            messagebox.showerror("No data?", "Please Upload a file or type numbers")
        else:
            numbers = [i.strip().rstrip() for i in st.split(",")]
    try:
        msg = urllib.parse.quote(message.get())
    except Exception:
        messagebox.showerror("Sorry!", "Given Message is not supported!No emojis please!")
    if msg == "" and imagepath == "":
        messagebox.showerror("No data?", "Please type or attach a msg")
    else:
        c = 1
        if imagepath == "":
            print(len(numbers))
            for i in range(20):
                if c == 1:
                    webbrowser.open("https://web.whatsapp.com")
                    time.sleep(12)
                    gui.keyDown('ctrl')
                    gui.press('w')
                    gui.keyUp('ctrl')
                    time.sleep(8)
                    c += 1
                url = "https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(numbers[i], msg)
                webbrowser.open(url)
                time.sleep(12)
                gui.press('enter')
                time.sleep(3)
                gui.keyDown('ctrl')
                gui.press('w')
                gui.keyUp('ctrl')
                time.sleep(1)
                gui.press('enter')
                if i == numbers[-1]:
                    time.sleep(2)
                else:
                    time.sleep(8)
        else:
            image_success.place_forget()
            filepath = imagepath
            try:
                image = Image.open(filepath)
                output = BytesIO()
                image.convert("RGB").save(output, "BMP")
                data = output.getvalue()[14:]
                output.close()
                send_to_clipboard(win32clipboard.CF_DIB, data)
            except Exception:
                messagebox.showerror("sorry", "Not suitable attachment")
                return

            for i in range(20):
                if c == 1:
                    webbrowser.open("https://web.whatsapp.com")
                    time.sleep(12)
                    gui.keyDown('ctrl')
                    gui.press('w')
                    gui.keyUp('ctrl')
                    time.sleep(8)
                    c += 1
                url = "https://web.whatsapp.com/send?phone={}&text={}&source&data&app_absent".format(numbers[i], msg)
                webbrowser.open(url)
                time.sleep(12)
                gui.keyDown('ctrl')
                gui.press('v')
                gui.keyUp('ctrl')
                time.sleep(5)
                gui.press('enter')
                time.sleep(3)
                gui.keyDown('ctrl')
                gui.press('w')
                gui.keyUp('ctrl')
                time.sleep(1)
                gui.press('enter')
                if i == numbers[-1]:
                    time.sleep(2)
                else:
                    time.sleep(8)
        imagepath = ""
        path = ""
        numentry.delete(0, END)
        message.delete(0, END)


canvas1 = Canvas(root, bg="orange")
canvas1.place(relx=0, rely=0, relwidth=1, relheight=0.2)

f1 = Frame(canvas1, bg="orange")
f1.place(relx=0.02, rely=0.02, relwidth=0.9, relheight=0.5)

head_text = Label(f1, text="Whatsapp Bulk SMS", font="Helvetica 40 bold", fg="black", bg="orange")
head_text.place(relx=0.18, rely=0.03)

number = Label(root, text="Enter(,) separated numbers(without '+')", font="Helvetica 16 bold", bg="snow")
number.place(relx=0.02, rely=0.22)

numentry = Entry(root, font="Helvetica 16")
numentry.place(relx=0.02, rely=0.30, relwidth=0.9, relheight=0.15)

insert_label = Label(root, text="or insert .csv file", bg="snow", font="Helvetica 14 bold")
insert_label.place(relx=0.02, rely=0.48)

select = Button(root, text="Select a file", command=selectfile)
select.place(relx=0.05, rely=0.54, relwidth=0.4)

Message_label = Label(root, text="Enter your message below", font="Helvetica 16 bold", bg="snow")
Message_label.place(relx=0.02, rely=0.6)

attachment_label = Label(root, text="Add an image:", font="Helvetica 16 bold", bg="snow")
attachment_label.place(relx=0.65, rely=0.6)

select_image = Button(root, text="Select an attachment", command=selectimage)
select_image.place(relx=0.65, rely=0.66, relwidth=0.3)

message = Entry(root, font="Helvetica 18")
message.place(relx=0.02, rely=0.65, relwidth=0.6, relheight=0.2)

submit = Button(root, text="Submit", font="impact 20 bold", fg="white", bg="green", command=submitt)
submit.place(relx=0.3, rely=0.87, relwidth=0.4)

# please_read = Label(root, text="Please read instructions\nbefore you start!", font="times 14", bg="snow", fg="red")
# please_read.place(relx=0.76, rely=0.78)

# instructions = Button(root, text="Instructions!!", font="impact 16", bg="skyblue", fg="white", command=instructionss)
# instructions.place(relx=0.78, rely=0.87, relwidth=0.18, relheight=0.12)

root.mainloop()