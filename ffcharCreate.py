import json
"""

This program will track the stats of characters such as wounds, strain and credits.
It will also keep track of a characters skill points and give the option to use the
default values provided thereby when making skill checks. 

These values will be stored in a dictionary called char and the dictionary skills will
be contained within that dictionary in this format {gunnery: 1, 2} with the first 
number being the number of yellow and the second being the number of green. I will
have to make another dieNum function in ffdice.py to handle these preassigned parameters

All of these values will be stored in seperate files called, for example, koss.char.
"""

def charCreate():
    """
    Main function that sets up some variables. Could rewrite as a class.
    """
    brawn=agility=intellect=cunning=willpower=presence=0
    characterList = [brawn, agility, intellect, cunning, willpower, presence]
    
    def charAssign(characterList):
        """
        assigns values to characterList
        """
        characterList[0] = int(input('Brawn? '))
        characterList[1] = int(input('Agility? '))
        characterList[2] = int(input('Intellect? '))
        characterList[3] = int(input('Cunning? '))
        characterList[4] = int(input('Willpower? '))
        characterList[5] = int(input('Presence? '))
        
        return characterList

    charAssign(characterList)

   
    def nameAssign(char):
        """
        Assigns values to Name, Career Species.
        """
        
        for key in char:
            if type(char[key]) != (list or dict):
                if type(char[key]) == str or int:
                    print('{}?'.format(key))
                    if type(char[key]) == str:
                        char[key] = input('> ')
                    elif type(char[key]) == int:
                        char[key] = int(input('> '))
                    else:
                        pass
                else:
                    pass
   #Initializes skills dicts
    general = {'Astrogation': [characterList[2], 0], 'Athletics': [characterList[0], 0], 'Charm': [characterList[5], 0], 'Coercion': [characterList[4], 0],\
        'Computers': [characterList[2], 0], 'Cool': [characterList[5], 0], 'Coordination': [characterList[1], 0], 'Deception': [characterList[3], 0],\
        'Discipline': [characterList[4], 0], 'Leadership': [characterList[5], 0], 'Mechanics': [characterList[2], 0], 'Medicine': [characterList[2], 0],\
        'Negotiation': [characterList[5], 0], 'Perception': [characterList[3], 0], 'Piloting: Planetary': [characterList[1], 0],\
        'Piloting: Space': [characterList[2], 0], 'Resilience': [characterList[0], 0], 'Skullduggery': [characterList[3], 0], 'Stealth': [characterList[1], 0],\
        'Streetwise': [characterList[3], 0], 'Survival': [characterList[3], 0], 'Vigilance': [characterList[4], 0]}
    combat = {'Brawl': [characterList[0], 0], 'Gunnery': [characterList[1], 0], 'Melee': [characterList[0], 0], 'Ranged: Light': [characterList[1], 0],\
        'Ranged: Heavy': [characterList[1], 0]}
    knowledge = {'Knowldge: Core Worlds': [characterList[2], 0], 'Knowledge: Education': [characterList[2], 0], 'Knowledge: Lore': [characterList[2], 0],\
        'Knowledge: Outer Rim': [characterList[2], 0], 'Knowledge: Underworld': [characterList[2], 0], 'Knowledge: Xeneology': [characterList[2], 0]}
    
    def skillAssign(genearl, combat, knowledge):
        """
        Assigns values for skill ranks.
        """
        for key in general:
            print('Ranks in {}?'.format(key))
            general[key][1] = int(input('> '))
        for key in combat:
            print('Ranks in {}?'.format(key))
            combat[key][1] = int(input('> '))
        for key in knowledge:
            print('Ranks in {}?'.format(key))
            knowledge[key][1] = int(input('> '))
    
    #Calls skillAssign() function to iterate through the different skills.
    skillAssign(general, combat, knowledge)                                  
    
    #Combines the skills dicts into larger dict
    skills = {'General': general, 'Combat': combat, 'Knowledge': knowledge}
    
    #Creates a dict to contain all values
    char = {'Name': '', 'Career': '', 'Species': '', 'WoundTH': 0, 'StrainTH': 0,\
            'Skills': skills, 'Characteristics': characterList}

    #Calls name assign to get final values
    nameAssign(char)
    
    #writes the char dict to a file with the name of the character name
    f = open(char['Name'], 'w')
    json.dump(char, f)
    f.close()
    
charCreate()
