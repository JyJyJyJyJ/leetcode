class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        count = 0
        if(numerator==0):
        	return(str(0))
        if(denominator==0):
        	return("error!")
        flags = "" if(numerator*denominator>0) else "-"

        numerator = abs(numerator)
        denominator = abs(denominator) 

        yu = numerator%denominator
        newresult = numerator//denominator
        if(yu==0):
        	return(flags+str(newresult))
        result = str(newresult)+"."
        zheng = len(result)

        listcircle = []
        while True:
        	listcircle.append(yu)
        	numerator=yu*10
        	yu=numerator%denominator
        	newresult = numerator//denominator
        	result+=str(newresult)

        	if yu in listcircle:
        		lenn = zheng+listcircle.index(yu)		
        		return flags+result[:lenn]+"("+ result[lenn:]+")"
        		
        	if yu == 0:return flags+result
        	
        	
sol = Solution()
print(sol.fractionToDecimal(1,6))
