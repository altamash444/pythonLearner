from random import choice
import string

def sendword(word):
    if len(word) == 2:
        word.append(word[0])
        word.pop(0)
        return word
    elif len(word) == 1:
        return word
    elif len(word) > 2:
        word.append(word[0])
        word.pop(0)
        word.insert(0, choice(string.ascii_letters).lower())
        word.insert(0, choice(string.ascii_letters).lower())
        word.insert(0, choice(string.ascii_letters).lower())
        word.append(choice(string.ascii_letters).lower())
        word.append(choice(string.ascii_letters).lower())
        word.append(choice(string.ascii_letters).lower())
        return word

def decoder(word):
    if len(word) == 2:
        word.append(word[0])
        word.pop(0)
        return word
    elif len(word) == 1:
        return word
    elif len(word) > 2:
        
        word.pop(0)
        word.pop(0)
        word.pop(0)
        word.pop(len(word)-1)
        word.pop(len(word)-1)
        word.pop(len(word)-1)
        word.insert(0, word.pop(len(word)-1))
        return word
def code():
    print("Enter your messege's words one at a time, you can send the messege by typing 'done'.")
    coded = list()
    confirmList = ['d', 'o', 'n', 'e']

    
    while True:
        word = list(input("type word: "))
        if word == confirmList:
            return coded
            break
        else:
            coded.append(sendword(word))
            if coded[len(coded)-1] == None:
                coded.remove(None)

def decode():
    print("Enter your coded messege's word one at a time, you can confirm by typing 'done'.")
    decoded = list()
    confirmList = ['d', 'o', 'n', 'e']

    while True:
        word = list(input("type word: "))
        if word == confirmList:
            return decoded
            break
        else:
            decoded.append(decoder(word))
            if decoded[len(decoded)-1] == None:
                decoded.remove(None)

while True:
    uchoice = input("Type 'c' to code, or 'd' to decode: ")
    if uchoice.lower() == 'c':
        codedList = code()
        if codedList[0]:
            
            for word in codedList:
                for letter in word:
                    print(letter, end="")
                print(end=" ")
        else:
            print("No messege given.")
        break
    elif uchoice.lower() == 'd':
        decodedList = decode()
        if decodedList[0]:
            for word in decodedList:
                for letter in word:
                    print(letter, end="")
                print(end=" ")
        else:
            print("No messege given.")
        break
    else:
        print("Invalid input, enter again...")
