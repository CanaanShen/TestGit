'''
Created on Mar 12, 2015

@author: dcsliub
'''
import re
class DataStat:
    
    def statData(self, fileName):
        
        inputFileHandler = open(fileName, "r")
        
        line = " "
        totalCount = 0
        count = 0
        while len(line) != 0:
            line = inputFileHandler.readline().strip("\n").strip()
            
            if len(line) < 3:
                continue
            
            lineList = line.split(":")
            if len(lineList) < 2:
                print("lineList error")
                continue
            
            wordList =[]
            wordList = lineList[1].strip().split(" ")
            #wordList = re.split("\s+", lineList[1])
            
            print(lineList[0], " ", str(len(wordList)))
            count = count + 1
            totalCount =totalCount + len(wordList)
        #-->while
        print("totalCount", str(totalCount))
        
dataStat = DataStat()
folder = "lastfm"
fileName = folder + "\\" + "user_tag_order.dat"
dataStat.statData(fileName)