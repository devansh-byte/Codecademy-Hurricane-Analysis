# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages

def convert_damages(damages):
  conversion = {"M": 1000000,
              "B": 1000000000}
  updated_damages = list()

  for damage in damages:
    if damage == "Damages not recorded":
            updated_damages.append(damage)
    if damage[-1] == "M":
            updated_damages.append(float(damage[:-1]) * conversion["M"])
    if damage[-1] == "B":
            updated_damages.append(float(damage[:-1]) * conversion["B"])

  return(updated_damages)
   
# test function by updating damages
updated_damages = convert_damages(damages)
print(updated_damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary
def create_ditionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
  
  return hurricanes

print("")
hurricanes = create_ditionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)
print("")

# 3
# Organizing by Year
hurricanes_by_year = {}
# create a new dictionary of hurricanes with year and key
for i in hurricanes:
  current_year = hurricanes[i]["Year"]
  current_cane = hurricanes[i]
  if current_year not in hurricanes_by_year:
    hurricanes_by_year[current_year] = current_cane

print(hurricanes_by_year) 
print("")

# 4
# Counting Damaged Areas
affected_areas = {}
# create dictionary of areas to store the number of hurricanes involved in
for area in areas_affected:
  for i in area:
    if i not in affected_areas:
      affected_areas[i] = 1
    else:
      affected_areas[i] += 1

print(affected_areas)
print("")
# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def affected_by_hurricanes(affected_areas):
  max_area = "Central America"
  max_area_count = 0
  for area in affected_areas:
    if max_area_count < affected_areas[area]:
      max_area = area
      max_area_count = affected_areas[area]
  return max_area, max_area_count

max_area, max_area_count = affected_by_hurricanes(affected_areas)
print(max_area + " was hit by hurricanes the most times. " + "The exact number is " + str(max_area_count) + " times.")
print("")


# 6
# Calculating the Deadliest Hurricane
def deaths_by_hurricanes(hurricanes):
  max_mortality_cane = "Cuba I"
  max_mortality = 0
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] > max_mortality:
      max_mortality_cane = cane
      max_mortality = hurricanes[cane]["Deaths"]
  return max_mortality_cane, max_mortality

max_mortality_cane, max_mortality = deaths_by_hurricanes(hurricanes)
print("The deadliest hurricane is " + max_mortality_cane + " which caused " + str(max_mortality) + " deaths.")
print("")
# find highest mortality hurricane and the number of deaths
hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}
def mortality(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for hurricane in hurricanes:
    death = hurricanes[hurricane]["Deaths"]
    if death < 100:
      hurricanes_by_mortality[0].append(hurricane)
    elif death >= 100 and death < 500:
      hurricanes_by_mortality[1].append(hurricane)
    elif death >= 500 and death < 1000:
      hurricanes_by_mortality[2].append(hurricane)
    elif death >= 1000 and death < 10000:
      hurricanes_by_mortality[3].append(hurricane)
    elif death >= 10000:
      hurricanes_by_mortality[4].append(hurricane)
  return hurricanes_by_mortality

hurricanes_by_mortality = mortality(hurricanes) 

print("Hurricanes rated by mortality rate = " + str(hurricanes_by_mortality))
print("")
# 7
# Rating Hurricanes by Mortality
def most_damage(hurricanes):
  max_damage_cane = "Cuba I"
  max_damage = 0
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Damage"] == "Damages not recorded":
      pass
    elif hurricanes[hurricane]["Damage"] > max_damage:
      max_damage_cane = hurricane
      max_damage = hurricanes[hurricane]["Damage"]
  return max_damage_cane, max_damage

max_damage_cane, max_damage = most_damage(hurricanes)
print("The most devastating hurricane was " + max_damage_cane + ". " + "It caused " + str(max_damage) + " USD of damage.")
print("")
# categorize hurricanes in new dictionary with mortality severity as key
fatality_by_hurricanes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
# 8 Calculating Hurricane Maximum Damage
def fatality(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for hurricane in hurricanes:
    damage_info = hurricanes[hurricane]["Damage"]
    if damage_info == "Damages not recorded":
      fatality_by_hurricanes[0].append(hurricane)
    elif damage_info > 0 and damage_info <= 100000000:
      fatality_by_hurricanes[1].append(hurricane)
    elif damage_info > 100000000 and damage_info <= 1000000000:
      fatality_by_hurricanes[2].append(hurricane)
    elif damage_info > 1000000000 and damage_info <= 10000000000:
      fatality_by_hurricanes[3].append(hurricane)
    elif damage_info > 10000000000 and damage_info <= 50000000000:
      fatality_by_hurricanes[4].append(hurricane)
    elif damage_info > 50000000000:
      fatality_by_hurricanes[5].append(hurricane)
  return fatality_by_hurricanes

fatality_by_hurricanes = fatality(hurricanes)
print(" Hurricanes according to how much damage they cause: " + str(fatality_by_hurricanes))




      




# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
