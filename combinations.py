####learning gui with multithreading

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as tkst
from collections import OrderedDict



class main():
    def __init__(self):
        self.root = Tk()
        self.word = ''
        self.full_list = self.wordlist = []
        self.count = self.count_all = 0
        self.root.title("Possibilities")
        greeting = Label(self.root, text="Hi, There\n This software creates all possible combinations of a string.", fg="RED")
        greeting.config(font=("Times New Roman", 17))
        greeting.pack(side="top", fill=X)
        strinput = Label(self.root, text = "Enter the string in below box. :-")
        strinput.config(font=("Roman",15))
        strinput.pack()
        outputs = Label(self.root, text="Results are shown below....:-")
        outputs.config(font=("Courier", 15))
        self.text_area = Text(self.root, height = 2, width = 30)
        self.text_area.pack(fill=X)
        outputs.pack()
        self.scrolltext = tkst.ScrolledText()
        self.scrolltext.pack()
        close_button = Button(self.root, text="Exit", command=lambda: self.root.destroy())
        close_button.pack(side="right")
        clear_button = Button(self.root, text="Clear All", command = self.clear_all)
        clear_button.pack(side="right")
        self.count_button = Button(self.root, text="Count Words", command=self.loops)
        self.count_button.pack(side="right")
        self.show_button = Button(self.root, text="Show Words", command=self.loops)
        self.show_button.pack(side="right")
        send_button = Button(self.root, text="Show Letters",command=self.get_input)
        send_button.pack(side="right")
        self.root.mainloop()

    def clear_all(self):
        self.scrolltext.delete(1.0, END)
        self.text_area.delete(1.0, END)
        self.count = self.count_all = 0
        self.wordlist = self.full_list = []

    def get_input(self):
        value = self.text_area.get("1.0","end-1c")
        if(value == None or value == ''):
            messagebox.showerror("No Input Error", "Nothing has been provided.")
            return()
        self.word = value
        self.getInput(self.word)

    def getInput(self, string):
        self.wordlist = []
        for i in range(len(string)):
            self.wordlist.append(self.word[i])
        self.wordlist = list(OrderedDict.fromkeys(self.wordlist))
        for i in range(len(self.wordlist)):
            self.scrolltext.insert(tk.END, self.wordlist[i]+"\n")
        return()

    def combinations(self, wordlist):
        wordlist_in = []
        for i in range(len(self.word)):
            for j in range(len(self.wordlist)):
                if((self.word[i]+self.wordlist[j]) not in self.full_list):
                    self.root.update()
                    wordlist_in.append(self.word[i]+self.wordlist[j])
                    self.full_list.append(self.word[i]+self.wordlist[j])
                    self.count += 1
                    if(self.show_button):
                        self.scrolltext.insert(tk.END, self.word[i]+self.wordlist[j]+"\n")
                    elif(self.count_button > 0):
                        self.scrolltext.delete(1.0, END)
                        self.scrolltext.insert(tk.END, str(self.count))
                else:
                    pass
                self.count_all += 1
                j +- 1
            i += 1
        wordlist_in  = list(OrderedDict.fromkeys(wordlist_in))
        return wordlist_in

    def loops(self):
        k = 0
        self.get_input()
        while(k<(len(self.word)-1)):
            wordlist_out = self.combinations(self.wordlist)
            wordlist_out = list(OrderedDict.fromkeys(wordlist_out))
            self.wordlist = wordlist_out
            k += 1
        if(self.count == self.count_all):
            self.scrolltext.insert(tk.END, "\nTotal words are "+str(self.count)+"\n")
            self.scrolltext.insert(tk.END, "There are no repeating words.\n")
        else:
            self.scrolltext.insert(tk.END, "\nTotal words are "+str(self.count)+"\n")
            self.scrolltext.insert(tk.END, "Total words with repeatition " +str(self.count_all)+"\n")
        self.wordlist = self.full_list =[]
        self.count = self.count_all = 0


window = main()
