import sys
from PySide.QtGui import *
from PySide.QtCore import *
from ui_Formatter import Ui_MainWindow

import os

HexCardData = "HexCardData.csv"
UserHome = os.path.expanduser("~")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()
        
        self.CardKey = {}
        self.CardTypes = ["Troop","Action","Artifact","Constant","Resource","Reserve"]
        
        with open(HexCardData) as f:
            for line in f:
               (cardname, uuid, cardtype) = line.split("|")
               cardname = cardname.strip()
               uuid = uuid.strip()
               cardtype = cardtype.strip().split(",")[0]
               if "Action" in cardtype:
                   cardtype = "Action"
               self.CardKey[cardname] = {"uuid":uuid, "type":cardtype}
   
    def assignWidgets(self):
        self.generateImage.clicked.connect(self.goPushed)
   
    def goPushed(self):
        self.ReadableDeck = {}
        self.DeckOrder = {"Champion":None,"Troop":[],"Action":[],"Artifact":[],"Constant":[],"Resource":[],"Reserve":[]}
        
        inReserves = False
        nextLineChamp = False
        
        for line in self.deckListEntry.toPlainText().split("\n"):
            if nextLineChamp:
                self.DeckOrder["Champion"] = line
                nextLineChamp = False
            else:
                if line.lower() == "reserves":
                    inReserves = True
                
                ourSplit = line.split(" ")
                cardname = ""
                
                for i in range(1, len(ourSplit)):
                    if "[" in ourSplit[i]:
                        break
                    cardname = "%s %s"%(cardname, ourSplit[i])
                
                cardname = cardname.strip()
                
                formattedline = "%s %s"%(ourSplit[0].strip("x"), cardname)
                
                if not inReserves:
                    if cardname in self.CardKey:
                        cardtype = self.CardKey[cardname]["type"]
                        self.DeckOrder[cardtype].append(formattedline)
                else:
                    if cardname in self.CardKey:
                        self.DeckOrder["Reserve"].append(formattedline)
                
                if "Champion:" in line:
                    self.DeckOrder["Champion"] = line.split(": ")[1]
                
                if line == "CHAMPION":
                    nextLineChamp = True
                
        decklist = "[decklist Title=TITLE]\n"
        
        for t in self.CardTypes:
            if len(self.DeckOrder[t]) > 0 and t != "Champion":
                decklist = "%s[%ss]\n"%(decklist, t)
                
                for card in self.DeckOrder[t]:
                    decklist = "%s%s\n"%(decklist, card)
                
                decklist = "%s[/%ss]\n"%(decklist, t)
        
        decklist = "%s[/decklist]\n<h4>Champion: [champ]%s[/champ]</h4>\n<hr>\n"%(decklist, self.DeckOrder["Champion"])
        
        self.deckListOutput.setText(decklist)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
