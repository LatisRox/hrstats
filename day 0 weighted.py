#Day 0: Mean, Median, and Mode
numberOfArrayElements = int (input())
#asigns the intergers separated by space into a list
elementsInArray = list(map(int,input().split())) 
#asigns the weights of the intergers separated by space into a list
weightsInArray = list(map(int,input().split())) 

def weightedAverage(fnumberOfArrayElements,felementsInArray,fweightsInArray):
    nominador=0
    denominador=0
    for x in range(fnumberOfArrayElements):
        nominador+=felementsInArray[x]*fweightsInArray[x]
        denominador+=fweightsInArray[x]
    return round(nominador/denominador,1)

print (weightedAverage(numberOfArrayElements,elementsInArray,weightsInArray))

