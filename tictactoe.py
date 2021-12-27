class Player():
    """Simulates a player, and his actions through the commands of the user."""

    def __init__(self, name='', symbol='', first_move=False, winner=False):
        self.name = name
        self.symbol = symbol
        self.first_move = first_move
        self.winner = winner
    
    def make_move(self):
        """Returns the input move of the player as a numeric value stored in two variables."""

        """
        So first we take a user input of two values in string type, then split them and pass them as int,
        forward on in a while loop we check the input is between the range of the matrices, if not then ask again.
        """
        
        pX, pY = (int(value) for value in input(f"-> {self.name} make your move: ").split(","))

        while True:
            
            if (pX < 3) and (pY < 3):   
                print(f"\t-> {self.name} move registered.")
                break
            else:
                print("\t-> Your move have to be betwen 0-2,0-2.")
                pX, pY = (int(value) for value in input(f"\n-> {self.name} make your move: ").split(","))
            
        return pX, pY

    def win(self):
        self.winner = True
        return self.winner

    def set_first_move(self, fm):
        self.first_move = fm

    def set_symbol(self, sy):
        self.symbol = sy

    def get_first_move(self):
        return self.first_move
    
    def get_symbol(self):
        return self.symbol


def vertical_win(lista=None, p1=Player(), p2=Player()): 
    """
    This function checks for any vertical win on both sides.
    Return the name of the winner.
    """

    wp1, wp2, i1, i2 = 0, 0, 0, 0 
      
    while i2 < 3:

        while i1 < 3:
            
            if lista[i1][i2] == 'x':
                wp1 += 1
                i1 += 1
            elif lista[i1][i2] == 'o':
                wp2 += 1
                i1 += 1
            else:
                i1 += 1

        if wp1 == 3:
            return p1.name
        elif wp2 == 3:
            return p2.name
        else:
            wp1, wp2, i1 = 0, 0, 0
            i2 += 1

    return 'None'


def diagonal_win(lista=None, p1=Player(), p2=Player()):
    """
    This function checks for any diagonal wins on either side of the table for the both of players
    It returns the name of the winner.
    """

    dw1, dw2, dw11, dw22, i1, i2 = 0, 0, 0, 0, 0, 0

    while i1 < 3:

        if lista[i1][i2] == 'x':
            dw1 += 1
            i1 += 1
            i2 += 1
        elif lista[i1][i2] == 'o':
            dw2 += 1
            i1 += 1
            i2 += 1
        else:
            i1 += 1
            i2 += 1

    i1, i2 = 0, 2

    while i1 < 3:

        if lista[i1][i2] == 'x':
            dw11 += 1
            i1 += 1
            i2 -= 1
        elif lista[i1][i2] == 'o':
            dw22 += 1
            i1 += 1
            i2 -= 1
        else:
            i1 += 1
            i2 -= 1

    if (dw1 == 3) or (dw11 == 3):
        return p1.name
    elif (dw2 == 3) or (dw22 == 3):
        return p2.name

    return 'None'


def display_game(lista=None):
    """A simple function that displays the table when called."""
    for val in lista:
        print('\t')
        print(val)


def end_game(lista=None, p1=Player(), p2=Player()):
        """
        This function check if there has been any winner so far
        if it founds one, it will change the status of the winner attribute of the said player
        """

        # Horizontal win
        i = 0
        while i < 3:

            if lista[i].count(p1.get_symbol()) == 3:
                return p1.win()
            elif lista[i].count(p2.get_symbol()) == 3:
                return p2.win()
            else:
                i+=1
        
        # Vertical Win
        if vertical_win(lista, p1, p2) == p1.name:
            return p1.win()
        elif vertical_win(lista, p1, p2) == p2.name:
            return p2.win()

        # Diagonal Win
        if diagonal_win(lista, p1, p2) == p1.name:
            return p1.win()
        elif diagonal_win(lista, p1, p2) == p2.name:
            return p2.win()

        #Is a tie
        if (lista[0].count('_') == 0) and (lista[1].count('_') == 0) and (lista[2].count('_') == 0):
            return '-> Is a tie.'
                

