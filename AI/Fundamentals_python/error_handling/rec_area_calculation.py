def area(length, width):
    try:
        if length.isdigit() and width.isdigit():
            length = float(length)
            width = float(width)
        result = length * width
        print(f"The area of the rectangle is: {result}")
    except TypeError as e:
        print("You have", e)
    finally:
        print("Execution completed.")
    


area(input("Please enter the length of the rectangle: "), input("Please enter the width of the rectangle: "))