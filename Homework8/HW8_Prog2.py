from random import randrange

print("INTEGER DIVISIONS")
repeat=5
while repeat >=0:
    try:
        #(print(str(a)+"/"+str(b)+"="))
        a = randrange(5)
        b = randrange(5)
        ans=int((input(str(a)+"/"+str(b)+"=")))
        if(a//b)==ans:
            print("CORRECT!")
        else:
            print("INCORRECT!")
            
    except ArithmeticError as e:
        print(e)

    except ValueError:
        print("Please enter Integers Only!")
        
    except TypeError as t:
        print(t)

    repeat-=1
    
    

   
        
