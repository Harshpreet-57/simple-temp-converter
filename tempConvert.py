# ⁡⁣⁢⁣⁡⁣⁢⁣𝗖𝗲𝗹𝗰𝗶𝘂𝘀 𝘁𝗼 𝗳𝗮𝗵𝗿𝗲𝗻𝗵𝗲𝗶𝘁 𝗰𝗼𝗻𝘃𝗲𝗿𝘁𝗲𝗿⁡

input_temp = int(input("Enter the temperature:"))

unit_list = ["C","F"]

input_tounit = str(input("Convert to"+str(unit_list)+":"))

if input_tounit not in unit_list:
    print("Enter a valid unit ❌")

if input_tounit == "F":
    calculated_temprature = (input_temp*9/5)+32
    print(calculated_temprature+"F")

elif input_tounit == "C":
    calculated_temprature = (input_temp-32)*5/9
    print(calculated_temprature)

else:
    print("Some error occurred ❌")
