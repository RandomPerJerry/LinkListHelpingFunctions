import random

class Node:
    def __init__(self, val):

        self.val = val
        self.next = None
class LinkList:
    def __init__(self):

        self.head = None
        self.ptr = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def get_last_node(self):
        if not self.head:
            return None

        current = self.head
        while current.next:
            current = current.next

        return current
    
    def list_all_values(self, output_list):

        if self.head == None:
            return None
        
        current = self.head
        
        while current:
            output_list.append(current.val)
            current = current.next

    def serach_value(self, target_value, output_list):
        # Put the index of all target_value and its adress in the output_list

        if self.head == None:
            return None
        
        current = self.head
        index_count = 0

        while current:
            if current.val == target_value:
                output_list.append((index_count, current))

            index_count += 1
            current = current.next



            




my_LinkList = LinkList()

for n in range(10):
    my_LinkList.push(n)

my_head = my_LinkList.head

my_list1 = []
my_list2 = []

my_LinkList.list_all_values(my_list1)

print(my_list1)





