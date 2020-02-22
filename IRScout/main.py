from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import copy


#from kivy.core.window import Window
#from kivy.config import Config
#ivy.config.Config.set('graphics','resizable', False)



# Global varialbes
MAX_POWER_CELLS_AUTON = 20
MAX_POWER_CELLS_CYCLE = 5
MAX_POWER_CELLS = 5

MAX_TELEOP_CYCLES = 20
DEBUG = 0

AllMatchData = []

ParamFileName = 'IRscout.txt'
FileName = ''
DefaultEventCode = ''



# Define a class to store date from a game match
class matchEntry:
    
    def __init__(self):
        global DefaultEventCode
        self.teamName = ''
        self.teamNumber = ''
        self.eventCode = DefaultEventCode
        self.matchNum = ''
        self.alliance = 'Blue'
        self.scoutName = ''
        self.initiationLine = 0
        self.powerCellLower = [ 0 ] * (MAX_TELEOP_CYCLES + 1)
        self.powerCellOuter = [ 0 ] * (MAX_TELEOP_CYCLES + 1)
        self.powerCellInner = [ 0 ] * (MAX_TELEOP_CYCLES + 1)
        self.powerCellMiss = [ 0 ] * (MAX_TELEOP_CYCLES + 1)
        self.totalCycles = [ 0 ] * (MAX_TELEOP_CYCLES + 1)
        self.controlPanelRot = 0
        self.controlPanelPos = 0
        self.endGamePark = 0
        self.endGameClimbAttempt = 0
        self.endGameClimbSuccess = 0
        self.endGameBalance = 0
        self.endGameDisabled = 0
        
    def outputEntryToString(self):
        # Write Header Seaction
        outStr = 'Team Name,' + self.teamName + '\n'
        outStr += 'Team Number,' + self.teamNumber  + '\n'
        outStr += 'Event Code,' + self.eventCode + '\n'
        outStr += 'Match Num,' + self.matchNum + '\n'
        outStr += 'Alliance,' + self.alliance + '\n'
        outStr += 'Scout Name,' + self.scoutName + '\n'
        
        # Write Cycle Section
        outStr += 'AUTON Initiation Line,' + str(self.initiationLine) + '\n'
        outStr += 'Power Cell Lower'
        for score in self.powerCellLower:
            outStr += ',' + str(score)
        outStr += '\n'
        outStr += 'Power Cell Outer'
        for score in self.powerCellOuter:
            outStr += ',' + str(score)
        outStr += '\n'
        outStr += 'Power Cell Inner'
        for score in self.powerCellInner:
            outStr += ',' + str(score)
        outStr += '\n'
        outStr += 'Power Cell Miss'
        for score in self.powerCellMiss:
            outStr += ',' + str(score)
        outStr += '\n'
        outStr += 'Cycle Completed Status'
        totalCycleIteration = 0
        for score in self.totalCycles:
            if((self.powerCellInner[totalCycleIteration] + self.powerCellLower[totalCycleIteration] + self.powerCellMiss[totalCycleIteration] + self.powerCellOuter[totalCycleIteration]) > 0):
                outStr += ',1'
            else:
                outStr += ',0'
            totalCycleIteration += 1
        outStr += '\n'
        
        # Write Control Panel and End Game Sections
        outStr += 'Control Panel Rotation,' + str(self.controlPanelRot) + '\n'
        outStr += 'Control Panel Position,' + str(self.controlPanelPos) + '\n'
        outStr += 'Game Park,' + str(self.endGamePark) + '\n'
        outStr += 'Climb Attempt,' + str(self.endGameClimbAttempt) + '\n'
        outStr += 'Climb Success,' + str(self.endGameClimbSuccess) + '\n'
        outStr += 'Balance Success,' + str(self.endGameBalance) + '\n'
        outStr += 'Robot Disabled,' + str(self.endGameDisabled) + '\n'
        
        # Footer
        outStr += '#\n'
        
        return outStr
    
    # Function to check if two match data entries are equal
    def isEqual( self, entry ):
        if( self.teamName != entry.teamName ): return 0
        if( self.teamNumber != entry.teamNumber ): return 0
        if( self.eventCode != entry.eventCode ): return 0
        if( self.matchNum != entry.matchNum ) : return 0
        if( self.alliance != entry.alliance) : return 0
        if( self.scoutName != entry.scoutName) : return 0
        if( self.initiationLine != entry.initiationLine ): return 0
        for i in range(0, MAX_TELEOP_CYCLES + 1):
            if( self.powerCellLower[ i ] != entry.powerCellLower[ i ] ): return 0
            if( self.powerCellOuter[ i ] != entry.powerCellOuter[ i ] ): return 0
            if( self.powerCellInner[ i ] != entry.powerCellInner[ i ] ): return 0
            if( self.powerCellMiss[ i ] != entry.powerCellMiss[ i ] ): return 0
            if( self.totalCycles[ i ] != entry.totalCycles[ i ] ): return 0
        if( self.controlPanelRot != entry.controlPanelRot ): return 0
        if( self.controlPanelPos != entry.controlPanelPos ): return 0
        if( self.endGamePark != entry.endGamePark ): return 0
        if( self.endGameClimbAttempt != entry.endGameClimbAttempt ): return 0
        if( self.endGameClimbSuccess != entry.endGameClimbSuccess ): return 0
        if( self.endGameBalance != entry.endGameBalance ): return 0
        if( self.endGameDisabled != entry.endGameDisabled): return 0
        return 1
    

        
