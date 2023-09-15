# Print numbers from 0 to 99 in ascending order with two digits, separated by ", "
for num in range(100):
    if num < 99:
        print("{:02d}, ".format(num), end="")
    else:
        print("{:02d}".format(num))
