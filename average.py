numbers = input("Enter numbers")
num_list = list(map(float, numbers.split()))
average = sum(num_list) / len(num_list)
print("The average is: {average}")
