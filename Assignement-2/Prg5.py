#lex_auth_012693788748742656146

def calculate_loan(account_number, salary, account_balance, loan_type, loan_amount_expected, customer_emi_expected):
    eligible_loan_amount = loan_amount_expected
    bank_emi_expected = customer_emi_expected
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    acc = str(account_number)

    if not acc.startswith("1") or len(acc) != 4:
        print("Invalid account number")
        return

    if account_balance < 100000:
        print("Insufficient account balance")
        return

    dic = {"Car": [25000, 500000, 36], "House": [
        50000, 6000000, 60], "Business": [75000, 7500000, 84]}

    if not loan_type in dic.keys() or dic[loan_type][0] >= salary:
        print("Invalid loan type or salary")
        return

    if dic[loan_type][1] < loan_amount_expected or dic[loan_type][2] < customer_emi_expected:
        print("The customer is not eligible for the loan")
        return

    if eligible_loan_amount != dic[loan_type][1]:
        eligible_loan_amount = dic[loan_type][1]

    if customer_emi_expected != dic[loan_type][2]:
        bank_emi_expected = dic[loan_type][2]

    print("Account number:", account_number)
    print("The customer can avail the amount of Rs.", eligible_loan_amount)
    print("Eligible EMIs :", bank_emi_expected)
    print("Requested loan amount:", loan_amount_expected)
    print("Requested EMI's:", customer_emi_expected)

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001, 40000, 250000, "Car", 300000, 30)
