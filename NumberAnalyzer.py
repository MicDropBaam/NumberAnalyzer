import statistics

#user input
nums = input("Enter the numbers separated by space: ")
num_list = list(map(int, nums.split()))

#Analyz
avg = statistics.mean(num_list)
max_val = max(num_list)
min_val = min(num_list)
even_count = len([n for n in num_list if n%2 == 0])
odd_count = len([n for n in num_list if n%2 != 0])

#print
print(f"Average: {avg}")
print(f"Maximum Value: {max_val}")
print(f"Minimum Value: {min_val}")
print(f"Even number count: {even_count}")
print(f"Odd number count: {odd_count}")