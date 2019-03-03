Look to Github for a more updated readme

After several failed attempts at solving a multi-layer, multi-server, system
using the various forms of the Gale-Shapeley algorithim, I gave up. :/
Instead, now I'm using a simpler, slightly less optimal system.

This is a scheduler program that uses a series of iterative blind auctions
and adaptive demand-based costs to assign classes as fairly as possible.

It's written entirely in Python, and interfaces with the Google Drive API to 
enable input directly via Google Sheet forms, allowing for easy and efficient 
collection of data from potential students. (Not bad for my first project in 
python, eh?)

Unfortunately, I didn't have the time to reasonably input 100's of people's 
worth of data, so I relied on random generation of input data from 'users' 
but the system would be much more efficient with intelligent entities 
providing logical data rather than random numbers, due to the way that the adaptive demand system works. (more info below)

Also, I've found that I'm severely restricted by the amount of Google API 
calls that I can make (100 calls every 100 seconds), limiting the max student 
body size (henceforth: system) to about 30 people (Obviously not ideal), though the algorithm works with n students and n classes. 

Additionally, the larger the system is, the more efficient this algorithm will become. By increasing not only the competition to get into classes, but also providing a more accurate reading of the demand for classes, the program can accurately and more heavily penalize people who enrol in high-demand classes or hold lots of credits. (High-demand classes will cost more to enrol in the more students there are; holding large amounts of credits will also make you go later--ie: 500th instead of 50th--in a larger system, meaning even if you have lots of credits, classes might fill before your turn.)


ALGORITM:

Betting phase 1:
Each student blind bids a number of credits, as well as their top three
class preferences in order.

Sorting phase 2:
Each class is then assigned a value porportional to demand for said class, as
well as inversely porportional to seats left in the class at the start of
sorting phase.
(ie: 
A popular class: MATH100 has 2 seats left, but 10 applicants: Credits: c*10/2
    where c is a constant -> let c = 5 -> 25 credits to enrol.
--An unpopular class: ENGL100 has 43 seats left, but 10 applicants:
    Credits: c*10/43 -> let c = 5 -> 1.15 -> Floor() to 1 credit to enrol. Note: c being a constant doesn't affect prices other than linearly scaling 
costs to all participants)

By making the popular, small classes more expensive, it creates a more fair
system similar to a blind bid, as well as preventing the people who enrol in 
popular classes from enroling in other classes (because they spend a lot of
currency on the popular ones)

Registration phase 3:
In order for students to enrol in a given class,
FIRST: Their current credit amount must be higher than the requirement for 
the class. (On any given round, you receive credits equal to your bid, plus
any unused rollover from previous rounds)
SECOND: They must have listed the class as one of the three desired classes
to take that round.

If there are no classes with requirements less than a student's current
credit within the three of that list, the student forfeits registration that
round, but keeps credits.
Additionally, students register in order of increasing credits to reward the
people who bet lower, and therefore have less 'currency' to purchase classes
and take more risk.
(ie: JOE with 9 credits registers before BOB with 184 credits, but JOE can't
register for the 12 credit physics class for lack of credits, while BOB may not be able to for lack of seats by the time it's his turn.)

Betting phase 4:
At the end of registration, the betting phase repeats. Any students who
have enroled in every course that they want will stop at this point, otherwise
the cycle of betting->sorting->registration->betting will repeat until every
student is equally dissatisfied with their share of classes.



TLDR;

While this registration system is more of a game theory problem than an actual
reasonable scheduler, it does serve the purpose of ensuring that everyone is
atleast approximately the same amount of unhappy by the end of the scheduling
period. (yay communism) Because it adjusts to given user input to make 
popular classes expensive and unpopular classes cheap, few people (if any) 
will end up being able to enrol in many popular classes, and few people will 
be given only unpopular classes. Additionally, the larger the student body
is, the more efficient it will become due to more accurate predictions, 
allowing for costs to approach true value faster.






  --  NOTE: This project relies extensively on the Google API, which obviously
      requires multi-step authentication protocols. I have not uploaded my
      private authentication tokens (for obvious reasons) here, and without
      them you'll be unable to access spreadsheets/run the scripts.

To run:

1) Execute
   \$ python Scheduler.py

2) In order to progress to the second stage, manually increment 
   'sheet_num' variable in Scheduler.py then execute again.
