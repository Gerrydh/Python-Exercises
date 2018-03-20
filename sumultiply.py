def sumultiply(x, y):
    #create a variable that will become the answer
    total = 0
    #loop over y adding x to the answer
    for i in range(y):
        total = total + x
    return total
#test with the below variables
print(sumultiply(11, 13))
print(sumultiply(5, 123))
