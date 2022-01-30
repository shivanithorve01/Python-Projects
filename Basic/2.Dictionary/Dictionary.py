'''
DICTIONARY 

With this Dictionary Project,we will learn how to load an external data file in our Python project.
In this Project,we will load a '.json' file consisting of python data structure Dictionary containing key-value pair,
where key will be Word in the dictionary and value will be its meaning.

There are some things needed in Dictionary :
    1)If user enter combination of captial and small letters,then also 
      it should print the output.eg sMall
    2)If user enter first letter capital and others small or vice-a-versa
      then also it should print the output.eg Dog,dOG
    3)If user enter word in capital letters then also it should print the output.eg.DOG
    4)If user enter wrong spelling for the word then it should print closely matched output for that word.
      eg. Dogi , it should print all closely matched outputs 
'''
# IMPORTING EXTERNAL DATA 
import json
data = json.load(open('data.json'))
# IMPORTING get_close_matches FUNCTION FROM difflib TO GET CLOSE MATCH OUTPUT FOR WRONG SPELLED INPUTS
from difflib import get_close_matches

#Function TO SEARCH FOR DATA VALUES FROM JSON FILE
def meaning(word):
    #To avoid combinations of capital and small letters in the input, convert it in lowercase for easy
    # searching in json file as all keys in json file are in lowercase letters.
    word = word.lower()
    #Here,word is key in the dictionary and if it is found in the dictionary then data[word]  
    #will return its value. 
    if word in data :
        return data[word]
    #if there is any spelling errors in the input, then get_close_matches function will return
    #the value of closest word of the input from the dictionary (json file)
    elif len(get_close_matches(word,data.keys())) > 0 :
        #(get_close_matches(word,data.keys())[0])) will return the first closest value from the list of
        # the close matches from the dictionary.
        print("Did you mean %s ?" %(get_close_matches(word,data.keys())[0]))
        choice = input("Press 'y' for Yes and 'n' for No: ")
        if choice == "y" :
            return data[get_close_matches(word,data.keys())[0]]
        elif choice == "n" :
           return ("Sorry, Your word doesn't exist !") 
        else:
            return ("You have entered a wrong choice.Please select 'y' for Yes or 'n' for No")
    else :
        return ("Sorry, Your word doesn't exist !")

# DRIVER CODE :
print ('***** WELCOME TO THE DICTIONARY *****')
x = 1
while x==1:
    word = input("\t\nEnter the word to be searched : ")
    output = meaning(word)
    #if there is more than one meanings for a word then it should print all of them.
    if type(output) == list :
        for item in output:
            print(item)
    else :
        print(output)
    condition = input("Enter 'y' to continue 'x' to exit the Dictionary:")
    if (condition == "x"):
        x+=1
    if condition == "y" :
        x=1

        


