class Solution(object):
    def reconstructQueue(self, people):
        newpeople = []
        if(len(people)!=0):
	        hlist,klist = zip(row for row in zip(*people))
	        hlist = list(set(hlist[0]))
	        hlist.sort()
	        hlist.reverse()
	        for h in hlist:
	        	part = []
	        	for i in range(len(people)):
	        		if(people[i][0]==h):
	        			part.append(people[i])
	        	part.sort()
	        	for partpart in part:
	        		if(len(newpeople)==0):
	        			newpeople.append(partpart)
	        		else:
	        			newpeople.insert(partpart[1],partpart)
        return newpeople
sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))
