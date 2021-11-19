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


Gowrishankar = "[[yellow]]ℂ𝕣𝕖𝕒𝕥𝕖𝕕: [[red]]𝒢ℴ𝓌𝓇𝒾𝓈𝒽𝒶𝓃𝓀𝒶𝓇 𝒱.𝒱[[white]]"
print(colorText(Gowrishankar))


Appu = "[[yellow]]𝕙𝕥𝕥𝕡𝕤://𝕘𝕚𝕥𝕙𝕦𝕓.𝕔𝕠𝕞/: [[green]]𝓱𝓽𝓽𝓹𝓼://𝓰𝓲𝓽𝓱𝓾𝓫.𝓬𝓸𝓶/𝓖𝓸𝔀𝓻𝓲𝓼𝓱𝓪𝓷𝓴𝓪𝓻𝓿𝓿 [[white]]"
print(colorText(Appu))


mobileNo=input("Mobile no. with country code:")
mobileNo=phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo)) 
print(carrier.name_for_number(mobileNo,"en")) 
print(geocoder.description_for_number(mobileNo,"e n")) 
print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
print("Checking number:",phonenumbers.is_possible_number(mobileNo))