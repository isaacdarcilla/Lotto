#Isaac Arcilla (isaacdarcilla@gmail.com)
#September 14, 2018

import random

print ("Lotto 6-58\n")

def generateNumber():
    lotteryList = []
    for i in range(6):
        lotteryList.append(random.randrange(1 ,58))
    print(lotteryList)
    return lotteryList
def display(lotteryList):
    for i in lotteryList:
        print(i)
lotteryList = generateNumber()
display(lotteryList)
