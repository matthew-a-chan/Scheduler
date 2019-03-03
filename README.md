This is a scheduler program that uses blind auctions to assign classes.

It's written entirely in Python, and interfaces with the Google Drive API to enable input directly via Google Sheet forms, allowing for easy and efficient collection of data from potential students.

Unfortunately, I didn't have the reasonably input 100's of people's worth of
data, so I relied on random generation of input data from users (making the
process seem random) but the system would be much more efficient with
multiple intelligent entities providing logical data rather than random
numbers.

Also, I've found that I'm severely restricted by the amount of Google API calls that I can make (100 calls every 100 seconds), limiting the max student body size to about 30 people (Obviously not ideal), though the algorithm works
with n students and n classes.


ALGORITM:

Betting phase 1:
Each student blind bets a number of credits, as well as their top three
class preferences in order.

Sorting phase 2:
Each class is then assigned a value porportional to demand for said class, as
well as inversely porportional to seats left in the class at the start of
sorting phase.
(ie: 
A popular class: MATH100 has 2 seats left, but 10 applicants: Credits: c*10/2
    where c is a constant -> let c = 5 -> 25 credits to enrol
A not popular class: ENGL100 has 43 seats left, but 10 applicants:
    Credits: c*10/43 -> let c = 5 -> 1.15 -> Floor() to 1 credit to enrol
)
By making the popular, small classes more expensive, it creates a more fair
system similar to a blind bid, as well as preventing the people who enrol in popular classes from enroling in other classes (because they spend a lot of
currency on the popular ones)

Registration phase 3:
In order for students to enrol in a given class,
FIRST: Their current credit amount (plus any carry from previous rounds) must
be higher than the requirement for the class.
SECOND: They must have listed the class as one of the three desired classes
to take that round.

If there are no classes with requirements less than a student's current
credit within the three of that list, the student forfeits registration that
round, but keeps credits.
Additionally, students register in order of increasing credits to reward the
people who bet lower, and therefore have less 'currency' to purchase classes
and take more risk.
(ie: JOE with 9 credits registers before BOB with 14 credits, but JOE can't
register for the 12 credit physics class, but BOB can if there's still seats left.)

Betting phase 2:
At the end of registration, the betting phase repeats. Any students who
have enroled in every course that they want will stop at this point, otherwise
the cycle of betting->sorting->registration->betting will repeat until every
student is equally dissatisfied with their share of classes.








  --  NOTE: This project relies extensively on the Google API, which obviously
      requires multi-step authentication protocols. I have not uploaded my
      private authentication tokens (for obvious reasons) here, and without
      them you'll be unable to access spreadsheets/run the scripts.

To run:

1) Execute
   \$ python Scheduler.py

2) In order to progress to the second stage, manually increment 
   'sheet_num' variable in Scheduler.py then execute again.