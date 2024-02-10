def get_numbers_input():
    numbers = []
    for i in range(10):
        num = input(float(f"Enter a number {i+1}: "))
        numbers.append(num)
    return numbers

def sort_numbers(numbers: list, order: str):
    if order.lower() == 'ascending':
        sorted_numbers = sorted(numbers)
    elif order.lower() == 'decending':
        sorted_numbers = sorted(numbers, reverse= True)
    else:
        print("Invalid order specified. Please enter 'ascending' or 'descending'.")
        sorted_numbers = []
    return sorted_numbers

def sort_string(string: str):
    return ''.join(sorted(string.lower().replace(' ','' )))

def rearrange_sentence(sentence):
    words = sentence.split()
    sorted_sentence = ' '.join(sorted(words))  
    return sorted_sentence
     
def main():
    print("1. Sort numbers ")
    print("2. Sort a string ")
    print("3. Rearrange a sentence ")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        numbers = get_numbers_input()
        user_order = input("Enter 'ascending' or 'descending': ")
        sorted_numbers = sort_numbers(numbers, user_order)
        print("Sorted numbers: ", sorted_numbers)
    elif choice == '2':
        user_string = input("Enter a string: ")
        sorted_string = sort_string(user_string)
        print("sorted_string: ", sorted_string)
    elif choice == '3':
        user_sentence = input("Enter a sentence: ")
        sorted_sentence = rearrange_sentence(user_sentence)
        print("sorted sentence: ",sorted_sentence)
    else:
        print("Invalid choice. Please Enter a valid option")

if __name__ =="__main__":
    main()
