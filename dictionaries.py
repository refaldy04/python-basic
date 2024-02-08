# key/value pair {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 6} # drink is key and price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"],"IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr", "Mort"]}
print(employees)
employees["Legal"] = ["Mr. Frond"] # add new key/value pair
print(employees)
employees.update({"Sales": ["Andie", "Ollie"]}) # add new key/value pair
print(employees)

drinks["White Russian"] = 8
print(drinks)
print(drinks.get("White Russian"))