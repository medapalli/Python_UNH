import math

lower=1
upper=100
#count = 0



def findguess(guessNo,lower,upper, count):
    print('Is it' + str(upper//2) + '? (yes/no)')
    YN = input().strip()
    if(YN == 'yes'):
        print('Congratulations you did it in ' + str(count) + ' try')
        print("Do you want to play more?")
        YN1=input().strip()
        if(YN1=='yes'):
            binarySearch(upper//2,0,upper,1)
        else:
            return
    else:
        print('if the number larger than ' + str(guessNo) + '? (yes/no)')
        isLarge=input().strip()
        if(isLarge == 'yes'):
            findguess(math.ceil((guessNo+upper)/2), guessNo,upper,count+1)
        else:
            findguess(math.ceil((guessNo+lower)/2), lower,guessNo,count+1)

print('Hello! What is your name?')
myName = input()
print('Hello ' + myName + '! Lets play a game!\n')
print('Think of random number from 1 to 100, and I\'ll try to guess it!')

findguess(upper//2,0,upper,1)
