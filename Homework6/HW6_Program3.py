import time
import shelve

dict={'name':'sameer', 'job':'software engineer','salary':10000}
shfile = shelve.open("shelf_file")

shfile.update(dict)

def timedurationDecorator(func):
    def inner():
        print("Dictionary exection time\n")
        start=time.time()
        print(dict)
        end=time.time()
        print(str(end-start))
        func()
        print("Shelve exection time\n")
        start=time.time()
        print(list(shfile.items()))
        end=time.time()
        print(str(end-start))
        
    return inner

@timedurationDecorator
def functionTime():
    print("Dictionary Vs Shelve exection time")


functionTime()
