#Day 0: Mean, Median, and Mode
numberOfArrayElements = int (input())
#asigns the intergers separated by space into a list
elementsInArray = list(map(int,input().split())) 

#mean
def mean(fnumberOfArrayElements, felementsInArray):
    total=0
    for x in range(fnumberOfArrayElements):
        total+=felementsInArray[x]
    return total/fnumberOfArrayElements

#median
def median(fnumberOfArrayElements, felementsInArray):
    srtredlist= sorted(felementsInArray)
    if fnumberOfArrayElements%2!=0:
        midl = int(fnumberOfArrayElements / 2)
        return srtredlist[midl]
    else:
        odd = int((fnumberOfArrayElements / 2) -1)
        ev = int((fnumberOfArrayElements / 2)) 
        return float(srtredlist[odd] + srtredlist[ev]) / float(2)
#mode
def mode(fnumberOfArrayElements, felementsInArray):
    srtredlist= sorted(felementsInArray)
    current=0
    mode= 0
    count, maxOccurrences=0, 0
    for x in range(fnumberOfArrayElements):
        if (srtredlist[x]==current):
            count +=1
        else:
            count = 1
            current = srtredlist[x]
        if (count > maxOccurrences or (count == maxOccurrences and current < mode)):
                maxOccurrences = count
                mode = current
    return mode
   
#print (elementsInArray)
print (mean(numberOfArrayElements, elementsInArray))
print (median(numberOfArrayElements, elementsInArray))
print (mode(numberOfArrayElements, elementsInArray))