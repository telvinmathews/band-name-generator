def band_name_gen():
    #1. Create a greeting for your program.

    print("Welcome to the band name Generator! ")

    #2. Ask the user for the city that they grew up in.

    user_city = input("What city did you grow up in?\n")

    #3. Ask the user for the name of a pet.

    user_pet = input("What is/was the name of your favorite pet?\n")

    #4. Combine the name of their city and pet and show them their band name.

    print("Your band name is: " + user_city + " " + user_pet)

# print("Try another name?")
choice_one = "Y"
choice_two = "N"
user_choice = input("Try another name (Y/N)?\n")

# user_choice = input("Y/N")
# if user type "Y"
if user_choice == choice_one:
    band_name_gen()
else: print("Goodbye!")


# repeat program

# if user type "N"
# print("Goodbye!")