prompt = "Please enter a number: "
numbers = [int(input(prompt)), int(input(prompt)), int(input(prompt)),
           int(input(prompt)), int(input(prompt))]

for x_count in numbers:
    output = ''
    for x in range(x_count):
        output += 'x'
    print(output)
