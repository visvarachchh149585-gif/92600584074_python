def show(name, age):
    print(name, age)

show("Vishw", 20)

def greet(name, msg="Hello"):
    print(msg, name)

greet("CJ")
greet("CJ", "Hi")

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    print(total)

sum_all(1, 2, 3)
