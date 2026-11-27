#Initiliasing variables and game introduction

name = input("Welcome to this maths quiz game! What's your name? ")
#ADD MORE EXPLANATION HERE

print("Hi there", name, "What mode would you like to try? Easy (1), medium (2) or hard (3)?")
mode = int(input(""))

#Question and answer banks for each mode
easy_q = ["2+3= ", "5+5= ", "23+21= ", "100-57= ", "88-12= "]
easy_a = [5,10,44,43,76]
med_q = ["45/5= ", "10*3= ", "15*4= ", "12*7= ", "27/9= "]
med_a = [9,30,60,84,3]
hard_q = ["(2+3)*4= ", "20/4*2= ", "5+2^3","3*(1+2^2)= ", "50-5*(6-2)= "]
hard_a = [20,10,13,15,30]

#subroutines for each difficulty mode

def easy_mode(points):

    for i in range(5):
        print(easy_q[i])
        answer = int(input(""))
        if answer == easy_a[i]:
            print("Correct!")
            points+=1
        else:
            print("Wrong. The answer is", easy_a[i])
    return points
def med_mode(points):

    for i in range(5):
        print(med_q[i])
        answer = int(input(""))
        if answer == med_a[i]:
            print("Correct!")
            points+=1
        else:
            print("Wrong. The answer is", med_a[i])
    return points
def hard_mode(points):
    for i in range(5):
        print(hard_q[i])
        answer = int(input(""))
        if answer == hard_a[i]:
            print("Correct!")
            points+=1
        else:
            print("Wrong. The answer is", hard_a[i])
    return points

#Code logic

match mode:
    case 1:
        points = easy_mode(0)
    case 2:
        points = med_mode(0)
    case 3:
        points = hard_mode(0)
    case _:
        print("That is not an option. Please restart the game.")
        quit()


print("Well done", name, "You earned", points, "points!")