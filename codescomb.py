#program to find out the maximum possible combinations in a word and the maximum words.

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as tkst
from collections import OrderedDict
import threading


root = Tk()
root.title("Possibilities")
greeting = Label(root, text="Hi, There\n This software creates all possible combinations of a string.", fg="RED")
greeting.config(font=("Times New Roman", 17))
greeting.pack(side="top", fill=X)
strinput = Label(root, text = "Enter the string in below box. :-")
strinput.config(font=("Roman",15))
strinput.pack()
outputs = Label(root, text="Results are shown below....:-")
outputs.config(font=("Courier", 15))
text_area = Text(root, height = 2, width = 30)
text_area.pack(fill=X)
outputs.pack()
scrolltext = tkst.ScrolledText()
scrolltext.pack()

word = ""
wordlist = []
full_list = []
count = 0
count_all = 0


def getInput(userInput):
    global word, wordlist
    if(userInput == None or userInput == ""):
        messagebox.showerror("No Input Error", "Nothing has been provided.")
        return
    word = userInput
    wordlist = []
    for i in range(len(word)):
        wordlist.append(word[i])
    wordlist = list(OrderedDict.fromkeys(wordlist))
    for i in range(len(wordlist)):
        #sending text to gui scroll box
        scrolltext.insert(tk.END, wordlist[i]+"\n")
    return word


def get_input():
    value = text_area.get("1.0","end-1c")
    if(value == None):
        messagebox.showerror("No Input Error", "Nothing has been provided.")
        return()
    global word
    word = value
    getInput(word)




def combinations(wordlist):
    wordlist_in = []
    global count, count_all
    for i in range(len(word)):
        for j in range(len(wordlist)):
            if((word[i]+wordlist[j]) not in full_list):
                #print(word[i]+wordlist[j])
                scrolltext.insert(tk.END, word[i]+wordlist[j]+"\n")
                wordlist_in.append(word[i]+wordlist[j])
                full_list.append(word[i]+wordlist[j])
                count += 1
            else:
                pass
            count_all += 1
            j += 1
        i += 1
    return wordlist_in

def loops():
    k = 0
    global wordlist, wordlist_out, word, count , count_all
    if(len(word)>6):
        messagebox.showinfo("Info.....", "Word is of greater length so please be patient.")
    get_input()
    while(k<(len(word)-1)):
        wordlist_out = combinations(wordlist)
        wordlist_out = list(OrderedDict.fromkeys(wordlist_out))
        wordlist = wordlist_out
        k +=1
    if(count == count_all):
        scrolltext.insert(tk.END,"Total words are "+str(count)+"\n")
        scrolltext.insert(tk.END,"There are no repeating words.\n")
    else:
        scrolltext.insert(tk.END,"Total words are "+str(count)+"\n")
        scrolltext.insert(tk.END,"Total words with repeatition " +str(count_all)+"\n")
    wordlist = full_list = []

################################

def ccombinations(wordlist):
    wordlist_in = []
    global count, count_all
    for i in range(len(word)):
        for j in range(len(wordlist)):
            if((word[i]+wordlist[j]) not in full_list):
                wordlist_in.append(word[i]+wordlist[j])
                full_list.append(word[i]+wordlist[j])
                count += 1
            else:
                pass
            count_all += 1
            j += 1
        i += 1
    return wordlist_in

def cloops():
    k = 0
    global wordlist, wordlist_out, word
    if(len(word)>6):
        messagebox.showinfo("Info.....", "Word is of greater length so please be patient.")
    get_input()
    while(k<(len(word)-1)):
        wordlist_out = ccombinations(wordlist)
        wordlist_out = list(OrderedDict.fromkeys(wordlist_out))
        wordlist = wordlist_out
        k +=1




def counts():
    global count, count_all, wordlist, full_list
    if(wordlist == [] or full_list == []):
        cloops()
    if(count == count_all):
        scrolltext.insert(tk.END,"Total words are "+str(count)+"\n")
        scrolltext.insert(tk.END,"There are no repeating words.\n")
    else:
        scrolltext.insert(tk.END,"Total words are "+str(count)+"\n")
        scrolltext.insert(tk.END,"Total words with repeatition " +str(count_all)+"\n")
    count = count_all = 0
    wordlist = full_list = []

def clear_all():
    global count, count_all, wordlist, full_list
    scrolltext.delete(1.0,END)
    count = count_all = 0
    wordlist = full_list = []

#buttons

close_button = Button(root, text="Exit", command=lambda: root.destroy())
close_button.pack(side="right")

clear_button = Button(root, text="Clear All", command=clear_all)
clear_button.pack(side="right")

count_button = Button(root, text="Count Words",command=counts)
count_button.pack(side="right")

show_button = Button(root, text="Show Words",command=loops)
show_button.pack(side="right")

send_button = Button(root, text="Show Letters",command=get_input)
send_button.pack(side="right")



root.mainloop()
