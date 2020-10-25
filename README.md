# Assignment 3 Part A
Github Repo - 
## Q1. Common Leader
1. Read json using `json.load`
2. Stored leader-employee in dictionary in form `{employee:leader}`
3. Created a list for each queried employee.
4. Level of common leader is the index of common in respective list.
5. Printed `No common leader` if one of the queried employees is the topmost leader.

## Q2. Date Difference
1. Accepted input date formats - `dd/mm/yyyy` or `dd.mm.yyyy` or `dd-mm-yyyy` or `ddth Month, yyyy` or `ddth Mon, yyyy`.
2. Converted date to tuple with `(dd,mm,yyyy)`
3. Calculated number of days from year `0000`.
4. Calculated difference of both days and saved in output file.

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