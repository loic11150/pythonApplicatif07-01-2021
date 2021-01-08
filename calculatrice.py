# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:17:41 2021
J'ai peu commenté le code car il est simple
@author: loicR
"""
import PyQt5.QtWidgets as qtw
evitchar = ["+","-","*","/",".","%"]
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setLayout(qtw.QVBoxLayout())
        self.setUI()

        self.show()

    def setUI(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # create the buttons
        btn_1 = qtw.QPushButton('1',clicked = self.onClick1)
        btn_2 = qtw.QPushButton('2',clicked = self.onClick2)
        btn_3 = qtw.QPushButton('3',clicked = self.onClick3)
        btn_4 = qtw.QPushButton('4',clicked = self.onClick4)
        btn_5 = qtw.QPushButton('5',clicked = self.onClick5)
        btn_6 = qtw.QPushButton('6',clicked = self.onClick6)
        btn_7 = qtw.QPushButton('7',clicked = self.onClick7)
        btn_8 = qtw.QPushButton('8',clicked = self.onClick8)
        btn_9 = qtw.QPushButton('9',clicked = self.onClick9)
        btn_0 = qtw.QPushButton('0',clicked = self.onClick0)
        
        btn_v = qtw.QPushButton('.',clicked = self.onClickV)
        
        btn_c = qtw.QPushButton('CLEAR',clicked = self.onClickC)
        btn_b = qtw.QPushButton('RETURN',clicked = self.onClickB)
        
        btn_p = qtw.QPushButton('+',clicked = self.onClickP)
        btn_m = qtw.QPushButton('-',clicked = self.onClickM)
        btn_d = qtw.QPushButton('/',clicked = self.onClickD)
        btn_f = qtw.QPushButton('*',clicked = self.onClickF)
        btn_mo = qtw.QPushButton('%',clicked = self.onClickMo)
        btn_sqr = qtw.QPushButton('²',clicked = self.onClickSqr)
        
        btn_e = qtw.QPushButton('=',clicked = self.onClickE)
        self.resLabel = qtw.QLabel()
        
    


        # add buttons to layout
        container.layout().addWidget(self.resLabel,0,0,1,3)
        
        
        container.layout().addWidget(btn_7,1, 0 )
        container.layout().addWidget(btn_8,1, 1 )
        container.layout().addWidget(btn_9,1, 2 )
        container.layout().addWidget(btn_p,1, 3 )

        container.layout().addWidget(btn_4,2, 0 )
        container.layout().addWidget(btn_5,2, 1 )
        container.layout().addWidget(btn_6,2, 2 )
        container.layout().addWidget(btn_m,2, 3 )

        container.layout().addWidget(btn_1,3, 0 )
        container.layout().addWidget(btn_2,3, 1 )
        container.layout().addWidget(btn_3,3, 2 )
        container.layout().addWidget(btn_d,3, 3 )

        container.layout().addWidget(btn_0,4,0 )
        container.layout().addWidget(btn_v,4,1 )
        container.layout().addWidget(btn_e,4,2 )
        container.layout().addWidget(btn_f,4,3 )
        
        container.layout().addWidget(btn_c,5,0)
        container.layout().addWidget(btn_b,5,1)  
        container.layout().addWidget(btn_mo,5,2)
        container.layout().addWidget(btn_sqr,5,3)

        self.layout().addWidget(container)
        
    #def cleanError(xxx):
     #   txt = xxx.resLabel.text()
      #  if(txt == "Error"):
       #     xxx.resLabel.setText("")
            
    
    def onClick1(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"1")
    def onClick2(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"2")
    def onClick3(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"3")
    def onClick4(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"4")
    def onClick5(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"5")
    def onClick6(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"6")
    def onClick7(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"7")
    def onClick8(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"8") 
    def onClick9(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"9")
    def onClick0(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb+"0") 
        
    def onClickC(self):
        self.resLabel.setText("")     
    def onClickB(self):
        nb = self.resLabel.text()
        self.resLabel.setText(nb[:-1])

    def onClickP(self):
        nb = self.resLabel.text()
        if (nb != "" and nb[-1] not in evitchar):#on rajoute un + que si le dernier caractère n'est pas
        #dans la liste des opérateurs
            self.resLabel.setText(nb+"+")
    def onClickM(self):
        nb = self.resLabel.text()
        if (nb != "" and nb[-1] not in evitchar):
            self.resLabel.setText(nb+"-")
    def onClickD(self):
        nb = self.resLabel.text()
        if (nb != "" and nb[-1] not in evitchar):
            self.resLabel.setText(nb+"/")
    def onClickF(self):
        nb = self.resLabel.text()
        if (nb != "" and nb[-1] not in evitchar):
            self.resLabel.setText(nb+"*")
    def onClickMo(self):
        nb= self.resLabel.text()
        if (nb != "" and nb[-1] not in evitchar):
            self.resLabel.setText(nb+"%")
    
    def onClickV(self):
        nb = self.resLabel.text()
        if (nb != "" and nb[-1] not in evitchar):
            self.resLabel.setText(nb+".")
    
    def onClickE(self):
        nb = self.resLabel.text()
        if (nb != ""  and nb[-1] not in evitchar ):
            try:
                nb = eval(nb)
                self.resLabel.setText(str(nb))
            except Exception:
               self.resLabel.setText("Error")
    def onClickSqr(self):
        nb = self.resLabel.text()
        if (nb != ""  and nb[-1] not in evitchar ):
            try:
                nb = eval(nb)
                nb = nb*nb
                self.resLabel.setText(str(nb))
            except Exception:
               self.resLabel.setText("Error")
            
                
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()