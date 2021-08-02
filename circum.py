while(True):
    print("Let's find out the area and circumference of the circle.")
    r = input("Enter a radius:\n")
    area = ((22/7)*r)**2
    circum = 2*(22/7)*r
    if r == int:
        area = ((22/7)*r)**2
        circum = 2*(22/7)*r
    elif r == float:
        area = ((22/7)*r)**2
        circum = 2*(22/7)*r
    print("Area of the circle is", area)
    print("Circumference of the circle is", circum)

    else:
    print("Invalid Input!")

    interest = input("Do you want to try again? Y/N:  ")
    if interest == "n" or interest == "N":
            break
    elif interest== "Y"or interest=="y":
            continue

        
