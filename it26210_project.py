import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MjbUBdR1NQfUAX4iE2bTUb2CFUgpcVqO"

print("\n")
print("  __  __                 ____                     _   ")
print(" |  \/  |               / __ \                   | |  ")
print(" | \  / |  __ _  _ __  | |  | | _   _   ___  ___ | |_ ")
print(" | |\/| | / _` || '_ \ | |  | || | | | / _ \/ __|| __|")
print(" | |  | || (_| || |_) || |__| || |_| ||  __/\__ \| |_ ")
print(" |_|  |_| \__,_|| .__/  \___\_\ \__,_| \___||___/ \__|")
print("                | |                                   ")
print("                |_|                                   ")
print("\n")

while True:
    
    
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ") 
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        
        highway = (json_data["route"]["hasHighway"])
        tollRoad = (json_data["route"]["hasTollRoad"])
        tripDuration = (json_data["route"]["formattedTime"])

        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest) + "\n")
        print("Trip Duration: " + tripDuration)
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        if highway == True:
            print("Route will pass through a highway")
        elif highway == False:
            print("Route will not pass through a highway")
        
        if tollRoad == True:
            print("Toll Gate is present in route")
        elif tollRoad == False:
            print("Toll Gate is not present in route")
        
        print("Fuel Used (Ltr): " + str("{:.2f}".format(json_data["route"]["fuelUsed"]*3.78))+"\n")
        print("=============================================\n")
        print("DIRECTIONS\n")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("\n=============================================\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")

    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")

    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************")
        