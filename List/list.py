import random

class ListManager:
    def __init__(self):
        self.my_list = []
    
    def generating_lists(self, start, stop, count):
        for _ in range(count):
            self.my_list.append(random.randint(start, stop))
        return self.my_list
    
    def inserting_element(self, position, element):
        self.my_list[position:position] = [element]
        return self.my_list
    pass