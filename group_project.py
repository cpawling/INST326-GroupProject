#MILTO TASISSA
#CHARLES PAWLING
#NIKITA PATEL
#ADAM MILLS
import random
from collections import Counter
#from statistics import mode 

def roll_dice():
    '''Nikita
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
    return dice_count

class Checks:
    def __init__(self):
        ''' ADD DOC '''
        #Need dice count?
        self._current_dice_list = list()
        self._current_kept_dice = list()
            
    def ones(self,dice_count):
        onesc = 0
        for i in dice_count:
            if i == 1:
                onesc += 1
    def twos(self,dice_count):
        twosc = 0
        for i in dice_count:
            if i == 2:
                twosc += 2
    def threes(self,dice_count):
        threesc = 0
        for i in dice_count:
            if i == 3:
                threesc += 3
    def fours(self,dice_count):
        fourssc = 0
        for i in dice_count:
            if i == 4:
                foursc += 4
    def fives(self,dice_count):
        fivesc = 0
        for i in dice_count:
            if i == 5:
                fivesc += 5
    def sixes(self,dice_count):
        sixesc = 0
        for i in dice_count:
            if i == 6:
                sixesc += 6
    def three_of_a_kind(self,dice_count):
        one_test = dice_count.count(1)
        two_test = dice_count.count(2)
        three_test = dice_count.count(3)
        four_test = dice_count.count(4)
        five_test = dice_count.count(5)
        six_test = dice_count.count(6)
        if one_test or two_test or three_test or four_test or five_test or six_test >= 3:
            three_kind = sum(dice_count)
        else:
            four_kind = 0
    def four_of_a_kind(self,dice_count):
        one_testing = dice_count.count(1)
        two_testing = dice_count.count(2)
        three_testing = dice_count.count(3)
        four_testing = dice_count.count(4)
        five_testing = dice_count.count(5)
        six_testing = dice_count.count(6)
        if one_testing or two_testing or three_testing or four_testing or five_testing or six_testing >= 4:
            four_kind = sum(dice_count)
        else:
            four_kind = 0
    def smallstraight(self,dice_count):
        ss_check1 = [1, 2, 3, 4]
        ss_check2 = [2, 3, 4, 5]
        ss_check3 = [3, 4, 5, 6]
        ss = all(item in dice_count for item ss_check1)
        ss2 = all(item in dice_count for item ss_check2)
        ss3 = all(item in dice_count for item ss_check3)
        if ss or ss2 or ss3  is True:
            smallstraightc = sum(dice_count)
        else:
            smallstraightc = 0
    def largestraight(self,dice_count): 
        dice_sorted = sort(dice_count)
        if dice_sorted == [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6]
            largestraightc = 40
        else:
            largestraightc = 0
    def full_house(self,dice_count):
        """ CHARLES
        
            Check to see if player got three of a kind + 1 pair
            Ex: 1,1,1,6,6 or 2,2,5,5,5
            Points: 25
        Args:
                dice_count (list): a list containing what the player rolled.
        """
        dice_count.sort()
        if len(set(dice_count))!= 2:
            print('You did not roll a full house!')
            #fullhouse = False
            #return False
        elif dice_count[0] != dice_count[3] or dice_count[1] != dice_count[4]:
            print('You rolled a full house!')
            #fullhouse = True
            #return True
        #else:
         #   fullhouse = False
        #if fullhouse == True:
           # Points += 50
    #full house --> was made for points, ommitted to make code work, will include in final draft

    def chance(self,dice_count):
         """
        NIKITA
            For when the outcome of dice doesn't fit any other category.
            Chance is the sum of the dice.
        Args:
            dice_count (list): a list containing what the player rolled.
        """
        chances = sum(dice_count)
        return chances

    def Yahtzee (self,dice_count):
        ''' CHARLES 
            Check to see if player got five of a kind. 
            Ex: 2,2,2,2,2 or 5,5,5,5,5
            Points: 50
        Args:
                dice_count (list): a list containing what the player rolled.
        '''
        if len(set(dice_count)) == 1:
            return True
            print('Yahtzee!')
            #Points += 50 
        return False 

class Player: 
    def __init__(self, name):
       
        """
        This function establishes different variables, which will be used to track the players  name and parts of the scoreboard
        Args:
            name (str): a str containing what the player input for their name.capitalize
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
            print(x,y)   
            
def drive_game():
    """ EVERYONE 
    Drives game calling functions from the classes """
    categories = ["ones","twos","threes","fours","fives","sixes","Three-of-a-kind","Four-of-a-kind", "Full House", "Small Straight", "Large Straight", "Chance", "Yahtzee"]
    categoriesdict = {"ones":[],"twos":[],"threes":[],"fours":[],"fives":[],"sixes":[],"Three-of-a-kind":[],"Four-of-a-kind":[], "Full House":[], "Small Straight":[], "Large Straight":[], "Chance":[], "Yahtzee":[]}
    for i in range(13):
        roll1 = roll_dice()
        print(f'This is your roll {roll1}')
        print(categories)
        turn1 = input("Please pick a scoring category, this is case-sensetive ")
        categoriesdict[turn1].append(roll1)
        categories.remove(turn1)

if __name__ == '__main__':
    drive_game()