class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def add_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1
        
    def get_last(self):
        return self.tail.data

    def get_first(self):
        return self.head.data
    
    def get_length(self):
        return self.length

    def find_elem(self,value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False


    def delete_elem(self, data):
        if self.head is None:
            print("List is empty")
            
        if self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        else:
            current_node = self.head.next
            
            while current_node is not None and current_node.data != data:
                current_node = current_node.next
                
            current_node.prev.next = current_node.next # damit Zeiger nicht mehr auf zu löchendes Element zeigt
            if current_node.next is not None:
                current_node.next.prev = current_node.prev
            else:
                self.tail = current_node.prev
                
        self.length -= 1

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()



if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_at_end(1)
    doubly_linked_list.add_at_end(2)
    doubly_linked_list.add_at_end(3)
    doubly_linked_list.print_list()
    doubly_linked_list.delete_elem(2)
    doubly_linked_list.print_list()

    print(doubly_linked_list.get_last())
    print(doubly_linked_list.find_elem(3))
