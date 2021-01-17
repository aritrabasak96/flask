# create a linked list that contain the data
# we do not use any database here

class Node:

    def __init__(self,*data):

        self.next = None
        self.author = data[0]
        self.description = data[1]
        self.price = data[2]

class Linkedlist:

    def __init__(self):

        self.head = None

    # insert the data
    def insertData(self,*data):

        new_node = Node(*data)

        if self.head is None:  # this is the first time you insert data

            self.head = new_node # point to the first node
        else:

            temp = self.head
            while temp.next is not None:

                temp = temp.next

            temp.next = new_node

    # find the data

    def findData(self):

        data_list = []

        if self.head is None:
            return 'no data'

        else:

            temp = self.head

            while temp is not None:

                data_list.append({'author':temp.author,'desc':temp.description,'price':temp.price})

                temp = temp.next

            return data_list
