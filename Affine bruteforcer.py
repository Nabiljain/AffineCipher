import string
import math

alphabet = dict((enumerate(string.ascii_lowercase, 1)))
msg= input("Enter your message: ")
possible_a_inv = list(range(1, 52, 2))
b = [b1 for b1 in range(1,26)]
file = open("allshifts.txt", "w+")

def inverse(ai):
    for i in possible_a_inv:
        if (ai*i)%26 == 1:
            return i

def closer(msg):
    invalidChars = set(string.punctuation.replace(" ", ""))
    
    if (any(char in invalidChars for char in msg)) or any(num.isdigit() for num in msg):
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

#ai = inverse(a)

def AffineDecryption(msg, a1, b1):
    output = []
    for i in range(len(msg)):
        x = msg[i]
        num = (a1 * (x - b1)) % 26
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

def AllShifts(msg):
    for i in possible_a_inv:
        for j in b:
            dec = (AffineDecryption(msg, i, j))
            print(NumbersToLetters(dec))
            file.write(NumbersToLetters(dec) + "\n")
    file.close()
            

print("msg", msg, "\n")
closer(msg)
#print("n",ConvertLettersToNumbers(msg))
LettToNum = ConvertLettersToNumbers(msg)
#print("e",AffineEncryption(LettToNum))
#print(NumbersToLetters(AffineEncryption(LettToNum)))
#enc = AffineEncryption(LettToNum)
#print("d",AffineDecryption(enc))
AllShifts(LettToNum)
#print("DM",NumbersToLetters(dec))