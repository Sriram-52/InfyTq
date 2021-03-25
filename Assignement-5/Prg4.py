#lex_auth_012693816779112448160

def calculate(distance, no_of_passengers):
    pricePerTicket = 80
    pricePerLiter = 70
    cp = distance * pricePerLiter / 10
    sp = no_of_passengers * pricePerTicket
    if sp > cp:
        return sp - cp
    return -1
    #Remove pass and write your logic here


#Provide different values for distance, no_of_passenger and test your program
distance = 20
no_of_passengers = 50
print(calculate(distance, no_of_passengers))
