print("Enter number of users")
userCount = int(input())
dictionary = {}
allItemsList = []
completedAnalysis = set()


for i in range(userCount):
    print("Enter username")
    userName = str(input())
    dictionary[userName] = []
    print("How many items for " + userName)
    itemCount = int(input())


    for j in range(itemCount):
        print("Item " + str(j + 1))
        item = str(input())
        dictionary[userName].append(item)
        allItemsList.append(item)

print()

print("USER DATA:")

for user in dictionary:
    print(user + " -> " + str(dictionary[user]))


itemCounts = {}

for item in allItemsList:
    itemCounts[item] = itemCounts.get(item, 0) + 1 

print()

print(itemCounts)

print()

print()
print("COMMON ITEMS:")

for item in itemCounts:
    if itemCounts[item] > 1:
        print(item)
print()
print("UNIQUE ITEMS:")

for item in itemCounts:
    if itemCounts[item] == 1:
        print(item)
print()
print("MOST POPULAR ITEM:")
if itemCounts: 
    maxVal = max(itemCounts.values()) 

    for item in itemCounts:
        if itemCounts[item] == maxVal:
            print(item)