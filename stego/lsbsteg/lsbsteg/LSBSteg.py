#!/usr/bin/env python
# coding=UTF-8
'''
Copyright © 2015, Robin David - MIT-Licensed

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The Software is provided "as is", without warranty of any kind, express or implied, including but not limited
to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall
the authors or copyright holders X be liable for any claim, damages or other liability, whether in an action
of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other
dealings in the Software.

Except as contained in this notice, the name of the Robin David shall not be used in advertising or otherwise
to promote the sale, use or other dealings in this Software without prior written authorization from the Robin David.
'''

"""
How to install the dependencies on a mac
----------------------------------------

1) Reinstall brew.
```bash
rm -rf /usr/local/Cellar /usr/local/.git && brew cleanup
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2) Install opencv
```bash
brew tap homebrew/science
brew install opencv
```
3) Add the packages to python
```bash
mkdir -p $HOME/Library/Python/2.7/lib/python/site-packages
echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> $HOME/Library/Python/2.7/lib/python/site-packages/homebrew.pth
```
"""

import cv2 as cv
import sys

class SteganographyException(Exception):
    pass

class LSBSteg():
    def __init__(self, im):
        self.image = im
        self.width = im.width
        self.height = im.height
        self.size = self.width * self.height
        self.nbchannels = im.channels
        
        self.maskONEValues = [1,2,4,8,16,32,64,128]
        #Mask used to put one ex:1->00000001, 2->00000010 .. associated with OR bitwise
        self.maskONE = self.maskONEValues.pop(0) #Will be used to do bitwise operations
        
        self.maskZEROValues = [254,253,251,247,239,223,191,127]
        #Mak used to put zero ex:254->11111110, 253->11111101 .. associated with AND bitwise
        self.maskZERO = self.maskZEROValues.pop(0)
        
        self.curwidth = 0 #Current width position
        self.curheight = 0 #Current height position
        self.curchan = 0 #Current channel position
     
    def saveImage(self,filename):
    # Save the image using the given filename
        cv.SaveImage(filename, self.image)
                    

    def putBinaryValue(self, bits): #Put the bits in the image
        for c in bits:
            val = list(self.image[self.curheight,self.curwidth]) #Get the pixel value as a list
            if int(c) == 1:
                val[self.curchan] = int(val[self.curchan]) | self.maskONE #OR with maskONE
            else:
                val[self.curchan] = int(val[self.curchan]) & self.maskZERO #AND with maskZERO
                
            self.image[self.curheight,self.curwidth] = tuple(val)
            self.nextSpace() #Move "cursor" to the next space
        
    def nextSpace(self):#Move to the next slot were information can be taken or put
        if self.curchan == self.nbchannels-1: #Next Space is the following channel
            self.curchan = 0
            if self.curwidth == self.width-1: #Or the first channel of the next pixel of the same line
                self.curwidth = 0
                if self.curheight == self.height-1:#Or the first channel of the first pixel of the next line
                    self.curheight = 0
                    if self.maskONE == 128: #Mask 1000000, so the last mask
                        raise SteganographyException, "Image filled"
                    else: #Or instead of using the first bit start using the second and so on..
                        self.maskONE = self.maskONEValues.pop(0)
                        self.maskZERO = self.maskZEROValues.pop(0)
                else:
                    self.curheight +=1
            else:
                self.curwidth +=1
        else:
            self.curchan +=1

    def readBit(self): #Read a single bit int the image
        val = self.image[self.curheight,self.curwidth][self.curchan]
        val = int(val) & self.maskONE
        self.nextSpace()
        if val > 0:
            return "1"
        else:
            return "0"
    
    def readByte(self):
        return self.readBits(8)
    
    def readBits(self, nb): #Read the given number of bits
        bits = ""
        for i in range(nb):
            bits += self.readBit()
        return bits

    def byteValue(self, val):
        return self.binValue(val, 8)
        
    def binValue(self, val, bitsize): #Return the binary value of an int as a byte
        binval = bin(val)[2:]
        if len(binval) > bitsize:
            raise SteganographyException, "binary value larger than the expected size"
        while len(binval) < bitsize:
            binval = "0"+binval
        return binval

    def hideText(self, txt):
        l = len(txt)
        binl = self.binValue(l, 16) #Length coded on 2 bytes so the text size can be up to 65536 bytes long
        self.putBinaryValue(binl) #Put text length coded on 4 bytes
        for char in txt: #And put all the chars
            c = ord(char)
            self.putBinaryValue(self.byteValue(c))
       
    def unhideText(self):
        ls = self.readBits(16) #Read the text size in bytes
        l = int(ls,2)
        i = 0
        unhideTxt = ""
        while i < l: #Read all bytes of the text
            tmp = self.readByte() #So one byte
            i += 1
            unhideTxt += chr(int(tmp,2)) #Every chars concatenated to str
        return unhideTxt

    def hideImage(self, imtohide):
        w = imtohide.width
        h = imtohide.height
        if self.width*self.height*self.nbchannels < w*h*imtohide.channels:
            raise SteganographyException, "Carrier image not big enough to hold all the datas to steganography" 
        binw = self.binValue(w, 16) #Width coded on to byte so width up to 65536
        binh = self.binValue(h, 16)
        self.putBinaryValue(binw) #Put width
        self.putBinaryValue(binh) #Put height
        for h in range(imtohide.height): #Iterate the hole image to put every pixel values
            for w in range(imtohide.width):
                for chan in range(imtohide.channels):
                    val = imtohide[h,w][chan]
                    self.putBinaryValue(self.byteValue(int(val)))

                    
    def unhideImage(self):
        width = int(self.readBits(16),2) #Read 16bits and convert it in int
        height = int(self.readBits(16),2)
        unhideimg = cv.CreateImage((width,height), 8, 3) #Create an image in which we will put all the pixels read
        for h in range(height):
            for w in range(width):
                for chan in range(unhideimg.channels):
                    val = list(unhideimg[h,w])
                    val[chan] = int(self.readByte(),2) #Read the value
                    unhideimg[h,w] = tuple(val)
        return unhideimg
    
    def hideBin(self, filename):
        f = open(filename,'rb')
        bin = f.read()
        l = len(bin)
        if self.width*self.height*self.nbchannels < l+64:
            raise SteganographyException, "Carrier image not big enough to hold all the datas to steganography"
        self.putBinaryValue(self.binValue(l, 64))
        for byte in bin:
            self.putBinaryValue(self.byteValue(ord(byte)))
    
    def unhideBin(self):
        l = int(self.readBits(64),2)
        output = ""
        for i in range(l):
            output += chr(int(self.readByte(),2))
        return output



