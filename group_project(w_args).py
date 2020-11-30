#MILTO TASISSA
#CHARLES PAWLING
#NIKITA PATEL
#ADAM MILLS

class Roll:
    def __init__(self):


    def numbers(self,dice_count):
        """
            Check to see if player got as many of a particular number as possible.
            Get as many of the same nunber as possible 
            Function checks to see if there are at least one pair of: one, two, three, four, five, and six
            Uses Arguments
        Args:
            dice_count (list): a list containing what the player rolled.
        """
    def small_straight (self,dice_count):
    """
        Check to see if player got four sequential dice.
        Ex: 1,2,3,4 or 3,4,5,6
        Points: 30’’’
        Checks to see if dice are in sequential order between 1-5
    Args:
            dice_count (list): a list containing what the player rolled.
    """


    def large_straight(self,dice_count):
    """
        Check to see if player got five sequential dice
        Ex: 1,2,3,4,5 or 2,3,4,5,6
        Points: 40’’’
        Checks to see if dice are in sequential order between 2-6
    Args:
            dice_count (list): a list containing what the player rolled.
    """

    def check_full_house(self,dice_count):
    """
        Check to see if player got three of a kind + 1 pair
        Ex: 1,1,1,6,6 or 2,2,5,5,5
        Points: 25
    Args:
            dice_count (list): a list containing what the player rolled.
    """

    def chance_update(self,dice_count):
    """
        For when the outcome of dice doesn’t fit any other category.
        Chance is the sum of the dice.
    Args:
            dice_count (list): a list containing what the player rolled.
    """


    def Yahtzee (self,dice_count):
    """ 
        Check to see if player got five of a kind. 
        Ex: 2,2,2,2,2 or 5,5,5,5,5
        Points: 50
    Args:
            dice_count (list): a list containing what the player rolled.
    """


    def roll_dice(self):
    """
        First roll, creates random value between one and six and returns list
    """
    

    def keep_dice(self)
    """
        This Function will ask the player which dice they want to keep and store in separate list 

    Return:
    list 

    """
    def  reroll_dice(self, dice_count):
    """
        This function will roll again, but based on what's left of the original roll
    Args:
            dice_count (list): a list containing what the player rolled.
    """

    def get_current_dice(self):
    """This function will return the (current) dice list that was kept (the one in pay)"""


    def get_kept_dice(self):
    """This function will return the current kept dice list """


    def forced_keep(self, dice_count):
    """
    This function will just force the roll to be added to the kept dice list. This is used after your third roll
    Args:
            dice_count (list): a list containing what the player rolled.
    """"
class Player: 

    def __init__(self, name):
        """ 
        This function establishes different variables, which will be used to track the player’s name and parts of the scoreboard
        
        Args:
            name (str): a str containing what the player input for their name.
        """
    def add_dice_rolled(self, rolled, value):
        """
        This function takes the dice rolls and adds them to the scoreboard
        Args:
            rolled (list): a list containing what the player rolled.
            value (int): the amount to be added to the scoreboard
        """
    def add_upper_score(self, value):
        """
        This function adds a rolled score to the top part of the scoreboard, which tracks ones, twos, threes, fours, fives, and sixes.
        Args:
            value (int): the amount to be added to the scoreboard
        """
    def add_upper_bonus(self):
        """
        This function compares the top scoreboard with the values needed to earn a bonus
        """
    def get_upper_score(self):
        """
        This function sums the users top score and bonus if any points were earned
        """
    def final_scoreboard(self):
        """
        This function prints the scoreboard for the user to see
        """
