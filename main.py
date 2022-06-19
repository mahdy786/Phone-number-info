# we import the module phonenumbers
import phonenumbers
# from the file (test) we get the targets phone number
from test import number

# this is where we get the country name
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))

# this is where we get the carrier name
from phonenumbers import carrier
service_nmber = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))
