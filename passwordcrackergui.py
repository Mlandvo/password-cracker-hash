import tkinter as tk
import passwordcracker2 as pc #readwordlist, bruteforce, hash, wordlist
#from passwordcracker import *

#Function to parse passwordcracker

'''
def cracked():
    password = ent_password.get()
    actual_password_hash = hash(str(password))
    wordlist = readwordlist('words_list.txt')
    crackedP = bruteforce(wordlist, actual_password_hash)
    lbl_results = crackedP
'''

window = tk.Tk()
window.title("Brute Force Password Cracker")
window.resizable(width=False, height=False)

#Frames for password entry
frm_entry = tk.Frame(master=window)
ent_password = tk.Entry(master=frm_entry, width=10)
lbl_password = tk.Label(master=frm_entry, text="Enter Password to be found")

#Layout for frames
ent_password.grid(row=0, column=0, sticky="e")
lbl_password.grid(row=0, column=1, sticky="w")

actual_password_hash = hash(ent_password)

wordlist = pc.readwordlist('words_list.txt')
#button to crack password
btn_crack = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command= pc.bruteforce(wordlist, actual_password_hash))

#display hash
lbl_hash = tk.Label(master=window, text= "Hash: " + str(actual_password_hash))
#display results
lbl_results = tk.Label(master=window, text= "results")

#setup frames
frm_entry.grid(row=0, column=0, padx=10)
btn_crack.grid(row=0,column=1, pady=10)
lbl_results.grid(row=0, column=2, padx=10)
lbl_hash.grid(row=1, column=2, padx=10)

window.mainloop()