
#install function
install (){
    echo  "Select which category" 
    echo ""
    read CT                       #stores the category in CT
    echo "Select tool"
    echo ""
    read IN                       #stores the tool in IN 
    ./$CT/$IN/install-ctf.sh                  #calls the tool file  
}



#list function
list (){
    
    ETC=`cat ./toolList/index.txt`  
    echo $ETC                       #opens the index.txt which includes the all the categories
    echo "Select Catagory"
    read IN                         #stores the category in IN    
    case $IN in                     #switch case for the various categories, it displays the tool of the category chosen
        1) ETC=`cat ./toolList/Binary.txt`;;
        2) ETC=`cat ./toolList/Crypto.txt`;;
        3) ETC=`cat ./toolList/Fuzzers.txt`;;
        4) ETC=`cat ./toolList/Stego.txt`;;
        *) echo "GUSS HAS HAD A STONK";;
    esac
    echo $ETC
    echo "Press Any Key To Return"
    read $IN

}

#check
check(){
    md5=`md5sum ./Binary`
    echo $md5
}




#main
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
while true; do
read CHC
case $CHC in
    install) install;;
    -i)      install;;
    list)    list;;
    -l)      list;;
    help)    echo "abhi fuction code nahi kara";;
    -h)      echo "abhi fuction code nahi kara";;
    fix)     echo "abhi fuction code nahi kara";;
    -f)      echo "abhi fuction code nahi kara";;
    *)       echo "fuck, didnt think about this one ";;
esac
$CHC = ""
$IN = ""
done