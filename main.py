import work_lottery_functions
unique_numbers = []
our_tickets = {
    "Bob Bailey" : [1,3,10,23,30,46], "Brian" : [4,9,16,28,35,40], "Dan Farmer" : [6,11,14,25,29,31], 
    "Jacky" : [2,3,5,15,21,23], "James" : [4,7,13,15,16,18], "Julie" : [4,8,15,19,24,30], 
    "Lorraine" : [6,18,27,29,38,47], "Mary D" : [11,13,24,29,40,56], "Martin R" : [9,14,23,27,41,47],
    "Mary" : [8,13,14,37,41,55], "Pam Farmer" : [5,9,17,23,30,42], "Peter Gunn" : [6,10,19,25,30,45],
    "Steve W" : [5,11,25,27,31,49], "Terry Blyth" : [5,8,14,22,33,55], "Tina" : [1,8,17,21,22,49],
    "Amanda" : [3,9,17,20,42,55], "Jim McCoy" : [5,13,16,28,36,59], "Ellie/Billie" : [7,13,24,33,47,52],
    "Katie" : [6,8,9,15,21,31], "Brenda" : [6,14,36,28,17,59]
}
file = "prev_numbers.csv"
week_numbers = []

prev_numbers = work_lottery_functions.read_file(file)

number_position = ["first", "second", "third", "fourth", "fith", "sixth", "seventh"]

print("******************")
print("Enter 'q' at any time to quit application")
print("Enter 'w' at any time to wipe the previous numer list for new")
while len(week_numbers) < 7:
    number = input(f"What was the {number_position[len(week_numbers)]} number this week: ")
    if number == "q":
        break
    if number == "w":
        print("******************")
        while True:
            choice = input("are you sure you want to wipe the previous numbers from the list \nPress Y/N for Yes or no: ")
            choice.lower()
            if choice == "y":
                prev_numbers = work_lottery_functions.clear_previous_numbers(prev_numbers)
                work_lottery_functions.write_numbers(file, prev_numbers)
                print("******************")
                break
            if choice == "n":
                print("******************")
                break
            else:
                print("you must answer with 'y' or 'n'.")
    else:
        try:
            number = int(number)
            week_numbers.append(number)
        except ValueError:
            print("What was inputted, was not a number.")
if len(week_numbers) == 7:
    print("******************")
    unique_numbers, prev_numbers = work_lottery_functions.sorting_week_and_prev_numbers(week_numbers, prev_numbers)
    work_lottery_functions.check_tickets(unique_numbers, our_tickets)
    work_lottery_functions.write_numbers(file, week_numbers)