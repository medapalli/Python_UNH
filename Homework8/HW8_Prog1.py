class Animal():
    
    def __init__(self, name):
        self.name=name

       
    def guess_who_am_i(self):

         print("I will give you 3 hints, guess what animal I am\n")
         while True:
             if (self.name=="Elephant"):
                 
                 print("I have exceptional memory")
                 str1=input("Who am I?:")
                 if (str1=="Elephant" or str1=="elephant"):
                     print("You got it! I am  elephant\n")
                     break
                                      
                 else:
                     print("Nope, try again!\n")
                 print("I am the largest land-living mammal in the world\n")
                 str1=input("Who am I?:")
                 if (str1=="Elephant" or str1=="elephant"):
                     print("You got it! I am  elephant\n")
                     break
                                      
                 else:
                     print("Nope, try again!\n")
                 print("I Big Trunk")
                 str1=input("Who am I?:")
                 if (str1=="Elephant" or str1=="elephant"):
                     print("You got it! I am  elephant\n")
                     
                 else:
                     print("I'm out of hints! The answer is: Elephant\n")
                 break
          
             elif (self.name=="Tiger"):
                  
                  
                   
                 print("I am the biggest cat")
                 str1=input("Who am I?:")
                 if (str1=="Tiger" or str1=="tiger"):
                     print("You got it! I am  tiger\n")
                     break
                 else:
                     print("Nope, try again!\n")
                 print("I come in black and white or orange and black\n")
                 str1=input("Who am I?:")
                 if (str1=="Tiger" or str1=="tiger"):
                     print("You got it! I am  tiger\n")
                     break
                 else:
                     print("Nope, try again!\n")
                 print("I am wild Animal ")
                 str1=input("Who am I?:")
                 if (str1=="Tiger" or str1=="tiger"):
                     print("You got it! I am  tiger\n")
                 else:
                     print("I'm out of hints! The answer is: Tiger\n")
                 break
                
             elif (self.name=="Bat"):
                 
                 print("I use echo-location")
                 str1=input("Who am I?:")
                 if (str1=="Bat" or str1=="bat"):
                     print("You got it! I am  Bat\n")
                     break
                 else:
                     print("Nope, try again!\n")
                 print("I can fly")
                 str1=input("Who am I?:")
                 if (str1=="Bat" or str1=="bat"):
                     print("You got it! I am  Bat\n")
                     break
                 else:
                     print("Nope, try again!\n")
                 print("I see well in dark")
                 str1=input("Who am I?:")
                 if (str1=="Bat" or str1=="bat"):
                     print("You got it! I am  Bat\n")
                 else:
                     print("I'm out of hints! The answer is: Bat")
                 break
       
e = Animal("Elephant")
t = Animal("Tiger")
b = Animal("Bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()

        
    
    
