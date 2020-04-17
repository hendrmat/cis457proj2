# Matt Hendrick
# CIS 457
# Project 2

# This is the GUI for the chat application
import tkinter
from tkinter import *

root = Tk()

#replace_regex = re.compile(r"[\U00010000-\U0010FFFF]")

#def match_surrogate(match):
#    c = match.group()
#    encoded = c.encode("utf-16-le")
 #   return chr(int.from_bytes(encoded[:2], "little")) + \
 #          chr(int.from_bytes(encoded[2:], "little"))

#def replace_emoji(string):
 #   return replace_regex.sub(match_surrogate, string)


# This function will copy the text from the text box to the chat log
# and then delete the text from the text box afterwards
def send_text(event=None):
    # This will check to make sure the text box is not empty before
    # sending a message, otherwise a misuser can flood someone's textbox
    # with empty messages
    if len(text_window.get("1.0", "end-1c")) != 0:
        chat_window.config(state=NORMAL)
        message = text_window.get("1.0", "end")
        text_window.delete("1.0", "end-1c")
        chat_window.insert("end", message)
    chat_window.see(tkinter.END)
    chat_window.config(state=DISABLED)


# This function will prevent the annoying effect of the cursor dropping
# one level when the Enter key is pressed to deliver the typed message
# Function obtained from
# https://stackoverflow.com/questions/18565414/tkinter-keyrelease-event-
# inserting-new-line-while-keypress-doesnt
def prevent_return(event):
    if event.keysym == "Return":
        send_text()
        return 'break'

# Series of small functions that will print what matches the corresponding
# buttons on the side of the GUI
def print_smile(event):
    text_window.insert(tkinter.END, ":-) ")


def print_sad(event):
    text_window.insert(tkinter.END, ":-( ")


def print_cry(event):
    text_window.insert(tkinter.END, ":'-( ")


def print_wink(event):
    text_window.insert(tkinter.END, ";-) ")


def print_squint_laugh(event):
    text_window.insert(tkinter.END, "X-D ")


def print_wow(Event):
    text_window.insert(tkinter.END, ":-O ")


def print_tongue(Event):
    text_window.insert(tkinter.END, ":-P ")


def print_angry(Event):
    text_window.insert(tkinter.END, ">:[ ")


def print_anime_smile(Event):
    text_window.insert(tkinter.END, "^_^ ")


def print_anime_wink(Event):
    text_window.insert(tkinter.END, "^_~ ")


def print_anime_angry(Event):
    text_window.insert(tkinter.END, ">_< ")


def print_anime_shock(Event):
    text_window.insert(tkinter.END, "O_O ")

#def printTestSmiley(Event):
#    textWindow.insert(tkinter.END, replace_emoji("\U0001F600"))

# Creating the chat history window
chat_window = Text(root, height="10", width="70", borderwidth=2,
                  relief=FLAT, wrap=WORD)
chat_window.place(x=2, y=2, width=400, height=170)

# Creating a scrollbar so the user can go through the chat history
scrollbar = Scrollbar(chat_window)
scrollbar.config(command=chat_window.yview)
scrollbar.pack(side=RIGHT, fill=Y)
# Creating the text window for the user to type into
text_window = Text(root)
text_window.focus()
text_window.place(x=2, y=180, width=400, height=110)

# Creates the Send button, which will invoke the command to transfer the
# text within to the chat history window and delete the text in the
# text box
send_message = Button(root, text="Send")
send_message.place(x=415, y=250, width=70, height=20)
send_message.bind("<Button-1>", send_text)
text_window.bind("<KeyPress>", prevent_return)

# Creates the various emoji buttons found on the side of the GUI
# Due to technical bugs/limitations, porting emojis to Tkinter
# is not possible without significant workarounds
grin_emoji = Button(root, text=":-)")
grin_emoji.place(x=415, y=200, width=30, height=30)
grin_emoji.bind("<Button-1>", print_smile)

sad_emoji = Button(root, text=":-(")
sad_emoji.place(x=450, y=200, width=30, height=30)
sad_emoji.bind("<Button-1>", print_sad)

cry_emoji = Button(root, text=":'-(")
cry_emoji.place(x=415, y=160, width=30, height=30)
cry_emoji.bind("<Button-1>", print_cry)

wink_emoji = Button(root, text=";-)")
wink_emoji.place(x=450, y=160, width=30, height=30)
wink_emoji.bind("<Button-1>", print_wink)

squint_laugh_emoji = Button(root, text="X-D")
squint_laugh_emoji.place(x=415, y=120, width=30, height=30)
squint_laugh_emoji.bind("<Button-1>", print_squint_laugh)

wow_emoji = Button(root, text=":-O")
wow_emoji.place(x=450, y=120, width=30, height=30)
wow_emoji.bind("<Button-1>", print_wow)

tongue_emoji = Button(root, text=":-P")
tongue_emoji.place(x=415, y=80, width=30, height=30)
tongue_emoji.bind("<Button-1>", print_tongue)

angry_emoji = Button(root, text=">:[")
angry_emoji.place(x=450, y=80, width=30, height=30)
angry_emoji.bind("<Button-1>", print_angry)

anime_smile_emoji = Button(root, text="^_^")
anime_smile_emoji.place(x=415, y=40, width=30, height=30)
anime_smile_emoji.bind("<Button-1>", print_anime_smile)

anime_wink_emoji = Button(root, text="^_^")
anime_wink_emoji.place(x=450, y=40, width=30, height=30)
anime_wink_emoji.bind("<Button-1>", print_anime_wink)

anime_angry_emoji = Button(root, text=">_<")
anime_angry_emoji.place(x=415, y=0, width=30, height=30)
anime_angry_emoji.bind("<Button-1>", print_anime_angry)

anime_shock_emoji = Button(root, text="O_O")
anime_shock_emoji.place(x=450, y=0, width=30, height=30)
anime_shock_emoji.bind("<Button-1>", print_anime_shock)

# Creates the main window with title and makes it not resizeable
root.title("Matt's Awesome Instant Messenger")
root.geometry("500x300")
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
