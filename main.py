weight = input("Type in your weight: ")
unit = input("L for Lb or K for kg: ")
use_unit = unit.upper()
weight_kg = int(weight) * 0.45
weight_lb = int(weight) * 2.2
if use_unit == "L":
    print(weight_lb)
else:
    print(weight_kg)
