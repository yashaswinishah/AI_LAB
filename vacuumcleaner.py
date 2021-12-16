def check(stack):
    if stack[-1]=="Right" or stack[-1]=="Left":
        if stack[-2]=="Left" or stack[-2]=="Right" :
            return False
stack=[]
flag=True
count=1
while flag:
    perc=input("Enter the percept")
    loc=input("Enter the location")
    if loc=="A":
        if perc=="Dirty":
            print("Action: suck...turn right")
            stack.append("Suck")
            stack.append("Right")  
        else:
            print("Action: turn right")
            stack.append("Right")
    else:
        if perc=="Dirty":
            print("Action: suck.....turn left")
            stack.append("Suck")
            stack.append("Left")
        else:
            print("Action: turn left")
            stack.append("Left")
    count=count+1
    if count>2:
        flag=check(stack)
print("Both A and B are clean")
