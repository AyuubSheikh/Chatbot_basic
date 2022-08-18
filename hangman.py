import random

likelyAnswers = ["arsenal" , "chelsea", "liverpool", "spurs", "huddersfield", "leicester", "southampton", "watford", "burnley"] #I changed the list to football teams.

random.shuffle(likelyAnswers)

answer = list(likelyAnswers[0])

display = [] #Empty list named display
used = []

display.extend(answer)#This includes the variable answer to display

used.extend(display)

for i in range(len(display)): #This iterates through the list 'display'
    display[i] = "_" #This replaces each index in the list with '_'


print(' '.join(display)) #The join command puts a space between each '_'
print()

count = 0 #This counter stops once all letters have been guessed

incorrect = 5

while count < len(answer)and incorrect > 0: #it keeps asking until the user gusses it
    guess = input("Enter a guess: ")
    guess = guess.lower()
    print(count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count + 1
            
            used.remove(guess)
            
    if guess not in display:
        incorrect = incorrect - 1
        print("Nope! You have", incorrect, "chances")
    print("You have guessed: ", count, "correct letters.")
    print("You have", incorrect, "chances left.")
        

    print(' '.join(display))
    print()
    
if count == len(answer):
    print("Congratulations, you guessed the word!")
else:
    print("Game Over, You ran out of guesses!") #The print statements were adjusted.
    
#https://www.youtube.com/watch?v=jPmBUoSZ6tY&t=3s <------ I got the idea/code from here 
#https://www.youtube.com/watch?v=QgqWINDe59Q <------ This is the second part of the code (bug fixing)
#https://www.youtube.com/watch?v=klqXcvohw5Q <------ This is the code for making it so theres a limit to the guesses