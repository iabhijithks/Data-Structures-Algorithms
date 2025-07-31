def function(input,req):
    for i in range(0, len(input)):
        if (input[i]==req):
            return i
    else:
     return "Not found"

print(function([2,5,8,9,4],8))