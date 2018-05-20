import tkinter as tk
from tkinter import ttk
from dice import roll
import json


class Main(tk.Frame, ttk.Frame):
    """
    This is the main frame of the applications. It will handle
    importing and displaying character stats by importing a file
    with json. It also handles two types of dice rollers. One
    that automatically accounts for the characters skill and 
    characteristic stats and one that is free roll.
    """
    def __init__(self, master=None):
        super().__init__(master)
        #self.c = tk.Frame(root, padding="3 3 12 12")
        #self.c.grid(

        self.pack()
        self.grid()
        self.skillW()
        self.charW()
        self.rollW()
        self.charName.focus()
        self.charName.bind('<Return>', self.getChar)
        for child in self.winfo_children(): child.grid_configure(padx=10, pady=10)
    
    def roller(self, *args):
        """
        This function takes the selections from
        the die spin boxes and the appropriate 
        character stats and creates two dicts
        that are appropriate to pass to the
        dice module
        """
        dice = {}
        skill = {}
        x = self.genBox.get(tk.ACTIVE)
        y = self.set.get()
        if y == 'General':
            print('In General')
            skill['ch'] = self.general[x][0]
            skill['pr'] = self.general[x][1]
        elif y == 'Combat':
            print('In Combat')
            skill['ch'] = self.combat[x][0]
            skill['pr'] = self.combat[x][0]
        else:
            print('In Knowledge')
            skill['ch'] = self.knowledge[x][0]
            skill['pr'] = self.knowledge[x][0]

        dice['bo'] = self.boostBox.get()
        dice['re'] = self.redBox.get()
        dice['pu'] = self.purpleBox.get()
        dice['se'] = self.setBox.get()
        print(skill)
        print(dice)
        result = roll(skill, dice)
        print(result)
        self.resultOut(result)
        
    def froller(self, *args):
        skill = {}
        dice = {}
        skill['ch'] = self.fyellowBox.get()
        skill['pr'] = self.fgreenBox.get()
        dice['bo'] = self.fboostBox.get()
        dice['re'] = self.fredBox.get()
        dice['pu'] = self.fpurpleBox.get()
        dice['se'] = self.fsetBox.get()
        print(skill)
        print(dice)
        result = roll(skill, dice)
        print(result)
        self.resultOut(result) 
    
    def getChar(self, *args):
        """
        This function loads the character file and then
        creates dicts for different uses through the 
        program
        """

        print('Inside getChar')
        name = self.charName.get()
        f = open(name, 'r')
        name = json.load(f)
        f.close()
        self.general = name['Skills']['General']
        self.combat = name['Skills']['Combat']
        self.knowledge = name['Skills']['Knowledge']
        self.nameVar.set('Name: ' + name['Name'])
        self.careerVar.set('Career: ' + name['Career'])
        self.speciesVar.set('Species: ' + name['Species'])
        self.woundVar.set('Wound Threshold: ' + (str(name['WoundTH'])))
        self.strainVar.set('Strain Threshold: ' + (str(name ['StrainTH'])))
        self.woundBox.config(from_=0, to=name['WoundTH']*2)
        self.strainBox.config(from_=0, to=name['StrainTH']*2)
        self.wdef.set('0')
        self.sdef.set('0')
        print(self.general)
        print(name)

    def skillSet(self):
        """
        This function sets the list boxes based on the
        values of the radio button selection
        """

        b = self.set.get()
        if b == 'General':
            self.boxList.set(self.genList)
        elif b == 'Combat':
            self.boxList.set(self.comList)
        else:
            self.boxList.set(self.knoList)
    
    def resultOut(self, result):
        """
        This function creates a string used by the label
        that shows results
        """
        resStr = ''
        
        if result['combSuccess'] == 1:
            resStr += '1 Success '
        elif result['combSuccess'] == -1:
            resStr += '1 Failure '
        elif result['combSuccess'] > 1:
            resStr += str(result['combSuccess']) + ' Successes '
        elif result['combSuccess'] < -1:
            resStr += str(abs(result['combSuccess'])) + ' Failures '
        
        if result['combBoon'] == 1:
            resStr += '1 Advantage '
        elif result['combBoon'] == -1:
            resStr += '1 Threat '
        elif result['combBoon'] > 1:
            resStr += str(result['combBoon']) + ' Advantages '
        elif result['combBoon'] < -1:
            resStr += str(abs(result['combBoon'])) + ' Threats '

        if result['triumph'] == 1:
            resStr += ' 1 Triumph '
        elif result['triumph'] > 1:
            resStr += str(result['triumph']) + ' Triumphs '
        
        if result['despair'] == 1:
            resStr += ' 1 Despair'
        elif result['despair'] > 1:
            resStr += str(result['despair'])

        
        if result['combSuccess'] == 0 and  result['combBoon'] == 0\
                and result['triumph'] == 0 and result['despair'] == 0:
            resStr += 'Everything canceled out'
        
        self.resVar.set(resStr)

    def skillW(self):
        """
        This function will take information from the character file and use it to automatically
        apply to rolls. If someone selects a skill from the list, plugs in the remaining dice 
        numbers it will spit out the appropriate successes and failures. It also creates the
        appropriate widgets.

        This section uses the imported roll method.
        """
        #Lists of skill names to populate list boxes
        self.genList = ['Astrogation', 'Athletics', 'Charm', 'Coercion', 'Computers', 'Cool', 'Coordination', 'Deception',\
            'Discipline', 'Leadership', 'Mechanics', 'Medicine', 'Negotiation', 'Perception', 'Piloting: Planetary',\
            'Piloting: Space', 'Resilience', 'Skullduggery', 'Stealth', 'Streetwise', 'Survival', 'Vigilance']
        self.comList = ['Brawl', 'Gunnery', 'Melee', 'Ranged: Light', 'Ranged: Heavy']
        self.knoList = ['Knowldge: Core Worlds', 'Knowledge: Education', 'Knowledge: Lore', 'Knowledge: Outer Rim',\
            'Knowledge: Underworld', 'Knowledge: Xeneology']
        
        #Setup list boxes for skills
        self.boxList = tk.StringVar(value=self.genList)
        self.genBox = tk.Listbox(listvariable=self.boxList, height=15)

        #setup Radio buttons for skill skillSet()
        self.set = tk.StringVar(value='General')
        self.r1 = ttk.Radiobutton(text='General', value='General', variable=self.set, command=self.skillSet)
        self.r2 = ttk.Radiobutton(text='Combat', value='Combat', variable=self.set, command=self.skillSet)
        self.r3 = ttk.Radiobutton(text='Knowledge', value='Knowledge', variable=self.set, command=self.skillSet)

        #Setup spin boxes for Skill roll dice
        self.boostBox = tk.Spinbox(from_=0, to=5, width=1)
        self.redBox = tk.Spinbox(from_=0, to=5, width=1)
        self.purpleBox = tk.Spinbox(from_=0, to=5, width=1)
        self.setBox = tk.Spinbox(from_=0, to=5, width=1)

        #Setup labels for dice spinboxes
        self.boostLabel = ttk.Label(text='Boost Dice')
        self.redLabel = ttk.Label(text='Red Dice')
        self.purpleLabel = ttk.Label(text='Purple Dice')
        self.setbackLabel = ttk.Label(text='Setback Dice')

        #Setup labels for skill listboxes
        self.genLabel = ttk.Label(textvariable=self.set)

        #Setup roll button for skill roll
        self.skillRoll = ttk.Button(text='Skill Roll', command=self.roller)

        #Setup label for result
        self.resVar = tk.StringVar(value='Results: ')
        self.resLabel = ttk.Label(textvariable=self.resVar)

        #Grid for skill listboxes
        self.genBox.grid(column=1, row=4, rowspan=9, columnspan=3)

        #Grid for skillSet() radiobuttons
        self.r1.grid(column=1, row=2)
        self.r2.grid(column=2, row=2)
        self.r3.grid(column=3, row=2)
       
        #Grid for Skill listboxes Labels
        self.genLabel.grid(column=2, row=3)

        #Grid for Dice spinbox Labels
        self.boostLabel.grid(column=4, row=3)
        self.redLabel.grid(column=4, row=5)
        self.purpleLabel.grid(column=4, row=7)
        self.setbackLabel.grid(column=4, row=9)

        #Grid for dice spinboxes
        self.boostBox.grid(column=4, row=4)
        self.redBox.grid(column=4, row=6)
        self.purpleBox.grid(column=4, row=8)
        self.setBox.grid(column=4, row=10)

        #Grid for Roll Button
        self.skillRoll.grid(column=4, row=12, rowspan=3)

        #grid for result label
        self.resLabel.grid(column=1, row=15, columnspan=3)

    #Group of widgets that handle the character entry and stat display
    def charW(self):
        #Entry widget for entering the character's name.
        self.charName = ttk.Entry(width=15)
        self.charBut = ttk.Button(text='Get Character', command=self.getChar)

        #Grid for the char Entry Bar
        self.charName.grid(column=2, row=1)
        self.charBut.grid(column=3, row=1)

        #Labels for displaying character stats
        self.nameVar=self.careerVar=self.speciesVar=\
            self.wouldVar=self.strainVar=''
        self.nameVar = tk.StringVar(value='Name: ')
        self.careerVar = tk.StringVar(value='Career: ')
        self.speciesVar = tk.StringVar(value='Species: ')
        self.woundVar = tk.StringVar(value='Wound Threshold: ')
        self.strainVar = tk.StringVar(value='Strain Threshhold: ')
        name = ttk.Label(textvariable=self.nameVar)
        career = ttk.Label(textvariable=self.careerVar)
        species = ttk.Label(textvariable=self.speciesVar)
        wounds = ttk.Label(textvariable=self.woundVar)
        strain = ttk.Label(textvariable=self.strainVar)
        
        #Spinboxes for wounds and strain
        self.wdef=self.sdef=0
        self.wdef = tk.StringVar(value=0)
        self.sdef = tk.StringVar(value=0)
        self.woundBox = tk.Spinbox(from_=0, to=0, width=3,\
            textvariable=self.wdef)
        self.strainBox = tk.Spinbox(from_=0, to=0, width=3,\
            textvariable= self.sdef)
        
        #Grid for Chracter stat labels
        name.grid(column=5, row=3)
        career.grid(column=5, row=4)
        species.grid(column=5, row=5)
        wounds.grid(column=5, row=6)
        strain.grid(column=5, row=7)
        
        #Grid for wound/strain spinboxes
        self.woundBox.grid(column=5, row=8)
        self.strainBox.grid(column=5, row=9)

        
    def rollW(self):
        """
        Group of widgets that will handle the "free roll" aspect that
        ignores character stats
        """
        
        #Setup spinboxes for freeroll dice
        self.fyellowBox = tk.Spinbox(from_=0, to=5, width=1)
        self.fgreenBox = tk.Spinbox(from_=0, to=5, width=1)
        self.fboostBox = tk.Spinbox(from_=0, to=5, width=1)
        self.fredBox = tk.Spinbox(from_=0, to=5, width=1)
        self.fpurpleBox = tk.Spinbox(from_=0, to=5, width=1)
        self.fsetBox = tk.Spinbox(from_=0, to=5, width=1)
        
        #Setup labels for freeroll dice
        self.fyellowLabel = ttk.Label(text='Yellow Dice')
        self.fgreenLabel = ttk.Label(text='Green Dice')
        self.fboostLabel = ttk.Label(text='Boost Dice')
        self.fredLabel = ttk.Label(text='Red Dice')
        self.fpurpleLabel = ttk.Label(text='Purple Dice')
        self.fsetbackLabel = ttk.Label(text='Setback Dice')
        
        #Setup roll button for skill roll
        self.freeRoll = ttk.Button(text='Free Roll', command=self.froller)
        
        #Grid for spinboxes for freeroll grid
        self.fyellowBox.grid(column=6, row=4)
        self.fgreenBox.grid(column=6, row=6)
        self.fboostBox.grid(column=6, row=8)
        self.fredBox.grid(column=6, row=10)
        self.fpurpleBox.grid(column=6, row=12)
        self.fsetBox.grid(column=6, row=14)
        
        #Grid for labels for freeroll dice
        self.fyellowLabel.grid(column=6, row=3)
        self.fgreenLabel.grid(column=6, row=5)
        self.fboostLabel.grid(column=6, row=7)
        self.fredLabel.grid(column=6, row=9)
        self.fpurpleLabel.grid(column=6, row=11)
        self.fsetbackLabel.grid(column=6, row=13)
        
        #Grid for Roll Button
        self.freeRoll.grid(column=6, row=16, rowspan=3)
        
        
        
        

root = tk.Tk()
c = Main(master=root)
c.mainloop()
