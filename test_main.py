import work_lottery_functions

def test_sorting_numbers():
    """test to check if weekly numbers are added to previous weeks' numbers"""
    week_numbers = [5,6,7]
    prev_numbers = [1,2,3,4]
    unique_numbers, prev_numbers = work_lottery_functions.sorting_week_and_prev_numbers(week_numbers, prev_numbers)
    assert unique_numbers == [5,6,7], prev_numbers == [1,2,3,4,5,6,7]

def test_check_tickets(capsys):
    """test to check if our tickets will be checked with our unique numbers of the week"""
    unique_numbers = [55,1,2]
    our_ticket = {"JJB" : [1,45,33]}
    work_lottery_functions.check_tickets(unique_numbers,our_ticket)
    captured = capsys.readouterr()
    assert captured.out == "******************\nJJB needs 1 number(s) ticked off, these are: [1]\n"

def test_dud_ticket(capsys):
    """test to see if program will ignore my ticket if it has no common numbers this week"""
    unique_numbers = [1,2,3]
    our_ticket = {"JJB" : [4,5,6]}
    work_lottery_functions.check_tickets(unique_numbers, our_ticket)
    captured = capsys.readouterr()
    assert captured.out == ""
