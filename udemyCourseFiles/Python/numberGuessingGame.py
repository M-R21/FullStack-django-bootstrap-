import random

def genRandom():
    list_n = list(range(1,10))
    number = []
    n = random.choice(list_n)
    number.append(n)
    list_n.remove(n)
    list_n.append(0)
    for i in range(2):
        n = random.choice(list_n)
        number.append(n)
        list_n.remove(n)
    return number


n = genRandom()
# print(n)
length =  len(n)
print('Number has been generated')
while(True):
    n1 = input('Enter your guess: ')
    guess = [int(x) for x in n1]
    match = 0
    matched = [0 for x in range(length)]
    for i in range(length):
        if guess[i] == n[i]:
            matched[i] = 1
            match+=1

    print("match:",match)

    if(match<2):
        close = 0
        for i in range(length):
            if matched[i] == 0:
                if n[i] in guess:
                    close+=1
        print("close:",close)

    if(match == 3):
        print('congratulations,you have guessed the correctnumber :',n1)
        break
