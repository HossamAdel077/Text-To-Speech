from tkinter import*
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
def read_text():
    text = Entry.get(myEntry)
    engine.say(text)
    engine.runAndWait()

def delete_text():
    myEntry.delete(0, END)

myFrame = Tk()
myFrame.title("Text To Speech")
myFrame.geometry("400x300")

myLabel1 = Label(myFrame, text="Text To Speech", font="Tahoma 20 bold")
myEntry = Entry(myFrame, width=60)

Button1 =Button(myFrame, text="Play", command=read_text, fg="white",bg="green", font="Helvatica 10 bold") 
Button2 =Button(myFrame, text="Set", command= delete_text, fg="white",bg="gray", font="Helvatica 10 bold")
Button3 =Button(myFrame, text="Exit", command=exit, fg="white",bg="red", font="Helvatica 10 bold")

myLabel1.pack()
myEntry.pack(side=TOP, pady=30)
Button1.pack(side=LEFT, padx=20)
Button2.pack(side=LEFT, padx=20)
Button3.pack(side=LEFT, padx=20)

myFrame.mainloop()