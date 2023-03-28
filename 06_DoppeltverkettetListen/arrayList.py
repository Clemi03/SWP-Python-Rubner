class ArrayList:
    def __init__(self):
        self.list = []

    def add_at_end(self, data):
        self.list.append(data)

    def get_last(self):
        return self.list[len(self.list)-1]

    def get_first(self):
        if len(self.list) > 0:
            return self.list[0]
        else:
            return None
    
    def get_length(self):
        return len(self.list)

    def find_elem(self,value):
        for i in self.list:
            if i == value:
                return True
        return False       


    def delete_elem(self, data):
        for i in self.list:
            if i == data:
                self.list.remove(i)

    def print_list(self):
        print(self.list)


if __name__ == '__main__':
    arraylist = ArrayList()
    arraylist.add_at_end(1)
    arraylist.add_at_end(2)
    arraylist.add_at_end(3)
    arraylist.print_list()
    arraylist.delete_elem(2)
    arraylist.print_list()
    print(arraylist.get_length())
    print(arraylist.get_first())
    print(arraylist.get_last())
    print(arraylist.find_elem(2))
