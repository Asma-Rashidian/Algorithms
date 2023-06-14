listItems = [2,10,18,26,32,54,58,59,66,69,70,71,95,98,100,110]
guess = int(input())

def Binary_Search (guess , listItems):
    
    low = 0 
    high = len(listItems)-1

    found = False

    while low <= high and found is not True:
        mid = (low + high) // 2
        
        if abs(low - high) == 1 and listItems[low]<guess and listItems[high]> guess:
            break
        elif listItems[mid] > guess:
            high = mid 
        elif listItems[mid] < guess:
            low = mid
        elif listItems[mid] == guess :
            found = True 
            print("Guess is found as %dth element of our list !!" %mid+1)
        
    if found is  False :
        print("The element does not exist !!!")

Binary_Search(guess , listItems)


# Recursive Form 

low = 0 
high = len(listItems) -1

def RBinary_Search(guess , listItems, low , high ):
    if high >= low :
        mid = (low + high ) // 2

        if listItems[mid] == guess:
            return mid+1
            
        elif listItems[mid] < guess :
            return RBinary_Search(guess , listItems , mid+1 , high)

        else:
            return RBinary_Search(guess , listItems , low , mid-1 )

    else :
        return -1 
    
result = RBinary_Search(guess , listItems , low , high)

if result != -1 :
    print("RBS: Guess is found as %dth element of our list !!" %(result)) 
else :
    print("RBS: The element does not exist !!!")

