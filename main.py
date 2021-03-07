import pandas as pd
import random


foodChoices = pd.read_excel("food_choices.xlsx")
foodChoicesDF = pd.DataFrame(foodChoices)
print(foodChoicesDF)



#lists to store ingredients
meatList = []
vegList = []
sideDishList = []
soupList = []
satLunchList = []



col = foodChoicesDF['meat']
# print(meatChoice)
for item in col:
    if pd.isnull(item) == False:
        meatList.append(item)
print(meatList)    

col = foodChoicesDF['veg']
for item in col:
    if pd.isnull(item) == False:
        vegList.append(item)

col = foodChoicesDF['side dish']
for item in col:
    if pd.isnull(item) == False:
        sideDishList.append(item)

col = foodChoicesDF['soup']
for item in col:
    if pd.isnull(item) == False:
        soupList.append(item)
    else:
        continue

col = foodChoicesDF['sat lunch']
for item in col:
    if pd.isnull(item) == False:
        satLunchList.append(item)

# calendar = pd.DataFrame(rows=['Monday', 'Tuesday'])

#getting number of days in month
numDays = input("How many days are in the month?:\n")
numDays = int(numDays)
#creating exception
#if new item is repeated within 5 days from previous item
meatMenu = []
vegMenu = []
soupMenu = []

for i in range(numDays):
#each day need to take one meat, veg and soup from above
    meat = random.choice(meatList)
    while meat in meatMenu[-5:]: #item appears in meatMenu
        meat = random.choice(meatList)
    meatMenu.append(meat)

    veg = random.choice(vegList)
    while veg in vegMenu[-5:]:
        veg = random.choice(vegList)
    vegMenu.append(veg)

    soup = random.choice(soupList)
    while soup in soupMenu[-5:]:
        soup = random.choice(soupList)
    soupMenu.append(soup)

satDate = input("what date is the first sat of the month?\n")
satDate = int(satDate)
if satDate > 1:
    satDate = satDate - 1

#replacing rows on sat with sat menu
counter = 0
while satDate < numDays + 1:
    dish = random.choice(satLunchList)
    meatMenu[satDate] = dish
    vegMenu[satDate] = ""
    soupMenu [satDate] = ""
    counter += 1
    # print(f'counter: {counter}')
    # print(f'satDate: {satDate}')
    satDate += 7
#creating output
output = {
    'meat' : meatMenu,
    'veg' : vegMenu,
    'soup' : soupMenu
}
output_df = pd.DataFrame.from_dict(output, orient='columns',dtype=None, columns=None)
output_df.index.name = 'Date'
output_df.index += 1
print(output_df)

filepath = r"C:\Users\geral\Desktop\Food Generator\output\monthlyMenu.xlsx"
output_df.to_excel (r"C:\Users\geral\Desktop\Food Generator\output\monthlyMenu.xlsx", index=True)
 