phone = input("Phone: ")
number_dict = {
    "1": "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
num_word = ""
for ch in phone:
    num_word += number_dict.get(ch, "!") + " "
print(num_word)