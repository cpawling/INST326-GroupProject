#MILTO TASISSA
#CHARLES PAWLING
#NIKITA PATEL
#ADAM MILLS
import random
from collections import Counter
import sys 

def roll_dice():
    '''The purpose of this function is to simulate the rolling of a dice, three times. After each roll, the user can decide which 'dice' they
        would like to roll again, and which they would like to keep.
        Returns:
            Dice_count (list): list containing the final numbers of the "dice" rolled.
    '''     
    #roll1
    dice_count = []
    for x in range(5):
        dice_count.append(random.randint (1,6))
    print ('The numbers rolled are:', dice_count)

    #roll2
    roll2 = (input('What is the position(s) of the die you would like to roll again? (Format-# # # # #) '))
    roll2 = roll2.split()
    for x, y in enumerate(roll2):
        roll2[x]=int(y) - 1 
    for x in roll2:
        dice_count[x] = random.randint(1,6)
        print ('The numbers rolled are:', dice_count)

    #roll3
    roll3 = (input('What is the position(s) of the die you would like to roll again? (Format-# # # # #) '))
    roll3 = roll3.split()
    for x, y in enumerate(roll3):
        roll3[x]=int(y) - 1 
    for x in roll3:
        dice_count[x] = random.randint(1,6)
        print ('The final numbers rolled are: ', dice_count)
    return dice_count

class Checks:
    '''Purpose: Checks to see which category dice_count fits into.
       Attributes:
            dice_count (list): The numbers rolled on the dice of the final roll, implemented as a list.'''
    def __init__(self):
        pass
    def ones(self,dice_count):
        '''Purpose: Checks to see how many 1's are in dice_count, and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''        
        onesc = 0
        for i in dice_count:
            if i == 1:
                onesc += 1
        return onesc
    def twos(self,dice_count):
        '''Purpose: Checks to see how many 2's are in dice_count, and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''
        twosc = 0
        for i in dice_count:
            if i == 2:
                twosc += 2
        return twosc
    def threes(self,dice_count):
        '''Purpose: Checks to see how many 3's are in dice_count, and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''        
        threesc = 0
        for i in dice_count:
            if i == 3:
                threesc += 3
        return threesc
    def fours(self,dice_count):
        '''Purpose: Checks to see how many 4's are in dice_count, and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.
        '''
        foursc = 0
        for i in dice_count:
            if i == 4:
                foursc += 4
        return foursc
    def fives(self,dice_count):
        '''Purpose: Checks to see how many 5's are in dice_count, and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''
        fivesc = 0
        for i in dice_count:
            if i == 5:
                fivesc += 5
        return fivesc
    def sixes(self,dice_count):
        '''Purpose: Checks to see how many 6's are in dice_count, and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''
        sixesc = 0
        for i in dice_count:
            if i == 6:
                sixesc += 6
        return sixesc
    def three_of_a_kind(self,dice_count):
        '''Purpose: Checks to see if dice_count contains atleast three rolled '3's and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.
           Source Used:
                https://medium.com/better-programming/interview-questions-write-yahtzee-in-python-72695550d84e'''
        dice_count.sort()
        if dice_count[0] == dice_count[2] or dice_count[1] == dice_count[3] or dice_count[2] == dice_count[4]:
            three_kind = sum(dice_count)
        else:
            three_kind = 0
        return three_kind
    def four_of_a_kind(self,dice_count):
        '''Purpose: Checks to see if dice_count contains atleast four rolled '4's and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.
           Source Used:
                https://medium.com/better-programming/interview-questions-write-yahtzee-in-python-72695550d84e'''
        dice_count.sort()
        if dice_count[0] == dice_count[3] or dice_count[1] == dice_count[4]:
            four_kind = sum(dice_count)
        else:
            four_kind = 0
        return four_kind
    def smallstraight(self,dice_count):
        '''Purpose: Checks to see if dice_count contains any sequence of four consecutive numbers and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''
        ss_check1 = [1, 2, 3, 4]
        ss_check2 = [2, 3, 4, 5]
        ss_check3 = [3, 4, 5, 6]
        ss = all(item in dice_count for item in ss_check1)
        ss2 = all(item in dice_count for item in ss_check2)
        ss3 = all(item in dice_count for item in ss_check3)
        if ss or ss2 or ss3  is True:
            smallstraightc = sum(dice_count)
        else:
            smallstraightc = 0
        return smallstraightc
    def largestraight(self,dice_count): 
        '''Purpose: Checks to see if dice_count contains any sequence of five consecutive numbers and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''
        dice_sorted = sorted(dice_count)
        if dice_sorted == [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6]:
            largestraightc = 40
        else:
            largestraightc = 0
        return largestraightc
    def full_house(self,dice_count):
        '''Purpose: Checks to see if dice_count contains three of the same number, as well as one pair and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.
           Source Used:
                https://www.geeksforgeeks.org/how-to-count-unique-values-inside-a-list/'''
        unique_dice = []
        num = 0
        for item in dice_count:
            if item not in unique_dice:
                num += 1
                unique_dice.append(item)
        if num == 2:
            fullhousec = 25
        else:
            fullhousec = 0
        return fullhousec
    def chance(self,dice_count):
        '''Purpose: Adds sum of numbers rolled in dice_count and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.
           Source Used:
                https://medium.com/better-programming/interview-questions-write-yahtzee-in-python-72695550d84e'''
        chances = sum(dice_count)
        return chances
    def Yahtzee (self,dice_count):
        '''Purpose: Checks to see if player rolled five of the same number in dice_count and updates points accordingly.
           Args:
                dice_count (list): A list containing what the player rolled.'''
        solo_dice = []
        num = 0
        for item in dice_count:
            if item not in solo_dice:
                num += 1
                solo_dice.append(item)
        if num == 1:
            yahtzee_score = 50
        else:
            yahtzee_score = 0
        return yahtzee_score

