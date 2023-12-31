# take input from the user
num = int(input("Enter a number: "))

# use a for loop to iterate from 1 to 10
for i in range(1, 11):
    # calculate the product of num and i
    product = num * i

    # print the result
    print(num, "x", i, "=", product)