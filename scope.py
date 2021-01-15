class Difference:
    def __init__(self, a):
        self.__elements = a
    
    # Add your code here
    
    def computeDifference(self):
        self.minn = self.__elements[0]
        self.maxx = self.__elements[0]
        
        for n in self.__elements:
            if n <self.minn:
                self.minn = n
            if n > self.maxx:
                self.maxx = n
        self.maximumDifference = abs(self.maxx - self.minn)
        
        return self.maximumDifference
            

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)