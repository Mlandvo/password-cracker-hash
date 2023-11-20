import hashlib
from urllib.request import urlopen
#import tkinter as tk
#import passwordcrackergui as pcg
#Function to real wordlist online

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
            print("Password is: ", word)
            exit()
    return word

#Wordlist
#url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
#actual wordlist: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
#code partially sourced from: https://workshops.hackclub.com/passwordcracker/
##actual password entered by user

actual_password = input('Enter the password to test: ')
#actual_password = lbl_password

##converts password to hash
actual_password_hash = hash(str(actual_password))

'''
#wordlist = readwordlist(url).decode('UTF-8')
#guesspasswordlist = wordlist.split('\n')
'''

wordlist = readwordlist('words_list.txt')
#print(len(wordlist))

print("The hash generated is: " + hash(actual_password))

#bruteforce attack test
bruteforce(wordlist, actual_password_hash)
#password not in list
print("Password not found")

#################### Tkinter Graphical Interface ###################


