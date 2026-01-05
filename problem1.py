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






	
			
		
		
