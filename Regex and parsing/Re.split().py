'''Problem statement:
Input Format

A single line of input containing the string .

Output Format

Print the numbers obtained after splitting the string on separate lines.

Sample Input

100,000,000.000

Sample Output

100
000
000
000

Note: Each line of output should only be the numbers. 
'''
______________________________________________________________________________________________________
## Solution:

# import model
import re
# get numbers 
numbers = input()
#split on any character that is not a number
print(*re.split('[\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]',numbers), sep = '\n')
______________________________________________________________________________________________________
'''
*: the '*' at the beginning removes '[]'
[\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]: special characters defined to split on

'''
