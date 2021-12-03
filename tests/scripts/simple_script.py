name = input("Your name: ")
print(f"Hello, {name}.")

while True:
    result = input("What is 2**10? ")
    if result == "1024":
        print("correct")
        break
    else:
        print("wrong")
