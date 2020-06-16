
from tkinter import *
from datetime import date

root = Tk()
root.geometry("700x500")
root.title("Age Calculator")

photo = PhotoImage(file="filename.ipg")
myimage = Label(image = photo)
myimage.grid(row = 0 , column = 1)

def calculator_Age():
    today = date.today()
    birthdayDate = date(int(yearEntry.get()),
    int(monthEntry.get()),
    int(dayEnter.get()))

    age = today.year - birthdayDate.year - ((today.month, birthdayDate.day))

    Label(text = f"{nameValue.get()} your age is {age}").grid(row = 6, column =1)

    Label(text = "Name").grid(row = 1, column = 0 , padx =90)
    Label(text = "Year").grid(row = 2, column =  0)
    Label(text = "Month").grid(row = 3, column = 0)
    Label(text = "Day").grid(row = 4, column = 0)

    nameValue = StringVar()
    yearValue = StringVar()
    monthValue = StringVar()
    dayValue = StringVar()
    nameEntry = Entry(root, textvariable = nameValue)
    yearEntry = Entry(root, textvariable = yearValue)
    monthEntry = Entry(root, textvariable = monthValue)
    dayEntry = Entry(root, textvariable = dayValue)

    nameEntry.grid(row = 1, column = 1, pady = 10)
    nameEntry.grid(row = 2, column = 1, pady = 10)
    nameEntry.grid(row = 3, column = 1, pady = 10)
    nameEntry.grid(row = 4, column = 1, pady = 10)

    Button(text ="Calculate age", command = calculteAge).grid(rwo =5, column = 1, pady = 10)

    root.mainloop()
