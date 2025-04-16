def round_to_tenth():
    try:
        number = float(input("Enter a number: "))
        rounded = round(number, 1)
        print(f"The number rounded to the nearest tenth is: {rounded}")
    except ValueError:
        print("Please enter a valid number.")

round_to_tenth()
