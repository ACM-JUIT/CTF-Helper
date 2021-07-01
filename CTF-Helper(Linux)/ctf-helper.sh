#checks if the software is installed
checkinstall (){
    if which $IN >/dev/null; then             #checks if the software is installed
    echo ""
    echo "The program is already installed you are good to go ;)"
    echo "do you want to reinstall it (yes/no)"
    echo ""
    read YE           
    else
    echo ""
    echo "The program is not installed, dont worry we will install it for you"
    fi
}


#install function
install (){
    echo  "Select which category" 
    echo ""
    read CT                       #stores the category in CT
    echo "Select tool"
    echo ""
    read IN                       #stores the tool in IN 
    checkinstall
    if [ "$YE" = "no" ]; then
    $IN                          #calls the tool file  
    else                            
    ./$CT/$IN/install-ctf.sh      #
    fi
}



#list function
list (){
    while true; do
    ./toolList/index.sh  
    echo $ETC                       #opens the index.txt which includes the all the categories
    echo "Select Catagory"
    read IN                         #stores the category in IN    
    case $IN in                     #switch case for the various categories, it displays the tool of the category chosen
        1) ETC=`cat ./toolList/Binary.txt`;;
        2) ETC=`cat ./toolList/Crypto.txt`;;
        3) ETC=`cat ./toolList/Fuzzers.txt`;;
        4) ETC=`cat ./toolList/Stego.txt`;;
     exit) break;;  
        *) echo "Helper HAS HAD A STONK";;
    esac
    echo $ETC
    echo "Press Any Key To Return"
    read $IN
    done
}

#check
check (){
     
    HA=find . -type f -exec md5sum {} + | LC_ALL=C sort | md5sum  #finds the hash
    if [$HA == 121c476533b28474dc2e09d9b6751ca0]; then            #checks if the hash is same    
    echo "you are good to go"                                       
    else
    echo "your files are little messed up let us fix it for you"
    #git pull repository_link                           
    fi 
}

ascii (){

    AF=$(($RANDOM%4))
    chmod +x ./Ascii_art/$AF.sh
    ./Ascii_art/$AF.sh
}


#main
#AF=`cat ./Ascii_art/3.txt`
#echo $AF
while true; do
ascii

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
echo "           =[ CTF-Helper version 1.1 " 
echo "+ -- -- -- =[ CTF tools at your fingertips "
echo "+ -- -- -- =[ Star us on github, if you are loving it "
echo ""
echo "Note: we would love if you could contribute to our project"
echo ""
echo ""


echo "What you wanna do today 0_0:";
echo ""
echo "(-i) install            (-l) list"
echo "(-f) fix                (-h) help"
echo ""



read CHC                                          #reads
case $CHC in
    install) install;;                            #calls install function
    -i)      install;;                      
    list)    list;;                               #calls list function  
    -l)      list;;                                 
    help)    echo "abhi fuction code nahi kara";; #calls help funtion(not coded)    
    -h)      echo "abhi fuction code nahi kara";; 
    fix)     check;;                              #calls fix function  
    -f)      echo "abhi fuction code nahi kara";;
    exit)    break;;
    *)       echo "fuck, didnt think about this one ";; #default case
esac
done