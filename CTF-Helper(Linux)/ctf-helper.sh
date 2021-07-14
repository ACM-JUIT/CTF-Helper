#checks if the software is installed
checkinstall (){
    if which $IN >/dev/null; then             #checks if the software is installed
    echo ""
    printf "${GREEN}[+] The program is already installed you are good to go ;)\n${NC}"
    printf "${ORANGE}[*] do you want to reinstall it (yes/no)\n${NC}"
    echo ""
    read YE
    if [ "$YE" = "yes" ]; then
    sudo apt --purge remove $IN
    echo ""
    fi
    elif [[ -d "$IN" ]]; then
    echo ""
    printf "${GREEN}[+] The program is already installed you are good to go ;)\n${NC}"
    printf "${ORANGE}[*] do you want to reinstall it (yes/no)\n${NC}"
    echo ""
    read YE
        if [ "$YE" = "yes" ]; then
        sudo rm -r $IN
        else
        echo ""
        fi
    else
    echo ""
    printf "${RED}[-] The program is not installed, dont worry we will install it for you\n${NC}"
    fi
}



uninstall (){
    echo ""
    printf "${ORANGE}[*] which tools you want to uninstall:\n${NC}"
    echo ""
    read UN
    if [[ -d "$UN" ]]; then
    sudo rm -r $UN
    printf "${GREEN}[+] Tool is uninstalled\n${NC}"
    elif apt list -a $UN  2>/dev/null; then
    sudo apt --purge remove $UN
    printf "${GREEN}[+] Tool is uninstalled\n${NC}"
    else
    printf "${RED}[ERR] Tool is not installed\n${NC}"
    fi
}




run (){
    if [ "$MD" == "69" ]; then
    echo ""
    printf "${ORANGE}[*] which tool you want to run\n${NC}"
    echo ""
    read IN
    if which $IN || [[ -d "$IN" ]]; then
    printf "${GREEN}[++] run your tool, try $IN -h or if you have to install the setup cd $IN \n${NC}"
    echo ""
    while true;do
    read CD
    if [ "$CD" == "exit" ]; then
    break
    else
    $CD  2>/dev/null
    fi
    done
    else
    printf "${RED}[-] The tool is not installed\n${NC}"
    printf "${ORANGE}[*] Do you want to install the tool(yes/no)\n${NC}"
    echo ""
    read YN
    if [ "$YN" == "yes" ]; then
    install
    else
    echo ""
    fi
    fi
    else
    printf "${GREEN}[++] run your tool, try $IN -h or if you have to install the setup cd $IN \n${NC}"
    echo ""
    while true;do
    read CD
    if [ "$CD" == "exit" ]; then
    break
    else
    $CD 2>/dev/null
    fi
    done
    fi
}

#install function
install (){
    list    
    checkinstall
    if [ "$YE" = "no" ]; then
    run    
    else 
        chmod +x  ./$CT/$IN/install-ctf.sh                 
        ./$CT/$IN/install-ctf.sh 2>/dev/null      #installing the tool
        echo ""
        printf "${GREEN}[+] Tool is installed\n${NC}"
        run
    fi
    
}



#list function
list (){
    printf  "${ORANGE}[*] Select which category\n${NC}" 
    echo ""
    cat ./toolList/index.txt
    echo ""
    read CT                         #stores the category in CT
    echo ""
    case $CT in                     #switch case for the various categories, it displays the tool of the category chosen
        Binary) cat ./toolList/Binary.txt;;
        crypto) cat ./toolList/Crypto.txt;;
        fuzzers)cat ./toolList/Fuzzers.txt;;
        stego)  cat ./toolList/Stego.txt;;
        web)    cat ./toolList/web.txt;;
     exit) break;;  
        *) printf "${RED}[ERR] select from the options available\n${NC}";;
    esac
    echo ""
    printf "${ORANGE}[*] Select your tool\n${NC}"
    read IN                       #stores the tool in IN 
    echo ""
}

#check
check (){
     
    HA=find . -type f -exec md5sum {} + | LC_ALL=C sort | md5sum  #finds the hash
    if [$HA == 121c476533b28474dc2e09d9b6751ca0]; then            #checks if the hash is same    
    echo "[+] you are good to go"                                       
    else
    echo "[-] your files are little messed up let us fix it for you"
    #git pull repository_link                           
    fi 
}

ascii (){

    AF=$(($RANDOM%4))
    chmod +x ./Ascii_art/$AF.sh
    ./Ascii_art/$AF.sh
}

help (){
        echo 'For installing a tool:'
        echo '1.Type install and press enter'
        echo '2.)You will now see a list of categories of tools'
        echo '3.)Type the name of the category you want.For example:Binary'
        echo '4.)List of tools will appear.Type the name of the tool you want to unstall and press enter.For example: dex2ja'
        echo '5.)Selected tool will soon be downloaded.Happy Hacking! :)'
        echo 'For exiting type exit and hit enter'
}

#main
#AF=`cat ./Ascii_art/3.txt`
#echo $AF
while true; do
ascii
ORANGE='\033[0;33m'
PURPLE='\033[0;35m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Colo
echo ""
echo ""
echo "
░█████╗░████████╗███████╗  ██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██████╗░
██╔══██╗╚══██╔══╝██╔════╝  ██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██╔══██╗
██║░░╚═╝░░░██║░░░█████╗░░  ███████║█████╗░░██║░░░░░██████╔╝█████╗░░██████╔╝
██║░░██╗░░░██║░░░██╔══╝░░  ██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██╔══██╗
╚█████╔╝░░░██║░░░██║░░░░░  ██║░░██║███████╗███████╗██║░░░░░███████╗██║░░██║
░╚════╝░░░░╚═╝░░░╚═╝░░░░░  ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝"
echo ""
echo ""
echo ""
printf "${ORANGE}           =[ CTF-Helper version 1.1\n${NC}" 
printf "${ORANGE}+ -- -- -- =[ CTF tools at your fingertips\n${NC}"
printf "${ORANGE}+ -- -- -- =[ Star us on github, if you are loving it\n${NC}"
echo ""
printf "${GREEN}[++] we would love if you could contribute to our project${NC}"
echo ""
echo ""


echo "What you wanna do today 0_0:";
echo ""
echo "(-i) install            (-e) exit"
echo "(-u) uninstall          (-r) run"
echo "(-f) fix                (-h) help"

echo ""

read CHC                                          #reads
case $CHC in
    install) install;;                            #calls install function
    -i)      install;;                      
    list)    list;;                               #calls list function  
    -l)      list;;                                 
    help)    help;;                               #calls help funtion(not coded)    
    -h)      help;; 
    fix)     check;;                              #calls fix function  
    -f)      check;;
    uninstall) uninstall;;
    -u)      uninstall;;
    run)    MD="69"
            run;;
    -r)     MD="69"
            run;;   
    exit)    break;;
    *)       printf "${RED}[ERR] fuck, didnt think about this one${NC}";; #default case
esac
done