def bunny_Ears(bunnies):
    if (bunnies == 0):
        return 0
    elif ((bunnies%2) == 0):
        return 3 + bunny_Ears (bunnies-1)
    else:
        return 2 + bunny_Ears (bunnies-1)
        
    



print(bunny_Ears(0))
print(bunny_Ears(1))
print(bunny_Ears(2))
print(bunny_Ears(3))

