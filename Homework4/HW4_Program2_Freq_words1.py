#Program to count frequency of words and put it in dictionary format
#with Word as Key and Frequency as Values

def count_frequency(list):
    wordfreq=[list.count(p) for p in list]
    return dict(zip(list,wordfreq))

mylist = ["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"] 

print(count_frequency(mylist))
