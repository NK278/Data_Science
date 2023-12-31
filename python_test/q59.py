# Define the list of integers
int_list = [2, 4, 6, 8, 10]

# Initialize the product variable to 1
product = 1

# Loop through each integer in the list and multiply it with the product variable
index = 0
while index < len(int_list):
    product *= int_list[index]
    index += 1

# Print the final product
print(product)