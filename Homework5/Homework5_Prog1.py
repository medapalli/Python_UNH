def my_range(start, stop=None, step=None):

    if stop == None:
        stop = start + 0
        start = 0

    if step == None:
        step = 1

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield start # return number
        start = start + step

for i in my_range(0,5,2):
    print(i)


for i in my_range(0,5):
    print(i)


