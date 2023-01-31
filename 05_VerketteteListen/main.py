class ListElement:
    def __init__(self, value):
        self.value = value
        self.next = None



class EinfachVerketteteListe:

    def __init__(self):
        self.head = None
        
    def add_at_end(self, value):
        new_ListElem = ListElement(value)
        if not self.head:
            self.head = new_ListElem
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_ListElem

    def get_last(self):
        current = self.head
        while current:
            last = current.value
            current = current.next
        return last

    def get_first(self):
        return self.head.value

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find_elem(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def delete_elem(self,value):
        current = self.head
        while current:
            if current.value == value:
                current.value = None
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next




if __name__ == '__main__':
    list = EinfachVerketteteListe()
    list.add_at_end(1)    
    list.add_at_end(2)    
    list.add_at_end(3)    
    list.add_at_end(4)    

    print(list.get_last())
    print(list.get_first())
    print(list.find_elem(6))
    list.delete_elem(2)
    list.print_list()
