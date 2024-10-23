from curses.ascii import isdigit
from itertools import count
from random import random, randint
from tkinter import *
from tkinter import ttk

listString=""
global a,b
a=0
b=100
def rangeSelector():
    global a,b
    tempA=int(aEntry.get())
    tempB=int(bEntry.get())
    if tempA>tempB:
        a=tempA
        b=tempB
    else:
        b=tempB
        a=tempA
#Tworzy liste, o dlugosci podanej przez uzytkownika i wyswietla ja w GUI
def makeList():
    listString = ""
    global list
    list=[]
    z=int(numberEntry.get())
    for i in range(0,z):
        #print(a,b)
        list.append(randint(a,b))
        listString=listString+str(list[i])+" "
    label.config(text=listString)
    print(list)
    avg()
    medianlabel.config(text="")


#Aktualizuje liste po wywolaniu funkcji sortowania
def updateList():
    global list
    listString = ""
    print(list)
    for i in list:
        listString = listString + str(i) + " "
    label.config(text=listString)
#Sortowanie babelkowe
def bubbleSort():
    global list
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    updateList()
    median()
#Sortowanie przez wybor
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
    median()
#Sortowanie przez wstawianie
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
    median()
def avg():
    global list
    avg=sum(list)/len(list)
    avg=round(avg,2)
    avgLabel.config(text="Srednia: "+str(avg))
def median():
    global list
    size=len(list)
    median=0
    if size%2!=0:
        median=list[size/2]
    else:
        print(size)
    medianlabel.config(text="Mediana: "+str(median))
    #TODO: Median

#Tworzenie GUI
root=Tk()
root.title("Sortowanie")
root.geometry('800x600')
root.grid()
#Styl
root.configure(bg="#564c4d")
style=ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#564c4d', foreground='white',font=('Helvetica', 12, 'bold'))
style.configure('TLabel',background='#564c4d',font=('Helvetica', 16))
style.configure('TEntry',background='#564c4d',font=('Helvetica', 22))
#Wstawianie kontrolek
numberEntry=ttk.Entry(root)
aEntry=ttk.Entry(root)
bEntry=ttk.Entry(root)
rangebutton=ttk.Button(root,text="Wybierz zakres",command=rangeSelector)
aEntry.grid(row=0, column=0, padx=5, pady=5)
bEntry.grid(row=0, column=1,padx=5, pady=5)
rangebutton.grid(column=2, row=0)
numberEntry.grid(column=0, row=1)
button=ttk.Button(root,text="Wylosuj",command=makeList)
button.grid(column=1, row=1)
avgLabel=ttk.Label(root,text="")
medianlabel=ttk.Label(root,text="")
avgLabel.grid(column=0, row=3)
medianlabel.grid(column=1, row=3)
label=ttk.Label(root,text="")
label.grid(column=0, row=2,columnspan=12,pady=10,sticky='ew')
bubbleSortButton=ttk.Button(root,text="Bubble sort",command=bubbleSort)
selectionSortButton=ttk.Button(root,text="Selection sort",command=selectionSort)
insertionSortButton=ttk.Button(root,text="Insertion sort",command=insertionSort)
bubbleSortButton.grid(column=0, row=5,sticky="ew")
selectionSortButton.grid(column=1, row=5,sticky="ew")
insertionSortButton.grid(column=2, row=5,sticky="ew")
exitButton=ttk.Button(root,text="Wylacz",command=root.quit)
exitButton.grid(column=0, row=6,columnspan=12,pady=10)

root.mainloop()