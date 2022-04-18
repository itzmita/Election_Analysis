voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")
    # print(f"{county_dict['county']}") 
    # print(county_dict["registered_voters"])
# for county_dict in voting_data:

#      print(county_dict['county'])
# for county_dict in voting_data:
#     print(county_dict)

# for county in range(len(voting_data)):

#      print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")
# for county in counties_dict:
#     print(counties_dict.get(county))
# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)
# counties_tuple = ("Arapahoe","Denver","Jefferson")
# for county in counties_tuple:

#       print(county)

# count = 7

# while count < 1:

#     print("Hello World")