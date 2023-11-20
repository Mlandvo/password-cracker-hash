import hashlib
from urllib.request import urlopen
import tkinter as tk

"""
def readwordlist(url):
    try:
        wordlisitfile = urlopen(rl).read()
    except Exception as e:
        print("Error opening wordlist")
        exit()
    return wordlisitfile
"""

#function to load wordlist on pc
def readwordlist(words_List):
    print("Loading word list...")
    wordlist = list()
    with open(words_List) as f:
        for line in f:
            wordlist.append(line.rstrip('\n'))
    return wordlist

#Function to convert password to hash
def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

#Function to bruteforce password
def bruteforce(wordlist, actual_password_hash):
    for word in wordlist:
        if hash(word) == actual_password_hash:
            #print("Password is: ", word)
            #return word

            #exit()
            #return word
            lbl_results["Text"] = word

        else:
            password_found = False

#Wordlist
#url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
#actual wordlist: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
#code partially sourced from: https://workshops.hackclub.com/passwordcracker/
##actual password entered by user

#actual_password = input('Enter the password to test: ')

##converts password to hash
#actual_password_hash = hash(str(actual_password))

'''
#wordlist = readwordlist(url).decode('UTF-8')
#guesspasswordlist = wordlist.split('\n')
'''

#wordlist = readwordlist('words_list.txt')

#print("The hash generated is: " + hash(actual_password))

#bruteforce attack test
#print(bruteforce(wordlist, actual_password_hash))

#password not in list
#print("Password not found")

#################### Tkinter Graphical Interface ###################

window = tk.Tk()
window.title("Brute Force Password Cracker")
window.resizable(width=False, height=False)

#Frames for password entry
frm_entry = tk.Frame(master=window)

ent_password = tk.Entry(master=frm_entry, width=10)
lbl_password = tk.Label(master=frm_entry, text="Enter Password to be found")

actual_password = str(ent_password.get())
#Layout for frames
ent_password.grid(row=0, column=0, sticky="e")
lbl_password.grid(row=0, column=1, sticky="w")

actual_password_hash = hash(actual_password)

wordlist = readwordlist('words_list.txt')
#button to crack password

#display hash
lbl_hash = tk.Label(master=window, text= "Hash: ")
#display results
lbl_results = tk.Label(master=window, text= "results")

btn_crack = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command= bruteforce(wordlist, actual_password_hash))

#setup frames
frm_entry.grid(row=0, column=0, padx=10)
btn_crack.grid(row=0,column=1, pady=10)
lbl_results.grid(row=0, column=2, padx=10)
lbl_hash.grid(row=1, column=2, padx=10)

window.mainloop()

