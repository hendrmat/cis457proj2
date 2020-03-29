# This is the GUI for the chat application
import tkinter
from tkinter import *

root = Tk()


# This function will copy the text from the text box to the chat log
# and then delete the text from the text box afterwards
def sendText(event=None):
    # This will check to make sure the text box is not empty before
    # sending a message, otherwise a misuser can flood someone's textbox
    # with empty messages
    if len(textWindow.get("1.0", "end-1c")) != 0:
        chatWindow.config(state=NORMAL)
        message = textWindow.get("1.0", "end")
        textWindow.delete("1.0", "end-1c")
        chatWindow.insert("end", message)
    chatWindow.see(tkinter.END)
    chatWindow.config(state=DISABLED)


# This function will prevent the annoying effect of the cursor dropping
# one level when the Enter key is pressed to deliver the typed message
# Function obtained from
# https://stackoverflow.com/questions/18565414/tkinter-keyrelease-event-
# inserting-new-line-while-keypress-doesnt
def preventReturn(event):
    if event.keysym == "Return":
        sendText()
        return 'break'

# Series of small functions that will print what matches the corresponding
# buttons on the side of the GUI
def printSmile(event):
    textWindow.insert(tkinter.END, ":-) ")


def printSad(event):
    textWindow.insert(tkinter.END, ":-( ")


def printCry(event):
    textWindow.insert(tkinter.END, ":'-( ")


def printWink(event):
    textWindow.insert(tkinter.END, ";-) ")


def printSquintLaugh(event):
    textWindow.insert(tkinter.END, "X-D ")


def printWow(Event):
    textWindow.insert(tkinter.END, ":-O ")


def printTongue(Event):
    textWindow.insert(tkinter.END, ":-P ")


def printAngry(Event):
    textWindow.insert(tkinter.END, ">:[ ")


def printAnimeSmile(Event):
    textWindow.insert(tkinter.END, "^_^ ")


def printAnimeWink(Event):
    textWindow.insert(tkinter.END, "^_~ ")


def printAnimeAngry(Event):
    textWindow.insert(tkinter.END, ">_< ")


def printAnimeShock(Event):
    textWindow.insert(tkinter.END, "O_O ")


# Creating the chat history window
chatWindow = Text(root, height="10", width="70", borderwidth=2,
                  relief=FLAT, wrap=WORD)
chatWindow.place(x=2, y=2, width=400, height=170)

# Creating a scrollbar so the user can go through the chat history
scrollbar = Scrollbar(chatWindow)
scrollbar.config(command=chatWindow.yview)
scrollbar.pack(side=RIGHT, fill=Y)
# Creating the text window for the user to type into
textWindow = Text(root)
textWindow.focus()
textWindow.place(x=2, y=180, width=400, height=110)

# Creates the Send button, which will invoke the command to transfer the
# text within to the chat history window and delete the text in the
# text box
sendMessage = Button(root, text="Send")
sendMessage.place(x=415, y=250, width=70, height=20)
sendMessage.bind("<Button-1>", sendText)
textWindow.bind("<KeyPress>", preventReturn)

# Creates the various emoji buttons found on the side of the GUI
# Due to technical bugs/limitations, porting emojis to Tkinter
# is not possible without significant workarounds
grinEmoji = Button(root, text=":-)")
grinEmoji.place(x=415, y=200, width=30, height=30)
grinEmoji.bind("<Button-1>", printSmile)

sadEmoji = Button(root, text=":-(")
sadEmoji.place(x=450, y=200, width=30, height=30)
sadEmoji.bind("<Button-1>", printSad)

cryEmoji = Button(root, text=":'-(")
cryEmoji.place(x=415, y=160, width=30, height=30)
cryEmoji.bind("<Button-1>", printCry)

winkEmoji = Button(root, text=";-)")
winkEmoji.place(x=450, y=160, width=30, height=30)
winkEmoji.bind("<Button-1>", printWink)

squintLaughEmoji = Button(root, text="X-D")
squintLaughEmoji.place(x=415, y=120, width=30, height=30)
squintLaughEmoji.bind("<Button-1>", printSquintLaugh)

wowEmoji = Button(root, text=":-O")
wowEmoji.place(x=450, y=120, width=30, height=30)
wowEmoji.bind("<Button-1>", printWow)

tongueEmoji = Button(root, text=":-P")
tongueEmoji.place(x=415, y=80, width=30, height=30)
tongueEmoji.bind("<Button-1>", printTongue)

angryEmoji = Button(root, text=">:[")
angryEmoji.place(x=450, y=80, width=30, height=30)
angryEmoji.bind("<Button-1>", printAngry)

animeSmileEmoji = Button(root, text="^_^")
animeSmileEmoji.place(x=415, y=40, width=30, height=30)
animeSmileEmoji.bind("<Button-1>", printAnimeSmile)

animeWinkEmoji = Button(root, text="^_^")
animeWinkEmoji.place(x=450, y=40, width=30, height=30)
animeWinkEmoji.bind("<Button-1>", printAnimeWink)

animeAngryEmoji = Button(root, text=">_<")
animeAngryEmoji.place(x=415, y=0, width=30, height=30)
animeAngryEmoji.bind("<Button-1>", printAnimeAngry)

animeShockEmoji = Button(root, text="O_O")
animeShockEmoji.place(x=450, y=0, width=30, height=30)
animeShockEmoji.bind("<Button-1>", printAnimeShock)

# Creates the main window with title and makes it not resizeable
root.title("Matt's Awesome Instant Messenger")
root.geometry("500x300")
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