class Game():
    """This simulates a Tic Tac Toe game"""

    def __init__(self, player_1=Player(), player_2=Player()):
        self.player_1 = player_1
        self.player_2 = player_2
        self.table = [["_" for c in range(3)] for r in range(3)]         

    def game(self):
        """This is where the 'game' logic is."""

        if self.player_1.get_first_move():

            """We have two while loops for each player moves, and between them we have two check points to see if there's a winner,
            and if there is then stop the game and anounce a winner if there is."""
            while True:

                i1, i2 = self.player_1.make_move()

                if self.table[i1][i2] == '_':

                    table_holder = self.table[i1]
                    table_holder[i2] = self.player_1.get_symbol()
                    print("\t-> Player " + self.player_1.name + " has made a move.")
                    display_game(self.table)
                    print('\n')
                    break
                else:
                    print("\t-> There is already a pice in that place, try again in an empty place.\n")       

            """Winner logic."""
            end_game(self.table, self.player_1, self.player_1) # Checking if theres a winner.

            if self.player_1.winner:
                message = "-> Congratulations " + self.player_1.name.title() + " you have won!"
                print(message)
                return True
            elif self.player_2.winner:
                message = "->Congratulations " + self.player_2.name.title() + " you have won!"
                print(message)
                return True
            elif end_game(self.table, self.player_1, self.player_1):
                print("-> Is a tie.")
                return True
                

            while True: # 2nd while loop for player 2, everything is the same except the chracteristics of the player.

                i1, i2 = self.player_2.make_move()

                if self.table[i1][i2] == '_':

                    table_holder = self.table[i1]
                    table_holder[i2] = self.player_2.get_symbol()
                    print("\t-> Player " + self.player_2.name + " has made a move.")
                    display_game(self.table)
                    print('\n')
                    break
                else:
                    print("\t-> There is already a pice in that place, try again in an empty place.\n")
                
            end_game(self.table, self.player_1, self.player_1)

            if self.player_1.winner:
                message = "-> Congratulations " + self.player_1.name.title() + " you have won!"
                print(message)
                return True
            elif self.player_2.winner:
                message = "->Congratulations " + self.player_2.name.title() + " you have won!"
                print(message)
                return True
            elif end_game(self.table, self.player_1, self.player_1):
                print("-> Is a tie.")
                return True

        else: # This part is the exact same as the one above, but the 2nd player have the first turn.

            while True:

                i1, i2 = self.player_2.make_move()

                if self.table[i1][i2] == '_':

                    table_holder = self.table[i1]
                    table_holder[i2] = self.player_2.get_symbol()
                    print("\t-> Player " + self.player_2.name + " has made a move.")
                    display_game(self.table)
                    print('\n')
                    break
                else:
                    print("\t-> There is already a pice in that place, try again in an empty place.\n")
                
            end_game(self.table, self.player_1, self.player_1)

            if self.player_1.winner:
                message = "-> Congratulations " + self.player_1.name.title() + " you have won!"
                print(message)
                return 1
            elif self.player_2.winner:
                message = "->Congratulations " + self.player_2.name.title() + " you have won!"
                print(message)
                return 1
            elif end_game(self.table, self.player_1, self.player_1):
                print("-> Is a tie.")
                return True

            while True:

                i1, i2 = self.player_1.make_move()

                if self.table[i1][i2] == '_':

                    table_holder = self.table[i1]
                    table_holder[i2] = self.player_1.get_symbol()
                    print("\t-> Player " + self.player_1.name + " has made a move.")
                    display_game(self.table)    
                    print('\n')  
                    break
                else:
                    print("\t-> There is already a pice in that place, try again in an empty place.\n")   
                
            end_game(self.table, self.player_1, self.player_1)

            if self.player_1.winner:
                message = "-> Congratulations " + self.player_1.name.title() + " you have won!"
                print(message)
                return 1
            elif self.player_2.winner:
                message = "->Congratulations " + self.player_2.name.title() + " you have won!"
                print(message)
                return 1
            elif end_game(self.table, self.player_1, self.player_1):
                print("-> Is a tie.")
                return True
                

def main():

    name1 = input("\n-> Enter your name: ")
    print("\t-> Nice to meet you player 1: " + name1 + "!")

    name2 = input("\n-> Enter your name: ")
    print("\n\t-> Nice to meet you player 2: " + name2 + "!")

    notice = """
    -----------------------------------------------------------------------------------------------------------------------
    -> The game plays out the following way:
        You will have to write a cordenate in the range of 0-2, for the program to know where it will place your symbol
        Example of input: row -> 1,2 <-column 
                                                    ['0,0', '0,1', '0,2']
        Game representation with indexes ->         ['1,0', '1,1', '1,2']
                                                    ['2,0', '2,1', '2,2']

        Then what will happen is that in the position '1,2' will change to an 'x' or 'o' depending wich player are you.
        Hope you like it.
    -----------------------------------------------------------------------------------------------------------------------
    """

    print(notice)

    player1 = Player(name1, "x", first_move=True)
    player2 = Player(name2, "o")

    game = Game(player1, player2)

    display_game(game.table)
    print('\n')

    while True:
        if game.game():
            break
            
            

if __name__ == '__main__':
    main()