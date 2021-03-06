import subprocess
import random
import os
import shutil
exceptTools=["index.txt"]
tools=os.listdir("./toolList")
tools.remove(exceptTools[0])


def checkinstall(TI):
    rc = subprocess.call(['where', TI])
    if rc == 0:
        print(TI + 'installed!')
        print('do you want to reinstall(yes/no)')
        YO = input()
        return YO
    else:
        print(TI + ' missing in path!')
        return 'yes'


def uninstall():
    print("Which tool you want to uninstall?")
    UT = input("Choice:")
    ans = os.path.isdir('Tools/'+UT)
    if ans:
        print("The tool is being uninstalled")
        print("..")
        print("..")
        print("..")
        directory = UT
        parent = "Tools/"
        path = os.path.join(parent, directory)
        shutil.rmtree(path)
        print("Tool is uninstalled")
    else:
        print("Tool is not installed")

def streamOptions(choice):
    choice=str(choice).lower()
    f = os.listdir(f"./{choice}")
    print("\n".join([i for i in f]))

def install():
    print("select category")
    while True:
        print("\n".join([i.replace(".txt","") for i in tools]))
        choice = input("Choice:")
        if choice == "exit":
            exit()
        elif f"{choice}.txt" in tools:
            streamOptions(choice)
            break
        else:
            print("Invalid choice, please choose again\n")
    print("select tool")
    TI = input("Choice:")
    CH = checkinstall(TI)
    if CH == "no":
        print("we are running the tool for you\n")
    else:
        try:
            exec(   open("./" + choice.lower() + "/" + TI + ".py").read())
        except(Exception):
            print("Tools coming soon")

# Fix Function (Md5)
def fix():
    # if(subprocess.call("git remote -v"))
    # print(subprocess.call("git remote -v"))
    subprocess.call("git fetch && git reset --hard",shell=True)
    # import checksumdir
    # hash = checksumdir.dirhash("c:\\temp")


def ascii1():
    RA = random.randint(0, 5)
    f = open("./ascii_art/" + str(RA) + ".txt", "r")
    print(f.read())
    print("")
    print("           =[ CTF-Helper version 1.1 ")
    print("+ -- -- -- =[ CTF tools at your fingertips ")
    print("+ -- -- -- =[ Star us on github, if you are loving it ")
    print("")
    print("Note: we would love if you could contribute to our project")
    print("")
    print("")

def main():
    ascii1()

    while True:
        a='\t'*2
        print("What you wanna do today 0_0:",end="\n\n")
        print(f"install (i){a}exit(e)")
        print(f"uninstall(u){a}fix(f)")
        print("help(h)")
        print("")
        choice = input("Choice:")
        if choice == "exit" or choice =="e":
            break
        elif choice == "install" or choice =="i":
            install()
        elif choice == "uninstall" or choice =="u":
            uninstall()
        elif choice == "fix" or choice =="f":
            fix()
            # print('I got bored so I am leaving it here')
        elif choice == "help" or choice =="h":
            subprocess.call("cls",shell=True)
            ascii1()
            print('For installing a tool:')
            print('1.Type install and press enter')
            print('2.)You will now see a list of categories of tools')
            print('3.)Type the name of the category you want.For example:Binary')
            print(
                '4.)List of tools will appear.Type the name of the tool you want to unstall and press enter.For example: dex2ja')
            print('5.)Selected tool will soon be downloaded.Happy Hacking! :)')
            print('For exiting type exit and hit enter')
        else:
            print("Invalid choice, please choose again")

    print("Thank you for using ctf-helper")
    print("Happy Hacking!:)")


# START
if __name__ == '__main__':
    main()