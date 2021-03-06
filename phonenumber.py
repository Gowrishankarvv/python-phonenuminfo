import phonenumbers
from phonenumbers import carrier, geocoder, timezone


import os

os.system("clear") #use this for linux. change to os.system("cls") for windows

COLORS = {\

"red": "\u001b[31;1m",
"green":"\u001b[32m",
"white":"\u001b[37m",
"yellow":"\u001b[33;1m",
}
#You can add more colors and backgrounds to the dictionary if you like.


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text



#Example printing out some text


Gowrishankar = "[[yellow]]βπ£πππ₯ππ: [[red]]π’β΄πππΎππ½πΆπππΆπ π±.π±[[white]]"
print(colorText(Gowrishankar))


Appu = "[[yellow]]ππ₯π₯π‘π€://πππ₯ππ¦π.ππ π/: [[green]]π±π½π½πΉπΌ://π°π²π½π±πΎπ«.π¬πΈπΆ/ππΈππ»π²πΌπ±πͺπ·π΄πͺπ»πΏπΏ [[white]]"
print(colorText(Appu))


mobileNo=input("Mobile no. with country code:")
mobileNo=phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo)) 
print(carrier.name_for_number(mobileNo,"en")) 
print(geocoder.description_for_number(mobileNo,"e n")) 
print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
print("Checking number:",phonenumbers.is_possible_number(mobileNo))