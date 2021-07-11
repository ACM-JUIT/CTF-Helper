import subprocess
import random


def checkinstall(TI):
    rc = subprocess.call(['where', TI])
    if rc == 0:
        print(TI+'installed!')
        print('do you want to reinstall(yes/no)')
        YO = input()
        return YO
    else:
        print(TI + 'missing in path!')
        return 'no'


def install():
    print("select category")
    CT = input()
    print("select tool")
    TI = input()
    CH = checkinstall(TI)
    if CH == "no":
        print("we are running the tool for you\n")
    else:
        execfile(TI+'.py')

# Fix Function (Md5)
# def fix():
#     import checksumdir
#     hash = checksumdir.dirhash("c:\\temp")

def list1():
    while True:
        f = open("./toolList/index.txt", "r")
        print(f.read())
        choice = input()
        if choice == "exit":
            break
        elif choice == "binary":
            f = open("./toolList/Binary.txt", "r")
            print(f.read())
        elif choice == "crypto":
            f = open("./toolList/Crypto.txt", "r")
            print(f.read())
        elif choice == "stego":
            f = open("./toolList/Fuzzers.txt", "r")
            print(f.read())
        elif choice == "fuzzers":
            f = open("./toolList/Stego.txt", "r")
            print(f.read())
        else:
            print("Invalid choice, please choose again\n")


def ascii1():
    RA = random.randint(0, 4)
    f = open("./ascii_art/"+str(RA)+".txt", "r")
    print(f.read())


while True:
    ascii1()
    print("")
    print("")
    print("░█████╗░████████╗███████╗  ██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██████╗░")
    print("██╔══██╗╚══██╔══╝██╔════╝  ██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██╔══██╗")
    print("██║░░╚═╝░░░██║░░░█████╗░░  ███████║█████╗░░██║░░░░░██████╔╝█████╗░░██████╔╝")
    print("██║░░██╗░░░██║░░░██╔══╝░░  ██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██╔══██╗")
    print("╚█████╔╝░░░██║░░░██║░░░░░  ██║░░██║███████╗███████╗██║░░░░░███████╗██║░░██║")
    print("░╚════╝░░░░╚═╝░░░╚═╝░░░░░  ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝")

    print("")
    print("")
    print("")
    print("           =[ CTF-Helper version 1.1 ")
    print("+ -- -- -- =[ CTF tools at your fingertips ")
    print("+ -- -- -- =[ Star us on github, if you are loving it ")
    print("")
    print("Note: we would love if you could contribute to our project")
    print("")
    print("")

    print("What you wanna do today 0_0:")
    print("")
    print("(-i) install            (-l) list")
    print("(-f) fix                (-h) help")
    print("")
    choice = input()
    if choice == "exit":
        break
    elif choice == "install":
        install()
    elif choice == "list":
        list1()
    elif choice == "fix":
        print('I got bored so I am leaving it here')
    elif choice == "help":
        print('I got bored so I am leaving it here')
    else:
        print("Invalid choice, please choose again\n")

print("Thank you for using ctf-helper")
print(".")
