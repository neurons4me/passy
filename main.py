import random
import pyperclip
import time

def menu_main():
    password_entry = input('Password:')
    #take as input master password and optionally a keyfile location (have a default set)
    #1. log new entry 
        # collect this info: website/resource-name: password, category, additonal notes
        #create dictionary entry in dict[category] with info
        #take args for password gen options
    #2. delete entry
        #delete dict entry
    #3. update entry
        #generate new password and provide option to update other info in dict entry
    #4. change master password and keyfile

def get_cha():
    char_list = []
    for i in range(33, 126):
        char_list.append(str(chr(i)))
    return ''.join(char_list)



def make_password():
    chars = get_cha()
    password = []
    pass_length = 60
    for i in range(pass_length):
        password.append(random.choice(chars))
    return "".join(password)

def copy_new_password(new_password):    
    pyperclip.copy(new_password)
    time.sleep(30)
    print("Password coppied to the clipboard.\nClipboard will be cleared in 30 seconds.")
    pyperclip.copy('')

def log_new_entry():
    # create encrypted file with password as content and named by website
    # warn if a password already exists for website
    # return new password to downstream for copying

def delete_log():
    pass

def update_log():
    pass



def make_internal_key(password, keyfile):
    #password should be key to decrypt keyfile, which then provides an internal key to decrypt password files    
    #allow decryption to silently fail to make brute force harder

def
