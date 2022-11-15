# goals for the lab are to:
# read the real estate template JSON into a dict call "template"
# get new address / referrer info from user when script is ran
# make a copy of the template and update values with user input
# create json and write new values to the file while replace spaces with dashes

# importing json to enable functionality with json files
from json import load, dump
import copy
from datetime import date, timedelta

# setting variable equal to string of file name to read from,
# in this case, template.json
json_file_name = "template.json"


# This variable must be defined and populated for tests.
template = None

# opening file using variable above and loading data
with open(json_file_name) as json_file:
  template = load(json_file)

# printing text to screen and prompting user for address info
def gather_property_info():
    print("Address")
    street_1 = input("Street 1: ")
    street_2 = input("Street 2: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP: ")

    print("\nDetails")
# casting sq footage to integer and removing commas
    square_footage = int(input("Square Footage: ").replace(",", ""))
    bedrooms = int(input("Bedrooms: "))
    bathrooms = int(input("Bathrooms: "))
# creating list of amenities via prompting user for input and instructing
# to put a | between items, then program will read | as delimiter to separate
# items in list
    ammenities = list(
        map(str.strip, input("Ammenities (use | between items): ").split("|"))
    )
# returning dictionary with labels as keys ('street', 'city', etc.) and
# values as corresponding label values (street name, city name, etc)
    return {
        "address": {
            "street_1": street_1,
            "street_2": street_2,
            "city": city,
            "state": state,
        "zip": zip_code,
        },
        "square_footage": square_footage,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "ammenities": ammenities,
    }

def gather_referrer_info():
# prompting user to confirm if there was a referrer
# if answer begins with 'y', then we prompt for referrer
# otherwise we return nothing
    has_referrer = input("Was there a referrer? (Y or n): ")
    if has_referrer.lower().startswith("y"):
        return input("Referrer: ")
    else:
        return None

def main():
    # Place all logic in here (or in functions called here)
# creating deep copy of template (i.e., a copy that if altered, 
# will not cause the original to be altered
    output = copy.deepcopy(template)
# gathering property and referrer info using functions above
    property_info = gather_property_info()
    referrer = gather_referrer_info()
# adding new key/value pairs to copied dict
# Setting listing date as string of tomorrow's date, property info as 
# value of property_info (i.e., gather_property_info output)
    output["listing_date"] = str(date.today() + timedelta(days=1))
    output["property"] = property_info
    output["broker"]["referrer"] = referrer

    output_file_name = property_info["address"]["street_1"].replace(" ", "-") + ".json"

    print(output)

# creating output file via json library ('w' specifies 'write' mode)
    with open(output_file_name, "w") as output_file:
        dump(output, output_file)
        print(f"Created {output_file}")

if __name__ == "__main__":
    main()
