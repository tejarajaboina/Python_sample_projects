import os
import urllib.request

def open_file():
    os.chdir(r"C:\Users\Raviteja\Downloads")
    names= open('test.txt','r')
    names_b= names.read()
    print(names_b)
    names.close()
    check_curr_word(names_b)
    
open_file()

def check_curr_word(words):
    conn=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+words)
    output=conn.read()
    print(output)
    conn.close()
    if "true" in output:
        print("profanity alert!!!!!!!")
    elif "false" in output:
        print("This is sentece has nocruse words")
    
check_curr_word(words)

#open_file()
