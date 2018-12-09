import string
import math

alphabet = dict((enumerate(string.ascii_lowercase, 1)))
msg= input("Enter your message: ")
a= int(input("Enter A: "))
possible_a_inv = [x for x in range(0,26) if math.gcd(1, 26) == 1]
b= int(input("Enter B: "))

def inverse(ai):
    for i in possible_a_inv:
        if (ai*i)%26 == 1:
            return i

def closer(msg):
    invalidChars = set(string.punctuation.replace(" ", ""))
    
    if (inverse(a) == 0):
        print("The inverse for the supplied 'A' value doesn't exist")
        exit()
    elif (any(char in invalidChars for char in msg)) or any(num.isdigit() for num in msg):
        print("You have entered invalid characters")
        exit()

def ConvertLettersToNumbers(msg):
    input=msg.lower()
    input = input.replace(" ","")
    output = []
    for i in input:
        num = (ord(i) - 96)
        output.append(num)
    #print(type(output[1]))
    return output

def AffineEncryption(msg):
    output = []
    for i in range(len(msg)):
        x = msg[i]
        num = ((a * x) + b) % 26
        #num = (a * x + b) % 26
        if (num == 0):
            num = 26
        output.append(num)
        #print(output[i])
    return output

ai = inverse(a)

def AffineDecryption(msg):
    output = []
    for i in range(len(msg)):
        x = msg[i]
        num = (ai * (x - b)) % 26
        if (num == 0):
            num = 26
        output.append(int(math.ceil(num)))
    return output

def NumbersToLetters(msg):
    output = []
    for i in range(len(msg)):
        letter = alphabet[msg[i]]
        output.append(letter)
    return ''.join(output)

#For Debugging
def Checker(cleartext, decrypted):
    
    if (cleartext == decrypted):
        print("Success")
    else:
        print("Fail")

def Encrypt(msg):
    closer(msg)
    LettToNum = ConvertLettersToNumbers(msg)
    num = AffineEncryption(LettToNum)
    ciphertext = NumbersToLetters(num)
    return ciphertext

def Decrypt(msg):
    LettToNum = ConvertLettersToNumbers(msg)
    decNum = AffineDecryption(LettToNum)
    cleartext = NumbersToLetters(decNum)
    return cleartext
   
#print("The message given is", msg)
#print("The ciphertext is:", Encrypt(msg))

#ciphertext = Encrypt(msg)

#print("The cleartext is:", Decrypt(ciphertext))

#Checker(ConvertLettersToNumbers(msg), AffineDecryption(AffineEncryption(ConvertLettersToNumbers(msg))))
      
print("The message entered is:", msg)
closer(msg)
print("n",ConvertLettersToNumbers(msg))
LettToNum = ConvertLettersToNumbers(msg)
print("e",AffineEncryption(LettToNum))
print("The encrypted message is:", NumbersToLetters(AffineEncryption(LettToNum)))
enc = AffineEncryption(LettToNum)
print("d",AffineDecryption(enc))
dec = AffineDecryption(enc)
print("The decrypted message is",NumbersToLetters(dec))
print(Checker(LettToNum, dec))
input()