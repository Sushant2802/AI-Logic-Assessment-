

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
			
			




