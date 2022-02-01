#Python code that takes a number & returns a list of its digits
#Using Function
def return_list_of_digits(number_1):
    c = str(number_1)
    int_list = []
    for i in range(len(c)):
        int_list.append(int(c[i]))
    return int_list
input_number = input("Enter the number: ")
list_of_digits = return_list_of_digits(input_number)
print(list_of_digits)