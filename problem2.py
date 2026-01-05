


# Problem 2 – Maximum Signal Strength


def maxi_signal_strenth(signals) :
	
	signals.sort(reverse=True)
	
	max_strenth = 0
	for i in range(k):
		max_strenth += signals[i]

	return max_strenth 
		





'''

Hidden Cases 

Problem 2 – Maximum Signal Strength
Hidden Test 1
Input

5

4 2 7 1 9

1

Output :-  9


---------------------

Hidden Test 2
Input

4

1 2 3 4

Output :- 0

---------------------


Hidden Test 3
Input

5

-8 -3 -6 -2 -5

2

Output :- -5

---------------------


Hidden Test 4
Input

5

1 2 3 4 5

3

Output :- 12


--------------------------

Hidden Test 5
Input

6

4 -1 2 1 -5 4

2

Output :- 8


'''



