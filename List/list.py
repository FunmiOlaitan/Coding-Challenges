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
    
    def extract_list_of_list(self, input_list, num_list, num_elements):
        list_of_list = []
        for _ in range(num_list):
            random_elements = random.sample(input_list, num_elements)
            list_of_list.append(random_elements)
        return list_of_list
    
    def sort_list_of_list(self, list_of_lists):
        return sorted(list_of_lists)

if __name__ == "__main__":
    pass