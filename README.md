# Quinn-Mccluskey
Quinn-Mccluskey Algortihm for Logic gates.
In this project we will input "elements" and "Dont'Cares".
And outputs include:
1-Classification of Elements by number of binary numbers
2-First step of constructing PIs 
3-Extraction of EPIs 
And finally the final answer which is based on ABCD classification.

Example:

Enter Elements: 1,2,3,4,5,6,7

Enter DontCares: 0

1)Minterm 2)Maxterm : 1

Sorted Elements:  {'zero': [0], 'one': [1, 2, 4], 'two': [3, 5, 6], 'three': [7], 'four': []}

1st Combine:  {(0, 1): '000-', (0, 2): '00-0', (0, 4): '0-00', (1, 3): '00-1', (1, 5): '0-01', (2, 3): '001-', (2, 6): '0-10', (4, 5): '010-', (4, 6): '01-0', (3, 7): '0-11', (5, 7): '01-1', (6, 7): '011-'}

2nd Combine:  {(0, 1, 2, 3): '00--', (0, 1, 4, 5): '0-0-', (0, 2, 4, 6): '0--0'}

PIs:  {(3, 7): '0-11', (5, 7): '01-1', (6, 7): '011-', (0, 1, 2, 3): '00--', (0, 1, 4, 5): '0-0-', (0, 2, 4, 6): '0--0'}

EPIs:  []

Answer:  ['0---']

The Answer is:  A'
