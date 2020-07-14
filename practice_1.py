while True:
    try:
        input_number = int(input("Please a number: "))
        break
    except ValueError:
        print("This is an invalid number. Please re-enter a valid number: ")
print("Success")