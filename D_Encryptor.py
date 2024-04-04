import binascii
import math
import numpy as np
import tkinter as tk

print ("D-Encriptor")

def message():
    m = input(str("write your message"))

    return m

def key():
    key = int(input("write your key"))
    print(key)
    for c in key:
        karray += [ord(c)]

def Text2ASCII(m):
    print(m)
    marray = []
    
    for c in m:
        marray += [ord(c)]
        
    print(marray)
    return marray
        
def CaesarCipher(marray):
    key = 6
    cipherout = []

    for c in marray:
        cipherout.append(c + key)
    
    print(cipherout)
    return cipherout

def CaesarDecipher(marray):
    key = 6
    decipherout = []

    for c in marray:
        decipherout.append(c - key)
    
    print(decipherout)
    return decipherout

def VigenereCipher(marray):
    key = "tractor"
    keyASCII = Text2ASCII(key)
    cipherout = []


    if len(marray) == len(keyASCII):
        for i in range(len(marray)):
            cipherout.append((marray[i] + keyASCII[i])%128)  


    elif len(marray) < len(keyASCII):
        diff = len(keyASCII) - len(marray)
        
        for i in range(diff):
            keyASCII.pop(-i)
            
        for i in range(len(marray)):
            cipherout.append((marray[i] + keyASCII[i])%128)  

    elif len(marray) > len(keyASCII):
        diff = len(marray) - len(keyASCII)
        
        for i in range(diff):
            keyASCII.append(keyASCII[i])
            
        for i in range(len(marray)):
            cipherout.append((marray[i] + keyASCII[i])%128)       
            
    return cipherout
    #c = (p + k)
    
def VigenereDecipher(marray):
    key = "tractor"
    keyASCII = Text2ASCII(key)
    decipherout = []


    if len(marray) == len(keyASCII):
        for i in range(len(marray)):
            decipherout.append((marray[i] - keyASCII[i])%128)  


    elif len(marray) < len(keyASCII):
        diff = len(keyASCII) - len(marray)
        
        for i in range(diff):
            keyASCII.pop(-i)
            
        for i in range(len(marray)):
            decipherout.append((marray[i] - keyASCII[i])%128)  

    elif len(marray) > len(keyASCII):
        diff = len(marray) - len(keyASCII)
        
        for i in range(diff):
            keyASCII.append(keyASCII[i])
            
        for i in range(len(marray)):
            decipherout.append((marray[i] - keyASCII[i])%128)       
            
    return decipherout
    #c = (p + k)    

def RowColumnTCipher(marray):
    key = [5,2,6,1]
    column = len(key)
    row = math.ceil(len(marray)/column)
    
    matrix = [["0" for i in range(column)] for i in range(row)]
    
    index = 0
    for i in range(row):
        for j in range(column):
            if index < len(marray):
                matrix[i][j] = marray[index]
                print(index)
                print(marray[index])
                print(matrix)
                index += 1
            else: break
            
    matrix_np = np.array(matrix)  
    mergedArray = np.concatenate((np.array([key]), matrix_np), axis=0)
    
    #sortedArray = np.array([mergedArray[:, mergedArray[0, :].argsort()]])
    sorted_indices = np.argsort(mergedArray[0])[::]
    sortedArray = mergedArray[:, sorted_indices]

    transposedArray = sortedArray.transpose()
    

    outputList =[]
    for x in np.array(transposedArray[:,1:]).flat:
        print(x)
        outputList.append(int(x))          
    
      
    print("mergedArray")
    print(mergedArray)
    print("sorted array")
    print(sortedArray)
    print("tarray", transposedArray)
    print("outputList", outputList)
    #print(matrix)
    return outputList

def RowColumnTDecipher(marray):
    key = [5,2,6,1]
    sortedKey = sorted(key)
    keyIndex = 0
    print("sortedKey",sortedKey)
    print("key", key)

    column = len(key)
    row = math.ceil(len(marray)/column)
    
    matrix = [[None for i in range(column)] for i in range(row)]
    marrayIndex = 0

    print("matrix", matrix)
 
    for i in range(column):
        current_idx = key.index(sortedKey[keyIndex])
        print("current index", current_idx)
        for j in range(row):
            if marrayIndex < len(marray):
               matrix[j][current_idx] = marray[marrayIndex]
               marrayIndex += 1
               print("matrix icinde",matrix)
            else: break
        keyIndex += 1
            
            
    outputList =[]
    for x in np.array(matrix).flat:
        if x != None:
            print(x)
            outputList.append(int(x)) 
    
    print("outputList", outputList)
    print(matrix)
    return outputList
    
def OutputMessage(method):
    converted_text = ""
    
    for c in method:
        converted_text += chr(c)
        print(c)
        
    print(converted_text)
    return converted_text
    
class MyGUI:
    def __init__(self):
        # Create the main window widget.
        main_window = tk.Tk()
        # Enter the tkinter main loop
        tk.mainloop()

my_gui = MyGUI()

n = message()
#OutputMessage(CaesarCipher(Text2ASCII(n)))

#OutputMessage(VigenereDecipher(Text2ASCII(n)))
#OutputMessage(RowColumnTCipher(Text2ASCII(n)))
#OutputMessage(RowColumnTDecipher(Text2ASCII(n)))
#key() asd
