#lex_auth_012694465248329728100

def validate_name(name):
    #Start writing your code here
    if name == "" or len(name) > 15 or not name.isalpha():
        return False
    return True


def validate_phone_no(phno):
    #Start writing your code here
    ph = str(phno)

    if len(ph) != 10 or not phno.isdigit() or ph.count(ph[0]) == len(ph):
        return False

    return True


def validate_email_id(email_id):
    #Start writing your code here
    if email_id.count("@") != 1 or email_id.count(".com") != 1 or not email_id.endswith(".com"):
        return False
    domain_name = email_id[email_id.index("@") + 1: email_id.index(".")]

    #print(domain_name)

    if domain_name not in ["gmail", "yahoo", "hotmail"]:
        return False

    return True


def validate_all(name, phone_no, email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    flag = True
    if not validate_name(name):
        print("Invalid Name")
        flag = False
    if not validate_phone_no(phone_no):
        print("Invalid phone number")
        flag = False
    if not validate_email_id(email_id):
        print("Invalid email id")
        flag = False
    if flag:
        print("All the details are valid")
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
