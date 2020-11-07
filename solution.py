

# We all love the future president (or Führer or duce or sōtō as he could find 
# them more fitting) donald trump, but we might fear that some of his many fans 
# like John Miller or John Barron are not making him justice, sounding too much 
# like their (and our as well, of course!) hero and thus risking to compromise him.

# For this reason we need to create a function to detect the original and unique 
# rythm of our beloved leader, typically having a lot of extra vowels, all ready 
# to fight the estabilishment.

# The index is calculated based on how many vowels are repeated more than 
# once in a row and dividing them by the total number of vowels a petty enemy 
# of America would use.

#RULES
#how many voewls are repeated more than once 
# and then divide by the total number of vowels
#round decimals by two decimal digits 



def trump_detector(trump_speech):
    """Gziven a string find the extra vowels and divide."""

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    trump_speech = trump_speech.lower()
    total = 0
    vcount = set()
    a = []

    for char in trump_speech:
        count = trump_speech.count(char)
        if char in vowels and count > 1:
            total +=1
            vcount.add(char)
            print(vcount)
    
            # print(vcount)

    #identify vowels 
    # get a total of all vowels that appear more than once 

    #each vowel has it's own count 
    # also count all the vowels in the string of the extras 


print(trump_detector("I will build a huge wall")) #, 0 vowels greater than one : 7
print(trump_detector("HUUUUUGEEEE WAAAAAALL")) #, 4 vowels greater than one : 15
print(trump_detector("MEXICAAAAAAAANS GOOOO HOOOMEEEE")) #, 2.5 vowels greater than one : 20
print(trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa")) #, 1.89 vowels greater than one : 25
print(trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT")) #, 1.56 vowels greater than one : 21