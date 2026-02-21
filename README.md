### summary
This was a side project I did for my work in a bar, we had a game where you would put £10 into a pot, and pick six numbers for our "fake" lottery. Everytime the "real" lottery went on (which is once a week), any numbers you had in common, were ticked off and carried to the next week. the first person to get all their numbers crossed off would win all the money, on average it took around 8 weeks for someone to win. But on our side, every week, we would look at the lottery numbers and slowly check everyone's six numbers, and tick away. Which prompted me to make this program. 

### How the program runs
It's not complex but gets the job done. It asks for the seven "real" lottery numbers this week then it checks if the current weeks numbers have been called already by using a CSV file which will have our previous numbers.
Then it takes our tickets and checks who has winning numbers this week. After it has done that it then tells us who has winning numbers, and skips who does not (as that will be useless information). After that, it then saves our new numbers back into our CSV, then the next week it is used, next week's numbers will be compared with our numbers as well as previous numbers to check any unique numbers that have been drawn to do the same thing again.

### a function to wipe the CSV file included