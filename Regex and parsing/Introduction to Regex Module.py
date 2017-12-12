## Problem Statement:
---------------------------------------------------------------------------------------------
Sample Input

4  
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output

False
True
True
False

Explanation

4.0O0: O is not a digit.
-1.00: is valid.
+4.54: is valid.
SomeRandomStuff: is not a number.
-----------------------------------------------------------------------------------------------

Solution:
    
#regex library
import re
#Count how many inputs
quantity = int(input())
#Create a for loop to iterate over qauntity
for index in range(quantity):
    #Create regex expression that catches numbers only and gives out True for numbers else False
    print(bool(re.match(r'[-+]*[0-9]\.[0-9]+$', input())))

'''
[-+] : says it can start with - or +
*: says "0 or more"
[0-9]: says any number ranging from 0 to 9
\.: says followed by a dot
[0-9]+$: says any number between 0 to 9 followed by 1 or more of those numbers and $ means match only those previousely written
'''
