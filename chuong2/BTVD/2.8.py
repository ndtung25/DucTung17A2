import json

python_dict = {
    "name": "Alice",
    "age": 25,
    "city": "San Francisco",
    "hobbies": ["photography", "cooking", "hiking"]
}

json_data = json.dumps(python_dict, sort_keys=True, indent=4)

print("Dữ liệu JSON đã được sắp xếp theo khóa và thụt lề:")
print(json_data)
