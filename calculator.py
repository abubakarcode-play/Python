def add(P,Q):
    return P+Q

def subtract(P,Q):
    return P-Q

def multiply(P,Q):
    return P*Q

def divide(P,Q):
    return P/Q

print("Please select the operation")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

choose = input("Please Enter Your Choice a/ b/ c/ d/")

num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter the second number: "))

if choose=='a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choose =='b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choose =='c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choose =='d':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("This is an invalid input")