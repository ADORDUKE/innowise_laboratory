
def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age:
        return "Adult"
    else:
        return "Age must be between 0 and 100"



user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year


hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby == 'stop':
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies,
}

print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile.get('name')}")
print(f"Age: {user_profile.get('age')}")
print(f"Life Stage: {user_profile.get('stage')}")
if user_profile.get('hobbies'):
    print(f"Favorite Hobbies ({len(user_profile.get('hobbies'))}):")
    for hobby in user_profile.get('hobbies'):
        print(f"- {hobby}")
else:
    print("You didn't mention any hobbies.")
print("---")
