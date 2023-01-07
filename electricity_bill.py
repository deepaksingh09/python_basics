"""
electricity bill
unit  - electricity comsumed by the user
amount-- bill generated on the basis of usage
"""
amount=0
unit=int(input("enter the unit that comsumed="))
if unit<=100:
    amount=0
    print("charges=",amount)
elif unit>100 and unit<=200 :
    amount=(unit-100)*5
    print("charges",amount)
elif unit>200:
    amount=500+(unit-200)*10
    print("charges",amount)
print("thank you for paying the bills")




