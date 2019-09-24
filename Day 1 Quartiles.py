#Day 1: quartiles
#Task
#Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.
numberOfArrayElements = int (input())
#asigns the intergers separated by space into a list
elementsInArray = list(map(int,input().split())) 

#median
def median(fnumberOfArrayElements, felementsInArray):
    srtredlist= sorted(felementsInArray)
    if fnumberOfArrayElements%2!=0:
        midl = int(fnumberOfArrayElements / 2)
        return srtredlist[midl]
    else:
        odd = int((fnumberOfArrayElements / 2) -1)
        ev = int((fnumberOfArrayElements / 2)) 
        return int(float(srtredlist[odd] + srtredlist[ev]) / float(2))


#odd or even number of elements
def isOdd(fnumberOfArrayElements):
    result= False
    if (fnumberOfArrayElements %2 !=0):
        result= True
    return result

#odd quartiles
def oddQuartiles (fnumberOfArrayElements, felementsInArray):
    sortedElements=sorted(felementsInArray)
    lowerhalfupperlimit=int((fnumberOfArrayElements / 2) )
    upperhalflowerlimit=int((fnumberOfArrayElements / 2) +1)
    #print(felementsInArray[:lowerhalfupperlimit])
    #print(lowerhalfupperlimit)
    firstQuartile=int(median(lowerhalfupperlimit,sortedElements[:lowerhalfupperlimit]))
    #print(felementsInArray[upperhalflowerlimit:])
    #print(upperhalflowerlimit)
    thirdquartile=int(median(upperhalflowerlimit-1,sortedElements[upperhalflowerlimit:]))
    return firstQuartile, thirdquartile

#even quartiles
def evenQuartiles (fnumberOfArrayElements, felementsInArray):
    sortedElements=sorted(felementsInArray)
    lowerhalfupperlimit=int((fnumberOfArrayElements / 2))
    upperhalflowerlimit=int((fnumberOfArrayElements / 2))
    #print(felementsInArray[:lowerhalfupperlimit])
    #print(lowerhalfupperlimit)
    firstQuartile=int(median(lowerhalfupperlimit,sortedElements[:lowerhalfupperlimit]))
    #print(felementsInArray[upperhalflowerlimit:])
    #print(upperhalflowerlimit)
    thirdquartile=int(median(upperhalflowerlimit,sortedElements[upperhalflowerlimit:]))
    return firstQuartile, thirdquartile
#quartiles answer Q1, Q2, Q3
#print(isOdd(numberOfArrayElements))
if(isOdd(numberOfArrayElements)):
    firstquart,thirdquart=oddQuartiles(numberOfArrayElements,elementsInArray)
    print(firstquart)
    print(median(numberOfArrayElements,elementsInArray))
    print(thirdquart)
else:
    firstquart,thirdquart=evenQuartiles(numberOfArrayElements,elementsInArray)
    print(firstquart)
    print(median(numberOfArrayElements,elementsInArray))
    print(thirdquart)
