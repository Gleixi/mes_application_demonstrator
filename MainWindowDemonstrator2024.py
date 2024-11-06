from typing import Self
import requests
# from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
import base64
import json
import time
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QStatusBar, QApplication,QMainWindow, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import logging 



               

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        sVersion = '3.01 Build 14.10.2024'
        sCurrDir = os.getcwd()
        print(sCurrDir)
        print("Start Version: " + sVersion)
        self.do_config()
        logger.debug("Start Version: " + sVersion)
        # 
        self.timer = QTimer()
        self.counter = 1
        self.timer.timeout.connect(self.update_counter)


        self.row_text_col0 = str
        self.row_text_col1 = str
        self.row_text_col2 = str
        self.row_text_col3 = str
        self.row_text_col4 = str
        self.row_text_col5 = str
        self.row_text_col6 = str
        self.row_text_col7 = str
        self.row_text_col8 = str
        self.row_text_col9 = str
        self.row_text_col10 = str
        
        self.sSelectedTool = str
        self.nWkzgCounter = 1
        self.nWWkzgActual = 1
        #
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1127, 888)
        MainWindow.resize(1000, 750)
        icon = QtGui.QIcon.fromTheme("OperatorGuidance")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        
        """
        # Erstelle eine Statusleiste
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        
        
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("background-color: red;")      
        
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Jep")
        self.statusbar.setVisible(True)

        """
       


        iposX = 20
        iposY = 40
        # Flag zum steuern das Eingabefeldes 
        self.sControlFlag =""

        self.lHelpText = QtWidgets.QLabel(self.centralwidget)
        self.lHelpText.setEnabled(True)
        self.lHelpText.setGeometry(QtCore.QRect(250, 0+iposY, 621, 91))
        self.lHelpText.setFont(font)
        self.lHelpText.setStyleSheet("background-color: rgb(208, 203, 199);")
        self.lHelpText.setObjectName("lHelpText")

        self.eInputMain = QtWidgets.QLineEdit(self.centralwidget)
        self.eInputMain.setGeometry(QtCore.QRect(250, 91+iposY, 621, 71))
        self.eInputMain.setObjectName("eInputMain")
        self.eInputMain.setFont(font)
        self.eInputMain.setInputMethodHints(QtCore.Qt.ImhNone)
        self.eInputMain.editingFinished.connect(self.editFinished)
              

        self.lResultText = QtWidgets.QLabel(self.centralwidget)
        self.lResultText.setEnabled(True)
        self.lResultText.setGeometry(QtCore.QRect(250, 162+iposY, 621, 110))

        self.lCurrentOrder = QtWidgets.QLabel(self.centralwidget)
        self.lCurrentOrder.setEnabled(True)
        self.lCurrentOrder.setGeometry(QtCore.QRect(250, 462+iposY, 621, 110))
        self.lCurrentOrder.setStyleSheet("background-color: rgb(208, 203, 199);")
        self.lCurrentOrder.setFont(font)
        self.lCurrentOrder.setText( "Aktuell kein laufender Auftrag auf der Maschine!")


        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        """
        self.lAA2 = QtWidgets.QLabel(self.centralwidget)
        self.lAA2.setGeometry(QtCore.QRect(360+iposX, 110+iposY, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lAA2.setFont(font)
        self.lAA2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lAA2.setAlignment(QtCore.Qt.AlignCenter)
        self.lAA2.setText("")
        self.lAA2.setObjectName("lAA2")
         
        self.lAAS = QtWidgets.QLabel(self.centralwidget)
        self.lAAS.setGeometry(QtCore.QRect(763+iposX, 110+iposY, 51, 21))
        self.lAAS.setFont(font)
        self.lAAS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lAAS.setObjectName("lAAS")
        self.lAAS.setText("UP150")
        """

       

       
        """
        self.lPicArena = QtWidgets.QLabel(self.centralwidget)
        self.lPicArena.setGeometry(QtCore.QRect(50, 700, 500, 50)) #-20
        self.lPicArena.setText("")
        self.lPicArena.setPixmap(QtGui.QPixmap(sCurrDir +"\picture\Logo_VWS4LS_AAS.png"))
        self.lPicArena.setAlignment(QtCore.Qt.AlignCenter)
        self.lPicArena.setObjectName("lPicArena")
        """
        #self.lPicAAS2 = QtWidgets.QLabel(self.centralwidget)
        #self.lPicAAS2.setGeometry(QtCore.QRect(500+iposX ,350+iposY, 571, 201)) #-20
        #self.lPicAAS2.setText("")
        #self.lPicAAS2.setPixmap(QtGui.QPixmap(sCurrDir +"\picture\AAS.jpg"))
        #self.lPicAAS2.setAlignment(QtCore.Qt.AlignCenter)
        #self.lPicAAS2.setObjectName("lPicAAS2")
        
        #self.lPicAAS3 = QtWidgets.QLabel(self.centralwidget)
        #self.lPicAAS3.setGeometry(QtCore.QRect(45+iposX, 225+iposY, 571, 201)) #-20
        #self.lPicAAS3.setText("")
        #self.lPicAAS3.setPixmap(QtGui.QPixmap(sCurrDir + self.config.sProduktPicture1))
        #self.lPicAAS3.setAlignment(QtCore.Qt.AlignCenter)
        #self.lPicAAS3.setObjectName("lPicAAS3")
        
        #self.lPicAAS4 = QtWidgets.QLabel(self.centralwidget)
        #self.lPicAAS4.setGeometry(QtCore.QRect(500+iposX, 235+iposY, 571, 201)) #-20
        #self.lPicAAS4.setText("")
        #self.lPicAAS4.setPixmap(QtGui.QPixmap(sCurrDir + self.config.sMaschinePicture1 ))
        #self.lPicAAS4.setAlignment(QtCore.Qt.AlignCenter)
        #self.lPicAAS4.setObjectName("lPicAAS4")
        #        
        #self.lPicAAS5 = QtWidgets.QLabel(self.centralwidget)
        #self.lPicAAS5.setGeometry(QtCore.QRect(15+iposX, 270+iposY, 571, 201)) #-20
        #self.lPicAAS5.setText("")
        #self.lPicAAS5.setPixmap(QtGui.QPixmap(sCurrDir +self.config.sProduktPicture2))
        #self.lPicAAS5.setAlignment(QtCore.Qt.AlignCenter)
        #self.lPicAAS5.setObjectName("lPicAAS5")
         
        

        self.pushButtonStartProdukt1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartProdukt1.setGeometry(QtCore.QRect(30, 40, 151, 71))
        self.pushButtonStartProdukt1.setObjectName("pushButton")
        self.pushButtonStartProdukt1.setFocus()

        self.pushButtonStartProdukt2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartProdukt2.setGeometry(QtCore.QRect(30, 140, 151, 71))
        self.pushButtonStartProdukt2.setObjectName("pushButton")
        self.pushButtonStartProdukt2.setFocus()
        
        self.pushButtonStartProdukt3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartProdukt3.setGeometry(QtCore.QRect(30, 240, 151, 71))
        self.pushButtonStartProdukt3.setObjectName("pushButton")
        self.pushButtonStartProdukt3.setFocus()
        

        self.pushButtonMachinenCommunication = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMachinenCommunication.setGeometry(QtCore.QRect(30, 340, 151, 71))
        self.pushButtonMachinenCommunication.setObjectName("pushButton")
        self.pushButtonMachinenCommunication.setHidden(True)

        self.pushButtonReset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReset.setGeometry(QtCore.QRect(30, 440, 151, 71))
        self.pushButtonReset.setObjectName("pushButton")

        
               
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lResultText.setFont(font)
        self.lResultText.setAutoFillBackground(False)
        self.lResultText.setStyleSheet("background-color: rgb(208, 203, 199);")
        self.lResultText.setText("")
        self.lResultText.setObjectName("lResultText")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21)) #1127
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
       # self.statusbar.setStyleSheet("background-color:  rgb(208, 203, 199);")
        MainWindow.setStatusBar(self.statusbar)

         # Erstelle ein QLabel und lade ein Bild
        self.imageLabel = QLabel()
        pixmap = QPixmap("Statusbar.png")  # Pfad zum Bild anpassen
        self.imageLabel.setPixmap(pixmap)
         # Verkleinere das Bild
        scaledPixmap = pixmap.scaled(300, 75)  # Neue Größe anpassen (Breite, Höhe)
        self.imageLabel.setPixmap(scaledPixmap)

        # Füge das QLabel zur Statusleiste hinzu
        
        self.statusbar.addPermanentWidget(self.imageLabel)
        

        


        self.tableWidget_Machine = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Machine.setGeometry(QtCore.QRect(250, 320, 621, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.tableWidget_Machine.sizePolicy().hasHeightForWidth())
        self.tableWidget_Machine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_Machine.setFont(font)
        self.tableWidget_Machine.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_Machine.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_Machine.setAutoScroll(True)
        self.tableWidget_Machine.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Machine.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_Machine.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_Machine.setShowGrid(True)
        self.tableWidget_Machine.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_Machine.horizontalHeader().setVisible(True)
        self.tableWidget_Machine.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Machine.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_Machine.setObjectName("tableWidget_Machine")
        self.tableWidget_Machine.setColumnWidth(0, 180)
        self.tableWidget_Machine.setColumnWidth(2, 90)
        self.tableWidget_Machine.setColumnWidth(4, 90)
        self.tableWidget_Machine.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: lightblue; }")
        # Table Dimension festlegen:
        self.tableWidget_Machine.setRowCount(5)
        self.tableWidget_Machine.setColumnCount(11)
        headers = ["Maschine", "Werkzeug 1", "Counter1", "Werkzeug 2" , "Counter 2", "Werkzeug 3" , "Counter 3", "Werkzeug 4" , "Counter 4", "Werkzeug 5" , "Counter 5"]
        self.tableWidget_Machine.setHorizontalHeaderLabels(headers)

        item = QtWidgets.QTableWidgetItem()
        row = 0
        while row < 5:
            col = 0
            while col < 11:
                self.tableWidget_Machine.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText("")
                col = col + 1
            row = row + 1
        ##############################################        
        self.tableWidget_Machine.verticalHeader().setDefaultSectionSize(28)

       
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 560, 431, 225))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        i=0
        while i <= 7:
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            i= i+1
        i=0
        while i <= 7:
            self.tableWidget.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            i= i+1

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(28)

        
        
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget2.setGeometry(QtCore.QRect(575, 560, 431, 225))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget2.setFont(font)
        self.tableWidget2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget2.setAutoScroll(True)
        self.tableWidget2.setRowCount(7)
        self.tableWidget2.setColumnCount(2)
        self.tableWidget2.setObjectName("tableWidget2")
        item = QtWidgets.QTableWidgetItem()
        i=0
        while i <= 6:
            self.tableWidget2.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            i= i+1
        i=0
        while i <= 6:
            self.tableWidget2.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            i= i+1

        self.tableWidget2.horizontalHeader().setVisible(False)
        self.tableWidget2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget2.verticalHeader().setDefaultSectionSize(28)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButtonStartProdukt1.clicked.connect(lambda:self.pressStartButton(self.config.sProdukt1))
        self.pushButtonStartProdukt2.clicked.connect(lambda:self.pressStartButton(self.config.sProdukt2))
        self.pushButtonStartProdukt3.clicked.connect(lambda:self.pressStartButton(self.config.sProdukt3))
        self.pushButtonMachinenCommunication.clicked.connect(self.wait4MaschineResult)
        self.pushButtonReset.clicked.connect(self.pressResetButton)
        self.tableWidget_Machine.itemClicked.connect(lambda:self.clickedMachineTable())
        
        # Aufräumer nach eventuellen Maschinenabsturz
        #self.updateMachineProcessEnd("false")
        self.tableWidget.setHidden(True)
        self.tableWidget2.setHidden(True)
                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MES Demonstrator"))
        self.lHelpText.setText(_translate("MainWindow", "Produkt auswählen"))
        self.lResultText.setText(_translate("MainWindow" , ""))
        self.pushButtonStartProdukt1 .setText(_translate("MainWindow", self.config.sProdukt1))
        self.pushButtonStartProdukt2 .setText(_translate("MainWindow", self.config.sProdukt2))
        self.pushButtonStartProdukt3 .setText(_translate("MainWindow", self.config.sProdukt3))
        self.pushButtonMachinenCommunication.setText(_translate("MainWindow", ""))
        self.pushButtonReset.setText(_translate("MainWindow", "Reset"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Job Number"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Quantity to Produced")) 
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Product Number"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Wire Number"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Wire Batch"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "Terminal Number"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "Terminal Batch"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "Product Batch"))
        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        #machine table:
        __sortingEnabled = self.tableWidget2.isSortingEnabled()
        self.tableWidget2.setSortingEnabled(False)
        item = self.tableWidget2.item(0, 0)
        item.setText(_translate("MainWindow", "Machine Number"))
        item = self.tableWidget2.item(1, 0)
        item.setText(_translate("MainWindow", "Status")) 
        item = self.tableWidget2.item(2, 0)
        item.setText(_translate("MainWindow", "Released"))
        
        item = self.tableWidget2.item(3, 0)
        item.setText(_translate("MainWindow", "Counter OK"))
        item = self.tableWidget2.item(4, 0)
        item.setText(_translate("MainWindow", "Counter NOK"))
        item = self.tableWidget2.item(5, 0)
        item.setText(_translate("MainWindow", "Start Production"))
        item = self.tableWidget2.item(6, 0)
        item.setText(_translate("MainWindow", "End Production"))
        self.tableWidget2.setSortingEnabled(__sortingEnabled)
          
        
          
   
    
    def start_timer(self):
        self.timer.start(2000)  # Timer goes off every 2 seconds
           
    def stop_timer(self):
        self.timer.stop()
        self.counter = 1
       

    def update_counter(self):
       if self.counter == 1:
        self.lResultText.setText("")
       if self.counter == 2: 
        self.lHelpText.setText("Order wird angelegt...")
       return
        
    def getMESInfoStatus(self):
        value = "$value"
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_status + value
        response = requests.get(api_url, auth=self.url.auth)
        if response.status_code > 400:
            print(f"Fehler bei getMESInfoStatus: {response.status_code}")
            sStatus = ''
            return False
        sStatus = response.json()
        return sStatus
    
    def getMESInfoMaterialID(self, type : str):
        value = "$value"
        if type == "W":
            api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_material1 + value
        else:
            api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_material2 + value
        response = requests.get(api_url, auth=self.url.auth)
        if response.status_code > 400:
            print(f"Fehler bei getMESInfoStatus: {response.status_code}")
            sMaterialID = ''
            return False
        sMaterialID = response.json()
        return sMaterialID
    
    def UpdateMESInfoStatus(self, value_patch : str):
        value = "$value"
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_status + value
        # für upates use patch
        response = requests.patch(api_url,json = value_patch, auth=self.url.auth)
        if response.status_code > 400:
            print(f"Fehler beim patch! Statuscode STARTED: {response.status_code}")
            return False
       
        if self.AAS_ProductInstance.MatNoFinishedProduct == self.config.sProdukt1:
            value_patch  = self.config.sAASProduct1
            
        if self.AAS_ProductInstance.MatNoFinishedProduct == self.config.sProdukt2:
            value_patch = self.config.sAASProduct2
            
        if self.AAS_ProductInstance.MatNoFinishedProduct == self.config.sProdukt3:
            value_patch = self.config.sAASProduct3
            

        api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_product_ID + value
        response = requests.patch(api_url,json = value_patch, auth=self.url.auth)
        if response.status_code > 400:
            print(f"Fehler beim patch! Product_ID: {response.status_code}")
            return False    
        
        return True    
    def open_message_dialog(self, s : str):
        
        Dialog = QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(713, 248)
        Dialog.setWindowTitle("Hinweis!")
        Dialog.setModal(True)
        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        label = QtWidgets.QLabel(Dialog)
        label.setGeometry(QtCore.QRect(90, 70, 491, 41))
        label.setObjectName("label")
        label.setFont(font)
        label.setText( s)

        if s == "Warte auf Rückmeldung von der Maschine...":
            close_timer = QTimer(Dialog)
            close_timer.timeout.connect(Dialog.close)
            close_timer.start(1000)

        Dialog.exec_()
    
    def getMachineFromAASMESInfo(self,url_machine : str):
        value = "$value"
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + url_machine + value
        response = requests.get(api_url, auth=self.url.auth)
        if response.status_code > 400:
            #print(f"Fehler bei getMachineFromAASMESInf: {response.status_code}")
            return ""
        return response.json()
    
    def getProductionOrder_ID(self):
        value = "$value"
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_ProductionOrder_ID + value
        response = requests.get(api_url, auth=self.url.auth)
        if response.status_code > 400:
            #print(f"Fehler bei getMachineFromAASMESInf: {response.status_code}")
            return ""
        return response.json()
    
     
    def getToolsFromAASMESInfo(self, url_tools : str):
        value = "$value"
        
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + url_tools + value
        response = requests.get(api_url, auth=self.url.auth)
        if response.status_code > 400:
            #print(f"Fehler bei getToolsFromAASMESInf: {response.status_code}")
            return ""
        return response.json()
    
    def getCounterFromAASMESInfo(self, url_counters : str):
        value = "$value"
        
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + url_counters + value
        
        response = requests.get(api_url, auth=self.url.auth)
        if response.status_code > 400:
            #print(f"Fehler bei getCounterFromAASMESInf: {response.status_code}")
            return ""
                
        return response.json()
        
    def getToolName(self, id : str):
        # KOMAX TOOLS    
        if id == "http://arena2036.de/vws4ls/aas/5bc3eb68-870f-4719-8234-ed51810321bc" :
            name = "TE_App_I3"
            return name    
        if id == "http://arena2036.de/vws4ls/aas/b6d0fc62-b4c9-4b2a-9ce1-b2ced123f482" :
            name = "TE_App_I4"
            return name  
        if id == "http://arena2036.de/vws4ls/aas/b72ee287-1644-4751-8844-3ca917411bd9" :
            name = "TE_App_I5"
            return name  
        if id == "http://arena2036.de/vws4ls/aas/f574e9eb-e6cf-45e0-a76c-5d5785255312" :
            name = "TE_App_I6"
            return name  
        if id == "http://arena2036.de/vws4ls/aas/e79657f0-08da-4f61-8bba-68e34e3e3c36" :
            name = "TE_App_I2"
            return name  
        if id == "http://arena2036.de/vws4ls/aas/f8804ede-005a-4266-8650-fe4ae2c110a7" :
            name = "TE_App_I1"
            return  name     
        # WEZAG TOOLS
        if id == "https://example.com/ids/aas/5040_1161_8042_5361" :
            name = "W_50s_I1"
            return name  
        if id == "https://example.com/ids/aas/7053_1161_8042_5856" :
            name = "W_50_I1"
            return name  
        if id == "https://example.com/ids/sm/3404_0110_2042_7933" :
            name = "W_35_I1"
            return name  
        return ""  
    
    def getMachineName(self, id : str):
        # KOMAX Machines
        if id == "http://smart.komaxgroup.com/aas/03bb64b3-2563-4f22-a475-b3732bad1e16" :
            name = "K_ALPHA_550_I1" 
            return name
        if  id == "http://smart.komaxgroup.com/aas/6462aa9f-40d9-4385-a51c-175bce470600"  :
            name = "K_ALPHA_550_I2"   
            return name
        if  id == "http://smart.komaxgroup.com/aas/dd619733-cab3-4b75-aee7-dfff4d81c82e" :
            name = "K_ALPHA_550_I3" 
            return name

        #WEZAG machines
        if  id == "https://finaldemo.vws4ls.com/ids/sm/2321_8080_2042_7808" :
            name = "W_UP150_I1" 
            return name
        if  id == "https://finaldemo.vws4ls.com/ids/sm/2321_8080_2042_7809" :
            name = "W_UP150" 
            return name
        
        return "" 
    
    def fillMachinetable(self):
        
        self.AAS_MES_Info.Machine_ID = str(self.getMachineFromAASMESInfo(self.url.sm_value_Machine_ID1))
        if self.AAS_MES_Info.Machine_ID != "":
            sMachineName = self.getMachineName(self.AAS_MES_Info.Machine_ID)
            item = self.tableWidget_Machine.item(0, 0)
            item.setText(sMachineName)

            sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID1_Machine1))
            sToolName = self.getToolName(sToolID)
            item = self.tableWidget_Machine.item(0, 1)
            item.setText( sToolName)

            sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID2_Machine1))
            sToolName = self.getToolName(sToolID)
            item = self.tableWidget_Machine.item(0, 3)
            item.setText( sToolName)

            sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID3_Machine1))
            sToolName = self.getToolName(sToolID)
            item = self.tableWidget_Machine.item(0, 5)
            item.setText( sToolName)

            sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID4_Machine1))
            sToolName = self.getToolName(sToolID)
            item = self.tableWidget_Machine.item(0, 7)
            item.setText( sToolName)

            sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID5_Machine1))
            sToolName = self.getToolName(sToolID)
            item = self.tableWidget_Machine.item(0, 9)
            item.setText( sToolName)
            
            sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID1_Machine1))
            
            item = self.tableWidget_Machine.item(0, 2)
            item.setText( sCounter)

            sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID2_Machine1))
            
            item = self.tableWidget_Machine.item(0, 4)
            item.setText( sCounter)
            
            sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID3_Machine1))
            item = self.tableWidget_Machine.item(0, 6)
            item.setText( sCounter)

            sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID4_Machine1))
            item = self.tableWidget_Machine.item(0, 8)
            item.setText( sCounter)

            sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID5_Machine1))
            item = self.tableWidget_Machine.item(0, 10)
            item.setText( sCounter)
            
            self.AAS_MES_Info.Machine_ID = str(self.getMachineFromAASMESInfo(self.url.sm_value_Machine_ID2))
            if self.AAS_MES_Info.Machine_ID != "":
                sMachineName = self.getMachineName(self.AAS_MES_Info.Machine_ID)
                item = self.tableWidget_Machine.item(1, 0)
                item.setText(sMachineName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID1_Machine2))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(1, 1)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID2_Machine2))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(1, 3)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID3_Machine2))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(1, 5)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID4_Machine2))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(1, 7)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID5_Machine2))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(1, 9)
                item.setText( sToolName)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID1_Machine2))
                item = self.tableWidget_Machine.item(1, 2)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID2_Machine2))
                item = self.tableWidget_Machine.item(1, 4)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID3_Machine2))
                item = self.tableWidget_Machine.item(1, 6)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID4_Machine2))
                item = self.tableWidget_Machine.item(1, 8)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID5_Machine2))
                item = self.tableWidget_Machine.item(1, 10)
                item.setText( sCounter)

            self.AAS_MES_Info.Machine_ID = str(self.getMachineFromAASMESInfo(self.url.sm_value_Machine_ID3))
            if self.AAS_MES_Info.Machine_ID != "":
                sMachineName = self.getMachineName(self.AAS_MES_Info.Machine_ID)
                item = self.tableWidget_Machine.item(2, 0)
                item.setText(sMachineName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID1_Machine3))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(2, 1)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID2_Machine3))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(2, 3)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID3_Machine3))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(2, 5)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID4_Machine3))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(2, 7)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID5_Machine3))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(2, 9)
                item.setText( sToolName)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID1_Machine3))
                item = self.tableWidget_Machine.item(2, 2)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID2_Machine3))
                item = self.tableWidget_Machine.item(2, 4)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID3_Machine3))
                item = self.tableWidget_Machine.item(2, 6)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID4_Machine3))
                item = self.tableWidget_Machine.item(2, 8)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID5_Machine3))
                item = self.tableWidget_Machine.item(2, 10)
                item.setText( sCounter)

            self.AAS_MES_Info.Machine_ID = str(self.getMachineFromAASMESInfo(self.url.sm_value_Machine_ID4))
            if self.AAS_MES_Info.Machine_ID != "":
                sMachineName = self.getMachineName(self.AAS_MES_Info.Machine_ID)
                item = self.tableWidget_Machine.item(3, 0)
                item.setText(sMachineName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID1_Machine4))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(3, 1)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID2_Machine4))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(3, 3)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID3_Machine4))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(3, 5)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID4_Machine4))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(3, 7)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID5_Machine4))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(3, 9)
                item.setText( sToolName)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID1_Machine4))
                item = self.tableWidget_Machine.item(3, 2)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID2_Machine4))
                item = self.tableWidget_Machine.item(3, 4)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID3_Machine4))
                item = self.tableWidget_Machine.item(3, 6)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID4_Machine4))
                item = self.tableWidget_Machine.item(3, 8)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID5_Machine4))
                item = self.tableWidget_Machine.item(3, 10)
                item.setText( sCounter)

            self.AAS_MES_Info.Machine_ID = str(self.getMachineFromAASMESInfo(self.url.sm_value_Machine_ID5))
            if self.AAS_MES_Info.Machine_ID != "":
                sMachineName = self.getMachineName(self.AAS_MES_Info.Machine_ID)
                item = self.tableWidget_Machine.item(4, 0)
                item.setText(sMachineName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID1_Machine5))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(4, 1)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID2_Machine5))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(4, 3)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID3_Machine5))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(4, 5)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID4_Machine5))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(4, 7)
                item.setText( sToolName)

                sToolID = str(self.getToolsFromAASMESInfo(self.url.sm_value_possible_Tool_ID5_Machine5))
                sToolName = self.getToolName(sToolID)
                item = self.tableWidget_Machine.item(4, 9)
                item.setText( sToolName)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID1_Machine5))
                item = self.tableWidget_Machine.item(4, 2)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID2_Machine5))
                item = self.tableWidget_Machine.item(4, 4)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID3_Machine5))
                item = self.tableWidget_Machine.item(4, 6)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID4_Machine5))
                item = self.tableWidget_Machine.item(4, 8)
                item.setText( sCounter)

                sCounter = str(self.getCounterFromAASMESInfo(self.url.sm_value_counter_Tool_ID5_Machine5))
                item = self.tableWidget_Machine.item(4, 10)
                item.setText( sCounter)

            return
        
        
        return
        
    def getMachineList(self):
        self.fillMachinetable()
        return
    
    def clickedMachineTable(self):
        
        selected_items = self.tableWidget_Machine.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            self.row_text_col0 = self.tableWidget_Machine.item(selected_row, 0).text() # Maschine
            self.row_text_col1 = self.tableWidget_Machine.item(selected_row, 1).text() # possible Wkzg1
            self.row_text_col2 = self.tableWidget_Machine.item(selected_row, 2).text() # possible MaintenanceCounter1
            self.row_text_col3 = self.tableWidget_Machine.item(selected_row, 3).text() # possible Wkzg2
            self.row_text_col4 = self.tableWidget_Machine.item(selected_row, 4).text() # possible MaintenanceCounter2
            self.row_text_col5 = self.tableWidget_Machine.item(selected_row, 5).text() #...
            self.row_text_col6 = self.tableWidget_Machine.item(selected_row, 6).text() 
            self.row_text_col7 = self.tableWidget_Machine.item(selected_row, 7).text() 
            self.row_text_col8 = self.tableWidget_Machine.item(selected_row, 8).text() 
            self.row_text_col9 = self.tableWidget_Machine.item(selected_row, 9).text() 
            self.row_text_col10 = self.tableWidget_Machine.item(selected_row, 10).text() 
            #print(f'Text der selektierten Zeile von Spalte 0: {self.row_text_col0}')
            self.sControlFlag = 'Start'
            
        else:
            print('Keine Zeile selektiert')  
        return
    
    
    
    def pressStartButton(self, sProduct : str ):
        
        self.AAS_ProductInstance.MatNoFinishedProduct = sProduct
        self.counter = 1
        # Todo Status holen und Check ob die vorherige Produktion abgeschlossen ist
        sStatus = self.getMESInfoStatus()
        #sStatus ="IDLE"
        if sStatus != "IDLE":
            self.lResultText.setText("Produktion läuft noch! " + sStatus)
            self.start_timer()
            self.lHelpText.setText("Produkt auswählen")
            self.pushButtonStartProdukt1.setEnabled(True)
            self.pushButtonStartProdukt2.setEnabled(True)
            self.pushButtonStartProdukt3.setEnabled(True)
            return
        
        self.UpdateMESInfoStatus("STARTED")
        # ToDO dialog Order wird angelegt könnte hier rein
        self.pushButtonStartProdukt1.setEnabled(False)
        self.pushButtonStartProdukt2.setEnabled(False)
        self.pushButtonStartProdukt3.setEnabled(False)
            
        self.counter = 2
        self.start_timer()
        sStatus = ""
        while sStatus != "NEGOTIATED" :
            sStatus = self.getMESInfoStatus()
            if sStatus == "NEGOTIATED":
                self.stop_timer()
                self.UpdateMESInfoStatus("CHECKING")
                self.getMachineList()
                self.lHelpText.setText("Maschine auswählen und Werzeuge scannen:")
                self.lResultText.setText("Verhandlungsprozess und Capability Check durchgeführt,\nneuer Auftrag angelegt...")
                return
            #self.start_timer()

        return
       

    def pressResetButton(self):
        self.AAS_ProductInstance.MatNoFinishedProduct = ""
        self.pushButtonStartProdukt1.setEnabled(True)
        self.pushButtonStartProdukt2.setEnabled(True)
        self.pushButtonStartProdukt3.setEnabled(True)
        self.UpdateMESInfoStatus("RESET")
        self.sControlFlag =""
        self.lResultText.setText("Reset durchgeführt! " )
        self.lHelpText.setText("Neues Produkt auswählen:")
        self.lCurrentOrder.setText( "Aktuell kein laufender Auftrag auf der Maschine!")
        self.deleteTableContent()

    def deleteTableContent(self):
        row = 0
        while row < 5:
            col = 0
            while col < 11:
                item = self.tableWidget_Machine.item(row, col)
                item.setText("")
                col = col + 1
            row = row + 1
        i=0
        self.row_text_col0 = ""
        self.row_text_col1 = ""
        self.row_text_col2 = ""
        self.row_text_col3 = ""
        self.row_text_col4 = ""
        self.row_text_col5 = ""
        self.row_text_col6 = ""
        self.row_text_col7 = ""
        self.row_text_col8 = ""
        self.row_text_col9 = ""
        self.row_text_col10 = ""
        
        return
    
    
    def getToolID(self, name : str):
        # KOMAX TOOLS    
        if  name == "TE_App_I3" :
            id = "http://arena2036.de/vws4ls/aas/5bc3eb68-870f-4719-8234-ed51810321bc"  
            return id
        if  name == "TE_App_I4" :
            id = "http://arena2036.de/vws4ls/aas/b6d0fc62-b4c9-4b2a-9ce1-b2ced123f482"  
            return id
        if  name == "TE_App_I5" :
            id = "http://arena2036.de/vws4ls/aas/b72ee287-1644-4751-8844-3ca917411bd9"  
            return id
        if  name == "TE_App_I6" :
            id = "http://arena2036.de/vws4ls/aas/f574e9eb-e6cf-45e0-a76c-5d5785255312"  
            return id
        if  name == "TE_App_I2" :
            id = "http://arena2036.de/vws4ls/aas/e79657f0-08da-4f61-8bba-68e34e3e3c36"  
            return id
        if  name == "TE_App_I1" :
            id = "http://arena2036.de/vws4ls/aas/f8804ede-005a-4266-8650-fe4ae2c110a7"  
            return id
        
        # WEZAG TOOLS
        if name == "W_50s_I1":
            id = "https://example.com/ids/aas/5040_1161_8042_5361"
            return id
        if     name == "W_50_I1":
            id = "https://example.com/ids/aas/7053_1161_8042_5856"
            return name  
        if name =="W_35_I1":
            id = "https://example.com/ids/sm/3404_0110_2042_7933"
            return name    
        
        return ""
      
    def getMachineID(self, name : str):
        # KOMAX Machines
        if  name == "K_ALPHA_550_I1" :
            id = "http://smart.komaxgroup.com/aas/03bb64b3-2563-4f22-a475-b3732bad1e16"  
            return id
        if  name == "K_ALPHA_550_I2" :
            id = "http://smart.komaxgroup.com/aas/6462aa9f-40d9-4385-a51c-175bce470600"  
            return id
        if  name == "K_ALPHA_550_I3" :
            id = "http://smart.komaxgroup.com/aas/dd619733-cab3-4b75-aee7-dfff4d81c82e" 
            return id

        #WEZAG machines
        if  name == "W_UP150_I1" :
            id = "https://finaldemo.vws4ls.com/ids/sm/2321_8080_2042_7808" 
            return id
        if  name == "W_UP150" :
            id = "https://finaldemo.vws4ls.com/ids/sm/2321_8080_2042_7809" 
            return id
        
        return ""  
    
    def postSelectedMachine(self, value_patch : str):
        value = "$value"
        # umwandeln des Namen in ID
        value_patch = self.getMachineID(value_patch)
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_selected_Machine_ID + value
        # für upates use patch
        response = requests.patch(api_url,json = value_patch, auth=self.url.auth)
        if response.status_code > 400:
            print(f"Fehler beim patch! Selected machine: {response.status_code}")
            return False
    
    def postSelectedTool(self, value_patch : str):
        value = "$value"
        # umwandeln des Namen in ID
        value_patch = self.getToolID(value_patch)
        api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_selected_Tool_ID + value
        # für upates use patch
        response = requests.patch(api_url,json = value_patch, auth=self.url.auth)
        if response.status_code > 400:
            print(f"Fehler beim patch! selected tool: {response.status_code}")
            return False
        
    def postSelectedMaterials(self, value_patch : str, type : str):
        value = "$value"
        if type == "W":
            api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_selected_Material_ID1 + value
        else:
            api_url = self.url.server_url + self.url.base64_encoded_sm_url + self.url.sm_value_selected_Material_ID2 + value
        # für upates use patch
        response = requests.patch(api_url,json = value_patch, auth=self.url.auth)
        if response.status_code > 400:
            print(f"Fehler beim patch! selected materials: {response.status_code}")
            return False
        
    def wait4MaschineResult(self):
        self.lResultText.setText("")
        self.lHelpText.setText("Warte auf Prozessende")
       
        
        self.eInputMain.clear()
        self.postSelectedMachine(self.row_text_col0)
        self.postSelectedTool(self.sSelectedTool)
        

        self.UpdateMESInfoStatus("CHECKED")
        #todo
        self.open_message_dialog("Warte auf Rückmeldung von der Maschine...")
        self.start_timer()
        sStatus = ""
        while sStatus != "IDLE":
            sStatus = self.getMESInfoStatus()
            if sStatus == "IDLE":
                self.stop_timer()
                self.pushButtonStartProdukt1.setEnabled(True)
                self.pushButtonStartProdukt2.setEnabled(True)
                self.pushButtonStartProdukt3.setEnabled(True)
                self.lResultText.setText("Prozess abgeschlossen")
                self.lHelpText.setText("Neues Produkt auswählen")
                self.lCurrentOrder.setText( "Aktuell kein laufender Auftrag auf der Maschine!")
                self.deleteTableContent()
                return
                    
        return
    
    def editFinished(self):
        sInput = self.eInputMain.text() 
        if sInput == "":
            return
        if self.row_text_col0 == "":
            self.lResultText.setText("Bitte zuerst Maschine auswählen!")
            self.eInputMain.clear()
            return
        # Check ob eines der 5 Wkzg gescannt wurde
        if self.sControlFlag == 'Start':
            if self.nWkzgCounter == 1:
                if self.row_text_col1 == sInput or self.row_text_col3 == sInput or self.row_text_col5 == sInput or self.row_text_col7 == sInput or self.row_text_col9 == sInput:
                    self.sSelectedTool = sInput
                    self.lResultText.setText("Werkzeug akzeptiert!")
                    self.lHelpText.setText("Leitung scannen")
                    self.sControlFlag = 'LeitungMatNo'
                    self.eInputMain.clear()
                    self.nWWkzgActual = 1
                    return
                else:
                    self.lResultText.setText("Ungültiges Werkzeug!")
                    self.lHelpText.setText("Werkzeug erneut scannen")
                    self.eInputMain.clear()
                    return
            ### nach abstimmung in KW 33 wird immer nur ein Wkzg pro Maschine verbaut sein
            """"
            else:    
                if self.nWWkzgActual == 1:
                    if self.row_text_col1 == sInput:
                        self.lResultText.setText("Werkzeug akzeptiert!")
                        self.lHelpText.setText("2. Werkzeug scannen")
                        self.sControlFlag = 'Start'
                        self.eInputMain.clear()
                        self.nWWkzgActual = 2
                        return
                    else:
                        self.lResultText.setText("Falsches Werkzeug 1!")
                        self.lHelpText.setText("Werkzeug 1 erneut scannen")
                        self.eInputMain.clear()
                        return

                else:
                    if self.row_text_col3 == sInput:
                        self.lResultText.setText("Werkzeug 2 akzeptiert!")
                        self.lHelpText.setText("Leitung scannen")
                        self.sControlFlag = 'LeitungMatNo'
                        self.eInputMain.clear()
                        self.nWWkzgActual = 1
                        return
                    else:
                        self.lResultText.setText("Falsche Werkzeug 2!")
                        self.lHelpText.setText("Werkzeug 2 erneut scannen")
                        self.eInputMain.clear()
                        return
            """

        if self.sControlFlag == 'LeitungMatNo':
            sProduct = self.getMESInfoMaterialID("W")
            sProductSplitted = sInput.split("#")
            
            if sProduct == sProductSplitted[0]:
                self.postSelectedMaterials(sInput,"W")
                self.lResultText.setText("Leitung akzeptiert!")
                self.lHelpText.setText("Terminal scannen")
                self.sControlFlag = 'TerminalMatNo'
                self.eInputMain.clear()
                return
            else:
                self.lResultText.setText("Falsche Leitung!")
                self.lHelpText.setText("Leitung erneut scannen")
                self.eInputMain.clear()
                return
            
        
        if self.sControlFlag == 'TerminalMatNo':
            sProduct = self.getMESInfoMaterialID("T")
            sProductSplitted = sInput.split("#")
            if sProduct == sProductSplitted[0]:
                self.postSelectedMaterials(sInput,"T")
                self.pushButtonMachinenCommunication.animateClick(200)
                # ToDo Anzeige des aktuellen Auftrags mit ausgewählten Produkt
                sProductionOrder = self.getProductionOrder_ID()
                self.lCurrentOrder.setText("Aktuelle Produktion läuft")
                return  
            else:
                self.lResultText.setText("Falsches Terminal!")
                self.lHelpText.setText("Terminal erneut scannen")
                self.eInputMain.clear()
                return  
               
    
    
    class AAS_Leitungssatz:
        JobNo: str
        JobQuantity: int
        JobProgramNo: int
        MatNoFinishedProduct: str
        ChargeNoFinishedProduct: str
        MatNoWire: str
        MatNoContact: str
        JobQuantityProducedOk: int
        JobQuantityProducedNOk: int
        ChargeNoWire: str
        ChargeNoContact: str
        JobProductionDateTimeStart: str
        JobProductionDateTimeEnd: str
        cfmCurve: str
        CfmCurveLimitUpper: str
        CfmCurveLimitLower: str
        CfmCurveAnalysis: str
        cfmResult: str
        JobExecuted = False
        
        url_JobNo: str
        url_JobQuantity: int
        url_JobProgramNo: int
        url_MatNoFinishedProduct: str
        url_ChargeNoFinishedProduct: str
        url_MatNoWire: str
        url_MatNoContact: str
        url_JobQuantityProducedOk: int
        url_JobQuantityProducedNOk: int
        url_ChargeNoWire: str
        url_ChargeNoContact: str
        url_JobProductionDateTimeStart: str
        url_JobProductionDateTimeEnd: str
        url_CrimpCurve: str
        url_cfmCurve: str
        url_cfmResult: str
        url_Executed: str
        url_DateTimeStart: str
        url_DateTimeEnd: str
        url_CfmCurveLimitUpper: str
        url_CfmCurveLimitLower: str
        url_CfmAnalysis: str
        
    def do_config(self):
         # Define the path to your JSON file
        json_file_path = "config.json"
         

        
        json_key = "Location"
        sLocation = self.get_config_from_json(json_file_path, json_key)
        print(f"The value of '{json_key}' in the JSON file is: {sLocation}")

        self.config.sProdukt1= self.get_config_from_json(json_file_path,"Produkt1" )
        self.config.sAASProduct1 = self.get_config_from_json(json_file_path,"AAS_Produkt1" )
        self.config.sProduktPicture1= self.get_config_from_json(json_file_path,"Produktpicture1")
        self.config.sProdukt2= self.get_config_from_json(json_file_path,"Produkt2" )
        self.config.sAASProduct2 = self.get_config_from_json(json_file_path,"AAS_Produkt2" )
        self.config.sProduktPicture2= self.get_config_from_json(json_file_path,"Produktpicture2" )
        self.config.sProdukt3= self.get_config_from_json(json_file_path,"Produkt3" )
        self.config.sAASProduct3 = self.get_config_from_json(json_file_path,"AAS_Produkt3" )
        self.config.sProduktPicture3 = self.get_config_from_json(json_file_path,"Produktpicture3" )
        self.config.sMaschine1 = self.get_config_from_json(json_file_path,"Maschine1" )
        self.config.sMaschinePicture1 = self.get_config_from_json(json_file_path,"Maschinepicture1" )
        self.config.sMaschine2 = self.get_config_from_json(json_file_path,"Maschine2" )
        self.config.sMaschinePicture2 = self.get_config_from_json(json_file_path,"Maschinepicture2" )

        json_key = "User"
        self.url.url_user = self.get_config_from_json(json_file_path, json_key)
        json_key = "Pw"
        self.url.url_pw = self.get_config_from_json(json_file_path, json_key)
        self.url.auth = HTTPBasicAuth(self.url.url_user,self.url.url_pw)                                
        if sLocation    == 'Arena2036':
            #self.url.url_AASServer = "http://DESKTOP-2Q51HB1:4002/" # MESSE
            #self.url.url_AASServer4WEZAG = "http://DESKTOP-2Q51HB1:4001/" # MESSE
            
            self.url.server_url ="https://tractus-x-07.arena2036.de:8081/submodels/"
            self.url.base64_encoded_sm_url = "TUVTLUluZm8tU3VibW9kZWwtRGVtb25zdHJhdG9y"
            self.url.sm_value_status = "/submodel-elements/MES_Status/"
            #self.url.sm_value_material = "/submodel-elements/Material_ID/"
            self.url.sm_value_product_ID = "/submodel-elements/Product_ID/"
            self.url.value = "$value"
        else:
            self.url.url_AASServer = "http://lnxvib361:8081/" #VIB 2024
            self.url.url_AASServer4WEZAG = "http://lnxvib361:8081/" #VIB 2024

        #self.url.url_MachineSub = "http%3A%2F%2Fdemo2023.vws4ls.com%2Fids%2Faas%2F7031_8082_3022_7912/"
        #self.url.url_LeitungssatzSub = "http%3A%2F%2Fdemo2023.vws4ls.com%2Fshell%2F"
        #self.url.url_InformationModelDescriptionShell = "http%3A%2F%2Fwww.arena2036.com%2FInformationModelDescriptionShell%2F"
        #self.url.url_AASServer = "http://testw100065:4001/"  # bis 24.02 gültig


    # Function to read the JSON file and extract the value of a specific key        
    def get_config_from_json( self, json_path :str, json_key: str):
        try:
            with open(json_path, 'r') as file:
                data = json.load(file)
                if json_key in data:
                    return data[json_key]
                else:
                    return None
        except FileNotFoundError:
            print(f"File '{json_path}' not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
            return None

    class url:
        server_url ="https://tractus-x-07.arena2036.de:8081/submodels/"
        base64_encoded_sm_url = "TUVTLUluZm8tU3VibW9kZWwtRGVtb25zdHJhdG9y"
        sm_value_status = "/submodel-elements/MES_Status/"
        sm_value_product_ID = "/submodel-elements/Product_ID/"
        #new for final Demo
        sm_value_material1 = "/submodel-elements/possible_Material_IDs.Material_ID1/"
        sm_value_material2 = "/submodel-elements/possible_Material_IDs.Material_ID2/"
                                        
        sm_value_selected_Machine_ID = "/submodel-elements/selected_Machine_ID.Machine_ID/"
        sm_value_selected_Tool_ID = "/submodel-elements/selected_Machine_ID.selected_Tool_IDs.Tool_ID1/"
        sm_value_selected_Material_ID1 ="/submodel-elements/selected_Material_IDs.Material_ID1/"
        sm_value_selected_Material_ID2 ="/submodel-elements/selected_Material_IDs.Material_ID2/"


        sm_value_ProductionOrder_ID = "/submodel-elements/ProductionOrder_ID/"
        sm_value_Machine_ID1 = "/submodel-elements/possible_Machine_IDs.Machine_1.Machine_ID/"
        sm_value_Machine_ID2 = "/submodel-elements/possible_Machine_IDs.Machine_2.Machine_ID/"
        sm_value_Machine_ID3 = "/submodel-elements/possible_Machine_IDs.Machine_3.Machine_ID/"
        sm_value_Machine_ID4 = "/submodel-elements/possible_Machine_IDs.Machine_4.Machine_ID/"
        sm_value_Machine_ID5 = "/submodel-elements/possible_Machine_IDs.Machine_5.Machine_ID/"
                                                
        sm_value_possible_Tool_ID1_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool1.Tool_ID1/"
        sm_value_possible_Tool_ID2_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool2.Tool_ID2/"
        sm_value_possible_Tool_ID3_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool3.Tool_ID3/"
        sm_value_possible_Tool_ID4_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool4.Tool_ID4/"
        sm_value_possible_Tool_ID5_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool5.Tool_ID5/"
                                               

        sm_value_possible_Tool_ID1_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool1.Tool_ID1/"
        sm_value_possible_Tool_ID2_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool2.Tool_ID2/"
        sm_value_possible_Tool_ID3_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool3.Tool_ID3/"
        sm_value_possible_Tool_ID4_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool4.Tool_ID4/"
        sm_value_possible_Tool_ID5_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool5.Tool_ID5/"

        sm_value_possible_Tool_ID1_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool1.Tool_ID1/"
        sm_value_possible_Tool_ID2_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool2.Tool_ID2/"
        sm_value_possible_Tool_ID3_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool3.Tool_ID3/"
        sm_value_possible_Tool_ID4_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool4.Tool_ID4/"
        sm_value_possible_Tool_ID5_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool5.Tool_ID5/"

        sm_value_possible_Tool_ID1_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool1.Tool_ID1/"
        sm_value_possible_Tool_ID2_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool2.Tool_ID2/"
        sm_value_possible_Tool_ID3_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool3.Tool_ID3/"
        sm_value_possible_Tool_ID4_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool4.Tool_ID4/"
        sm_value_possible_Tool_ID5_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool5.Tool_ID5/"

        sm_value_possible_Tool_ID1_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool1.Tool_ID1/"
        sm_value_possible_Tool_ID2_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool2.Tool_ID2/"
        sm_value_possible_Tool_ID3_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool3.Tool_ID3/"
        sm_value_possible_Tool_ID4_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool4.Tool_ID4/"
        sm_value_possible_Tool_ID5_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool5.Tool_ID5/"
              
        sm_value_counter_Tool_ID1_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool1.Maintenance_Counter/"
        sm_value_counter_Tool_ID2_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool2.Maintenance_Counter/"
        sm_value_counter_Tool_ID3_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool3.Maintenance_Counter/"
        sm_value_counter_Tool_ID4_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool4.Maintenance_Counter/"
        sm_value_counter_Tool_ID5_Machine1 = "/submodel-elements/possible_Machine_IDs.Machine_1.possible_Tool_IDs.Tool5.Maintenance_Counter/"

        sm_value_counter_Tool_ID1_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool1.Maintenance_Counter/"
        sm_value_counter_Tool_ID2_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool2.Maintenance_Counter/"
        sm_value_counter_Tool_ID3_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool3.Maintenance_Counter/"
        sm_value_counter_Tool_ID4_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool4.Maintenance_Counter/"
        sm_value_counter_Tool_ID5_Machine2 = "/submodel-elements/possible_Machine_IDs.Machine_2.possible_Tool_IDs.Tool5.Maintenance_Counter/"

        sm_value_counter_Tool_ID1_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool1.Maintenance_Counter/"
        sm_value_counter_Tool_ID2_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool2.Maintenance_Counter/"
        sm_value_counter_Tool_ID3_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool3.Maintenance_Counter/"
        sm_value_counter_Tool_ID4_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool4.Maintenance_Counter/"
        sm_value_counter_Tool_ID5_Machine3 = "/submodel-elements/possible_Machine_IDs.Machine_3.possible_Tool_IDs.Tool5.Maintenance_Counter/"

        sm_value_counter_Tool_ID1_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool1.Maintenance_Counter/"
        sm_value_counter_Tool_ID2_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool2.Maintenance_Counter/"
        sm_value_counter_Tool_ID3_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool3.Maintenance_Counter/"
        sm_value_counter_Tool_ID4_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool4.Maintenance_Counter/"
        sm_value_counter_Tool_ID5_Machine4 = "/submodel-elements/possible_Machine_IDs.Machine_4.possible_Tool_IDs.Tool5.Maintenance_Counter/"

        sm_value_counter_Tool_ID1_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool1.Maintenance_Counter/"
        sm_value_counter_Tool_ID2_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool2.Maintenance_Counter/"
        sm_value_counter_Tool_ID3_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool3.Maintenance_Counter/"
        sm_value_counter_Tool_ID4_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool4.Maintenance_Counter/"
        sm_value_counter_Tool_ID5_Machine5 = "/submodel-elements/possible_Machine_IDs.Machine_5.possible_Tool_IDs.Tool5.Maintenance_Counter/"
    

        value = "$value"
        url_user : str
        url_pw : str
        auth : str
    
    class config:
        sProdukt1 : str
        sAASProduct1 = str
        sProduktPicture1 : str
        sProdukt2 : str
        sAASProduct2 = str
        sProduktPicture2 : str
        sProdukt3 : str
        sProduktPicture3 : str
        sAASProduct3 = str
        sMaschine1 :str
        sMaschinePicture1 : str
        sMaschine2 :str
        sMaschinePicture2 : str
   
   # toDo Hier die Variablen für die neue MES Info AAS anlegen 
    class AAS_MES_Info:
        MES_Status : str # not used yet
        Product_ID : str #not used yet
        #sProcess_Number :str #not used yet
        ProductionOrder_ID : str #not used yet
        Machine_ID : str
        Tool_ID1 : str
        Tool_ID2 : str
        Counter1 : str
        Counter2 : str


  
    class AAS_ProductInstance:
        MatNoFinishedProduct: int
        ProductNo: str
        ChargeLtg: str
        ChargeConatct: str
        ProductionDateTime: str 
        ProductionDateTimeEnd: str
        CrimpCurve: str

    class AAS_WEZAGMachine:
        MachineNo: str
        MachineStatus: str
        ProductionReleaseFlag: bool
        JobNo: str
        JobProgramNo: str
        JobQuantityProducedOk: str
        JobQuantityProducedNOk: str
        JobProductionDateTimeStart: str
        JobProductionDateTimeEnd: str
        cfmCurve: str
        cfmResult: str
        Executed: bool
        DateTimeStart: str
        DateTimeEnd: str
        CfmCurveLimitUpper: str
        CfmCurveLimitLower: str
        CfmAnalysis: str
        SemanticID: str

if __name__ == "__main__":
    import sys
    #
    #now we will Create and configure logger 
    logging.basicConfig(filename="Demonstrator2024.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

    #Let us Create an object 
    logger=logging.getLogger() 

    #Now we are going to Set the threshold of logger to DEBUG 
    logger.setLevel(logging.DEBUG) 
    bQRCodeflag = True
    

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
