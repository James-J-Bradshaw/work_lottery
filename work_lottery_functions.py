import csv

def read_file(file):
    """reads prev_numbers.csv into a int list"""
    week_numbers = []
    with open(file, mode = "r") as f:
        csvfile = csv.reader(f)
        for list in csvfile:
            for number in list:
                try:
                    week_numbers.append(int(number))
                except ValueError:
                    pass
    return week_numbers

def write_numbers(file,new_numbers):
    """writes our new set of numbers into prev_numbers.csv"""
    file = open(file, "w+", newline ="")
    with file:
        write = csv.writer(file)
        write.writerow(new_numbers)

def check_tickets(unique_numbers,our_tickets):
    """compares our weekly unique numbers with everyones tickets, 
    and tells us which person has a number that needs to be crossed off"""
    ticket_numbers = our_tickets.values()
    for ticket in ticket_numbers:
        winners = []
        for number in ticket:
            if number in unique_numbers:
                winners.append(number)
                name = [key for key, val in our_tickets.items() if val == ticket]
                chosen = name
                chosen = chosen[0]
        if len(winners) >= 1:
            print(f"{chosen} needs {len(winners)} number(s) ticked off, these are: {winners}")
        else:
            pass

def sorting_week_and_prev_numbers(week_numbers, previous_numbers):
    unique_numbers = []
    for number in week_numbers:
        if number not in previous_numbers:
            unique_numbers.append(number)
            previous_numbers.append(number)

    
    return unique_numbers, previous_numbers
