# Print numbers from 0 to 99 in ascending order with two digits, separated by ", "
for num in range(100):  # Range includes 0 to 99
    formatted_num = f"{num:02d}"
    # Print the formatted number followed by a comma and a space
    print(formatted_num, end=", ")