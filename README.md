# datepy
A python package for date related functionalities

At the moment, we can use this to do two things:
1.	Find the number of days between two dates.
2.	Find the names of days and their counts between two dates.
 
Steps to use:
1. git clone https://github.com/imaadmkhan1/datepy.git
2. cd datepy
3.	pip install .
 
Example usage:
 
import datepy
datepy.number_of_days(‘2018-01-01’,’2018-01-03’)</br>
->	3</br>
datepy.days_distribution(‘2018-01-01’,’2018-01-03’)</br>
-> {‘Monday’:1,’Tuesday’:1,’Wednesday’:1}</br>
