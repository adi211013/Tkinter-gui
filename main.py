from random import random, randint
from tkinter import *
from tkinter import ttk

listString=""

def makeList():
    listString = ""
    global list
    list=[]
    z=int(numberEntry.get())
    for i in range(0,z):
        list.append(randint(0,100))
        listString=listString+str(list[i])+" "
    label.config(text=listString)



def updateList():
    global list
    listString = ""
    print(list)
    for i in list:
        listString = listString + str(i) + " "
    label.config(text=listString)
def bubbleSort():
    global list
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    updateList()
def selectionSort():
    global list
    n = len(list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if list[j] < list[min_idx]:
                min_idx = j

        list[i], list[min_idx] = list[min_idx], list[i]
    updateList()

def insertionSort():
    global list
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    updateList()



root=Tk()
root.title("Sortowanie")
root.geometry('800x600')
root.grid()
numberEntry=ttk.Entry(root)
numberEntry.grid(column=0, row=0)
button=ttk.Button(root,text="Wylosuj",command=makeList)
button.grid(column=1, row=0)
label=ttk.Label(root,text="")
label.grid(column=0, row=1,columnspan=12,pady=10)
bubbleSortButton=ttk.Button(root,text="Bubble sort",command=bubbleSort)
selectionSortButton=ttk.Button(root,text="Selection sort",command=selectionSort)
insertionSortButton=ttk.Button(root,text="Insertion sort",command=insertionSort)
bubbleSortButton.grid(column=0, row=2,sticky="ew")
selectionSortButton.grid(column=1, row=2,sticky="ew")
insertionSortButton.grid(column=2, row=2,sticky="ew")
exitButton=ttk.Button(root,text="Wylacz",command=root.quit)
exitButton.grid(column=0, row=3,columnspan=12,pady=10)

root.mainloop()