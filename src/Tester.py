'''
Created on Oct 19, 2014

@author: xyshen
'''
import math
from decimal import Decimal
class Tester:

    def __init__(self):
        '''
        Constructor
        '''
        self.userCount = 23152
    
    def add(self, a, b):
        return a + b
    
    def output(self):
#         print("user count: " + str(self.userCount))
        strArray = []
        strArray.append("aaa")
        strArray.append("bbb")
        
#         for str in strArray:
#             print(str)
#         print(strArray[0])
        
        str1 = "           a  a b  "
        str2 = "aa"
        
#         if str1 == str2:
#             print(str1 + str2)
#         print(str1)
#         str1 = str1.strip()
#         print(str1)
        str3 = "9"
        #print(float(str), end="")
#         for i in range(1, 4):
#            print(i)
        #print(pow(2, 3+1))
        #print(math.log2(8))
        str3 = self.add(str1, str2)
        #print(str3)
        lineList = [3, 5, 1, 2]
        lineList.pop()
        #print(lineList)
        #print(range(len(lineList)))
        #for i in range(len(lineList)):
            #print(lineList[i])
#         print(lineList.index(3))
#         lineList.pop()
#         print(lineList)
#         lineList.insert(2, 10)
#         print(lineList)
#         lineList.insert(0, 11)
#         print(lineList)
        #lineList2 = lineList
        #lineList2.sort(reverse=True)
        #print(lineList)
        #print(lineList2)
        strd = "4.909192725185534E-4"
        d = float(strd) + 1.0
        if "2518" in strd:
            print(2518)
#         print(d)
#         for i in range(0, 3):
#             print(i)
        #print(1)
        #print(2)
        #
        #print(str(3) + " ", end="")
        #print(str(4) + " ", end="")
        #print(str(d))
    #definition
    
tester = Tester()
str = tester.output()
#print(str)
print("Program Ends")