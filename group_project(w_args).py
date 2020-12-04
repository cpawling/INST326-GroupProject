#MILTO TASISSA
#CHARLES PAWLING
#NIKITA PATEL
#ADAM MILLS
import random
from collections import Counter
from statistics import mode 

class Roll:
    def __init__(self):
        #fill here        
    def roll_dice():
        '''Nikita
        Purpose:
        The purpose of this function is to simulate the rolling of a dice, three times. After each roll, the user can decide which 'dice' they
        would like to roll again, and which they would like to keep.
        Returns:
            Dice_count (list): list containing the final numbers rolled
        '''     
        #roll1
        dice_count = []
        for x in range(5):
            dice_count.append(random.randint (1,6))
        print ('The numbers rolled are:', dice_count)

        #roll2
        roll2 = (input('What is the position(s) of the die you would like to roll again?'))
        roll2 = roll2.split()
        for x, y in enumerate(roll2):
            roll2[x]=int(y) - 1 
        for x in roll2:
            dice_count[x] = random.randint(1,6)
            print ('The numbers rolled are:', dice_count)

        #roll3
        roll3 = (input('What is the position(s) of the die you would like to roll again?'))
        roll3 = roll3.split()
        for x, y in enumerate(roll3):
            roll3[x]=int(y) - 1 
        for x in roll3:
            dice_count[x] = random.randint(1,6)
            print ('The numbers rolled are:', dice_count)
                    
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
            return False
            fullhouse = False
        elif dice_count[0] != dice_count[3] or dice_count[1] != dice_list[4]:
            fullhouse = True
            return True
        else:
            fullhouse = False
        if fullhouse == True:
            Points += 50

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
        if len(set(dice_count)) == 1:
            return True
            print('Yahtzee!')
            Points += 50 
        return False 

    def keep_dice(self):
        '''Docstring''''
        keep_input = input('which dice do you want to keep (comma separated: e.g. 1,1,5)? ')
        split_input = keep_input.split(',')
        if keep_input == '':
            return self._current_dice_list
        split_input_int = [int(item) for item in split_input]
        
        for die in split_input_int:
            self._current_kept_dice.append(die)

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
        
    def add_dice_rolled(self, rolled, Points):
        """ MILTO 
        This function takes the dice rolls and adds them to the scoreboard
        Args:
            ROLLED (list): a list containing what the player rolled.
            POINTS (int): the amount to be added to the scoreboard
        """
    def add_upper_score(self, Points):
        """CHARLES 
        This function adds a rolled score to the top part of the scoreboard, which tracks ones, twos, threes, fours, fives, and sixes.
        Args:
            value (int): the amount to be added to the scoreboard"""
        self.scoreboard_upperhalf += Points
    def add_upper_bonus(self): 
        """ADAM
        This function compares the top scoreboard with the points needed to earn a bonus
        """
        score_for_bonus = 63
        if self.scoreboard_upperhalf >= score_for_bonus:
            self.scoreboard['upper bonus'] = 50
        else:
            self.scoreboard['upper bonus'] = 0
        self.upper_bonus = self.scoreboard['upper bonus']
    def get_upper_score(self):
        """ADAM
        This function returns the users top score and bonus if any points were earned
        """
        return self.scoreboard_upperhalf
    def final_scoreboard(self):
        """ADAM
        This function prints the scoreboard for the user to see
        """
        for x, y in self.scoreboard:
            print(f'{x} : {y}')
        

def drive_game(self):
        """ EVERYONE 
        Drives game calling functions from the classes"""