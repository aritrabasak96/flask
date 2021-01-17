n = 10 # size of the list (data bucket)
my_list = [None] * n
flag = 0  # this flag is basically check the number of data present in the list

# probing function
def probing_function(x):

    sum = 9 * x
    return sum



# hash generator
def hashGenerator(inp):

    hashValue = 0
    for i in inp:
        hashValue = hashValue + ord(i)

    return hashValue


# the data is a string
def insertData(key,data):

    hashvalue =  hashGenerator(key)

    # now i have to store this value in the list
    x = 0

    global flag

    while (x < 10):

        find_index = ( hashvalue + probing_function(x) ) % n

        if my_list[find_index] is not None:

            x = x + 1

        else:
            my_list[find_index] = (key,data)
            flag = flag + 1
            break


    return 'successfully inserted'


def findData(key):

    hashvalue = hashGenerator(key)
    findData = ''
    y = 0

    while (y < 10):

        find_index =  ( hashvalue + probing_function(y) ) % n


        if my_list[find_index][0] == key:

            findData = my_list[find_index][1]
            break

        else:
            y = y + 1

    return findData

if __name__ == "__main__":

    insertData('aritra','developer')
    insertData('debesh','businessman')
    insertData('mrinal','businessman')
    insertData('souvik','momoman')
    insertData('dibu','hacker')
    insertData('rimo','teacher')
    insertData('santonu','politician')
    insertData('mou','doctor')
    insertData('rohan','kiteman')
    insertData('priya','nutritianist')



    data = findData('mou')
    print(data)
