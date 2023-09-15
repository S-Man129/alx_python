# Print numbers from 0 to 98 in decimal and hexadecimal
for num in range(99):  # Range includes 0 to 98
    decimal = num
    hexadecimal = hex(num)
    print("{} = {}".format(decimal,hexadecimal))
