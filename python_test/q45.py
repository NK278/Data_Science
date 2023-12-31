import csv

def calculate_column_average(csv_file_path, column_index):
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Skip the header if it exists
        next(csv_reader, None)
        val=[float(r[column_index]) for r in csv_reader]
        avg=sum(val)/len(val)
        return avg        
        # # Initialize variables for sum and count
        # total_sum = 0
        # count = 0

        # # Iterate through the rows and calculate the sum and count
        # for row in csv_reader:
        #     try:
        #         # Convert the column value to a float
        #         column_value = float(row[column_index])
                
        #         # Update sum and count
        #         total_sum += column_value
        #         count += 1
        #     except ValueError:
        #         # Handle the case where the column value is not a valid float
        #         print(f"Invalid value in row {csv_reader.line_num}, column {column_index + 1}")

        # # Calculate the average
        # if count > 0:
        #     average = total_sum / count
        #     return average
        # else:
        #     return None

# Example usage
csv_file_path = 'stud.csv'
column_index = 2  # Replace with the index of the column you want to calculate the average for
average_value = calculate_column_average(csv_file_path, column_index)

if average_value is not None:
    print(f"Average of column {column_index + 1}: {average_value}")
else:
    print(f"No valid values found in column {column_index + 1}")
