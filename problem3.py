

# Problem 3 – Communication Channel Analyzer Problem Statement

def channel_analyzer(s):

	n = len(s)
	max_cnt = 0
	
	i = 0
	st = ""
	for j in range(n) :

		cnt = 0
		if s[j] not in st :
			st += s[j]
			cnt = j - i + 1
		else :
			while s[i] != s[j] :
				i += 1
			

		max_cnt = max(cnt, max_cnt)

	return max_cnt
			
		


'''


Problem 3 – Communication Channel Analyzer
 

Hidden Test 1
Input

a

Output :- 1


------------------------


Hidden Test 2
Input

aaaaaa

Output :- 1


---------------------


Hidden Test 3
Input

abcdef

Output :- 6

--------------------


Hidden Test 4

Input

aa

Output :- 1

---------------------


Hidden Test 5
Input

abca

Output :- 3


''' 
