def locate_card(cards,query):
    p = 0
    while p < len(cards):
        if cards[p] == query:
            return p
        p +=1
    else:
        return -1
    
    

test = {'input': {'cards': [13,9,5,3,2,1], 'query':2 }, 'output': -1}

locate_card(**test['input']) == test['output']

#another way of testing:

result = locate_card(test['input']['cards'], test['input']['query'])
print(result)
