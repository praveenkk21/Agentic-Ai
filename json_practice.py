import json


# ============================================================
# 1. PYTHON DICTIONARY
# ============================================================

user = {
    "id": 101,
    "name": "Praveen",
    "age": 30,
    "skills": ["Java", "Python", "Spring Boot"],
    "address": {
        "city": "Mangalore",
        "state": "Karnataka"
    }
}

print(user)


# ============================================================
# 2. json.dumps()
# Python Object -> JSON String
# ============================================================

json_string = json.dumps(user)

print("\nJSON STRING:")
print(json_string)

print(type(json_string))       # str


# Pretty JSON
pretty_json = json.dumps(user, indent=4)

print("\nPRETTY JSON:")
print(pretty_json)


# ============================================================
# 3. json.loads()
# JSON String -> Python Object
# ============================================================

json_data = '{"id": 101, "name": "Praveen", "age": 30}'

python_object = json.loads(json_data)

print("\nAFTER loads():")
print(python_object)

print(type(python_object))     # dict


# ============================================================
# 4. GET VALUE
# ============================================================

print("\nGET VALUE:")

print(user["name"])
print(user["age"])


# ============================================================
# 5. get()
# Safer way to get a value
# ============================================================

print("\nUSING get():")

print(user.get("name"))
print(user.get("age"))

# If key doesn't exist
print(user.get("salary"))

# Give default value
print(user.get("salary", 0))


# ============================================================
# 6. INSERT / ADD NEW KEY-VALUE
# ============================================================

print("\nBEFORE INSERT:")
print(user)

user["salary"] = 100000

print("AFTER INSERT:")
print(user)


# ============================================================
# 7. UPDATE VALUE
# ============================================================

user["age"] = 31

print("\nAFTER UPDATE AGE:")
print(user)


# Update multiple values
user.update({
    "name": "Praveen Kumar",
    "salary": 120000
})

print("\nAFTER update():")
print(user)


# ============================================================
# 8. DELETE VALUE
# ============================================================

# Using del
del user["salary"]

print("\nAFTER del:")
print(user)


# ============================================================
# 9. pop()
# Removes key and returns its value
# ============================================================

age = user.pop("age")

print("\nREMOVED AGE:")
print(age)

print("USER:")
print(user)


# ============================================================
# 10. Check if KEY EXISTS
# ============================================================

print("\nCHECK KEY:")

if "name" in user:
    print("Name exists")

if "salary" not in user:
    print("Salary does not exist")


# ============================================================
# 11. GET ALL KEYS
# ============================================================

print("\nKEYS:")

for key in user.keys():
    print(key)


# ============================================================
# 12. GET ALL VALUES
# ============================================================

print("\nVALUES:")

for value in user.values():
    print(value)


# ============================================================
# 13. GET KEY + VALUE
# ============================================================

print("\nKEY + VALUE:")

for key, value in user.items():
    print(key, "=", value)


# ============================================================
# 14. WORKING WITH LIST INSIDE JSON
# ============================================================

print("\nSKILLS:")

for skill in user["skills"]:
    print(skill)


# Add skill
user["skills"].append("Kafka")

print("\nAFTER ADDING SKILL:")
print(user["skills"])


# Remove skill
user["skills"].remove("Java")

print("\nAFTER REMOVING JAVA:")
print(user["skills"])


# ============================================================
# 15. NESTED JSON
# ============================================================

print("\nNESTED VALUES:")

print(user["address"]["city"])
print(user["address"]["state"])


# Update nested value
user["address"]["city"] = "Bangalore"

print("\nAFTER CITY UPDATE:")
print(user["address"])


# ============================================================
# 16. ADD NEW NESTED VALUE
# ============================================================

user["address"]["pincode"] = 575001

print("\nAFTER ADDING PINCODE:")
print(user["address"])


# ============================================================
# 17. JSON FILE - WRITE
# json.dump()
# Python Object -> JSON FILE
# ============================================================

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

print("\nuser.json CREATED")


# ============================================================
# 18. JSON FILE - READ
# json.load()
# JSON FILE -> Python Object
# ============================================================

with open("user.json", "r") as file:
    data = json.load(file)

print("\nDATA FROM FILE:")
print(data)


# ============================================================
# 19. DIFFERENCE BETWEEN dump/dumps
# ============================================================

# dumps -> converts to STRING
result = json.dumps(user)

print("\ndumps():")
print(result)
print(type(result))


# dump -> writes directly to FILE
with open("output.json", "w") as file:
    json.dump(user, file, indent=4)


# ============================================================
# 20. LIST OF JSON OBJECTS
# ============================================================

users = [
    {
        "id": 1,
        "name": "Praveen",
        "age": 30
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 28
    },
    {
        "id": 3,
        "name": "Arun",
        "age": 32
    }
]

print("\nALL USERS:")

for u in users:
    print(u)


# ============================================================
# 21. GET PARTICULAR USER
# ============================================================

for u in users:

    if u["id"] == 2:
        print("\nUSER WITH ID 2:")
        print(u)


# ============================================================
# 22. INSERT USER INTO LIST
# ============================================================

new_user = {
    "id": 4,
    "name": "Kiran",
    "age": 25
}

users.append(new_user)

print("\nAFTER INSERT:")
print(users)


# ============================================================
# 23. UPDATE USER INSIDE LIST
# ============================================================

for u in users:

    if u["id"] == 4:
        u["age"] = 26

print("\nAFTER USER UPDATE:")
print(users)


# ============================================================
# 24. DELETE USER FROM LIST
# ============================================================

users = [
    u for u in users
    if u["id"] != 4
]

print("\nAFTER DELETE USER 4:")
print(users)


# ============================================================
# 25. FILTER USERS
# ============================================================

print("\nUSERS AGE > 29:")

for u in users:

    if u["age"] > 29:
        print(u)


# ============================================================
# 26. SEARCH BY NAME
# ============================================================

search_name = "Praveen"

for u in users:

    if u["name"] == search_name:
        print("\nUSER FOUND:")
        print(u)


# ============================================================
# 27. CONVERT LIST TO JSON STRING
# ============================================================

users_json = json.dumps(users, indent=4)

print("\nLIST -> JSON STRING:")
print(users_json)


# ============================================================
# 28. JSON STRING -> LIST
# ============================================================

users_again = json.loads(users_json)

print("\nJSON STRING -> LIST:")
print(users_again)


# ============================================================
# 29. CLEAR DICTIONARY
# ============================================================

temp = {
    "name": "Test",
    "age": 20
}

temp.clear()

print("\nAFTER clear():")
print(temp)


# ============================================================
# 30. REMOVE LAST ITEM FROM LIST
# ============================================================

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("\nREMOVED:")
print(removed)

print("LIST:")
print(numbers)