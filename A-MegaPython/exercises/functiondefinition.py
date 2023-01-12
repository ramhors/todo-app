def get_age(year_of_birth, current_year=2023):
    age = current_year - int(year_of_birth)
    return age


birth = input("What is your year of birth? ")
ages = get_age(birth)

if ages <= 120:
    print(f"You are {ages} years")
else:
    print("You deserve a respect, happy long lives")
