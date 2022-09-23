from typing import Text


print("\t\t *''WELLCOME''*\t\t")
# print(ord("Z"))
# print(chr(90))
# print(chr(65))
#print(100%101)
def encryption(text,shifts):
    encrypted = ""

    for i in text:
        if i == " ":
        #+= means encrypted = encrypted+ " "
            encrypted += " "
        else:
            #M = 77, A = 65///unicode value without shifting
            # 77 - 65 = (12 = M in alpha) 
            # 12 + 3 = (15 = P in alpha)//shifting in alpha
            # 15 + 65 = 80(P)/////unicode value with shifting
            encrypted += chr((ord(i)-65 +shifts)%26+65)
        

    return encrypted

def decryption(text,shifts):
    encrypted = ""
    for j in text:
        if j == " ":
            encrypted += " "
        else:
            encrypted += chr((ord(j)-65 -shifts)%26+65)
        
    return encrypted


get = input("What do you want to do ? \nEnter E for Encryptio:- \nEnter D for decryption:- ")
#getting all Values in uppercase
Text = input("Enter The text to encrypt or decrypt:- ").upper()
shifts = int(input("Enter the number of shifts 1 To 25:- "))
#Calling both functions
if get == "E" or get == "e":
    print("YOUR CEASER CIPHER TEXT IS :-",encryption(Text ,shifts))
elif get == "D" or get == "d":
    print("YOUR PLAIN TEXT IS :-",decryption(Text,shifts))
else:
    print("you Entered invalid string")

