#lex_auth_012693797166096384149

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def find_leap_years(given_year):
    n = given_year
    while not is_leap_year(given_year):
        given_year += (4 - given_year % 4)
    if given_year < n:
        given_year += 4

    list_of_leap_years = []
    count = 0
    while count < 15:
        if is_leap_year(given_year):
            list_of_leap_years.append(given_year)
            count += 1
        given_year += 4
    # Write your logic here

    return list_of_leap_years


list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)