# Function to save all matches in memory to file
def writeAllMatchData( ofp ):
    # Write header
    ofp.write('Number of matches,' + str(len(AllMatchData)) + '\n')

    # Write data
    for entry in AllMatchData:
        writeMatchEntry(ofp, entry)
 
        
 # Function to save a single matche to file       
def writeMatchEntry( ofp, entry ):
    # Get output string
    outStr = entry.outputEntryToString()

    if( DEBUG): print(outStr)
    ofp.write(outStr)
    

def readAllMatchData( ifp ):
    
    # Read the data
    indata = ifp.readlines()
    ifp.close()
    
    for i in range(0, len(indata)):
        indata[i] = indata[i].rstrip()    
    
    # Check if there is any data to read
    if( len(indata) <= 1 ):
        return   
    
    # Get the number of matches
    data = indata[0].split(',')
    numMatches = int(data[1])

    lineIdx = 1
    for i in range( 0, numMatches):
        entry = matchEntry()
        
        data = indata[lineIdx].split(',')
        entry.teamName = data[1]
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.teamNumber = data[1]
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.eventCode = data[1]
        lineIdx = lineIdx + 1
        
        data = indata[lineIdx].split(',')
        entry.matchNum = data[1]
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.alliance = data[1]
        lineIdx = lineIdx + 1
        
        data = indata[lineIdx].split(',')
        entry.scoutName = data[1]
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.initiationLine = int(data[1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        for i in range(0, MAX_TELEOP_CYCLES+1):
            entry.powerCellLower[i] = int(data[i+1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        for i in range(0, MAX_TELEOP_CYCLES+1):
            entry.powerCellOuter[i] = int(data[i+1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        for i in range(0, MAX_TELEOP_CYCLES+1):
            entry.powerCellInner[i] = int(data[i+1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        for i in range(0, MAX_TELEOP_CYCLES+1):
            entry.powerCellMiss[i] = int(data[i+1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        for i in range(0, MAX_TELEOP_CYCLES+1):
            entry.totalCycles[i] = int(data[i+1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.controlPanelRot = int(data[1])
        lineIdx = lineIdx + 1
        
        data = indata[lineIdx].split(',')
        entry.controlPanelPos = int(data[1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.endGamePark = int(data[1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.endGameClimbAttempt = int(data[1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.endGameClimbSuccess = int(data[1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.endGameBalance = int(data[1])
        lineIdx = lineIdx + 1

        data = indata[lineIdx].split(',')
        entry.endGameDisabled = int(data[1])
        lineIdx = lineIdx + 1
        
        
        # Skip footer
        lineIdx = lineIdx + 1
        
        # Append to match data
        AllMatchData.append(entry)
        
        # Set event code to last read event
        global DefaultEventCode
        DefaultEventCode = entry.eventCode
        
        if(DEBUG):
            print('READ DATA:')
            print(entry.outputEntryToString())
    
# Function to increase the number of power cells (limit = 5)
def increasePC( labPCwidget ):
    curVal = int(labPCwidget.text)
    labPCwidget.text = str(curVal+1)

# Function to decrease the number of power cells (limit = 0)
def decreasePC( labPCwidget ):
    curVal = int(labPCwidget.text)
    if( curVal > 0):
        labPCwidget.text = str(curVal-1)
        
# Function to set a toggle button
def setToggleButton( toggleButton, value ):
    if( value ): 
        toggleButton.state = 'down'
    else:
        toggleButton.state = 'normal'

# Function to set a toggle button
def getToggleButton( toggleButton ):
    if( toggleButton.state == 'down' ):
        return 1
    return 0

# Function to set the allanace buttong text and color
def setAllianceButton( button, value ):
    if( value == 'Blue' ):
        button.text = 'Blue'
        button.background_color = [0, 0, 1, 1]
    else:
        button.text = 'Red'
        button.background_color = [1, 0, 0, 1]
        
        
# IR Scout GUI class
class IRscoutGUI(GridLayout):

    
    def __init__(self, **kwargs):
        super(IRscoutGUI, self).__init__(**kwargs)
        
        # Fill form with blank data
        self.currentFormId = 0
        self.currentCycleId = 0
        self.currentEntry = matchEntry()
        self.fillEntryData()
        
        # File save control
        self.SaveEvent = ''
        
        # Read any existing match data
        try:
            ifp = open(FileName, 'r')
        except:
            #content = Button(text='Could load file\n' + FileName) 
            #popup = Popup(title='Error', content=content,
            #  auto_dismiss=False, size_hint=(None, None), size=(250,250))
            #content.bind(on_press=popup.dismiss)
            #popup.open()
            return

        # Read all MatchData
        readAllMatchData( ifp )     
        
        # Fill form with blank data
        if(len(AllMatchData) > 0):
            self.currentEntry = copy.deepcopy(AllMatchData[0])
        self.fillEntryData()
        
    
    
    # Function to fill the current match data
    def fillEntryData(self):
        
        #Get current entry
        entry = self.currentEntry
        
        # Fill Banner
        self.ids.labStatusBar.text = 'Current Form  ' + \
        str(self.currentFormId + 1) + ' / ' + str(len(AllMatchData)) + \
        ' Matches Saved'
        
        # Fill Header Section
        self.ids.txtTeamName.text = entry.teamName 
        self.ids.txtTeamNumber.text = entry.teamNumber
        self.ids.txtMatchNum.text = entry.matchNum
        self.ids.btnAlliance.text = entry.alliance
        self.ids.txtScoutName.text = entry.scoutName
        setAllianceButton( self.ids.btnAlliance, entry.alliance )
        
        # Fill the cycle data
        self.fillCycleData()
        
        # Fill Control Panel and End Game Section
        setToggleButton(self.ids.btnCPRot, entry.controlPanelRot)
        setToggleButton(self.ids.btnCPPos, entry.controlPanelPos)
        setToggleButton(self.ids.btnParkOnly, entry.endGamePark)
        setToggleButton(self.ids.btnClimbAtt, entry.endGameClimbAttempt)
        setToggleButton(self.ids.btnClimbSuc, entry.endGameClimbSuccess)
        setToggleButton(self.ids.btnBalance, entry.endGameBalance)
        if(entry.endGameDisabled > 0):
            setToggleButton(self.ids.btnRobotDisabled, 1)
            self.ids.btnRobotDisabled.text = "Disabled (" + str(entry.endGameDisabled) + "s)"
            self.ids.btnRobotDisabled.background_color = (1.0, 0.0, 0.0, 1.0)
        else:
            setToggleButton(self.ids.btnRobotDisabled, 0)
            self.ids.btnRobotDisabled.text = "Not Disabled"
            self.ids.btnRobotDisabled.background_color = (0.0, 1.0, 0.0, 1.0)
        
        # Reset button activities
        self.ids.btnParkOnly.disabled = False
        self.ids.btnClimbSuc.disabled = False
        self.ids.btnBalance.disabled = False
        
        # Set button activities
        if( entry.endGamePark ):
            self.cb_btnParkOnly(self.ids.btnParkOnly)
            self.ids.btnParkOnly.disabled = False
            self.ids.btnClimbSuc.disabled = True
            self.ids.btnBalance.disabled = True
            
        if( entry.endGameClimbSuccess or entry.endGameBalance ):
            self.ids.btnParkOnly.disabled = True
            self.ids.btnClimbSuc.disabled = False
            self.ids.btnBalance.disabled = False
        else:
            self.ids.btnParkOnly.disabled = False

    
    # Function to fill the current cycle data
    def fillCycleData(self):
        global MAX_POWER_CELLS, MAX_POWER_CELLS_CYCLE, MAX_POWER_CELLS_AUTON
        entry = self.currentEntry
        if (self.currentCycleId > 0):
            cycleStr = 'CYCLE #' + str(self.currentCycleId)
            self.ids.togInitLine.disabled = True
            MAX_POWER_CELLS = MAX_POWER_CELLS_CYCLE
        else:
            cycleStr = 'AUTON'
            self.ids.togInitLine.disabled = False
            setToggleButton(self.ids.togInitLine, entry.initiationLine)
            MAX_POWER_CELLS = MAX_POWER_CELLS_AUTON
        
        self.ids.labAutonCycle.text = cycleStr
        
        self.ids.labPClower.text = str(entry.powerCellLower[self.currentCycleId])
        self.ids.labPCouter.text = str(entry.powerCellOuter[self.currentCycleId])
        self.ids.labPCinner.text = str(entry.powerCellInner[self.currentCycleId])
        self.ids.labPCmiss.text  = str(entry.powerCellMiss[self.currentCycleId])
        self.checkPCbut()


    # Fucntion to get the match data
    def getEntryData(self):
        
        entry = self.currentEntry
        
        # Get Header Section
        entry.teamName = self.ids.txtTeamName.text.strip('\n')
        entry.teamNumber = self.ids.txtTeamNumber.text
        entry.matchNum = self.ids.txtMatchNum.text
        entry.alliance = self.ids.btnAlliance.text
        entry.scoutName = self.ids.txtScoutName.text
        
        # Get Cycle Section
        self.getCycleData()

        # Get Control Panel and End Game Section
        entry.controlPanelRot = getToggleButton( self.ids.btnCPRot )
        entry.controlPanelPos = getToggleButton( self.ids.btnCPPos )
        entry.endGamePark = getToggleButton( self.ids.btnParkOnly )
        entry.endGameClimbAttempt = getToggleButton( self.ids.btnClimbAtt )
        entry.endGameClimbSuccess = getToggleButton( self.ids.btnClimbSuc )
        entry.endGameBalance = getToggleButton( self.ids.btnBalance )
        
    # Fucntion to get cycle data
    def getCycleData(self):
        entry = self.currentEntry
        if (self.currentCycleId == 0):
            entry.initiationLine = getToggleButton(self.ids.togInitLine)
        
        entry.powerCellLower[self.currentCycleId] = int(self.ids.labPClower.text)
        entry.powerCellOuter[self.currentCycleId] = int(self.ids.labPCouter.text)
        entry.powerCellInner[self.currentCycleId] = int(self.ids.labPCinner.text)
        entry.powerCellMiss[self.currentCycleId]  = int(self.ids.labPCmiss.text)
        
    # Fucntion to determine if a save is needed
    def isSaveNeeded(self):
        if( self.currentFormId >= len(AllMatchData) ): return 1
        if( self.currentEntry.isEqual(AllMatchData[self.currentFormId])):
            return 0
        return 1
    
    # Pop up save is needed
    def savePopup(self):
        
        layout = GridLayout(cols = 2, padding = 20) 

        yesButton = Button(text = 'Yes') 
        noButton = Button(text = 'No')

        layout.add_widget(yesButton) 
        layout.add_widget(noButton)
                    
        popup = Popup(title='Do you want to save your updates?',
                           content=layout,
                           auto_dismiss=False,
                           size_hint=(None, None), size=(250,200))
        
        yesButton.bind( on_release = popup.dismiss )
        yesButton.bind( on_release =  self.cb_saveYesButton )
        noButton.bind( on_release = popup.dismiss )
        noButton.bind( on_release =  self.cb_saveNoButton )
        popup.open()

    # Save popup yes button actions
    def cb_saveYesButton(self, tmp ):
        # Save the database
        self.cb_btnSave()
        
        # Execute the original buttom
        if(self.SaveEvent == 'Prev'):
            self.SaveEvent = ''
            self.cb_btnPrev()
        elif(self.SaveEvent == 'Next'):
            self.SaveEvent = ''
            self.cb_btnNext()
        elif(self.SaveEvent == 'New'):
            self.SaveEvent = ''
            self.cb_btnNewEntry()
        
    # Save popup no buttone actions
    def cb_saveNoButton(self, tmp ):
        
        if(self.SaveEvent == 'Prev'):
            self.cb_btnPrev()
        elif(self.SaveEvent == 'Next'):
            self.cb_btnNext()
        elif(self.SaveEvent == 'New'):
            self.cb_btnNewEntry()

    def disabledPopup(self):
        entry = self.currentEntry

        parentLayout = GridLayout(cols = 1, padding = 20)
        layout2 = GridLayout(cols = 3, padding = 20)
        topSeconds = Button(text="Whole Match")
        noSeconds = Button(text="Not Disabled")
        if(entry.endGameDisabled > 0 and entry.endGameDisabled < 150):
            addSeconds = Button(text="+")
            removeSeconds = Button(text="-")
            setToggleButton(self.ids.btnRobotDisabled, 1)
            self.ids.btnRobotDisabled.text = "Disabled (" + str(entry.endGameDisabled) + "s)"
            self.ids.btnRobotDisabled.background_color = (1.0, 0.0, 0.0, 1.0)
        elif(entry.endGameDisabled >= 150):
            addSeconds = Button(text="+",disabled=True)
            removeSeconds = Button(text="-")
            setToggleButton(self.ids.btnRobotDisabled, 1)
            self.ids.btnRobotDisabled.text = "Disabled (" + str(entry.endGameDisabled) + "s)"
            self.ids.btnRobotDisabled.background_color = (1.0, 0.0, 0.0, 1.0)
            topSeconds.background_color= (1,0,0,1)
        else:
            addSeconds = Button(text="+")
            removeSeconds = Button(text="-",disabled=True)
            setToggleButton(self.ids.btnRobotDisabled, 0)
            self.ids.btnRobotDisabled.text = "Not Disabled" 
            self.ids.btnRobotDisabled.background_color = (0.0, 1.0, 0.0, 1.0)
            noSeconds.background_color= (0.0, 1.0, 0.0, 1.0)
        numSeconds = Label(text=str(entry.endGameDisabled)+"s")
        doneButton = Button(text="Done")
        
        layout2.add_widget(addSeconds)
        layout2.add_widget(numSeconds)
        layout2.add_widget(removeSeconds)
        layout = GridLayout(cols = 2, padding = 20) 
        layout.add_widget(topSeconds)
        layout.add_widget(noSeconds)
        parentLayout.add_widget(layout2)
        parentLayout.add_widget(layout)
        parentLayout.add_widget(doneButton)
        popup = Popup(title='Disabled Menu',
                           content=parentLayout,
                           auto_dismiss=False,
                           size_hint=(None, None), size=(500,400))
        addSeconds.bind( on_press = self.disabledSecAdd)
        addSeconds.bind( on_release = popup.dismiss)
        topSeconds.bind( on_press = self.disabledTop)
        topSeconds.bind( on_release = popup.dismiss)
        noSeconds.bind( on_press = self.disabledNot)
        noSeconds.bind( on_release = popup.dismiss)
        removeSeconds.bind( on_press = self.disabledSecSub)
        removeSeconds.bind( on_release = popup.dismiss)
        doneButton.bind( on_release = popup.dismiss )
        popup.open()
    def disabledSecAdd(self, tmp):
        entry = self.currentEntry

        entry.endGameDisabled = entry.endGameDisabled + 5
        if(entry.endGameDisabled > 150):
            entry.endGameDisabled = 150
        
        self.disabledPopup()
    def disabledSecSub(self, tmp):
        entry = self.currentEntry

        entry.endGameDisabled = entry.endGameDisabled - 5
        if(entry.endGameDisabled < 0):
            entry.endGameDisabled = 0
        self.disabledPopup()
    def disabledTop(self, tmp):
        entry = self.currentEntry

        entry.endGameDisabled = 150
        self.disabledPopup()
    def disabledNot(self, tmp):
        entry = self.currentEntry

        entry.endGameDisabled = 0
        self.disabledPopup()
    # Pop up confirm delete
    def deletePopup(self):
        layout = GridLayout(cols = 2, padding = 20) 

        yesButton = Button(text = 'Yes') 
        noButton = Button(text = 'No')

        layout.add_widget(yesButton) 
        layout.add_widget(noButton)   
                    
        popup = Popup(title='Delete this match data?',
                           content=layout,
                           auto_dismiss=False,
                           size_hint=(None, None), size=(250,200))
        
        yesButton.bind( on_release = popup.dismiss )
        yesButton.bind( on_release =  self.cb_deleteYesButton )
        noButton.bind( on_release = popup.dismiss )
        #noButton.bind( on_release =  self.cb_saveNoButton )
        popup.open()


    # Pop up confirm delete
    def savePopupConfirm(self):
        layout = GridLayout(cols = 1, padding = 20) 

        dismissButton = Button(text = 'Dismiss') 

        layout.add_widget(dismissButton) 
                    
        popup = Popup(title='File saved.',
                           content=layout,
                           auto_dismiss=False,
                           size_hint=(None, None), size=(500,400))
        
        dismissButton.bind( on_release = popup.dismiss )
        popup.open()


    # Save popup yes button actions
    def cb_deleteYesButton(self, tmp ):
        # Delete the entry if it is in the database
        if(self.currentFormId < len(AllMatchData)):
            del AllMatchData[self.currentFormId]
            
            if(self.currentFormId > 0 ):
                self.currentFormId = self.currentFormId - 1
                
            self.currentCycleId = 0
            if( len(AllMatchData) > 0):
                self.currentEntry = copy.deepcopy(AllMatchData[self.currentFormId])
            else:
                self.currentEntry = matchEntry()
        
        # Delete new entries that are not in the database
        else:
            if( self.currentFormId > 0 ):
                self.currentFormId = self.currentFormId -1
                self.currentEntry = copy.deepcopy(AllMatchData[self.currentFormId])
            else:
                self.currentEntry = matchEntry()

        self.currentCycleId = 0
        self.fillEntryData()
    def CheckNumCharacters():
        print("D")
  
    
        

    #####################
    # CALLBACK FUNCTIONS
    #####################
    # User button callback
    def cb_btnSetUser( self, btnSetUser ):
        layout = GridLayout(cols = 2, padding = 20) 

        btnStd = Button(text = 'Standard') 
        btnAdv = Button(text = 'Advanced')
        layout.add_widget(btnStd)
        layout.add_widget(btnAdv)

        popup = Popup(title='Select user type:',
                           content=layout,
                           auto_dismiss=False,
                           size_hint=(None, None), size=(250,200))
        
        btnStd.bind( on_release = popup.dismiss )
        btnStd.bind( on_release = self.cb_selectStdUser )
        btnAdv.bind( on_release = popup.dismiss )
        btnAdv.bind( on_release = self.cb_selectAdvUser )
        popup.open()
        
    # Set the GUI for a standard user
    def cb_selectStdUser(self, btnSetUser):
        self.ids.btnDelete.disabled = True
        self.ids.btnNew.disabled = True
        
    # Set the GUI for a standard user
    def cb_selectAdvUser(self, btnSetUser):
        self.ids.btnDelete.disabled = False
        self.ids.btnNew.disabled = False
    
    # Alliance button callback
    def cb_btnAlliance(self, btnAlliance):
        if( btnAlliance.text == 'Blue' ):
            btnAlliance.text = 'Red'
            btnAlliance.background_color = [1, 0, 0, 1]
        else:
            btnAlliance.text = 'Blue'
            btnAlliance.background_color = [0, 0, 1, 1]
    def checkPCbut(self):
        pcSum = int(self.ids.labPClower.text) + int(self.ids.labPCouter.text) + \
                int(self.ids.labPCinner.text) + int(self.ids.labPCmiss.text)
        if(pcSum >= MAX_POWER_CELLS):
            self.ids.butPCmissUp.disabled = True
            self.ids.butPCinnerUp.disabled = True
            self.ids.butPCouterUp.disabled = True
            self.ids.butPClowerUp.disabled = True
        else:
            self.ids.butPCmissUp.disabled = False
            self.ids.butPCinnerUp.disabled = False
            self.ids.butPCouterUp.disabled = False
            self.ids.butPClowerUp.disabled = False
        if(int(self.ids.labPClower.text) == 0):
            self.ids.butPClowerDown.disabled = True
        else:
            self.ids.butPClowerDown.disabled = False
        if(int(self.ids.labPCouter.text) == 0):
            self.ids.butPCouterDown.disabled = True
        else:
            self.ids.butPCouterDown.disabled = False
        if(int(self.ids.labPCinner.text) == 0):
            self.ids.butPCinnerDown.disabled = True
        else:
            self.ids.butPCinnerDown.disabled = False
        if(int(self.ids.labPCmiss.text) == 0):
            self.ids.butPCmissDown.disabled = True
        else:
            self.ids.butPCmissDown.disabled = False
    # Power cell up arrow callback
    def cb_btnPCup(self, labPC):
        pcSum = int(self.ids.labPClower.text) + int(self.ids.labPCouter.text) + \
                int(self.ids.labPCinner.text) + int(self.ids.labPCmiss.text)
        if( pcSum < MAX_POWER_CELLS):
            increasePC(labPC)
        self.checkPCbut()
        

    # Power cell down arrow callback
    def cb_btnPCdown(self, labPC):
        decreasePC(labPC)
        self.checkPCbut()

    def cb_btnParkOnly(self, btnParkOnly):
        if( getToggleButton( btnParkOnly ) ):
            # Turn Climb sucessful and Balance off
            setToggleButton(self.ids.btnClimbSuc, False )
            self.ids.btnClimbSuc.disabled = True
            setToggleButton(self.ids.btnBalance, False )
            self.ids.btnBalance.disabled = True
        else:  
            # Turn Climb sucessful and Balnce on
            self.ids.btnClimbSuc.disabled = False
            self.ids.btnBalance.disabled = False

    def cb_btnClimbOrBalance(self, btnClimbOrBalance):
        if( getToggleButton(self.ids.btnClimbSuc) or 
           getToggleButton(self.ids.btnBalance) ):
            # Turn Park Only off
            setToggleButton(self.ids.btnParkOnly, False )
            self.ids.btnParkOnly.disabled = True
        else:   
            self.ids.btnParkOnly.disabled = False

            
    # Move to PREVIOUS cycle
    def cb_btnCyclePrev(self):
        self.getCycleData()
        if( self.currentCycleId > 0 ):
            self.currentCycleId = self.currentCycleId - 1
        self.fillCycleData()

    # Move to NEXT cycle
    def cb_btnCycleNext(self):
        self.getCycleData()
        if( self.currentCycleId < MAX_TELEOP_CYCLES):
            self.currentCycleId = self.currentCycleId + 1
        self.fillCycleData()
    # Go to previous match
    def cb_btnPrev(self):
        if(self.currentFormId > 0):
            self.getEntryData()
            if( self.isSaveNeeded() and self.SaveEvent == ''):
                self.SaveEvent = 'Prev'
                self.savePopup()
            else:
                self.currentFormId = self.currentFormId - 1
                self.currentCycleId = 0
                self.currentEntry = copy.deepcopy(AllMatchData[self.currentFormId])
                self.fillEntryData()
                self.SaveEvent = ''

    # Go to next match
    def cb_btnNext(self):
        if(self.currentFormId < len(AllMatchData)-1):
            self.getEntryData()
            if( self.isSaveNeeded() and self.SaveEvent == ''):
                self.SaveEvent = 'Next'
                self.savePopup()
            else:
                self.currentFormId = self.currentFormId + 1
                self.currentCycleId = 0
                self.currentEntry = copy.deepcopy(AllMatchData[self.currentFormId])
                self.fillEntryData()
                self.SaveEvent = ''
    def cb_btnDisabled(self):
        self.disabledPopup()
    # Save the current database
    def cb_btnSave(self):
        # Get the input match data
        self.getEntryData()
        
        # Insert entry
        if( self.currentFormId == len(AllMatchData) ):
            AllMatchData.append(matchEntry())
            AllMatchData[-1] = copy.deepcopy(self.currentEntry)
        else:
            AllMatchData[self.currentFormId] = copy.deepcopy(self.currentEntry)
        
        # Open the output file
        try:
            ofp = open(FileName, 'w')
        except:
            content = Button(text='Could not save data to file')
            
            popup = Popup(title='Error', content=content,
              auto_dismiss=False, size_hint=(None, None), size=(250,250))
            content.bind(on_press=popup.dismiss)
            popup.open()
            
            return
        
        # Write the file
        writeAllMatchData(ofp)
        
        # CLose file
        ofp.close()
        
        # Update Header
        self.fillEntryData()
        
        # File popup
        self.savePopupConfirm()


    # Save the current database
    def cb_btnDelete(self):
        # Get the input match data
        self.deletePopup()
        
        
    # Creat a new match
    def cb_btnNewEntry(self):
        if( self.isSaveNeeded() and self.SaveEvent == '' ):
            self.SaveEvent = 'New'
            self.savePopup()
        else:
            if( self.currentFormId < len(AllMatchData)):
                self.currentFormId = len(AllMatchData)
            
                self.currentCycleId = 0
                self.currentEntry = matchEntry()
                self.fillEntryData()
                
            self.SaveEvent == ''

# IR Scout Application
class IRscoutApp(App):
    def build(self):
        # Window.size = (600,1024)   # Amazon Fire 7
        # Window.size = (800,1280)   # Amazon Fire 8
        return IRscoutGUI()


if __name__ == '__main__':
    # Set file name
    ifp = open(ParamFileName, 'r')
    indata = ifp.readlines()
    ifp.close()
    FileName = indata[0].rstrip()
    IRscoutApp().run()





















