# Problem 1 – Time Slot Consolidation 


def consolidation(slots) :

	slots.sort()
	
	res = []
	n = len(slots[0])
	
	for i in range(n -1):

		st = slots[i][0]
		end = slots[i][1]
		
		while slots[i][1] > slots[i+1][0] :
			end = slots[i+1][1] 
			i = i + 1

		res.append((st, end)) 

	return res 





'''

Problem 1 – Time Slot Consolidation 

Hidden Test 1
Input

1

5 10

Output :- [(5, 10)]

----------------------


Hidden Test 2
Input

3

1 10

2 8

3 7

Output :-  [(1, 10)]

--------------------------


Hidden Test 3
Input

3

1 2

4 5

7 8

Output :- [(1,2), (4, 5), (7, 8)]

---------------------------------


Hidden Test 4
Input

4

8 10

1 3

15 18

2 6

Output :- [(1, 6), (8, 10), (15, 18)]

----------------------------------------


Hidden Test 5
Input

3

1 5

5 7

7 10

Output :- [(1, 10)]


'''
	
			
		
		
