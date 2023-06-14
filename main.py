# phone = input("Phone: ")
# number_dict = {
#     "1": "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# num_word = ""
# for ch in phone:
#     num_word += number_dict.get(ch, "!") + " "
# print(num_word)

#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, is me {self.name}")
#
#
# john = Person('Bob smith')
# john.talk()

def lbs_to_kg(wieght):
    return wieght* 0.45

man = lbs_to_kg(50)
print(man)