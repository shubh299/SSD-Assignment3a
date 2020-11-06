# Assignment 3 Part A
Github Repo - https://github.com/shubh299/SSD-Assignment3a
Branch - 3b

## Q1. Common Leader
1. Changes in line 16 and 17 - changes to take multiple employees as input
2. Changes in line 20 -  to check if an input id is topmost employee in organisation.
3. Changes in line 24 to 33 - creating a list of lists of each employee's leaders
4. Changes in line 36 to 43 - finding common leader from list of leaders instead of 2 lists
5. Changes in line 44 to 47 - printing levels between employee and common leader.
6. Input file - `org.josn`.

## Q2. Date Difference
1. Change in Line 11 - Changed definition of `returnDate` function to handle mm/dd/yyyy format. In this case date_format=1, and 0 otherwise.
2. Added lines 14-15,19-20,24-25 - To handle mm/dd/yyyy case.
3. Modified lines 77 to 84 - To handle commandline argument and call to modified `returnDate` function.
4. Input file - `date_calculator.txt`.

## Q3. Common Slot
1. Added Line 3 - Added `import os` to read input files from a directory.
2. Changed lines 35 to 45 - Read files one by one, created an object of `Employee` for each, finding their free slots and listing them in `employee_list`.
3. Changed lines 49-50 - To write all available slots for all employees.
4. Changed lines 52 to 56 - Checking if given slot of all employees are on same date or not.
5. Changed lines 58-73 - To find list of common free slots along all employees.
6. Changed line 82 - To print date of slot booked.
7. Input files are in a directory named `input_files` which is in same folder as `q3.py`.