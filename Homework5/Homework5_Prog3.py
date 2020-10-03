import time
def timedurationDecorator(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print(str(end-start))
        
    return inner

@timedurationDecorator
def functionTime():
    print("Test function exection time")


functionTime()
