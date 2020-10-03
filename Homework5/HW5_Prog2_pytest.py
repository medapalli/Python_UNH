def bunny_Ears(bunnies):
    if (bunnies == 0):
        return 0
    elif ((bunnies%2) == 0):
        return 3 + bunny_Ears (bunnies-1)
    else:
        return 2 + bunny_Ears (bunnies-1)
        
    

def testBunny1():
    assert(bunny_Ears(0)==0)
    assert(bunny_Ears(1)==2)
    assert(bunny_Ears(2)==5)
    assert(bunny_Ears(3)==7)




 
    



