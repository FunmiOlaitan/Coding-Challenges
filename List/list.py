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
    manager = ListManager()

    # Generate a list of random integers
    generated_list = manager.generated_list(1, 20, 10)
    print('Generated List:', generated_list)

    # Insert an element into the generated list
    modified_list = manager.inserting_element(3, 2)
    print('Modified List:', modified_list)

    # Extract list of lists from the modified list
    list_of_lists = manager.extract_list_of_list(modified_list, 3, 3)
    print("List of Lists:", list_of_lists)

    # Sort the list of lists
    sorted_list_of_lists = manager.sort_list_of_list(list_of_lists)
    print("sorted List of List:", sorted_list_of_lists)