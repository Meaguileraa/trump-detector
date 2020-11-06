

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

def trump_detector(trump_speech):

print(trump_detector("I will build a huge wall")) #, 0
print(trump_detector("HUUUUUGEEEE WAAAAAALL")) #, 4
print(trump_detector("MEXICAAAAAAAANS GOOOO HOOOMEEEE")) #, 2.5
print(trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa")) #, 1.89
print(trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT")) #, 1.56