class Score: 
    '''Purpose: Calculates and displays various scores.'''
    def __init__(self):
        pass
    def add_upper_score(self, ones, twos, threes, fours, fives, sixes):
        '''Purpose: This function adds a rolled score to the top part of the scoreboard, which tracks ones, twos, threes, fours, fives, and sixes.
           Args:
                ones (method): Checks to see how many 1's are in dice_count, and updates points accordingly.
                twos (method): Checks to see how many 2's are in dice_count, and updates points accordingly.
                threes (method): Checks to see how many 3's are in dice_count, and updates points accordingly.
                fours (method): Checks to see how many 4's are in dice_count, and updates points accordingly.
                fives (method): Checks to see how many 5's are in dice_count, and updates points accordingly.
                sixes (method): Checks to see how many 6's are in dice_count, and updates points accordingly.'''
        upper_score = ones + twos + threes + fours + fives + sixes
        return upper_score
    def add_upper_bonus(self, upper_score): 
        '''Purpose: This function compares the top scoreboard with the points needed to earn a bonus
           Args:
                upper_score: Addition of points stored in methods one - six.  '''
        score_for_bonus = 63
        if upper_score >= score_for_bonus:
            upp_bonus = 35
        else:
            upp_bonus = 0
        return upp_bonus
    def get_upper_score(self, upper_score, upp_bonus):
        '''Purpose: This function returns the users top score and bonus if any points were earned
           Args:
                upper_score: Addition of points stored in methods one - six.
                upp_bonus:  '''
        total_upper_score = upper_score + upp_bonus
        return total_upper_score 
            
def drive_game():
    '''Purpose: Drives game calling functions from the classes. '''  
    categories = ["ones","twos","threes","fours","fives","sixes","Three-of-a-kind","Four-of-a-kind", "Full House", "Small Straight", "Large Straight", "Chance", "Yahtzee"]
    #categoriesdict = {"ones":[],"twos":[],"threes":[],"fours":[],"fives":[],"sixes":[],"Three-of-a-kind":[],"Four-of-a-kind":[], "Full House":[], "Small Straight":[], "Large Straight":[], "Chance":[], "Yahtzee":[]}
    categoriesdict = {}
    for i in range(13):
        roll1 = roll_dice()
        print(f'This is your roll {roll1}')
        print(categories)
        turn1 = input("Please pick a scoring category, this is case-sensetive to the list above; ")
        categoriesdict[turn1] = roll1
        categories.remove(turn1)
    c = Checks()
    s = Score()
    one = c.ones(categoriesdict['ones'])
    two = c.twos(categoriesdict['twos'])
    three = c.threes(categoriesdict['threes'])
    four = c.fours(categoriesdict['fours'])
    five = c.fives(categoriesdict['fives'])
    six = c.sixes(categoriesdict['sixes'])
    three_k = c.three_of_a_kind(categoriesdict['Three-of-a-kind'])
    four_k = c.four_of_a_kind(categoriesdict['Four-of-a-kind'])
    smalls = c.smallstraight(categoriesdict['Small Straight'])
    large = c.largestraight(categoriesdict['Large Straight'])
    fh = c.full_house(categoriesdict['Full House'])
    chan = c.chance(categoriesdict['Chance'])
    yahtz = c.Yahtzee(categoriesdict['Yahtzee'])
    upper = s.add_upper_score(one, two, three, four, five, six)
    bonus = s.add_upper_bonus(upper)
    total_up = s.get_upper_score(upper, bonus)
    Final_score = total_up + three_k + four_k + smalls + large + fh + chan + yahtz
    print(f'Ones: {one}')
    print(f'Twos: {two}')
    print(f'Threes: {three}')
    print(f'Fours: {four}')
    print(f'Fives: {five}')
    print(f'Sixes: {six}')
    print(f'Your Upper Bonus: {bonus}')
    print(f'Three-of-a-kind: {three_k}')
    print(f'Four-of-a-kind: {four_k}')
    print(f'Small Straight: {smalls}')
    print(f'Large Straight: {large}')
    print(f'Full House: {fh}')
    print(f'Chance: {chan}')
    print(f'Yahtzee: {yahtz}')
    print(f'Final Score: {Final_score}')
    
if __name__ == '__main__':
    drive_game()
    
