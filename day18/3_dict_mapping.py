selection = int(input("Select a number (1, 2, 3, 4, 5) "))
# if selection == 1:
#     print("1 chosen")
# elif selection == 2:
#     print("2 chosen")
# elif selection == 3:
#     print("3 chosen")
# elif selection == 4:
#     print("4 chosen")
# elif selection == 5:
#     print("5 chosen")
# else:
#     print("Something else chosen")
#

selection_mapping = {
    1: "1 chosen",
    2: "2 chosen",
    3: "3 chosen",
    4: "4 chosen",
    5: "5 chosen"
}

try:
    print(selection_mapping[selection])
except KeyError:
    print("Something else chosen")
