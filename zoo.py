zoo = ("lions", "tigers", "bears", "sheep", "zebra",
       "donkey", "monkey", "snake", "turkey", "gerbil")

print(zoo)

print(zoo.index("tigers"))

animal_to_find = "gerbil"
if animal_to_find in zoo:
    print("Animal found")

animal_to_find = "hampster"
if animal_to_find in zoo:
    print("Animal found")

zoo1 = ("lions", "tigers", "bears", "sheep")
(first_child, second_child, third_child, fourth_child) = zoo1

print(first_child)  # Output is "lions"
print(second_child)  # Output is "tigers"
print(third_child)  # Output is "bears"
print(fourth_child)  # Output is "sheep"

zoo2 = list(zoo1)
print(zoo1)


zoo2.extend(["hippo", "giraffe", "cricket"])

print("new list", zoo2)

newTup = tuple(zoo2)

print("new Tuple", newTup)
