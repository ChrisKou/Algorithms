number_matrix = [
    [1, 37, 7, 4, 5],
    [4, 14, 25, 23, 11],
    [12, 15, 9, 6, 0]
]

highest_number = number_matrix[0][0]
for number_list in number_matrix:
    for number in number_list:
        if number > highest_number:
            highest_number = number
print(highest_number)

condition = True
while condition:
    for number_list in number_matrix:
        new_number = input("Please enter a new number: ")
        if new_number.capitalize() == "Quit":
            condition = False
            break
        number_list.append(int(new_number))


number_matrix[0].sort()
number_matrix[1].sort()
number_matrix[2].sort()
print(number_matrix)

highest_number = number_matrix[0][0]
for number_list in number_matrix:
    for number in number_list:
        if number > highest_number:
            highest_number = number
print(highest_number)


remove_duplicates = input("Would you like to remove duplicates? (Y/N): ")
if remove_duplicates.capitalize() == "Y":
    unique_numbers = []
    for number_list in number_matrix:
        for number in number_list:
            if unique_numbers.count(number) == 0:
                unique_numbers.append(number)
    unique_numbers.sort()
    print(unique_numbers)
