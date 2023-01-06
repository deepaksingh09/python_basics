for x in range(3):
    pin_number=int(input("enter your pin:"))
    if pin_number == 1245:
        print("welcome to Bank")
        break
    else:
        print("you enter wrong pin")
        if x<2:
            ans= int(input("to continue press 1="))
            if ans==1:
                continue
            else:
                break
        else:
            print("card is blocked")
print("thank you")