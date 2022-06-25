#!/user/bin/env python3
# Copyright 2022 Empress Djata
user_name = input("Enter name: ")
user_height = float(input("Enter height: "))
user_weight = float(input("Enter weight: "))

def bmi_calculator(user_height, user_weight):
    user_bmi = float(((user_weight/(user_height ** 2))) * 703)

    if(user_bmi < 16):
        return "you're underweight", user_bmi
    elif(user_bmi >= 16 and user_bmi < 18.5):
        return "you're health", user_bmi
    elif(user_bmi >= 18.5 and user_bmi < 25):
        return "you're overweight", user_bmi
    elif(user_bmi >= 25 and user_bmi < 30):
        return "you're obese", user_bmi
    else:
        return "you're very, very obese", user_bmi

quote, bmi = bmi_calculator(user_height,user_weight)
print(user_name, quote, bmi)