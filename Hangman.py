
word = input("Enter the word you want guessed: ")

correctGuesses = ""
found = False
done = False # used to exit loop
lives = 6
previousGuess = ""
def searching(word,correctGuesses):
    search = input("enter a letter or a phase : ")
    search = search + correctGuesses
    # loops for comparing and outputing a string with the matching search word
    result = ""
    for char in word:
        found = False
        for char2 in search:
            if( char == char2):
                result = result + char        
                correctGuesses = correctGuesses + char  
                correctGuesses = "".join(set(correctGuesses)) # remove duplicate characters
                found = True
        if(found == False):
            result = result + "_"
    print(result)
    print("")
    print("")
    if (result.find("_")==-1):
        correctGuesses = result
    return correctGuesses

while(done == False):
  previousGuess = correctGuesses  
  correctGuesses = searching(word,correctGuesses)
  if (word == correctGuesses):
      print("you win, Well done")
      done = True
  if(previousGuess == correctGuesses):
      lives = lives - 1
      if(lives == 5 ):
          print("   o   ")
      elif(lives == 4):
          print("   o   ")
          print("  /    ")
      elif(lives == 3):
          print("   o   ")
          print("  /|   ")
      elif(lives == 2):
          print("   o   ")
          print("  /|\  ")
      elif( lives == 1):
          print("   o   ")
          print("  /|\  ")
          print("  /    ")
      elif(lives == 0 ):
          print("   o   ")
          print("  /|\  ")
          print("  / \  ")
          print("Game OVer")
          done = True
   

        
        

