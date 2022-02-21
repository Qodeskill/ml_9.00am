import phonenumbers
from phonenumbers import timezone,geocoder,carrier
# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
# phoneNumber = phonenumbers.parse("+919876543210")
  
# This will print the phone number and 
# it's basic details.
# print(phoneNumber)

number = input("Enter your mobile no. : ")
phone = phonenumbers.parse(number)
time  = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(time)
print(car)
print(reg)