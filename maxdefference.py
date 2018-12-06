class Difference:
    def __init__(self, a):
        self.__elements = a
        
	# Add your code here
    def computeDifference(self):
        self.__maxDifference = max(self.__elements) - min(self.__elements)

    def getmaximumDifference(self):
        return self.__maxDifference
    

    maximumDifference = property(getmaximumDifference)



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
