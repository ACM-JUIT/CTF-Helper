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
        print(TI + ' missing in path!')
        return 'yes'


def install():
    print("select category")
    while True:
        f = open("./toolList/index.txt", "r")
        print(f.read())
        choice = input()
        if choice == "exit":
            exit()
        elif choice == "binary":
            f = open("./toolList/Binary.txt", "r")
            print(f.read())
            break
        elif choice == "crypto":
            f = open("./toolList/Crypto.txt", "r")
            print(f.read())
            break
        elif choice == "stego":
            f = open("./toolList/Stego.txt", "r")
            print(f.read())
            break
        elif choice == "fuzzers":
            f = open("./toolList/Fuzzers.txt", "r")
            print(f.read())
            break
        elif choice == "web":
            f = open("./toolList/web.txt", "r")
            print(f.read())
            break
        else:
            print("Invalid choice, please choose again\n")
    print("select tool")
    TI = input()
    CH = checkinstall(TI)
    if CH == "no":
        print("we are running the tool for you\n")
    else:
        exec(open("./" + choice + "/"+TI+".py").read())

# Fix Function (Md5)
# def fix():
#     import checksumdir
#     hash = checksumdir.dirhash("c:\\temp")


def ascii1():
    RA = random.randint(0, 4)
    f = open("./ascii_art/"+str(RA)+".txt", "r")
    print(f.read())

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

while True:

    print("What you wanna do today 0_0:")
    print("")
    print("install                 help")
    print("fix                     exit")
    print("")
    choice = input()
    if choice == "exit":
        break
    elif choice == "install":
        install()
    elif choice == "fix":
        print('I got bored so I am leaving it here')
    elif choice == "help":
        print('For installing a tool:')
        print('1.Type install and press enter')
        print('2.)You will now see a list of categories of tools')
        print('3.)Type the name of the category you want.For example:Binary')
        print('4.)List of tools will appear.Type the name of the tool you want to unstall and press enter.For example: dex2ja')
        print('5.)Selected tool will soon be downloaded.Happy Hacking! :)')
        print('For exiting type exit and hit enter')
    else:
        print("Invalid choice, please choose again")

print("Thank you for using ctf-helper")
print("Happy Hacking!:)")
