#MILTO TASISSA
#CHARLES PAWLING
#NIKITA PATEL
#ADAM MILLS

class Roll:
    def __init__(self):
        
    def numbers(self,dice_count):
        """ Nikita
        
            Check to see if player got as many of a particular number as possible.
            Get as many of the same nunber as possible 
            Function checks to see if there are at least one pair of: one, two, three, four, five, and six
            Uses Arguments
        Args:
            dice_count (list): a list containing what the player rolled.
        """
    def straight (self,dice_count):
    """Nikita
    
        Small Straight
        Check to see if player got four sequential dice.
        Ex: 1,2,3,4 or 3,4,5,6
        Points: 30’’’
        Checks to see if dice are in sequential order between 1-5
    Args:
            dice_count (list): a list containing what the player rolled.
        
        Large Straight
        Check to see if player got five sequential dice
        Ex: 1,2,3,4,5 or 2,3,4,5,6
        Points: 40’’’
        Checks to see if dice are in sequential order between 2-6
    Args:
            dice_count (list): a list containing what the player rolled.
    """

    def check_full_house(self,dice_count):
    """ CHARLES
    
        Check to see if player got three of a kind + 1 pair
        Ex: 1,1,1,6,6 or 2,2,5,5,5
        Points: 25
    Args:
            dice_count (list): a list containing what the player rolled.
    """
            dice_count.sort()
        if len(set(dice_count))) != 2:
            fullhouse = False
        elif dice_count[0] != dice_count[3] or dice_count[1] != dice_list[4]:
            fullhouse = True
            
        else:
            fullhouse = False
        if fullhouse == True:
            fullhousescore = 50

    def chance_update(self,dice_count):
    """ NIKITA 
        For when the outcome of dice doesn’t fit any other category.
        Chance is the sum of the dice.
    Args:
            dice_count (list): a list containing what the player rolled.
    """


    def Yahtzee (self,dice_count):
    """ CHARLES 
        Check to see if player got five of a kind. 
        Ex: 2,2,2,2,2 or 5,5,5,5,5
        Points: 50
    Args:
            dice_count (list): a list containing what the player rolled.
    """
        self.yahtzeepoints = 0 
        if len(set(dice_count)) == 1:
            return True
            print('Yahtzee!')
            self.yahtzeepoints += 50 
        return False 

    def keep_dice(self)
    """ MILTO
        This Function will ask the player which dice they want to keep and store in separate list 

    Return:
    list 

    """
    def  roll_dice(self, dice_count):
    """ MILTO
        This function will roll again, but based on what's left of the original roll
    Args:
            dice_count (list): a list containing what the player rolled.
    
    
        First roll, creates random value between one and six and returns list
    """
class Player: 

    def __init__(self, name):
        """ 
        This function establishes different variables, which will be used to track the player’s name and parts of the scoreboard
        
        Args:
            name (str): a str containing what the player input for their name.
        """
        self.name = name
        self.scoreboard = {}
        self.scoreboard_upperhalf = 0
        self.scoreboard_lowerhalf = 0
        self._scoreboard_lowerbonus = 0
        self.scoreboard_total = 0 
        
    def add_dice_rolled(self, rolled, value):
        """ MILTO 
        This function takes the dice rolls and adds them to the scoreboard
        Args:
            rolled (list): a list containing what the player rolled.
            value (int): the amount to be added to the scoreboard
        """
    def add_upper_score(self, value):
        """ CHARLES 
        This function adds a rolled score to the top part of the scoreboard, which tracks ones, twos, threes, fours, fives, and sixes.
        Args:
            value (int): the amount to be added to the scoreboard
        """
        self.scoreboard_upperhalf += value
    def add_upper_bonus(self): 
        """ADAM
        This function compares the top scoreboard with the values needed to earn a bonus
        """
    def get_upper_score(self):
        """ADAM
        This function sums the users top score and bonus if any points were earned
        """
    def final_scoreboard(self):
        """ADAM
        This function prints the scoreboard for the user to see
        """

def drive_game(self):
        """ EVERYONE 
        Drives game 
        """