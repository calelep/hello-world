# Declare the value of total_charge to be zero.
total_charge = 0

# Request the user to input the money amount for his/her total_cart value.
# Converted that total cart_value to a float number.
cart_value = float(input("Enter the total charge from online order: "))

# Request user to input what Country are they buying from. Converted that to all caps.
country = input("Enter Country of origin: ").upper()

# IF and OR statements for all inputed data.
if country == "CANADA":
    province = input("What Province are you from? ").upper()
    # IF Alberta charge 5% tax
    if province == "ALBERTA":
        total_charge = cart_value + (cart_value * .05)
        print(total_charge)

# Lines 20 to 25 were the original lines of code. Which were re-written as single lines of code.
        # if province == "ALBERTA":
        #     total_charge = cart_value + (cart_value * .05)
        #     print(total_charge)
        # elif province == "ONTARIO" or province == "NEW BRUNSWICK" or province == "NOVA SCOTIA":
        #     total_charge = cart_value + (cart_value * .13)
        #     print(total_charge)
# Lines 27 to 38 are the re-written lines of code from lines 20 to 25.
    # IF Ontario charge 13% tax
    # elif province == "ONTARIO":
    #     total_charge = cart_value + (cart_value * .13)
    #     print(total_charge)
    # IF New Brunswick charge 13% tax
    # elif province == "NEW BRUNSWICK":
    #     total_charge = cart_value + (cart_value * .13)
    #     print(total_charge)
    # IF Nova Scotia charge 13% tax
    # elif province == "NOVA SCOTIA":
    #     total_charge = cart_value + (cart_value * .13)
    #     print(total_charge)

# The provinces of Ontario, New Brunswick, and Nova Scotia all have a 13% tax with this ELIF code it was "refactor"
    elif province == "ONTARIO" or province == "NEW BRUNSWICK" or province == "NOVA SCOTIA":
        total_charge = cart_value + (cart_value * .13)
        print(total_charge)

# Any province that "ARE NOT" the ones listed in the ELIF statement will get charge 5% and an additional 6%
    elif province != "ALBERTA" or "ONTARIO" or "NEW BRUNSWICK" or "NOVA SCOTIA":
        total_charge = cart_value + (cart_value * .05) + (cart_value * .06)
        print(total_charge)

# Any Country that is not Canada will not get charge a tax percentage
else:
    total_charge = cart_value
    print(total_charge)
