try:
    age = int(input("write your age : "))
    print(age)
except ValueError: 
    print("wrong move")
finally:
    print("Hello")