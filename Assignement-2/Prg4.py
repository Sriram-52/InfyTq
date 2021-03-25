#lex_auth_012693782475948032141

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    deliveryCharge = 0
    #write your logic here

    if (food_type != "V" and food_type != "N") or distance_in_kms <= 0 or quantity_ordered < 1:
        return -1

    if food_type == "N":
        bill_amount = 150 * quantity_ordered
    elif food_type == "V":
        bill_amount = 120 * quantity_ordered

    if distance_in_kms > 6:
        deliveryCharge = (distance_in_kms - 6) * 6 + 9
    elif distance_in_kms < 7 and distance_in_kms > 3:
        deliveryCharge = (distance_in_kms - 3) * 3
    else:
        deliveryCharge = 0
    return bill_amount + deliveryCharge


#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)
