import string
import random

s_alph = list(string.ascii_lowercase)
c_alph = list(string.ascii_uppercase)
number = []
numberForRandom = 4
for j in range(10):
    number.append(str(j))


def make_random(numberForRandom,checkbox):
    randomPassList = ""
    allPassList = []
    if 's_alph' in checkbox:
        allPassList.append(s_alph)
    if 'c_alph' in checkbox:
        allPassList.append(c_alph)
    if 'num' in checkbox:
        allPassList.append(number)
    
    for i in range(numberForRandom):
        randomPassAll = random.choice(allPassList)
        randomPassList += random.choice(randomPassAll)
    return randomPassList

def create_pass(checkbox,number):

    numberForRandom = int(number)
    randompass = make_random(numberForRandom,checkbox)
    
    print(checkbox)
    
    pass_code = randompass
    return pass_code