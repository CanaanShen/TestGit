'''
Created on Mar 21, 2015

@author: dcsliub
'''

class TopicExtractor:
    
    def extractTopKWord(self, lineList, idWordMap, topK):
        topKWordPrbtyListMap = {}
        topKIDList = []
        topKPrbtyList = []
        
        for i in range(len(lineList)):
            prbty = lineList[i]
            
            if len(topKIDList) == 0:
                topKPrbtyList.append(prbty)
                topKIDList.append(i)
                continue
            
            if len(topKPrbtyList) == topK:       
                if prbty <= topKPrbtyList[topK-1]:    #unnecessarily compared
                    continue; 
            
            mark = 0
            for k in range(len(topKPrbtyList)):
                if prbty > topKPrbtyList[k]:
                    topKPrbtyList.insert(k, prbty);
                    topKIDList.insert(k, i)
                    mark = 1
                    break;
            #for
            
            if mark == 0 and len(topKPrbtyList) < topK:
                topKPrbtyList.append(prbty)
                topKIDList.append(i)
            
            if len(topKPrbtyList) > topK:   # the length of list is topK
                topKPrbtyList.pop()
                topKIDList.pop()
        #for
                
        topKWordList = []  
        for i in topKIDList:
            word = idWordMap[i]
            topKWordList.append(word)
        
        if len(topKWordList) != topK or len(topKPrbtyList) != topK:
            print("topKWordList or topKPrbtyList size errors")
            return topKWordPrbtyListMap
        
        topKWordPrbtyListMap[0] = topKWordList
        topKWordPrbtyListMap[1] = topKPrbtyList
        return topKWordPrbtyListMap
    #definition
    
    def extractTopic(self, topicWordPrbtyFileName, wordMapFileName, topicalWordsFileName, topicalPrbtyFileName, topK):
        
        topicWordDisFileHandler = open(topicWordPrbtyFileName, "r")
        wordMapFileHandler = open(wordMapFileName, "r")
        
        idWordMap = {}
        line = " "
        while len(line) != 0:
            line = wordMapFileHandler.readline().strip("\n").strip()
            word_id = []
            word_id = line.split(":")
            
            if len(word_id) < 2:
                continue
            
            if "yelp" in wordMapFileName:
                wordStr = word_id[0]
                wordID = int(word_id[1])
            
            if "lastfm" in wordMapFileName:
                wordStr = word_id[1]
                wordID = int(word_id[0])
            
            idWordMap[wordID] = wordStr
        #while
        
        line = " "
        topicNumber = 0
        topicWordsMap = {}
        topicPrbtyMap = {}
        while len(line) !=0:
            print("topicNumber ", topicNumber)
            line = topicWordDisFileHandler.readline().strip("\n").strip()
            
            lineStrList = []
            lineList = []
            lineStrList = line.split(" ")
            for prbty in lineStrList:
                if prbty != " " and len(prbty) > 1 and prbty is not None:
                    lineList.append(float(prbty)) # string -> float
            
            if len(lineList) == 0:
                continue
            
            topKWordPrbtyListMap = {}
            topKWordPrbtyListMap = self.extractTopKWord(lineList, idWordMap, topK)
            
            topicWordsMap[topicNumber] = topKWordPrbtyListMap[0]  # word1 word2...
            topicPrbtyMap[topicNumber]= topKWordPrbtyListMap[1]  #prbty1  prbty2...
            
            topicNumber = topicNumber + 1

        #while
        print("topicNumber number ", str(topicNumber))

        self.output(topicalWordsFileName, topicalPrbtyFileName, topicWordsMap, topicPrbtyMap, topK, topicNumber)
    #definition
    
    #write to files
    def output(self, topicalWordsFileName, topicalPrbtyFileName, topicWordsMap, topicPrbtyMap, topK, topicNumber):
        
        topicalWordsFileHandler = open(topicalWordsFileName, "w") 
        topicalPrbtyFileHandler = open(topicalPrbtyFileName, "w")
        
        for k in range(0, topK):
            for t in range(0, topicNumber):
                topicWordList = []
                topicDisList = []
                topicWordList = topicWordsMap[t]
                topicDisList = topicPrbtyMap[t]
                
                word = topicWordList[k]
                prbty = topicDisList[k]
                
                topicalWordsFileHandler.write(word + "\t")
                topicalPrbtyFileHandler.write(str(prbty) + "\t")
            #for
            topicalWordsFileHandler.write("\n")
            topicalPrbtyFileHandler.write("\n")
        #for 
        topicalWordsFileHandler.close()
        topicalPrbtyFileHandler.close()
#class

topicExtrator = TopicExtractor()

dataset = "lastfm"  #lastfm
useroritem = "item"

topicNumber = 20
filePrefix = "C:\\Users\\Yueshen\\workspace_luna\\Campaign3\\" + dataset 
fileSuffix = "_2.0_0.1_1000.dat"

topicWordDisFileName = filePrefix + "\\lda\\" + useroritem + "_phi_" + str(topicNumber) + fileSuffix
wordMapFileName = filePrefix + "\\" + dataset + "_word_id_map.dat"
topicalWordsFileName = filePrefix + "\\lda\\" + useroritem + "_topicalwords_" + str(topicNumber) + ".dat"
topicalPrbtyFileName = filePrefix + "\\lda\\" + useroritem + "_topicalprbty_" + str(topicNumber) + ".dat"

topK = 20

topicExtrator.extractTopic(topicWordDisFileName, wordMapFileName, topicalWordsFileName, topicalPrbtyFileName, topK)
print("Program ends")
        