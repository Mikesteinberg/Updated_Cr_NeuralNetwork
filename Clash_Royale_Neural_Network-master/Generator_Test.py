from numpy.random import seed
seed(30)
from sklearn.utils import shuffle
# Importing the dataset
def Deck_Generator():
    with open('/home/mike/"Clash Royale Neural Network"/Clash_Royale_Neural_Network-master/new_match_file_ladder.txt,"r") as deck_file:
        while True:
            i = 0  
            while i < 3195150:
                for line in deck_file:
                    #Excludes the last three values and their commas.
                    line2 = line[-6:]
                    line = line[0: -7]
                    line_array = line.split(",")
                    line_array_two = line2.split(",")
                    deck_array = []
                    for num in line_array:
                        try:
                            deck_array.append(int(num))
                        except:
                            deck_array.append(float(num))
                    deck_array_tuple = tuple(deck_array)
                    winner_array = []
                    for num in line_array_two:
                        winner_array.append(int(num))
                    winner_array_tuple = tuple(winner_array)
                    i += 1
                    yield(deck_array_tuple, winner_array_tuple)
            deck_file.seek(0)
            continue
        deck_file.close()   

            
    

def Batch_Generator():
    my_deck = Deck_Generator()
    deck_batch_array = []
    win_batch_array = []
    while True:
        deck_batch_array = []
        win_batch_array = []
        for x in range (0,32):
            x = next(my_deck)
            deck_batch_array.append(x[0])
            win_batch_array.append(x[1])
        deck_batch_tuple = tuple(deck_batch_array)
        win_batch_tuple = tuple(win_batch_array)
        yield(np.array(deck_batch_tuple), np.array(win_batch_tuple))

my_deck = Deck_Generator()
print(next(my_deck))