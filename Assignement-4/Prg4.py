#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    keys = list(medical_speciality.keys())
    counter = dict.fromkeys(keys, 0)
    for i in range(1, len(patient_medical_speciality_list), 2):
        counter[patient_medical_speciality_list[i]] += 1
    return medical_speciality[max(counter, key=counter.get)]


#provide different values in the list and test your program
patient_medical_speciality_list = [
    101, 'O', 102, 'O', 103, 'O', 302, 'P', 305, 'E', 401, 'O', 656, 'O']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(
    patient_medical_speciality_list, medical_speciality)
print(speciality)
