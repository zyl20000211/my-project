first_name = "kwiyomi"
last_name = "iris"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

bicycles = ['apple','banana','car','dude']
print(f"my first bicycles was a {bicycles[0].title()}")

bicycles = ['apple','banana','car','dude']
bicycles.insert(1, 'elephant')
print(bicycles)

bicycles = ['apple', 'elephant', 'banana', 'car', 'dude']
middle_bicycles = bicycles.pop(-2)
print(f"my middle school bicycles was a {middle_bicycles.title()}")

bicycles = ['apple', 'elephant', 'banana', 'car', 'dude']
bicycles.remove('banana')
print(bicycles)



