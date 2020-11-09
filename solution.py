

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

import re

def trump_detector(trump_speech):
    """Gziven a string find the extra vowels and divide."""


    x=re.findall(r'([aeiou])(\1*)',trump_speech,re.I)
    y=[len(i[1]) for i in x]
    return round(sum(y)/len(y),2)

    # vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    # trump_speech = trump_speech.lower()
    # total = 0
    # vcount = set()

    # for char in trump_speech:
    #     count = trump_speech.count(char)
    #     if char in vowels and count > 1:
    #         total +=1
    #         vcount.add(char)
    #         l = len(vcount)
    #         final = total / l
    # print(total)
    # return final

#ISSUE IS THE EXTRAS 
#greater than one


print(trump_detector("I will build a huge wall")) #, 0 / total vowels: 8
# 0 because there are no extras 
print(trump_detector("HUUUUUGEEEE WAAAAAALL")) #, 4 / total vowels: 15
# 4 extra "U", 3 extra "E" and 5 extra "A" on 3 different vowel groups: 12/3 
print(trump_detector("MEXICAAAAAAAANS GOOOO HOOOMEEEE")) #, 2.5 / total vowels: 21 / greater than one: 
# 4 extra "U", 3 extra "E" and 5 extra "A" on 3 different vowel groups: 12/3 
print(trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa")) #, 1.89 / total vowels: 26 / greater than one: 
print(trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT")) #, 1.56 / total vowels: 24 / greater than one: 