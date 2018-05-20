from random import choice
from collections import Counter


#debugging values
#skill = {'ch': 3, 'pr': 3}
#dice = {'bo': 3, 're': 9, 'pu': 9, 'se': 9} 




def roll(skill, dice):
    """
    Main function, sets up some lists. probably should be rewritten
    to be a class with an __init__() function.
    """
    
    result = []
    # bl = blank, s = success, ds = double sucess, b = boon, sb = success and
    # boon, db = success and boon and tri = triump
    # f = failure, df = double failure, t = threat, ft = failure threat, dt =
    # double threat, des = despair
    yellow = ['bl', 's', 's', 'ds', 'ds', 'b', 'sb', 'sb', 'sb', 'db', 'db',\
            'tri']
    green = ['bl', 's', 's', 'ds', 'b', 'b', 'sb', 'db']
    blue = ['bl', 'bl', 's', 'sb', 'db', 'b']
    red = ['bl', 'f', 'f', 'df', 'df', 't', 't', 'ft', 'ft', 'dt', 'dt',\
            'des']
    purple = ['bl', 'f', 'df', 't', 't', 't', 'dt', 'ft']
    black = ['bl', 'bl', 'f', 'f', 't', 't']
    colourList = [yellow, green, blue, red, purple, black]
    
    def skillIter(result): 
        """
        Itereates through the keys int the skill dict from the 
        main module and then appends a random selection from the
        appropriate colour list.
        """
        colour = 0
        for key in skill:
            for i in range(int(skill[key])):
                result.append(choice(colourList[colour]))
            colour+=1
        return result

    def diceIter(result):
        """
        Iterates through the keys in the dice dict from the
        main module and then appends a random selection from
        it to the result dict.
        """
        
        colour = 2
        for key in dice:
            for i in range(int(dice[key])):
                result.append(choice(colourList[colour]))
            colour+=1
        return result

    result = skillIter(diceIter(result))
    
    def countResult(result, resultType):
        """
        As the combine() function moves through different keys in the
        result dictionary, countResult() uses the imported Counter()
        class to count the number of occurences of different roll 
        results.
        """
        c = Counter(result)
    
        return c[resultType]
    
    def add(result):
        """
        Adds, subtracts and combines different types of results into a hashtable

        """
        addedResult = {'combSuccess': (result['success'] + result['triumph']) -\
            (result['failure'] + result['despair'])}
        addedResult ['combBoon'] = result['boon'] - result['threat']
        addedResult ['triumph'] = result['triumph']
        addedResult ['despair'] = result['despair']
        
        return addedResult
    
    def combine(result):
        """
        Uses the countResult() function to create a hashtable of
        generated roll results.
        """
        combResult = {'success': countResult(result, 's') +\
        countResult(result, 'ds')*2 + countResult(result, 'sb')}
        combResult['boon'] = countResult(result, 'b') +\
        countResult(result, 'db')*2 + countResult(result, 'sb')
        combResult['triumph'] = countResult(result, 'tri')
        combResult['failure'] = countResult(result, 'f') +\
        countResult(result, 'df')*2 + countResult(result, 'ft')
        combResult['threat'] = countResult(result, 't') +\
        countResult(result, 'dt')*2 + countResult(result, 'ft')
        combResult['despair'] = countResult(result, 'des')
    
        return combResult
    
    result = add(combine(result))
    
    return result
        

