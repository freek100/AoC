# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:31:46 2020

@author: freek
"""
def readData(filename):
    data= open(filename, 'r').read().split('\n')
    for x in data:
        data[data.index(x)]=int(x)
    return data

def runSums(numbers):
    checknum= numbers[:25]
    for num in numbers[25:]:
        if checkSum(num,checknum)==True:
           checknum.append(num)
           checknum.pop(0)
        else:
            notsum= num
            break
    return notsum
      
def checkSum(number, checklist): #Check if number is a sum of 
    valid=False
    for i in range(len(checklist)-1):
        for j in range(i,len(checklist)):
            if checklist[i]+checklist[j]==number:
                valid=True
    return valid

def contSum(target,numbers):
    for i in range(len(numbers)):
        j=i
        sumval= numbers[i]
        while sumval<=target:
            j+=1
            sumval+=numbers[j]
            if sumval==target:
                contset= numbers[i:j+1]
    return min(contset)+max(contset)
 
def main():   
    numlist= readData('day9.txt')
    p1= runSums(numlist)
    print(f'Part 1) {p1}')
    print(f'Part 2) {contSum(p1,numlist)}')
    
def timedMain():
    from timeit import default_timer as timer
    start=timer()
    main()
    end=timer()
    print(f'Elapsed time= {end-start} seconds')

timedMain()