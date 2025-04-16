def round_to_hundreth():
    try:
      number = float(input("enter number: ")) 
      rounded = round(number, 2)
      print(f"the number rounded to the nearest hundreth is: {rounded}")
    except ValueError:
       print("please re enter number")

round_to_hundreth()   