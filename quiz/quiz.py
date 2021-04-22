'''
Created on Apr 21, 2021

@author: Yazmin Favela
'''

score = 0

print ("1) What is the power house of the cell?")
answerOne = input("ENTER A LETTER: A) mitochondria B) nucleous C) ribosome")

if (answerOne.lower() == "a"): 
        score = score + 1  
        print ("Correct") 
else:
    print ("Incorrect, the correct answer is A")
    

print ("2) How many states comprise the United States?")
answerTwo = input("ENTER A LETTER: A) 13 B) 45 C) 50")

if (answerTwo.lower() == "c"): 
        score = score + 1  
        print ("Correct") 
else: 
    print ("Incorrect, the correct answer is C")
    
    
print ("In y = mx + b, what does m stand for?")
answerThree =  input("A) slope B) output C) I don't understand math")

if (answerThree.upper() == "A"): 
        score = score + 1  
        print ("Correct") 
else:  
    print ("Incorrect, the correct answer is A")
    
    
print ("In English, a person, place or thing is called:")
answerFour = input("A) verb B) adjective C) noun")

if (answerFour.upper() == "C"): 
        score = score + 1   
        print ("Correct")  
else: 
    print ("Incorrect, the correct answer is C")
    
    
p = score/4
print ("You got a " + str(score) + "/4.")