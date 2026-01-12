import pandas as pd

csvFile = pd.read_csv(r'D:\python\student_data.csv')

# Subject-wise averages
avg_maths = csvFile["Math"].mean()
avg_science = csvFile["Science"].mean()
avg_English = csvFile["English"].mean()

print("\nEnglish_Average:", avg_English,
      "\nMaths_Average:", avg_maths,
      "\nScience_Average:", avg_science)

# Student-wise averages using loop
averages = []

for i in range(len(csvFile)):
    total = (
        csvFile.loc[i, "Math"] +
        csvFile.loc[i, "Science"] +
        csvFile.loc[i, "English"]
    )
    avg = total / 3
    averages.append(avg)

csvFile["Average"] = averages

print(csvFile[["Name", "Average"]])
highest = averages[0]
lowest = averages[0]

for avg in averages:
    if avg > highest:
        highest = avg
    if avg < lowest:
        lowest = avg

print("\nHighest Average:", highest)
print("Lowest Average:", lowest)
if avg_maths < avg_English and avg_maths < avg_science:
    print("Students should work on Maths")
elif avg_English < avg_maths and avg_English < avg_science:
    print("Students should work on English")
else:
    print("Students should work on Science")
