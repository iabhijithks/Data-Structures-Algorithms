def locate_card(cards,query):
    lo,high =  0,len(cards)-1
            
    while lo <= high:
     m = int(lo + high /2)
     if query == cards[m]:
        return m
     elif query < cards[m]:
        lo = m - 1
     elif query > cards[m]:
        high = m + 1
    else:
     return - 1

    
print(locate_card([10,9,8,7,6,5,4,3,2,1], 7))