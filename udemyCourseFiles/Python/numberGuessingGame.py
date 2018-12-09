import random

#function to generate a 3 digit  random number with unique digits
def genRandom(n_digits):
    list_n = list(range(1,10))
    number = []
    n = random.choice(list_n)
    number.append(n)
    list_n.remove(n)
    list_n.append(0)
    for i in range(n_digits -1):
        n = random.choice(list_n)
        number.append(n)
        list_n.remove(n)
    return number

#function to play the game
def play(n_digits):
    while(True):
        n1 = input('Enter your guess: ')
        if(len(n1)!=n_digits):
            print("Guessed number does not have",n_digits,"digits, please guess again\n")
            continue
        guess = [int(x) for x in n1]
        match = 0
        matched = [0 for x in range(length)]
        for i in range(length):
            if guess[i] == n[i]:
                matched[i] = 1
                match+=1

        print("Matches:",match)

        if(match == 3):
            print('Congratulations!!!, you have guessed the correct number :',n1)
            return

        if(match<2):
            close = 0
            for i in range(length):
                if matched[i] == 0:
                    if n[i] in guess:
                        close+=1
            print("Close:",close)
        print()



n_digits = 3
n = genRandom(n_digits)
length =  len(n)
print("WELCOME TO NUMBER GUESSING GAME")
print("---> You are supposed to guess a 3 digit number")
print("---> The number has all unique digits \n")
print("Hints are provided when you guess a wrong number")
print("--->'Matches' => This number of digits have been correctly guessed and are at the right position")
print("---->'Close'+> This number of digits are present in the number but are not at the correct place\n")
print('Number has been generated, now try to guess it\n')
play(n_digits)
