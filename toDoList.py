# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:03:49 2021

@author: loicr
"""

import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    clickedOnCreateTask = False
    labClicked = False
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My to do listl")
        self.setLayout(qtw.QVBoxLayout())
        self.setUI()

        self.show()

    def setUI(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # create the buttons
        btn_create = qtw.QPushButton('Créer une tâche',clicked = self.onClickCreateTask)
        btn_2 = qtw.QPushButton('Voir mes tâches',clicked = self.onClickSeeTasks)
        
        self.input1 = qtw.QLineEdit()
        self.btn_save = qtw.QPushButton('Enregistrer la tâche',clicked = self.onClickSave)


        # add buttons to layout
        container.layout().addWidget(btn_create,2, 0)
        container.layout().addWidget(btn_2,2, 1 )
        
        self.layout().addWidget(self.input1)
        self.layout().addWidget(self.btn_save)
        
        self.btn_save.setVisible(False)
        self.input1.setVisible(False)

        self.layout().addWidget(container)
        
        #4test
        self.btn_delete = qtw.QPushButton('Supprimer la tâche',clicked = self.onClickDelete)
        self.btn_doOrNot = qtw.QPushButton("Modifier l'état de la tâche",clicked = self.onClickDoOrNot)
        self.lab = qtw.QLabel()
        self.inputDel = qtw.QLineEdit()
        
    def onClickCreateTask(self):
        if (self.clickedOnCreateTask):
            self.input1.setText("")
            self.btn_save.setVisible(False)
            self.input1.setVisible(False)
            self.clickedOnCreateTask = False
            try :
                self.lab.setVisible(False)
            except Exception : 
                self.input1.setText("")
        else :
            self.btn_save.setVisible(True)
            self.input1.setVisible(True)
            self.clickedOnCreateTask = True
    
    def onClickSave(self):
        task = self.input1.text()
        file = open("todolist.txt", "r")
        lines = file.readlines()#lignes du ficher txt
        i = 0
        for line in lines:
            i=i+1
        
        if (task != ""):
            file = open("todolist.txt", "a")
            file.write(str(i)+" : "+task+" : Pas Fait\n")
            file.close()
            self.btn_save.setVisible(False)
            self.input1.setVisible(False)
            try:
                self.lab.clear()
                self.labClicked = False
            except Exception as e:
                print("not clear",e)
                
    def onClickSeeTasks(self):
        try :
            if (self.lab and self.labClicked == False):
                self.lab.clear()
                self.see()
            else : 
                self.lab.clear()
                self.inputDel.setVisible(False)
                self.btn_delete.setVisible(False)
                self.btn_doOrNot.setVisible(False)
                self.labClicked = False
        except Exception :
            print("test")
            self.see()
            
    def see(self):
        file = open("todolist.txt", "r")
        lines = file.readlines()#lignes du ficher txt
        i = 0
        for line in lines:
            self.lab.setText(self.lab.text()+line+"\n")
            i= i +1
        file.close()
        self.layout().addWidget(self.lab)
        self.layout().addWidget(self.btn_delete)
        self.layout().addWidget(self.inputDel)
        self.layout().addWidget(self.btn_doOrNot)
        self.lab.setVisible(True)
        self.labClicked = True
        self.inputDel.setVisible(True)
        self.btn_delete.setVisible(True)
        self.btn_doOrNot.setVisible(True)
        
    def onClickDelete(self):
        file = open("todolist.txt", "r")
        lines = file.readlines()#lignes du ficher txt
        i = 0
        newLines = ""
        for line in lines:
            xxx = line.split(":")
           # print(str(i)+" : "+xxx[0])
            if (int(xxx[0]) != int(self.inputDel.text())):
              #  print(line)
                newLines = newLines +line
            i = i + 1    
        
        file.close()
        file = open("todolist.txt", "w")
        file.write(newLines)
        file.close()
        self.lab.clear()
        self.see()
    
    def onClickDoOrNot(self):
        file = open("todolist.txt", "r")
        lines = file.readlines()#lignes du ficher txt
        i = 0
        newLines = ""
        for line in lines:
            xxx = line.split(":")
           # print(str(i)+" : "+xxx[0])
            if (int(xxx[0]) == int(self.inputDel.text())):
             #   print(line,xxx[2])
                if (xxx[2] == " Pas Fait\n"):
                    line = line.replace(" Pas Fait\n"," Fait\n")
                    
                else : 
                    line = line.replace(" Fait\n"," Pas Fait\n")
                newLines = newLines +line
            else :
                newLines = newLines +line
            i = i + 1
        file.close()
        file = open("todolist.txt", "w")
        file.write(newLines)
        file.close()
        self.lab.clear()
        self.see()
    
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()