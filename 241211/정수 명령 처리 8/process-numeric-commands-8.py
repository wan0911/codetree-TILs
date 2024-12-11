import sys

input = sys.stdin.readline

N = int(input().rstrip())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1

    def push_back(self, data):
        new_node = Node(data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail = new_node
            self.head = new_node
            new_node.next = None
        
        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print("List is empty")

        elif self.head.next == None:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data

        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            
            self.node_num -= 1
            return temp.data

    def pop_back(self):
        if self.tail == None:
            print("List is empty")

        elif self.tail.prev == None:
            temp = self.tail
            
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            return temp.data
            
    def size(self):
        return self.node_num

    def empty(self):
        if (self.node_num == 0):
            return 1
        else:
            return 0
            
    def front(self):
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data

    def back(self):
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data
            
llist = linkedList();
for _ in range(N):
    command = input().rstrip().split(" ")
    
    if command[0] == "push_front":
        llist.push_front(command[1])
    elif command[0] == "push_back":
        llist.push_back(command[1])
    elif command[0] == "pop_front":
        print(llist.pop_front())
    elif command[0] == "pop_back":
        print(llist.pop_back())
    elif command[0] == "size":
        print(llist.size())
    elif command[0] == "empty":
        print(llist.empty())
    elif command[0] == "front":
        print(llist.front())
    elif command[0] == "back":
        print(llist.back())