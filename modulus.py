#check the last no is divisble by 3  or not

div=0
no=int(input("enter the  no="))
div=no%10
if div%3==0:
    print("no is divisble by 3")
else:
    print("no is not divisble by 3")