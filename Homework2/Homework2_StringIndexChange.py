def split1(word): 
    return [char for char in word]  
      
# Split string code
print('Please enter string for LeetCode')
word = input()
print('please enter one index at a time and enter after each index')

lst = []
l2=[]
  
# number of elemetns as input 
n = len(word)
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 


#not used :print(index)
l1=split1(word)
print(l1)

string2=''


#for j in lst:
    #for k in l1:
for j in range(0,n):
    #l2.insert(1st[j],l1[j])
    print(word[j])
    print(lst[j])
    l2.insert(lst[j],word[j])
    #l2[lst[j]].append(word[j])
    
print('printing in list format')
print(l2)
for i in l2:  
        string2 += i
print('printing in string format as per reshuffle of index')
print(string2)
    
