# 1.1
print("prateek \n" *3)
# 2.1
a = 1
b = 2
c = 3
print(a+b+c)
# 2.2
a = "hello "
b = "artificial "
c = "intelligence"
print (a+b+c)
# 4.1
for i in range(1,11):
	print (i*7)
for j in range(1,11):
    print(j*9)
# 4.2    
n = int(input("Enter: "))
for i in range(1,11):
    print(i*n)
# 4.3
n = int(input("Enter:"))
print ("Sum is --> ", sum(range(1,n)))
# 5.1
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
# 5.2
n = int(input("Enter the value of n: "))
Sum = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        Sum += i
print(Sum)
# 5.3
n = int(input("Enter the value of n: "))
Sum = 0
for i in range(2, n + 1):
    if all(i % d != 0 for d in range(2, int(i**0.5) + 1)):  # double star means exponential
        Sum += i
print(Sum)
# 6.1
def sum_odd_numbers(n):
    total_sum = 0
    for i in range(1, n + 1, 2):  # Start at 1, step by 2 to get only odd numbers
        total_sum += i
    return total_sum
n = int(input("Enter the value of n: "))
result = sum_odd_numbers(n)
print(result)
# 6.2s
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Function to add all prime numbers from 1 to n
def sum_prime_numbers(n):
    total_sum = 0
    for i in range(2, n + 1):  # Start at 2 because 1 is not prime
        if is_prime(i):
            total_sum += i
    return total_sum
n = int(input("Enter the value of n: "))
result = sum_prime_numbers(n)
print(result)

