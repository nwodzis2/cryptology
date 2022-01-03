
def countFrequencies(msg):
    my_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    number = 0
    for i in msg:
        if(i != " "):
            number = ord(i) - 97
            my_list[number] += 1
    return my_list
def showFrequiencies(list):
    my_dict = {}
    iterations = 0
    for i in list:
        my_dict[chr(iterations + 97)] = i
        iterations += 1
    print(str(my_dict))

def cosets(msg, n):
    my_list = []
    iterations = 0
    for i in msg:
        if(iterations != 0 and iterations%n == 0):
            my_list.append(msg[iterations - n : iterations])
        iterations += 1
    return my_list

def friedman(msg):
    my_list = []
    IOC = 0
    k = 0
    my_freq = countFrequencies(msg)
    for i in my_freq:
        IOC += i * (i - 1)
    IOC = IOC / (len(msg) * (len(msg) - 1))
    my_list.append(IOC)
    k = abs((0.0265 * len(msg)) / ((0.065 - IOC) + (len(msg) * (IOC  - 0.0385))))
    my_list.append(k)
    return my_list




#tests
print(countFrequencies("hello"))
showFrequiencies( countFrequencies("hello"))
print(str(cosets("hello my name is bob the builder", 3)))
print(str(friedman("hello my name is bob the builder")))