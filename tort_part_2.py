#Driver: Kate Anderson U21933376
#Navigator: Christiana Hellenbrand U29955524

#This program is designed to mimic the race between a tortoise and a hare by randomly choosing their positions based off of given probabilities and looping through the race until one wins



import random

print('ON YOUR MARK... GET SET...')
print('GO!!!!!!')
print("AND THEY'RE OFF!")
print()


    
def main():

    tortprog = 0 #initialized necessary variables

    hareprog = 0
    seconds = 0


    finalseconds = raceprog(seconds, hareprog, tortprog) #counts how many iterations it took to win the race
    
    print('Time of race:',finalseconds,'seconds.') 
    
def tortoise(tortposition,tortprog): #tortoise progress function

    tortprog = random.randint(1,10)#initializes random int into tortprog

    #if statement creates probabilities for each type of movement and updates tortposition
    if tortprog in range(1,6): 
        tortposition += 3 #fastplod
        return tortposition
    
    elif tortprog in range(6,8):
        tortposition -= 5 #slip
        return tortposition
    
    else :
        tortposition += 1 #slowplod
        return tortposition
        
def hare(hareposition,hareprog): #hare progress function

    hareprog = random.randint(1,10)#initializes random int into hareprog

    #if statement creates probabilities for each type of movement and updates tortposition
    if hareprog in range(1,3):
        hareposition += 0 #sleep
        return hareposition
       
    elif hareprog in range(3,5):
        hareposition += 7 #bighop
        return hareposition
        
    elif hareprog in range (5,6):
        hareposition -= 10 #bigslip
        return hareposition
        
    elif hareprog in range (6,9):
        hareposition +=1 #smallhop
        return hareposition
        
    else:
        hareposition -= 2 #smallslip
        return hareposition



def finishLine(tortposition, hareposition): #checks for when race is finished 
    if (tortposition >=50) or (hareposition >=50):
        return True

def fin(hareposition, tortposition): #function outputs results of race by comparing positions
    if hareposition > tortposition:
        print('Hare wins. Yay.')
        game = True
    else:
        print('Tortoise wins!! Yay!')
        game = True

def checkFalseStart(position): #function for checking false starts (meaning falls behind position 1)
    if (position <1):
        return 1
    else:
        return position

    
def raceprog(seconds, hareprog, tortprog): #function to keep track of race progress
    hareposition = 1 #initializes variables to 1 originally
    tortposition = 1


    #begins iteration for each second
    for i in range (1,51): 
        seconds += 1 #adds second after each iteration
        #initialize counting line spaces for both hare and tort position
        j = 0
        n = 0
        
        #calls hareposition for each iteration
        hareposition = hare(hareposition,hareprog)
        hareposition = checkFalseStart(hareposition) #checks for a false start

        #calls tortposition for each iteration
        tortposition = tortoise(tortposition,tortprog)
        tortposition = checkFalseStart(tortposition)#checks for a false start

        #checks to see if race is completed (if have reached 50 spaces) and if so it calls the fin function to print out results
        if finishLine(tortposition, hareposition) == True:
            fin(hareposition, tortposition)
            return seconds 
            
        # determines who is in lead and which animal to print first
        if (hareposition > tortposition): #for hare being in lead
            while tortposition != j: #counts number of spaces until prints T
                print(' ',end='') #prints that number of spaces
                j += 1

            print('T',end='')

            #subtracts tort from hare position in order to determine difference in spacing
            while (hareposition - tortposition) != n:
                print(' ',end='') #prints the difference of their spacing
                n += 1

            print('H',end='')

        #for tortoise being in the lead  
        elif (tortposition > hareposition):
            while hareposition != j: #counts number of spaces until prints H
                print(' ',end='') #prints that number of spaces
                j += 1

            print('H',end='')

            while (tortposition - hareposition) != n: #subtracts hare from tort position to determine difference in spacing  
                print(' ',end='') #prints the difference in the spacing
                n += 1

            print('T',end='')
            
        else: #if they equal each other, prints OW
            print('OW!!',end='')
            

        print() #adds newline between each iteration
    fin(hareposition, tortposition) #calls the fin function to get results
    return seconds #returns number of iterations for game
        
            
    

main()