'''
Methods to expose this functionality to the command-line
'''
def binary_steg_hide(image, binary, result):
    carrier = cv.LoadImage(image)
    steg = LSBSteg(carrier)
    steg.hideBin(binary)
    steg.saveImage(result)

def binary_steg_reveal(steg_image, out):
    inp = cv.LoadImage(steg_image)
    steg = LSBSteg(inp)
    bin = steg.unhideBin()
    f = open(out, "wb")
    f.write(bin)
    f.close()

import argparse

parser = argparse.ArgumentParser(description='This python program applies LSB Steganography to an image and some type of input')

def main(av):
    bgroup = parser. add_argument_group("Hide binary with steg")
    bgroup.add_argument('-image', help='Provide the original image')
    bgroup.add_argument('-binary', help='The binary file to be obfuscated in the image')
    bgroup.add_argument('-steg-out', help='The resulting steganographic image')

    bgroup = parser.add_argument_group("Reveal binary")
    bgroup.add_argument('-steg-image', help='The steganographic image')
    bgroup.add_argument('-out', help='The original binary')

    args = parser.parse_args(av[1:])

    if len(av) == 7:
	binary_steg_hide(args.image, args.binary, args.steg_out)
    elif len(av) == 5:
        binary_steg_reveal(args.steg_image, args.out)
    else:
        print "Usage: '", av[0], "-h' for help", "\n", args

if __name__=="__main__":
    from sys import argv as av
    main(av)

