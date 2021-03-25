#lex_auth_012693810762121216155

def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count

    if heads > legs:
        print(error_msg)
        return

    c2 = 4 * heads - legs
    r2 = legs - 2 * heads

    if c2 % 2 or r2 % 2:
        print(error_msg)
        return
    else:
        print(c2 // 2, r2 // 2)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)


#Provide different values for heads and legs and test your program
solve(38, 131)
