# Assignment 3 Part A
Github Repo - https://github.com/shubh299/SSD-Assignment3a
Branch - 3b

## Q1. Common Leader
1. Changes in line 16 and 17 - changes to take multiple employees as input
2. Changes in line 20 -  to check if an input id is topmost employee in organisation.
3. Changes in line 24 to 33 - creating a list of lists of each employee's leaders
4. Changes in line 36 to 43 - finding common leader from list of leaders instead of 2 lists
5. Changes in line 44 to 47 - printing levels between employee and common leader.

## Q2. Date Difference
1. 

## Q3. Common Slot
1. Used datetime and json library.
2. Read input files and replaced `'` with `"` to bring it to json format.
3. Used json.loads to get the input as dictionary.
4. Created `Employee` class which has
* Attributes -
    * Name
    * Date of given slots
    * List of Busy Slots
    * List of Free Slots
* Method -
    * findFreeSlots - which finds free slots(using `datetime`)and appends to list of free slots

5. Used `datetime` to find common slots slots and get first common slot which can accomodate given slots