# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CVI_Python_Interface_Config.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import sys
import socket
import select

import time
import math

#For File Writing
import os
import shutil

#GUI imports
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtNetwork import *

#For plotting within pyqt
import pyqtgraph
from pyqtgraph import PlotWidget, ViewBox
import numpy as np
from numpy.polynomial import polynomial

####IF PROGRAM FAILS, RUN COMMAND "lsof -i" and kill the pid associated with python####

class Ui_MainWindow(QObject):

	dataReceived = pyqtSignal(object,object)
	errorSignal = pyqtSignal(object)
	logSignal = pyqtSignal(object)
	
	tdlReturn = pyqtSignal(object)
	
	def __init__(self, parent=None):
		super(Ui_MainWindow, self).__init__(parent)

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		self.MainWindow = MainWindow
		
		#qr = MainWindow.frameGeometry()
		#cp = QtGui.QDesktopWidget().availableGeometry().center()
		#qr.moveCenter(cp)
		#MainWindow.move(qr.topLeft())
		
		#MainWindow.sizePolicy.ignored()
		#MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Removes window such that it cannot be closed.
		MainWindow.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)		
		#MainWindow.setMinimumSize(800,600)
		#MainWindow.minimumSizeHint()
		#MainWindow.adjustSize()

		#self.errorstatus.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		#self.errorstatus.setMinimumSize(1,1)
		
		#verticalLine 	=  QFrame()
		#verticalLine.setFrameStyle(QFrame.VLine)
		#verticalLine.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
		
		'''
		import os
		print os.environ['HOME']
		Or you can see a list of all the environment variables using:

		os.environ
		As sometimes you might need to see a complete list!

		# using get will return `None` if a key is not present rather than raise a `KeyError`
		print os.environ.get('KEY_THAT_MIGHT_EXIST')

		# os.getenv is equivalent, and can also give a default value instead of `None`
		print os.getenv('KEY_THAT_MIGHT_EXIST', default_value)
		'''
		
		QApplication.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))
		#MainWindow.setStyleSheet("background-color: darkgray")
		#MainWindow.setStyleSheet("""QMainWindow{background-color: lightgray;}""")
		MainWindow.setStyleSheet("""QMainWindow{background-color: rgb(0, 0, 100);}""")
		
		
		#Creation of Main Layout
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
			
		#Creation of Tabs to nest within Layout
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setObjectName("tabWidget")
		#self.tabWidget.setStyleSheet("""QTabWidget{background-color: lightgray;}""")
		self.tabWidget.setStyleSheet("""QTabWidget{background-color: rgb(220,220,255);}""")

		#Create First Tab
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.tabWidget.addTab(self.tab, "")
		
		
		self.tabLayout_1 = QtWidgets.QGridLayout(self.tab)
		self.tabLayout_1.setContentsMargins(10, 10, 10, 10)
		self.tabLayout_1.setObjectName("tabLayout_1")
		self.tabLayout_1.setSpacing(5)
		
		'''
		#Create first tab sublayout
		self.subTabLayout_1 = QtWidgets.QGridLayout(self.tab)
		self.subTabLayout_1.setContentsMargins(10, 10, 10, 10)
		self.subTabLayout_1.setObjectName("subTabLayout_1")
		self.subTabLayout_1.setSpacing(10)
		'''
		
		#Create Second Tab
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tabWidget.addTab(self.tab_2, "")
		self.tabLayout_2 = QtWidgets.QGridLayout(self.tab_2)
		self.tabLayout_2.setContentsMargins(10, 10, 10, 10)
		self.tabLayout_2.setObjectName("tabLayout_2")	
		self.tabLayout_2.setSpacing(5)

		#Create Third Tab
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.tabWidget.addTab(self.tab_3, "Connect Auxiliary Instruments")
		self.tabLayout_3 = QtWidgets.QGridLayout(self.tab_3)
		self.tabLayout_3.setContentsMargins(10, 10, 10, 10)
		self.tabLayout_3.setObjectName("tabLayout_3")
		self.tabLayout_3.setSpacing(5)
		
		#Create Fourth Tab
		self.tab_4 = QtWidgets.QWidget()
		self.tab_4.setObjectName("tab_4")
		self.tabWidget.addTab(self.tab_4, "TDL Calibration")
		self.tabLayout_4 = QtWidgets.QGridLayout(self.tab_4)
		self.tabLayout_4.setContentsMargins(10, 10, 10, 10)
		self.tabLayout_4.setObjectName("tabLayout_4")
		self.tabLayout_4.setSpacing(5)
		
		
		#Create uniform grid spacing for layout resizing purposes

		'''
		for i in range(0, 21):
			self.tabLayout_1.setRowStretch(i,1)
			self.tabLayout_1.setRowMinimumHeight(i,1)	####
#
		for i in range(0, 51):
			self.tabLayout_1.setColumnStretch(i,1)
			self.tabLayout_1.setColumnMinimumWidth(i,1)	####
		'''

		for i in range(0, 101):
			self.tabLayout_1.setColumnMinimumWidth(i,1) ###
			self.tabLayout_1.setColumnStretch(i,1)
			self.tabLayout_2.setColumnMinimumWidth(i,1) ###
			self.tabLayout_2.setColumnStretch(i,1)
			self.tabLayout_3.setColumnMinimumWidth(i,1) ###
			self.tabLayout_3.setColumnStretch(i,1)	
			self.tabLayout_4.setColumnMinimumWidth(i,1) ###
			self.tabLayout_4.setColumnStretch(i,1)	
			#self.subTabLayout_1.setColumnMinimumWidth(i,1)
			#self.subTabLayout_1.setColumnStretch(i,1)
		for i in range(0, 51):
			self.tabLayout_1.setRowMinimumHeight(i,1)	####
			self.tabLayout_1.setRowStretch(i,1)
			self.tabLayout_2.setRowMinimumHeight(i,1)	####
			self.tabLayout_2.setRowStretch(i,1)
			self.tabLayout_3.setRowMinimumHeight(i,1)	####
			self.tabLayout_3.setRowStretch(i,1)
			self.tabLayout_4.setRowMinimumHeight(i,1)	####
			self.tabLayout_4.setRowStretch(i,1)
			#self.subTabLayout_1.setRowMinimumHeight(i,1)
			#self.subTabLayout_1.setRowStretch(i,1)

		
		#Push buttons for establishing (or cancelling) server to receive data
		self.connect = QtWidgets.QPushButton(self.tab)
		self.connect.setObjectName("connect")
		self.tabLayout_1.addWidget(self.connect, 0, 0, 2, 20)
		self.disconnect = QtWidgets.QPushButton(self.tab)
		self.disconnect.setObjectName("disconnect")
		self.tabLayout_1.addWidget(self.disconnect, 0, 20, 2, 20)	

		#verticalLine 	=  QFrame()
		#verticalLine.setFrameStyle(QFrame.VLine)
		#verticalLine.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
		
		#tmpobject = QFrame()
		#tmpobject.setFrameStyle(QFrame.HLine)
		#tmpobject.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
		#self.tabLayout_1.addWidget(tmpobject, 2, 0, 1, 40)
					
		#Creation of arbitrary label
		tmpobject = QtWidgets.QLabel(self.tab)
		tmpobject.setObjectName("flowoptionslabel")
		self.tabLayout_1.addWidget(tmpobject, 2, 0, 2, 10)
		tmpobject.setText("FLOW OPTIONS")
		tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)	
		tmpobject.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))						
					
		#Flow on/off toggle
		self.flowio = QtWidgets.QPushButton(self.tab)
		self.flowio.setObjectName("flowio")
		self.tabLayout_1.addWidget(self.flowio, 2, 10, 2, 10)
		self.flowio.setCheckable(True)
		self.flowio.setStyleSheet("background-color: red")
		#self.flowio.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		
		#CVI Mode toggle for CVI/Total option
		self.cvimode = QtWidgets.QPushButton(self.tab)
		self.cvimode.setObjectName("cvimode")
		self.tabLayout_1.addWidget(self.cvimode, 2, 20, 2, 10)
		self.cvimode.setCheckable(True)
		
		#Autopilot Mode toggle
		self.autopilot = QtWidgets.QPushButton(self.tab)
		self.autopilot.setObjectName("autopilot")
		self.tabLayout_1.addWidget(self.autopilot, 2, 30, 2, 10)
		self.autopilot.setCheckable(True)	
		#self.autopilot.setDisabled(True)
		self.autopilot.setText("Autopilot: OFF")
		self.autopilot.clicked.connect(lambda: self.toggleswitched(MainWindow))
		

		self.cvf3cwlabel = QtWidgets.QLabel(self.tab)
		self.cvf3cwlabel.setObjectName("cvf3cwlabel")		
		self.tabLayout_1.addWidget(self.cvf3cwlabel, 5, 0, 2, 5)
		self.cvf3cw = QtWidgets.QLineEdit(self.tab)
		self.cvf3cw.setObjectName("cvf3cw")
		self.tabLayout_1.addWidget(self.cvf3cw, 5, 5, 2, 5)	
		#self.cvf3cwlabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		self.cvf3cw.editingFinished.connect(lambda: self.updateSliders(MainWindow, 'cvf3cw'))

		self.cvf3cwlabel.setStyleSheet("background-color: yellow")
		#self.cvf3cw.setStyleSheet("background-color: yellow")		

		self.cvf3cwSlider = QSlider(Qt.Horizontal, self.tab)
		self.cvf3cwSlider.setMinimum(-200)#0)
		self.cvf3cwSlider.setMaximum(800)
		self.cvf3cwSlider.setValue(0)
		self.cvf3cwSlider.setTickPosition(QSlider.TicksBelow)
		self.cvf3cwSlider.setTickInterval(100)
		self.cvf3cwSlider.setObjectName('cvf3cwSlider')
		self.tabLayout_1.addWidget(self.cvf3cwSlider, 7, 0, 2, 10)
		self.cvf3cwSlider.valueChanged.connect(lambda: self.syncSliders(MainWindow, 'cvf3cw'))	

		#self.cvf3cwSlider.setStyleSheet("background-color: yellow")


		#Internal flow control line edits
		#self.flowlabels = ['cvfx0label','cvfx2label','cvfx3label','cvfx4label']
		self.flowedit = ['cvfx0','cvfx2','cvfx3','cvfx4']
		self.internalFlows = [0.00]*4
		for i in range(0,len(self.flowedit)):
			tmpobject = QtWidgets.QLabel(self.tab)
			tmpobject.setObjectName(self.flowedit[i]+'label')
			self.tabLayout_1.addWidget(tmpobject, 9+4*i, 0, 2, 5)
			#tmpobject.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
			
			tmpobject = QtWidgets.QLineEdit(self.tab)
			tmpobject.setObjectName(self.flowedit[i])
			self.tabLayout_1.addWidget(tmpobject, 9+4*i, 5, 2, 5)
			tmpobject.editingFinished.connect(lambda i=i: self.updateSliders(MainWindow, self.flowedit[i]))
		
			sliderMin = 0
			sliderMax = 600
			sliderDiv = 100
			if i == 3: sliderMax = 20; sliderDiv = 10
			tmpobject = QSlider(Qt.Horizontal, self.tab)
			tmpobject.setMinimum(sliderMin)#0)
			tmpobject.setMaximum(sliderMax)#60)#50)
			tmpobject.setValue(0)
			tmpobject.setTickPosition(QSlider.TicksBelow)
			tmpobject.setTickInterval(sliderDiv)#10)
			tmpobject.setObjectName(self.flowedit[i]+'Slider')
			self.tabLayout_1.addWidget(tmpobject, 11+4*i, 0, 2, 10)
			tmpobject.valueChanged.connect(lambda new, i=i: self.syncSliders(MainWindow, self.flowedit[i]))

		#Preflight checklist
		self.preflightButton = QtWidgets.QPushButton(self.tab)
		self.preflightButton.setObjectName("preflightButton")
		self.tabLayout_1.addWidget(self.preflightButton, 25, 0, 2, 10)
		self.preflightButton.setStyleSheet("background-color: lightblue")
		self.preflightButton.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		#self.preflightButton.setDisabled(True)
		self.preflightButton.setText("Pre-Flight")
		self.preflightButton.clicked.connect(lambda: self.preflightChecklist(MainWindow))

		#Dropdown lists for selecting data for first plot
		self.commonNoteDropdown = QtWidgets.QComboBox(self.tab)
		self.commonNoteDropdown.setObjectName("commonNoteDropdown")
		self.tabLayout_1.addWidget(self.commonNoteDropdown, 23, 10, 2, 20)
		#self.commonNoteDropdown.setDisabled(True)
		
		self.commonNotes = ["Common Notes","Approaching Cloud", "In Cloud", "Exited Cloud","Taxi","Takeoff","Heaters ON","Landed"]
		self.commonNoteDropdown.addItems(self.commonNotes)
		self.commonNoteDropdown.activated.connect(lambda: self.addCommonNote(MainWindow))
		
		#Push to add custom note?
		self.customNoteButton = QtWidgets.QPushButton(self.tab)
		self.customNoteButton.setObjectName("customNoteButton")
		self.tabLayout_1.addWidget(self.customNoteButton, 23, 30, 2, 10)
		self.customNoteButton.setStyleSheet("background-color: lightblue")
		self.customNoteButton.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		#self.customNoteButton.setDisabled(True)
		self.customNoteButton.setText("User Entered Note")
		self.customNoteButton.clicked.connect(lambda: self.userNote(MainWindow))
		
		#Widget for displaying file that is being saved to
		#self.currentfilelabel = QtWidgets.QLabel(self.tab)
		#self.currentfilelabel.setObjectName("currentfilelabel")
		#self.tabLayout_1.addWidget(self.currentfilelabel, 25, 0, 2, 10)
		self.currentfile = QtWidgets.QLineEdit(self.tab)
		self.currentfile.setObjectName("currentfile")
		self.tabLayout_1.addWidget(self.currentfile, 25, 10, 2, 30)
		self.currentfile.setDisabled(True)		
		self.currentfile.setStyleSheet("QLineEdit:disabled {color:black; background-color: lightblue}")

					
		#Status indicator for instructional display and current operation of instrument
		self.mainstatus = QtWidgets.QTextBrowser()#QTextEdit()
		self.mainstatus.setObjectName("mainstatus")
		self.mainstatus.setAlignment(Qt.AlignTop)
		self.mainstatus.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))
		self.tabLayout_1.addWidget(self.mainstatus, 4, 11, 19, 28)
		self.mainstatus.verticalScrollBar().setValue(self.mainstatus.verticalScrollBar().maximum())
		#self.mainstatus.ensureCursorVisible()
				
		#Create Table for Viewing uncorrected, corrected, and calibrated flows
		self.tableWidget = QtWidgets.QTableWidget(self.tab)
		self.tableWidget.setObjectName("tableWidget")
		self.tabLayout_1.addWidget(self.tableWidget, 27, 0, 18, 23)
		
		#Create Table for viewing raw input and output data
		self.rawtableWidget = QtWidgets.QTableWidget(self.tab)
		self.rawtableWidget.setObjectName("rawtablewidget")
		self.tabLayout_1.addWidget(self.rawtableWidget, 27, 23, 18, 17)
		
		#Create table for viewing uncorrected,corrected, and calibrated inputs on first tab
		self.tablerowlabels = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4',
			'cvfx5','cvfx6','cvfx7','cvfx8','cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai']
		self.tablecolumnlabels = ['raw','calibrated','crunched','Last Received (s)']
		self.tableWidget.setColumnCount(len(self.tablecolumnlabels))
		self.tableWidget.setRowCount(len(self.tablerowlabels))
		for i in range(0,len(self.tablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setVerticalHeaderItem(i,item)
		for i in range(0,len(self.tablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setHorizontalHeaderItem(i, item)
		for i in range(0,len(self.tablerowlabels)):
			for j in range(0, len(self.tablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.tableWidget.setItem(i, j, item)
		self.tableErrorTracker = np.c_[[0]*len(self.tablerowlabels),[0]*len(self.tablerowlabels)]
		#self.plotdata = np.c_[[-9999]*(self.dropdownlist.count()+1)]#np.c_[[np.nan]*4]

		#table for raw input output parameters
		self.rawtablecolumnlabels = ['Input','Last Received (s)']
		self.rawtablerowlabels = ['time', 'cvtas', 'counts', 'cvf1', 'cvfx0', 
			'cvfx1', 'cvfx2', 'cvfx3', 'cvfx4', 'cvfx5', 'cvfx6', 'cvfx7', 'cvfx8',
			 'cvpcn', 'cvtt', 'cvtp', 'cvts', 'cvtcn', 'cvtai', 'H2OR', 'ptdlR', 
			'ttdlR', 'TDLsignal', 'TDLlaser', 'TDLline', 'TDLzero', 'TTDLencl', 
			'TTDLtec', 'TDLtrans', 'opc_cnts', 'opc_flow_raw', 'opc_pres_raw', 
			'ext1', 'ext2', 'H2O-PIC', '18O', 'HDO']
		self.rawOutputTableRowLabels = ['']
		self.rawtableWidget.setColumnCount(len(self.rawtablecolumnlabels))
		self.rawtableWidget.setRowCount(len(self.rawtablerowlabels))
		for i in range(0,len(self.rawtablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.rawtableWidget.setVerticalHeaderItem(i,item)
		for i in range(0,len(self.rawtablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.rawtableWidget.setHorizontalHeaderItem(i, item)
		for i in range(0,100):#len(self.tablerowlabels)):
			for j in range(0, len(self.rawtablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.rawtableWidget.setItem(i, j, item)	
		#self.rawtableWidget.verticalHeader().setVisible(False)

		self.rawTableErrorTracker = np.c_[[0]*len(self.rawtablerowlabels),[0]*len(self.rawtablerowlabels)]
		

		#Error indicator for alerting if there is a problem
		self.errorstatus = QtWidgets.QTextBrowser()#QTextEdit()
		self.errorstatus.setObjectName("errorstatus")
		self.errorstatus.setAlignment(Qt.AlignTop)
		self.errorstatus.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))
		self.errorstatus.setStyleSheet("color: rgb(255, 0, 0);")
		self.errorstatus.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
		self.errorstatus.setMinimumSize(1,1)
		#self.errorstatus.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
		self.tabLayout_1.addWidget(self.errorstatus,45,0,5,40)
		self.errorstatus.verticalScrollBar().setValue(self.mainstatus.verticalScrollBar().maximum())


	

		###############################################################################
		###############################################################################
		
		#First Plotting Widget
		self.CVIplot = PlotWidget(self.tab)
		self.CVIplot.setObjectName("CVIplot")
		self.tabLayout_1.addWidget(self.CVIplot, 2, 40, 23, 60)
		self.CVIplot.show()
		self.CVIplot.setTitle("CVI Data",color='w')
		self.CVIplot.setLabel('bottom',text = 'Time (seconds)')
		self.CVIplot.setLabel('left',text = 'Y1')
		
		#Linking of two separately scaling lines in the first plot
		self.CVIplotline2 = ViewBox()
		#self.CVIplot.showAxis('right')
		self.CVIplot.scene().addItem(self.CVIplotline2)
		self.CVIplot.getAxis('right').linkToView(self.CVIplotline2)
		self.CVIplotline2.setXLink(self.CVIplot)
		#self.CVIplot.getAxis('right').setLabel('Y2', color = (255,150,255))#'#0000ff')

		#OLD PURPLISH COLOR  = (150,150,255)
		
		#Coloring of first plot axis items
		self.CVIplot.getAxis('left').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.CVIplot.getAxis('bottom').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.CVIplot.getAxis('right').setPen(pyqtgraph.mkPen(color=(0,255,0), width=3))

		#Second Plotting Widget
		self.CVIplot2 = PlotWidget(self.tab)
		self.CVIplot2.setObjectName("CVIplot")
		self.tabLayout_1.addWidget(self.CVIplot2, 27, 40, 23, 60)
		self.CVIplot2.setTitle("CVI Data",color='w')
		self.CVIplot2.setLabel('bottom',text = 'Time (seconds)')
		self.CVIplot2.setLabel('left',text = 'Y1')
		
		#Linking of two separately scaling lines in the second plot 
		self.CVIplot2line2 = ViewBox()
		#self.CVIplot2.showAxis('right')
		self.CVIplot2.scene().addItem(self.CVIplot2line2)
		self.CVIplot2.getAxis('right').linkToView(self.CVIplot2line2)
		self.CVIplot2line2.setXLink(self.CVIplot2)
		#self.CVIplot2.getAxis('right').setLabel('Y2', color = (150,150,255))#'#0000ff')
		
		#Coloring of second plot axis items
		self.CVIplot2.getAxis('left').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.CVIplot2.getAxis('bottom').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.CVIplot2.getAxis('right').setPen(pyqtgraph.mkPen(color=(0,255,0), width=3))
		
		
		#Dropdown lists for selecting data for first plot
		self.dropdownlist = QtWidgets.QComboBox(self.tab)
		self.dropdownlist.setObjectName("dropdownlist")
		self.tabLayout_1.addWidget(self.dropdownlist, 0, 40, 2, 30)

		self.dropdownlistline2 = QtWidgets.QComboBox(self.tab)
		self.dropdownlistline2.setObjectName("dropdownlistline2")
		self.tabLayout_1.addWidget(self.dropdownlistline2, 0, 70, 2, 30)
		
		#Dropdown lists for selecting data for second plot
		self.dropdownlist2 = QtWidgets.QComboBox(self.tab)
		self.dropdownlist2.setObjectName("dropdownlist2")
		self.tabLayout_1.addWidget(self.dropdownlist2, 25, 40, 2, 30)
		self.dropdownlist2line2 = QtWidgets.QComboBox(self.tab)
		self.dropdownlist2line2.setObjectName("dropdownlist2line2")
		self.tabLayout_1.addWidget(self.dropdownlist2line2, 25, 70, 2, 30)	
		
		###############################################################################
		###############################################################################		
		
				
		#Host and Port Configuration Labels and inputs
		self.dsmiplabel = QtWidgets.QLabel(self.tab_2)
		self.dsmiplabel.setObjectName("label")
		self.tabLayout_2.addWidget(self.dsmiplabel, 0, 0, 2, 10)
		self.ipaddress = QtWidgets.QLineEdit(self.tab_2)
		self.ipaddress.setObjectName("ipaddress")
		self.tabLayout_2.addWidget(self.ipaddress, 2, 0, 2, 10)
		self.ipaddress.setDisabled(True)

		self.portinlabel = QtWidgets.QLabel(self.tab_2)
		self.portinlabel.setObjectName("portinlabel")
		self.tabLayout_2.addWidget(self.portinlabel, 4, 0, 2, 10)
		self.portin = QtWidgets.QLineEdit(self.tab_2)
		self.portin.setObjectName("portin")
		self.tabLayout_2.addWidget(self.portin, 6, 0, 2, 10)
		self.portin.setDisabled(True)

		self.portoutlabel = QtWidgets.QLabel(self.tab_2)
		self.portoutlabel.setObjectName("portoutlabel")
		self.tabLayout_2.addWidget(self.portoutlabel, 8, 0, 2, 10)
		self.portout = QtWidgets.QLineEdit(self.tab_2)
		self.portout.setObjectName("portout")
		self.tabLayout_2.addWidget(self.portout, 10, 0, 2, 10)
		self.portout.setDisabled(True)
		
		#Base File Path
		self.basedirlabel = QtWidgets.QLabel(self.tab_2)
		self.basedirlabel.setObjectName("basedirlabel")
		self.tabLayout_2.addWidget(self.basedirlabel, 0, 10, 2, 10)
		self.basedirval = QtWidgets.QLineEdit(self.tab_2)
		self.basedirval.setObjectName("basedirval")
		self.tabLayout_2.addWidget(self.basedirval, 2, 10, 2, 10)
		self.basedirval.setDisabled(True)
		
		#Project specific path
		self.projectdirlabel = QtWidgets.QLabel(self.tab_2)
		self.projectdirlabel.setObjectName("projectdirlabel")
		self.tabLayout_2.addWidget(self.projectdirlabel, 4, 10, 2, 10)
		self.projectdirval = QtWidgets.QLineEdit(self.tab_2)
		self.projectdirval.setObjectName("projectdirval")
		self.tabLayout_2.addWidget(self.projectdirval, 6, 10, 2, 10)
		self.projectdirval.setDisabled(True)
		
		#Calibrations specific path
		self.caldirlabel = QtWidgets.QLabel(self.tab_2)
		self.caldirlabel.setObjectName("caldirlabel")
		self.tabLayout_2.addWidget(self.caldirlabel, 8, 10, 2, 10)
		self.caldirval = QtWidgets.QLineEdit(self.tab_2)
		self.caldirval.setObjectName("caldirval")
		self.tabLayout_2.addWidget(self.caldirval, 10, 10, 2, 10)
		self.caldirval.setDisabled(True)
	
		#Blank indicator for displaying the DSM header that is sent first upon connection
		self.dsmheaderlabel = QtWidgets.QLabel(self.tab_2)
		self.dsmheaderlabel.setObjectName("dsmheaderlabel")
		self.tabLayout_2.addWidget(self.dsmheaderlabel, 0, 20, 2, 30)
		self.dsmheader = QtWidgets.QTextBrowser(self.tab_2)#QtWidgets.QLabel(self.tab_2)
		self.dsmheader.setObjectName("dsmheader")
		self.tabLayout_2.addWidget(self.dsmheader, 2, 20, 10, 30)
		#self.dsmheader.setWordWrap(True)
		self.dsmheader.setStyleSheet("""QLabel { border: 3px inset palette(dark); 
			border-radius: 10px; background-color: white; color: #545454; }""")		
		#self.dsmheader.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.dsmheader.setAlignment(Qt.AlignTop)
		self.dsmheaderlabel.setText("DSM HEADER INFORMATION")
		
		#Text Boxes for displaying the raw data string to and from the DSM
		self.datafromdsmlabel = QtWidgets.QLabel(self.tab_2)
		self.datafromdsmlabel.setObjectName("datafromdsmlabel")
		self.tabLayout_2.addWidget(self.datafromdsmlabel, 12, 0, 2, 40)
		self.datafromdsm = QtWidgets.QTextBrowser(self.tab_2)#QtWidgets.QLabel(self.tab_2)
		self.datafromdsm.setObjectName("datafromdsm")
		self.tabLayout_2.addWidget(self.datafromdsm, 14, 0, 10, 50)
		#self.datafromdsm.setWordWrap(True)
		#self.datafromdsm.setStyleSheet("""QLabel { border: 3px inset palette(dark); 
			#border-radius: 10px; background-color: white; color: #545454; }""")
		#self.datafromdsm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.datafromdsm.setAlignment(Qt.AlignTop)


		#Error indicator for alerting if there is a problem
	#	self.errorstatus = QtWidgets.QTextBrowser()#QTextEdit()
	#	self.errorstatus.setObjectName("errorstatus")
	#	self.errorstatus.setAlignment(Qt.AlignTop)
	#	self.errorstatus.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
	#	self.errorstatus.setMinimumSize(1,1)
		#self.errorstatus.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
	#	self.tabLayout_1.addWidget(self.errorstatus,45,0,5,40)
	#	self.errorstatus.verticalScrollBar().setValue(self.mainstatus.verticalScrollBar().maximum())



		self.datatodsmlabel = QtWidgets.QLabel(self.tab_2)
		self.datatodsmlabel.setObjectName("datatodsmlabel")
		self.tabLayout_2.addWidget(self.datatodsmlabel, 24, 0, 2, 50)
		self.datatodsm = QtWidgets.QTextBrowser(self.tab_2)#QtWidgets.QLabel(self.tab_2)
		self.datatodsm.setObjectName("datafromdsm")
		self.tabLayout_2.addWidget(self.datatodsm, 26, 0, 7, 50)
		#self.datatodsm.setWordWrap(True)
		self.datatodsm.setStyleSheet("""QLabel { border: 3px inset palette(dark); 
			#border-radius: 10px; background-color: white; color: #545454; }""")		
		#self.datatodsm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.datatodsm.setAlignment(Qt.AlignTop)

		#Status indicator for server connection status
		self.statusindicatorlabel = QtWidgets.QLabel(self.tab_2)
		self.statusindicatorlabel.setObjectName("statusindicatorlabel")
		self.tabLayout_2.addWidget(self.statusindicatorlabel, 33, 0, 2, 30)

		#Toggle button/label for determining whether valves 
		#	are controlled by the user or by the calculation
		self.valvesourcelabel = QtWidgets.QLabel(self.tab_2)
		self.valvesourcelabel.setObjectName("valvesourcelabel")
		self.tabLayout_2.addWidget(self.valvesourcelabel, 35, 0, 2, 50)
		self.valvesource = QtWidgets.QPushButton(self.tab_2)
		self.valvesource.setObjectName("valvesource")
		self.tabLayout_2.addWidget(self.valvesource, 37, 0, 2, 50)
		self.valvesource.setCheckable(True)
		self.valvesourcelabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		self.valvesourcelabel.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
			
		
		#Label and checkboxes for the four manually controllable valves!
		self.v1 = QtWidgets.QPushButton(self.tab_2)
		self.v1.setObjectName("valve1")
		self.tabLayout_2.addWidget(self.v1, 39, 0, 2, 10)
		self.v2 = QtWidgets.QPushButton(self.tab_2)
		self.v2.setObjectName("valve2")
		self.tabLayout_2.addWidget(self.v2, 39, 10, 2, 10)
		self.v3 = QtWidgets.QPushButton(self.tab_2)
		self.v3.setObjectName("valve3")
		self.tabLayout_2.addWidget(self.v3, 39, 20, 2, 10)
		self.v4 = QtWidgets.QPushButton(self.tab_2)
		self.v4.setObjectName("valve4")
		self.tabLayout_2.addWidget(self.v4, 39, 30, 2, 10)
		self.v1.setCheckable(True)
		self.v2.setCheckable(True)
		self.v3.setCheckable(True)
		self.v4.setCheckable(True)
		
		#Toggle button/label for determining whether flows 
		#	are controlled by the user or by the calculation
		self.flowsourcelabel = QtWidgets.QLabel(self.tab_2)
		self.flowsourcelabel.setObjectName("flowsourcelabel")
		self.tabLayout_2.addWidget(self.flowsourcelabel, 41, 0, 2, 50)
		self.flowsource = QtWidgets.QPushButton(self.tab_2)
		self.flowsource.setObjectName("flowsource")
		self.tabLayout_2.addWidget(self.flowsource, 43, 0, 2, 50)
		self.flowsource.setCheckable(True)
		self.flowsourcelabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		
		self.flowsourcelabel.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		
		
		CVFXMIN = 0
		CVFXMAX = 50
		CVFXDIV = 10
		
		self.cvfManVoltLabels = ['cvfx0wr','cvfx2wr','cvfx3wr','cvfx4wr','cvf1wr']
		for i in range(0,len(self.cvfManVoltLabels)):
			tmpobject = QtWidgets.QLabel(self.tab_2)
			tmpobject.setObjectName(self.cvfManVoltLabels[i]+'label')
			self.tabLayout_2.addWidget(tmpobject, 45, 10*i, 1, 10)
			tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)				
			tmpobject.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
			
			tmpobject = QtWidgets.QLineEdit(self.tab_2)
			tmpobject.setObjectName(self.cvfManVoltLabels[i])
			self.tabLayout_2.addWidget(tmpobject, 46, 10*i, 2, 10)
			tmpobject.editingFinished.connect(lambda i=i: self.updateSliders(MainWindow, self.cvfManVoltLabels[i]))

			
			tmpobject = QSlider(Qt.Horizontal, self.tab_2)
			tmpobject.setMinimum(0)
			tmpobject.setMaximum(500)
			tmpobject.setValue(0)
			tmpobject.setTickPosition(QSlider.TicksBelow)
			tmpobject.setTickInterval(100)
			tmpobject.setObjectName(self.cvfManVoltLabels[i]+'Slider')
			self.tabLayout_2.addWidget(tmpobject, 48, 10*i, 2, 10)
			tmpobject.valueChanged.connect(lambda new, i=i: self.syncSliders(MainWindow, self.cvfManVoltLabels[i]))

		#Button for updating saved calibrations based on populated tables
		self.saveCals = QtWidgets.QPushButton(self.tab_2)
		self.saveCals.setObjectName("saveCals")
		self.tabLayout_2.addWidget(self.saveCals, 0, 50, 2, 50)
		
		#Refresh calibration coefficients from files
		self.refreshCals = QtWidgets.QPushButton(self.tab_2)
		self.refreshCals.setObjectName("refreshCals")
		self.tabLayout_2.addWidget(self.refreshCals, 2, 50, 2, 25)
		
		#Delete currently selected calibration coefficients
		self.deleteCals = QtWidgets.QPushButton(self.tab_2)
		self.deleteCals.setObjectName("deleteCals")
		self.tabLayout_2.addWidget(self.deleteCals, 2, 75, 2, 25)		
		
		#Dropdown menu for selecting which calibration version to use
		self.calversionlist = QtWidgets.QComboBox(self.tab_2)
		self.calversionlist.setObjectName("calversionlist")
		self.tabLayout_2.addWidget(self.calversionlist, 4, 50, 2, 50)
		
		#Create Table for MAIN Calibration Coefficients
		self.caltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.caltableWidget.setObjectName("caltableWidget")
		self.tabLayout_2.addWidget(self.caltableWidget, 6, 50, 22, 50)
		self.caltablerowlabels = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4',
			'cvfx5','cvfx6','cvfx7','cvfx8','cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai']
		self.caltablecolumnlabels = ['C0','C1','C2','UNUSED']
		self.caltableWidget.setColumnCount(len(self.caltablecolumnlabels))
		self.caltableWidget.setRowCount(len(self.caltablerowlabels))
		for i in range(0,len(self.caltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.caltableWidget.setVerticalHeaderItem(i,item)
		for i in range(0,len(self.caltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.caltableWidget.setHorizontalHeaderItem(i, item)
		for i in range(0,len(self.caltablerowlabels)):
			for j in range(0, len(self.caltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.caltableWidget.setItem(i, j, item)
				
								
		#Create Table for TDL Calibration Coefficients
		self.tdlcaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.tdlcaltableWidget.setObjectName("tdlcaltableWidget")
		self.tabLayout_2.addWidget(self.tdlcaltableWidget, 28, 50, 14, 50)
		self.tdlcaltablerowlabels = ['param_0','param_1','param_2','param_3']
		self.tdlcaltablecolumnlabels = ['TDL_C0','TDL_C1','TDL_C2','TDL_C3']
		self.tdlcaltableWidget.setColumnCount(len(self.tdlcaltablecolumnlabels))
		self.tdlcaltableWidget.setRowCount(len(self.tdlcaltablerowlabels))
		for i in range(0,len(self.tdlcaltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tdlcaltableWidget.setVerticalHeaderItem(i,item)
		for i in range(0,len(self.tdlcaltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tdlcaltableWidget.setHorizontalHeaderItem(i, item)
		for i in range(0,len(self.tdlcaltablerowlabels)):
			for j in range(0, len(self.tdlcaltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.tdlcaltableWidget.setItem(i, j, item)	
		
		#Create Table for OPC Calibration Coefficients
		self.opccaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.opccaltableWidget.setObjectName("opccaltableWidget")
		self.tabLayout_2.addWidget(self.opccaltableWidget, 42, 50, 4, 50)
		self.opccaltablerowlabels = ['OPC Pressure Cals']
		self.opccaltablecolumnlabels = ['OPC_C0','OPC_C1']
		self.opccaltableWidget.setColumnCount(len(self.opccaltablecolumnlabels))
		self.opccaltableWidget.setRowCount(len(self.opccaltablerowlabels))
		for i in range(0,len(self.opccaltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.opccaltableWidget.setVerticalHeaderItem(i,item)
		for i in range(0,len(self.opccaltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.opccaltableWidget.setHorizontalHeaderItem(i, item)
		for i in range(0,len(self.opccaltablerowlabels)):
			for j in range(0, len(self.opccaltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.opccaltableWidget.setItem(i, j, item)	
		
		#Create Table for More Calibration Coefficients
		self.morecaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.morecaltableWidget.setObjectName("morecaltableWidget")
		self.tabLayout_2.addWidget(self.morecaltableWidget, 46, 50, 4, 50)
		self.morecaltablecolumnlabels = ['RHOD','CVTBL','CVTBR','CVOFF1','LTip']
		self.morecaltablerowlabels = ['Coefficients']
		self.morecaltableWidget.setColumnCount(len(self.morecaltablecolumnlabels))
		self.morecaltableWidget.setRowCount(len(self.morecaltablerowlabels))
		for i in range(0,len(self.morecaltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.morecaltableWidget.setVerticalHeaderItem(i,item)
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.morecaltableWidget.setHorizontalHeaderItem(i, item)
		for i in range(0,len(self.morecaltablerowlabels)):
			for j in range(0, len(self.morecaltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.morecaltableWidget.setItem(i, j, item)			
		self.morecaltableWidget.verticalHeader().setVisible(False)						
		
		###############################################################################
		###############################################################################
		
		#Push buttons for connecting or disconnecting instruments
		self.devconnect = QtWidgets.QPushButton(self.tab_3)
		self.devconnect.setObjectName("devconnect")
		self.tabLayout_3.addWidget(self.devconnect, 0, 6, 3, 14)
		self.devdisconnect = QtWidgets.QPushButton(self.tab_3)
		self.devdisconnect.setObjectName("devdisconnect")
		self.tabLayout_3.addWidget(self.devdisconnect, 0, 20, 3, 14)
		
		#Text Box for displaying instructions for instrument connections
		self.devinstruct = QtWidgets.QTextBrowser(self.tab_3)#QtWidgets.QLabel(self.tab_3)
		self.devinstruct.setObjectName("devinstruct")
		self.tabLayout_3.addWidget(self.devinstruct, 12, 6, 38, 28)
		#self.devinstruct.setWordWrap(True)
		#self.devinstruct.setStyleSheet("""QLabel { border: 3px inset palette(dark); 
		#	border-radius: 10px; background-color: white; color: #545454; }""")
		self.devinstruct.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.devinstruct.setAlignment(Qt.AlignTop)		
		self.devinstruct.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))	
		self.defaultdevinstruct = "The connection and disconnection routine above is used to add or remove instrumentation from the flow. Upon either button press, counterflow will be raised and an instructional sequence will be displayed"
		self.devinstruct.setText(self.defaultdevinstruct)
		
		#Button for continuing addition/subtraction of instruments
		self.devcontinue = QtWidgets.QPushButton(self.tab_3)
		self.devcontinue.setObjectName("devcontinue")
		self.tabLayout_3.addWidget(self.devcontinue, 0, 6, 3, 14)
		self.devcontinue.hide()
		
		#Button for cancelling addition/subtraction of instruments
		self.devcancel = QtWidgets.QPushButton(self.tab_3)
		self.devcancel.setObjectName("devcancel")
		self.tabLayout_3.addWidget(self.devcancel, 0, 20, 3, 14)
		self.devcancel.hide()
					
		#USER INPUTS FOR DELAY, OFFSET, and CVF3CW
		self.delaylabel = QtWidgets.QLabel(self.tab_3)
		self.delaylabel.setObjectName("delaylabel")		
		self.tabLayout_3.addWidget(self.delaylabel, 3, 6, 2, 8)
		self.delay = QtWidgets.QLineEdit(self.tab_3)
		self.delay.setObjectName("delay")
		self.tabLayout_3.addWidget(self.delay, 5, 6, 2, 8)
		self.delaylabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		self.delay.editingFinished.connect(lambda: self.updateSliders(MainWindow, 'delay'))

		self.delaySlider = QSlider(Qt.Horizontal, self.tab_3)
		self.delaySlider.setMinimum(0)
		self.delaySlider.setMaximum(500)
		self.delaySlider.setValue(0)
		self.delaySlider.setTickPosition(QSlider.TicksBelow)
		self.delaySlider.setTickInterval(100)
		self.delaySlider.setObjectName('delaySlider')
		self.tabLayout_3.addWidget(self.delaySlider, 7, 6, 2, 8)
		self.delaySlider.valueChanged.connect(lambda: self.syncSliders(MainWindow, 'delay'))
		#tmpobject.setTracking(False)
					
		
		self.offsetlabel = QtWidgets.QLabel(self.tab_3)
		self.offsetlabel.setObjectName("offsetlabel")		
		self.tabLayout_3.addWidget(self.offsetlabel, 3, 14, 2, 8)
		self.offset = QtWidgets.QLineEdit(self.tab_3)
		self.offset.setObjectName("offset")
		self.tabLayout_3.addWidget(self.offset, 5, 14, 2, 8)
		self.offsetlabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		self.offset.editingFinished.connect(lambda: self.updateSliders(MainWindow, 'offset'))	

		self.offsetSlider = QSlider(Qt.Horizontal, self.tab_3)
		self.offsetSlider.setMinimum(0)
		self.offsetSlider.setMaximum(500)
		self.offsetSlider.setValue(0)
		self.offsetSlider.setTickPosition(QSlider.TicksBelow)
		self.offsetSlider.setTickInterval(100)
		self.offsetSlider.setObjectName('offsetSlider')
		self.tabLayout_3.addWidget(self.offsetSlider, 7, 14, 2, 8)	
		self.offsetSlider.valueChanged.connect(lambda: self.syncSliders(MainWindow, 'offset'))	

		self.cvf3cwIndicatorLabel = QtWidgets.QLabel(self.tab_3)
		self.cvf3cwIndicatorLabel.setObjectName("cvf3cwIndicatorLabel")
		self.cvf3cwIndicatorLabel.setText("Counterflow Excess")
		self.cvf3cwIndicatorLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		self.tabLayout_3.addWidget(self.cvf3cwIndicatorLabel, 3, 22, 2, 12)
		
		self.cvf3cwIndicator = QtWidgets.QLineEdit(self.tab_3)
		self.cvf3cwIndicator.setObjectName("cvf3cwIndicator")
		self.tabLayout_3.addWidget(self.cvf3cwIndicator, 5, 22, 2, 12)	
		self.cvf3cwIndicator.setDisabled(True)
		#self.cvf3cw.editingFinished.connect(lambda: self.updateSliders(MainWindow, 'cvf3cw'))	

		tmpobject = QtWidgets.QLabel(self.tab_3)
		tmpobject.setText("From Operations Tab")
		tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		self.tabLayout_3.addWidget(tmpobject, 7, 22, 2, 12)

		'''
		self.cvf3cwlabel = QtWidgets.QLabel(self.tab_3)
		self.cvf3cwlabel.setObjectName("cvf3cwlabel")		
		self.tabLayout_3.addWidget(self.cvf3cwlabel, 3, 22, 2, 12)
		self.cvf3cw = QtWidgets.QLineEdit(self.tab_3)
		self.cvf3cw.setObjectName("cvf3cw")
		self.tabLayout_3.addWidget(self.cvf3cw, 5, 22, 2, 12)	
		self.cvf3cwlabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		self.cvf3cw.editingFinished.connect(lambda: self.updateSliders(MainWindow, 'cvf3cw'))		

		self.cvf3cwSlider = QSlider(Qt.Horizontal, self.tab_3)
		self.cvf3cwSlider.setMinimum(-100)#0)
		self.cvf3cwSlider.setMaximum(500)
		self.cvf3cwSlider.setValue(0)
		self.cvf3cwSlider.setTickPosition(QSlider.TicksBelow)
		self.cvf3cwSlider.setTickInterval(100)
		self.cvf3cwSlider.setObjectName('cvf3cwSlider')
		self.tabLayout_3.addWidget(self.cvf3cwSlider, 7, 22, 2, 12)
		self.cvf3cwSlider.valueChanged.connect(lambda: self.syncSliders(MainWindow, 'cvf3cw'))
		'''	

		for i in range(1,5):
			tmpobject = QtWidgets.QPushButton(self.tab_3)
			tmpobject.setObjectName("auxdev"+str(i))
			self.tabLayout_3.addWidget(tmpobject,9,6+(i-1)*7,3,7)
			tmpobject.setStyleSheet("QPushButton {color:black; background-color:red}"
				"QPushButton:checked {color:black; background-color: lightgreen}")
			tmpobject.setCheckable(True)

		'''
		#Device toggles for selection of which instruments to add/remove
		self.auxdev1 = QtWidgets.QPushButton(self.tab_3)
		self.auxdev1.setObjectName("auxdev1")
		self.tabLayout_3.addWidget(self.auxdev1, 9, 6, 3, 7)
		self.auxdev1.setStyleSheet("QPushButton {color:black; background-color: red} QPushButton:checked {color:black; background-color: lightgreen}")
		self.auxdev1.setCheckable(True)
		self.auxdev2 = QtWidgets.QPushButton(self.tab_3)
		self.auxdev2.setObjectName("auxdev2")
		self.tabLayout_3.addWidget(self.auxdev2, 9, 13, 3, 7)
		self.auxdev2.setCheckable(True)		
		self.auxdev3 = QtWidgets.QPushButton(self.tab_3)
		self.auxdev3.setObjectName("auxdev3")
		self.tabLayout_3.addWidget(self.auxdev3, 9, 20, 3, 7)
		self.auxdev3.setCheckable(True)
		self.auxdev4 = QtWidgets.QPushButton(self.tab_3)
		self.auxdev4.setObjectName("auxdev4")
		self.tabLayout_3.addWidget(self.auxdev4, 9, 27, 3, 7)
		self.auxdev4.setCheckable(True)
		'''

		#Toggles for nulling channels
		self.signalnulls = self.caltablerowlabels
		tmpobject = QtWidgets.QLabel(self.tab_3)
		tmpobject.setObjectName("NullLabel")
		self.tabLayout_3.addWidget(tmpobject, 0, 40, 3, 10)
		tmpobject.setText("NULL SIGNALS")
		tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		
		tmpobject.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		for i in range(0,len(self.signalnulls)):
			tmpobject = QtWidgets.QLabel(self.tab_3)
			tmpobject.setObjectName("NullLabel"+str(i))
			self.tabLayout_3.addWidget(tmpobject, 3+3*i, 40, 3, 5)	
			tmpobject = QtWidgets.QPushButton(self.tab_3)
			tmpobject.setObjectName("Null"+str(i))
			self.tabLayout_3.addWidget(tmpobject, 3+3*i, 45, 3, 5)
			tmpobject.setCheckable(True)			
		
		#Label for device configurations
		tmpobject = QtWidgets.QLabel(self.tab_3)
		tmpobject.setObjectName("AuxDevLabel")
		self.tabLayout_3.addWidget(tmpobject, 0, 50, 3, 50)
		tmpobject.setText("AUXILIARY DEVICE CONFIGURATIONS")
		tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)				
		tmpobject.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		
		#Device configuration toggles and inputs
		self.auxdevtoggles = ['Flow','Data','Temp']
		self.auxdevtoggleslist = ['Label',self.auxdevtoggles[0],'FlowInput',self.auxdevtoggles[1],self.auxdevtoggles[2],'TempInput']
		for i in range(0,4):
			for j in range(0,len(self.auxdevtoggleslist)):
				if j in [0,2,5]:
					self.tmpobject = QtWidgets.QLineEdit(self.tab_3)
					self.tmpobject.setObjectName("cvfx"+str(i+5)+self.auxdevtoggleslist[j])
					self.tabLayout_3.addWidget(self.tmpobject, 3*j+3, 55+i*10, 3, 10)
				else:
					self.tmpobject = QtWidgets.QPushButton(self.tab_3)
					self.tmpobject.setObjectName("cvfx"+str(i+5)+self.auxdevtoggleslist[j])
					self.tabLayout_3.addWidget(self.tmpobject, 3*j+3, 55+i*10, 3, 10)
					self.tmpobject.setCheckable(True)

		#Text box displaying instructional interface for device configurations
		self.auxoptions = QtWidgets.QTextBrowser(self.tab_3)#QtWidgets.QLabel(self.tab_3)
		self.auxoptions.setObjectName("auxoptions")
		self.tabLayout_3.addWidget(self.auxoptions, 21, 55, 29, 40)
		#self.auxoptions.setWordWrap(True)
		#self.auxoptions.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")
		self.auxoptions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.auxoptions.setAlignment(Qt.AlignTop)		
		self.auxoptions.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))
		self.auxoptions.setText("This page is used for modifying connected instrumentation parameters and for providing a connection and disconnection routine for instrumentation during flight\n\n"+
			"The options above (in order) define the following:\n" +
			"\tLabeling: \t Way to name connected instruments\n" +
			"\tFlow Mode: \t Source of calibrated flow\n"+
			"\tData Type: \t Mass Vs. Volume Calculation\n" +
			"\tTemp Source: \t Use of CVTCN or User Input\n"+
			"\n"+
			"The Null Signals toggles to the left provide the ability to null any of the inputs so that they are not used in the flow calculation")
		
		###############################################################################
		###############################################################################
				
		#Push buttons for establishing (or cancelling) server to receive data
		self.tdlCalStart = QtWidgets.QPushButton(self.tab_4)
		self.tdlCalStart.setObjectName("tdlCalStart")
		self.tabLayout_4.addWidget(self.tdlCalStart, 0, 0, 3, 20)
		self.tdlCalCancel = QtWidgets.QPushButton(self.tab_4)
		self.tdlCalCancel.setObjectName("tdlCalCancel")
		self.tabLayout_4.addWidget(self.tdlCalCancel, 0, 20, 3, 20)	
		self.tdlCalStart.setText('Begin TDL Ramps')
		self.tdlCalCancel.setText('Cancel TDL Ramps')
		
		self.tdlCalStart.clicked.connect(lambda: self.startTDLCal(MainWindow))
		self.tdlCalCancel.clicked.connect(lambda: self.stopTDLCal(MainWindow))
		
		self.tdlCalCancel.setDisabled(True)

		self.tmpobject = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tmpobject, 3, 0, 2, 20)
		self.tmpobject.setText("Calibration Options")
		self.tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		
		self.tdlCalFlowLabel = QtWidgets.QLabel(self.tab_4)
		self.tdlCalFlowLabel.setObjectName("tdlCalFlowLabel")		
		self.tabLayout_4.addWidget(self.tdlCalFlowLabel, 5, 0, 2, 10)
		self.tdlCalFlow = QtWidgets.QLineEdit(self.tab_4)
		self.tdlCalFlow.setObjectName("tdlCalFlow")
		self.tabLayout_4.addWidget(self.tdlCalFlow, 5, 10, 2, 10)	

		self.tdlCalFlowLabel.setText("TDL Flow (Volts)")
		self.tdlCalFlow.setText('0.08')
		
		self.tdlCalRampToggle = QtWidgets.QPushButton(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampToggle, 7, 0, 3, 20)
		self.tdlCalRampToggle.setCheckable(True)
		self.tdlCalRampToggle.setText("Ramp: Calculated")
		self.tdlCalRampToggle.setObjectName("tdlCalRampToggle")
		self.tdlCalRampToggle.clicked.connect(lambda: self.tdlCalUpdateGUI(MainWindow, "tdlCalRampToggle"))
		#tmpobject.valueChanged.connect(lambda new, i=i: self.syncSliders(MainWindow, self.flowedit[i]))
		self.tdlCalRampToggle.setStyleSheet("QPushButton {color:black; background-color:red; text ='hi'}"
			"QPushButton:checked {color:black; background-color: lightgreen}")

		#tmpobject.setStyleSheet("QPushButton {color:black; background-color:red}"
		#	"QPushButton:checked {color:black; background-color: lightgreen}")
		#tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		
		self.tdlCalRampMinLabel = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampMinLabel, 10, 0, 2, 10)
		self.tdlCalRampMinLabel.setText("Initial Dew Point")
		self.tdlCalRampMin = QtWidgets.QLineEdit(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampMin, 10, 10, 2, 10)
		self.tdlCalRampMin.setText("20")
		self.tdlCalRampMin.editingFinished.connect(lambda: self.tdlCalUpdateGUI(MainWindow))

		
		self.tdlCalRampMaxLabel = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampMaxLabel, 12, 0, 2, 10)
		self.tdlCalRampMaxLabel.setText("Final Dew Point")
		self.tdlCalRampMax = QtWidgets.QLineEdit(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampMax, 12, 10, 2, 10)
		self.tdlCalRampMax.setText("0.5")
		self.tdlCalRampMax.editingFinished.connect(lambda: self.tdlCalUpdateGUI(MainWindow))
		
		self.tdlCalRampStepsLabel = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampStepsLabel, 14, 0, 2, 10)
		self.tdlCalRampStepsLabel.setText("# of Steps")
		self.tdlCalRampSteps = QtWidgets.QLineEdit(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampSteps, 14, 10, 2, 10)
		self.tdlCalRampSteps.setText("7")		
		self.tdlCalRampSteps.editingFinished.connect(lambda: self.tdlCalUpdateGUI(MainWindow))
		
		self.tdlCalRampDivToggle = QtWidgets.QPushButton(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampDivToggle, 16, 0, 3, 20)
		self.tdlCalRampDivToggle.setCheckable(True)
		self.tdlCalRampDivToggle.setText("Ramp: Linear")
		self.tdlCalRampDivToggle.setObjectName("tdlCalRampDivToggle")
		self.tdlCalRampDivToggle.clicked.connect(lambda: self.tdlCalUpdateGUI(MainWindow,"tdlCalRampDivToggle"))
		
		self.tdlCalRampTimeStepLabel = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampTimeStepLabel, 19, 0, 2, 10)
		self.tdlCalRampTimeStepLabel.setText("Time Step (min)")
		self.tdlCalRampTimeStep = QtWidgets.QLineEdit(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampTimeStep, 19, 10, 2, 10)
		self.tdlCalRampTimeStep.setText("5.0")
		self.tdlCalRampTimeStep.editingFinished.connect(lambda: self.tdlCalUpdateGUI(MainWindow))
		
		self.tdlCalRampTimeoutLabel = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampTimeoutLabel, 21, 0, 2, 10)
		self.tdlCalRampTimeoutLabel.setText("Timeout")
		self.tdlCalRampTimeout = QtWidgets.QLineEdit(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampTimeout, 21, 10, 2, 10)
		self.tdlCalRampTimeout.setText("10.0")
		self.tdlCalRampTimeout.editingFinished.connect(lambda: self.tdlCalUpdateGUI(MainWindow))
		
		self.tdlCalRampVariationLabel = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampVariationLabel, 23, 0, 2, 10)
		self.tdlCalRampVariationLabel.setText("Max Variation (C)")
		self.tdlCalRampVariation = QtWidgets.QLineEdit(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalRampVariation, 23, 10, 2, 10)
		self.tdlCalRampVariation.setText("0.01")
		self.tdlCalRampVariation.editingFinished.connect(lambda: self.tdlCalUpdateGUI(MainWindow))
		self.tdlCalRampVariation.setDisabled(True)
	
		#Status indicator for instructional display and current operation of instrument
		self.tdlCalRamp = QtWidgets.QTextBrowser(self.tab_4)#QTextEdit()
		self.tdlCalRamp.setObjectName("tdlCalRamp")
		self.tdlCalRamp.setAlignment(Qt.AlignTop)
		self.tdlCalRamp.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))
		self.tabLayout_4.addWidget(self.tdlCalRamp, 4, 20, 21, 20)
		self.tdlCalRamp.verticalScrollBar().setValue(self.mainstatus.verticalScrollBar().maximum())
		self.tdlCalRamp.setReadOnly(False)
		self.tdlCalRamp.setDisabled(True)
			
		#Create Table for TDL Calibration Coefficients
		self.tmpobject = QtWidgets.QLabel(self.tab_4)
		self.tabLayout_4.addWidget(self.tmpobject, 26, 0, 3, 40)
		self.tmpobject.setText("Derived Calibration Coefficients")
		self.tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		
		self.tdlCalSave = QtWidgets.QPushButton(self.tab_4)
		self.tabLayout_4.addWidget(self.tdlCalSave,29, 0, 3, 40)
		self.tdlCalSave.setText("Click to Transfer Coefficients to CVI Cal Files")
		self.tdlCalSave.setObjectName("tdlCalSave")
		self.tdlCalSave.clicked.connect(lambda: self.tdlCalUpdateGUI(MainWindow,"tdlCalSave"))
		self.tdlCalSave.setDisabled(True)

		
		self.tdlCalTableDerived = QtWidgets.QTableWidget(self.tab_4)
		self.tdlCalTableDerived.setObjectName("tdlCalTableDerived")
		self.tabLayout_4.addWidget(self.tdlCalTableDerived, 32, 0, 18, 40)
		self.tdlcaltablerowlabels = ['param_0','param_1','param_2','param_3']
		self.tdlcaltablecolumnlabels = ['TDL_C0','TDL_C1','TDL_C2','TDL_C3']
		self.tdlCalTableDerived.setColumnCount(len(self.tdlcaltablecolumnlabels))
		self.tdlCalTableDerived.setRowCount(len(self.tdlcaltablerowlabels))
		for i in range(0,len(self.tdlcaltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tdlCalTableDerived.setVerticalHeaderItem(i,item)
		for i in range(0,len(self.tdlcaltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tdlCalTableDerived.setHorizontalHeaderItem(i, item)
		for i in range(0,len(self.tdlcaltablerowlabels)):
			for j in range(0, len(self.tdlcaltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.tdlCalTableDerived.setItem(i, j, item)	
		
		#TDL Cal Coeffs Table
		for i in range(0,len(self.tdlcaltablerowlabels)):
			item = self.tdlCalTableDerived.verticalHeaderItem(i)
			item.setText(self.tdlcaltablerowlabels[i])
		for i in range(0,len(self.tdlcaltablecolumnlabels)):
			item = self.tdlCalTableDerived.horizontalHeaderItem(i)
			item.setText(self.tdlcaltablecolumnlabels[i])
		#__sortingEnabled = self.tdlCalTableDerived.isSortingEnabled()
		self.tdlCalTableDerived.setSortingEnabled(False)	
		
		#First Plotting Widget
		self.tdlCalPlot = PlotWidget(self.tab_4)
		self.tdlCalPlot.setObjectName("tdlCalPlot")
		self.tabLayout_4.addWidget(self.tdlCalPlot, 0, 40, 25, 60)
		self.tdlCalPlot.show()
		self.tdlCalPlot.setTitle("Dew Point Generator Set Point and Return",color='w')
		self.tdlCalPlot.setLabel('bottom',text = 'Time (seconds)')
		self.tdlCalPlot.setLabel('left',text = 'Set Dew Point')
		self.tdlCalPlot.setLabel('right',text = 'Measured Dew Point')
		
		#Linking of two separately scaling lines in the first plot
		self.tdlCalPlotline2 = ViewBox()
		#self.tdlCalPlot.showAxis('right')
		self.tdlCalPlot.scene().addItem(self.tdlCalPlotline2)
		self.tdlCalPlot.getAxis('right').linkToView(self.tdlCalPlotline2)
		self.tdlCalPlotline2.setXLink(self.tdlCalPlot)
		#self.tdlCalPlot.getAxis('right').setLabel('Y2', color = (255,150,255))#'#0000ff')

		#OLD PURPLISH COLOR  = (150,150,255)
		
		#Coloring of first plot axis items
		self.tdlCalPlot.getAxis('left').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.tdlCalPlot.getAxis('bottom').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.tdlCalPlot.getAxis('right').setPen(pyqtgraph.mkPen(color=(0,255,0), width=3))

		#Second Plotting Widget
		self.tdlCalPlot2 = PlotWidget(self.tab_4)
		self.tdlCalPlot2.setObjectName("tdlCalPlot2")
		self.tabLayout_4.addWidget(self.tdlCalPlot2, 25, 40, 25, 60)
		self.tdlCalPlot2.show()
		self.tdlCalPlot2.setTitle("TDL Signal (white), Pressure (green)",color='w')
		self.tdlCalPlot2.setLabel('bottom',text = 'Time (seconds)')
		self.tdlCalPlot2.setLabel('left',text = 'Y')
		self.tdlCalPlot2.setLabel('right',text = 'Y2')
		
		#Linking of two separately scaling lines in the second plot 
		self.tdlCalPlot2line2 = ViewBox()
		#self.tdlCalPlot2.showAxis('right')
		self.tdlCalPlot2.scene().addItem(self.tdlCalPlot2line2)
		self.tdlCalPlot2.getAxis('right').linkToView(self.tdlCalPlot2line2)
		self.tdlCalPlot2line2.setXLink(self.tdlCalPlot2)
		#self.tdlCalPlot2.getAxis('right').setLabel('Y2', color = (150,150,255))#'#0000ff')
		
		#Coloring of second plot axis items
		self.tdlCalPlot2.getAxis('left').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.tdlCalPlot2.getAxis('bottom').setPen(pyqtgraph.mkPen(color=(255,255,255), width=3))
		self.tdlCalPlot2.getAxis('right').setPen(pyqtgraph.mkPen(color=(0,255,0), width=3))
		
		self.tdlCalInProgress = False
		self.tdlCalIndex = 0
		self.tdlCalArray = []
		self.tdlCalArraySize = 0
		self.tdlCalDeviation = 0
		self.tdlTime = ''
		self.tdlData = []
		
		self.tdlCalUpdateGUI(MainWindow)
				
		###############################################################################
		###############################################################################				
		###############################################################################
		###############################################################################

		#print(MainWindow.findChildren(QWidget))
		#FORCES THE WIDGETS TO ADHERE TO CARTESIAN GRID
		for tmpobject in MainWindow.findChildren(QWidget):#QObject):
			tmpobject.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
			tmpobject.setMinimumSize(1,1)

		#VERY IMPORTANT for establishing layout to be resized
		self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		
		#Begin interface modification routine
		self.retranslateUi(MainWindow)
		
		#Connect buttons to listening loop
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "CVI Interface"))
		
		#Setting the default text of buttons and labels
		self.dsmiplabel.setText(_translate("MainWindow", "DSM IP Address"))
		self.ipaddress.setText(_translate("MainWindow", "192.168.184.145"))
		self.portin.setText(_translate("MainWindow", "30005"))
		self.portout.setText(_translate("MainWindow", "30006"))
		self.portinlabel.setText(_translate("MainWindow", "Incoming Port"))
		self.portoutlabel.setText(_translate("MainWindow", "Outgoing Port"))
		self.connect.setText(_translate("MainWindow", "Start"))
		self.disconnect.setText(_translate("MainWindow", "Stop"))
		self.datafromdsmlabel.setText(_translate("MainWindow", "Data From DSM"))
		self.datatodsmlabel.setText(_translate("MainWindow", "Data To DSM"))
		
		#Device connection button text
		self.devconnect.setText(_translate("MainWindow", "Device Connect"))
		self.devdisconnect.setText(_translate("MainWindow", "Device Disconnect"))
		self.devcontinue.setText(_translate("MainWindow", "Continue"))
		self.devcancel.setText(_translate("MainWindow", "Cancel"))
		
		#Status indicator for displaying what is working on the server/client side
		self.statusindicatorlabel.setText(_translate("MainWindow", "Status Indicator"))

		#Valve Labels
		self.v1.setText(_translate("MainWindow", "1"))
		self.v2.setText(_translate("MainWindow", "2"))
		self.v3.setText(_translate("MainWindow", "3"))
		self.v4.setText(_translate("MainWindow", "4"))
		
		#Directory labeling
		self.basedirlabel.setText(_translate("MainWindow","Base Directory"))
		self.basedirval.setText(_translate("MainWindow","C:/CVI/"))
		self.projectdirlabel.setText(_translate("MainWindow","Project Path"))
		self.projectdirval.setText(_translate("MainWindow","Testing"))
		self.caldirlabel.setText(_translate("MainWindow","Calibrations Path"))
		self.caldirval.setText(_translate("MainWindow","Calibrations"))
				
		#Current saved file labeling
		#self.currentfilelabel.setText(_translate("MainWindow","Current Saved File"))
		self.currentfile.setText(_translate("MainWindow","Waiting to save data"))
				
		#Instrument connection labels: delay, offset, counterflow excess
		self.delaylabel.setText(_translate("MainWindow","Delay"))
		self.delay.setText(_translate("MainWindow", "1"))
		self.offsetlabel.setText(_translate("MainWindow","Flow Offset"))
		self.offset.setText(_translate("MainWindow", "3"))
		self.cvf3cwlabel.setText(_translate("MainWindow", "CF_Excess"))#"Counterflow Excess"))
		self.cvf3cw.setText(_translate("MainWindow", "0.5"))
				
		#Auxiliary device labels
		#self.auxdev1.setText(_translate("MainWindow", "Dev1"))
		#self.auxdev2.setText(_translate("MainWindow", "Dev2"))
		#self.auxdev3.setText(_translate("MainWindow", "Dev3"))
		#self.auxdev4.setText(_translate("MainWindow", "Dev4"))
		for i in range(1,5):
			self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))\
				.setText(_translate("MainWindow","Dev"+str(i)))

		#Null button labels
		for i in range(0,len(self.signalnulls)):
			MainWindow.findChild(QtWidgets.QLabel,"NullLabel"+str(i)).setText(_translate("MainWindow",self.signalnulls[i]))
			MainWindow.findChild(QtWidgets.QPushButton,"Null"+str(i)).clicked.connect(lambda: self.toggleswitched(MainWindow))
	
		#Flow on off and cvi mode labels
		self.flowio.setText(_translate("MainWindow", "Flow OFF"))		
		self.cvimode.setText(_translate("MainWindow", "Mode: CVI"))

		#Valve and Flow Source Labels
		self.valvesourcelabel.setText(_translate("MainWindow","Valve Source"))
		self.flowsourcelabel.setText(_translate("MainWindow", " Flow Source"))
		
		#User selectable flow inputs and labels
		for i in range(0,len(self.cvfManVoltLabels)):
			MainWindow.findChild(QtWidgets.QLabel,self.cvfManVoltLabels[i]+'label').setText(_translate("MainWindow",self.cvfManVoltLabels[i]))
			MainWindow.findChild(QtWidgets.QLineEdit,self.cvfManVoltLabels[i]).setText(_translate("MainWindow",str(0.00)))
			self.updateSliders(MainWindow)
		
		#Initializing default internal device flow values
		#self.flowvalues = [0.00,2.00,5.00,2.00]
		for i in range(0,len(self.flowedit)):
			MainWindow.findChild(QtWidgets.QLabel,self.flowedit[i]+'label').setText(_translate("MainWindow",str(self.flowedit[i])+'c'))
		#	MainWindow.findChild(QtWidgets.QLineEdit, self.flowedit[i]).setText(_translate("MainWindow",str(self.flowvalues[i])))
		#	self.updateSliders(MainWindow)
		
		#Disabling the editability of cvfx4
		#MainWindow.findChild(QtWidgets.QLineEdit,self.flowedit[3]).setDisabled(True)
				
		#Raw input/output data fields labels
		self.datafromdsm.setText(_translate("MainWindow", "Awaiting Data to be received. . . . ."))
		self.datatodsm.setText(_translate("MainWindow", "Awaiting Data to be sent. . . . ."))

		#Plotting options
		#self.plottitles = ['H2O','ptdl','ttdl','cvf3','cvcnc1','cvcnc01','cvrho_tdl','cvrhoo_tdl','opcc','opcco']
		self.plottitles = ['H2O','ptdl','ttdl','cvf3','cvcnc1','cvcnc01','cvrho_tdl',
			'cvrhoo_tdl','opcc','opcco','cvfx5R','cvfx5c','cvts','cvtai','cvcfact']
		#self.ylabels = ['Concentration (g/m^3)','Pressure (mbar)','Temperature (C)','y','y','y','y','y','y','y']
		self.ylabels = ['Concentration (g/m^3)','Pressure (mbar)','Temperature (C)','y','y','y','y','y','y','y','y','y','y','y','y']
		self.dropdownlist.addItems(self.plottitles)
		self.dropdownlist.setCurrentIndex(7)
		self.dropdownlistline2.addItems([""]+self.plottitles)
		self.dropdownlist2.addItems(self.plottitles)
		self.dropdownlist2.setCurrentIndex(5)
		self.dropdownlist2line2.addItems([""]+self.plottitles)
		
		#Labeling Tabs on screen
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Operations"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Configuration"))
		
		#Populating tables with header information
		for i in range(0,len(self.tablerowlabels)):
			item = self.tableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tablerowlabels[i]))
		for i in range(0,len(self.tablecolumnlabels)):
			item = self.tableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tablecolumnlabels[i]))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tableWidget.setSortingEnabled(False)

		for i in range(0,len(self.rawtablerowlabels)):
			item = self.rawtableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.rawtablerowlabels[i]))
		for i in range(0,len(self.rawtablecolumnlabels)):
			item = self.rawtableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.rawtablecolumnlabels[i]))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.rawtableWidget.setSortingEnabled(False)
		
		#Cal Coeffs Table
		for i in range(0,len(self.caltablerowlabels)):
			item = self.caltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.caltablerowlabels[i]))
		for i in range(0,len(self.caltablecolumnlabels)):
			item = self.caltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.caltablecolumnlabels[i]))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.caltableWidget.setSortingEnabled(False)

		#More Cal Coeffs Table
		for i in range(0,len(self.morecaltablerowlabels)):
			item = self.morecaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.morecaltablerowlabels[i]))
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.morecaltablecolumnlabels[i]))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.morecaltableWidget.setSortingEnabled(False)
		
		#TDL Cal Coeffs Table
		for i in range(0,len(self.tdlcaltablerowlabels)):
			item = self.tdlcaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tdlcaltablerowlabels[i]))
		for i in range(0,len(self.tdlcaltablecolumnlabels)):
			item = self.tdlcaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tdlcaltablecolumnlabels[i]))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tdlcaltableWidget.setSortingEnabled(False)	
		
		#OPC Cal Coeffs Table
		for i in range(0,len(self.opccaltablerowlabels)):
			item = self.opccaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.opccaltablerowlabels[i]))
		for i in range(0,len(self.opccaltablecolumnlabels)):
			item = self.opccaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.opccaltablecolumnlabels[i]))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.opccaltableWidget.setSortingEnabled(False)
		
		#Button label for saving coefficients from tables
		self.saveCals.setText(_translate("MainWindow", "Click here to SAVE new calibrations"))
		self.refreshCals.setText(_translate("MainWindow","Reload Calibrations"))
		self.deleteCals.setText(_translate("MainWindow","Delete Currently Selected Calibration"))
		
		#Starting index for which data is plotted
		self.dropdownindices = [0,0,0,0]
		self.dropdownlist.currentIndexChanged.connect(self.CVIreplot)#self.selectionchange)
		self.dropdownlistline2.currentIndexChanged.connect(self.CVIreplot)#selectionchange)
		self.dropdownlist2.currentIndexChanged.connect(self.CVIreplot)#selectionchange)
		self.dropdownlist2line2.currentIndexChanged.connect(self.CVIreplot)#selectionchange)
		
		#Dropdown list for selecting which calibrations to use
		self.calversionlist.currentIndexChanged.connect(self.calVersionChange)#self.selectionchange)

		#connect the signal 'connect' to the slot 'connecting'
		self.connect.clicked.connect(self.connecting)
		self.disconnect.clicked.connect(self.disconnecting)
		
		#Counterflow excess to always be referenced to
		self.cfexcess = 0.5
		
		#Instrument addition/removal slots/signals
		#self.devconnect.clicked.connect(self.addinstruments)
		#self.devdisconnect.clicked.connect(self.removeinstruments)	

		self.devconnect.clicked.connect(lambda: self.devChangeRoutine(True))
		self.devdisconnect.clicked.connect(lambda: self.devChangeRoutine(False))

		
		#All calibration paramaters as their own files
		self.calarray = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4','cvfx5','cvfx6','cvfx7','cvfx8',
			'cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai',
			'RHOD','CVTBL','CVTBR','CVOFF1','LTip',
			'tdl_param_0','tdl_param_1','tdl_param_2','tdl_param_3','opc_pressure']
		self.calvalues = np.c_[[0.0]*len(self.calarray),[0.0]*len(self.calarray),[0.0]*len(self.calarray),[0.0]*len(self.calarray)]
		self.NIDASHeader = '#\n# dateFormat="%Y %b %d %H:%M:%S"\n# timeZone = "UTC"\n#'
		
		#Create filenaming structure
		self.basedir = os.path.expanduser('~/CVI/').replace("\\","/")
		self.project = 'Testing'
		self.calname = 'Calibrations'
		self.tmpfile = 'rollovervalues.txt'
		self.programdefaults = 'programdefaults.txt'
		self.path = self.basedir + '/' + self.project + '/'
		self.dataFile = time.strftime("%y%m%d%H.%Mq")
		self.errorFile = self.dataFile + '_errorlog'
		self.logFile = self.dataFile + '_log'
		
		self.tdlFile = self.dataFile + '_tdlCal'

		self.dataFile+= '_CVI.dat'
		self.errorFile+= '_CVI.dat'
		self.logFile+= '_CVI.dat'
		
		self.tdlFile+= '_CVI.dat'
		
		self.preflightPrefix = ''
						
		#Default header for file saving
		self.header = 'dsmtime, INLET, FXflows,  valve_changes, cvf1R, cvfx0R, cvfx1R, cvfx2R,  cvfx3R, cvfx4R, cvfx5R, cvfx6R, cvfx7R, cvfx8R, cvpcnR, cvttR, cvtpR, cvtsR, cvtcnR, cvtaiR, cvpcnC, cvttC, cvtpC, cvtsC, cvtcnC, cvtaiC, cvf1, cvfx0c, cvfx1c, cvfx2c,  cvfx3c, cvfx4c, cvfx5c, cvfx6c,  cvfx7c, cvfx8c, cvl, cvrhoo_tdl,   cvrho_tdl, cvrad, cvcfact_tdl,  cvf3, cvtas, cvcnc1, cvcno1, cvcfact,  cvftc, cvrh, cvdp, cvfx0WR, cvfx2WR, cvfx3WR,  cvfx4WR, cvfx1WR, cnt1, H2O_TDL,  pTDL, tTDL, TDLsignalL,TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec,TDLtrans, opcc, opcco, opcnts, opcflow, opcc_Pcor, opcco_Pcor, opcc_pres_mb'#, H2O_PIC_cvrtd, 180, HDO' #REMOVED Picarro headers
		self.header += '\n'
		
		#connect the signals/slots
		self.flowsource.clicked.connect(lambda: self.toggleswitched(MainWindow))
		self.flowio.clicked.connect(lambda: self.toggleswitched(MainWindow))
		self.cvimode.clicked.connect(lambda: self.toggleswitched(MainWindow))
		self.valvesource.clicked.connect(lambda: self.toggleswitched(MainWindow))
	
		#Disabling ability to change instrument connections without going through routine
		#self.auxdev1.setDisabled(True)
		#self.auxdev2.setDisabled(True)
		#self.auxdev3.setDisabled(True)
		#self.auxdev4.setDisabled(True)
		for i in range(1,5):
			self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i)).setDisabled(True)
		
		#Connecting signal/slots of external instrument configuration options
		for i in range(0,4):
			for j in range(0,len(self.auxdevtoggles)):
				MainWindow.findChild(QtWidgets.QPushButton,'cvfx'+str(i+5)+self.auxdevtoggles[j]).clicked.connect(lambda: self.toggleswitched(MainWindow))
				
		#Number for tracking how many times a connection or disconnection routine has been run.
		self.numchanges = 0 
				
		#Default flow values and external instrument options
		#self.flowlimits = [0]*4		
		self.cvfxoptions = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,[0]*4]
		#First index is the option, second index is the instrument
		#mode,modeval,datatype,tmpsource,tempval,i/o
		self.internalflowsetpts = [0.00]*4

		#In order of flowio, cvimode, and each of the five flows, cvfx0, cvfx2, cvfx3, cvfx4, and cvf3
		self.outputTracker = [0, False, False, 0,0,0,0,0]
		
		#Error and status lists for referencing to front panel from throughout the program
		self.mainerrorlist = ['No Errors Detected',
			'Some or all calibration coefficients have not been loaded. Perform one of the following:\n'
			+'1. Transfer correct calibration files into the calibrations path of the base directory.\n'
			+'2. Populate the calibration coefficient tables and SAVE as new calibrations.\n'
			+'3. Populate the calibration coefficient tables and run program with temporary values.\n'
			,'Some or all program defaults have not been loaded.\n'
			+'A programdefaults.txt template has been saved within the base directory.\n'
			+'Please modify the file where appropriate and restart program.\n'
			+'THIS ERROR WILL NOT BE SHOWN AGAIN\n'
			,'Error in counterflow calculations']
		
		self.mainstatuslist = ['Please read instructions before proceeding\n\n'
			+'This program provides full feedback control of the CVI. '
			+'Upon pressing start, a TCP server is established that waits for the DSM to establish a connection. '
			+'Once connected, the DSM will begin transmitting data for this program to process.\n\n'
			+'The Tabs provide functionality as follows: \n'
			+'1. The Operations tab will serve to provide primary visualization and data inputs and outputs.\n '
			+'2. The Configurations tab allows modification of calibration and startup parameters with manual valve and flow control. \n'
			+'3. The Connect Auxiliary Instruments tab provides control of external channel isntrumentation including interpretation of incoming voltages and an interface for connecting and disconnecting instruments with flow compensation.\n'
			+'\n'
			+'The general procedures for operation of the instrument are as follows:\n'
			+'1. Verify configurations are as desired and fields are populated.\n'
			+'2. Verify that the DSM has been turned on and is connected via Ethernet to the NCAR server for DSM DHCP assignment\n'
			+'3. Turn on rack mount instrumentation and CVI heaters.\n'
			+'4. Press START to allow communication with DSM.\n'
			+'5. Once valid data begins populating tables and once ready for feedback control, turn on the flow from the front panel\n'
			+'\n'
			+'At this point, the instrument should run autonomously; however, to add or remove auxiliary instrumentation, '
			+'go to the "Connect Auxiliary Instruments" tab, and use the connect or disconnect buttons to begin the connection/disconnection routine.'
			+'\n\n'
			+'Once the Start button is pressed, this instructional display will disappear and this indicator will serve as a operational status display with suggested operation instructions'
			,
			'Data are being received\n'
			,
			'Feedback data are being transmitted\n'
			,
			'Instructional message 4'
			,
			'Instructional message 5']
			
		#Setting error and main status to defaults
		self.mainstatus.setText(self.mainstatuslist[0])
		self.errorstatus.setText(self.mainerrorlist[0])
		
		#Load user option field defaults from defaults file
		self.loadprogramdefaults(MainWindow)
		
		#Full update routine for ensuring toggle text is updated
		self.toggleswitched(MainWindow)
		
		#Read calibration coefficients from file
		self.readcalsfromfiles(MainWindow)
		
		#Connect signal/slots for calibration saving
		self.saveCals.clicked.connect(lambda: self.savecalibrations(MainWindow))
		self.deleteCals.clicked.connect(lambda: self.deleteCalibrations(MainWindow))
		self.refreshCals.clicked.connect(lambda: self.readcalsfromfiles(MainWindow))
		

		self.cvpcnRunAvgArr = [np.nan]*10
		self.cvtcnRunAvgArr = [np.nan]*10
		

		self.cvpcnRunAvg = np.nan
		self.cvtcnRunAvg = np.nan


	
		#User Defined Signals
		self.dataReceived.connect(self.processData)
		self.errorSignal.connect(self.errorLog)
		self.logSignal.connect(self.mainLog)
		
		self.tdlReturn.connect(self.processTDLCal)
		
		#self.errorSignal.emit(*arg)
		
		# creates a server and starts listening to TCP connections
		self.runconnection = False
	

		self.flashTimer = QTimer()
		self.flashTimer.timeout.connect(lambda: self.flashing(MainWindow))
		self.flashTimer.start(500)	

		self.connectFlash = True

		self.timerPosition = False

		#Disabling buttons until Start button is pressed....
		self.flowio.setDisabled(True)
		self.cvimode.setDisabled(True)
		self.disconnect.setDisabled(True)

		#self.cvf3cw.setDisabled(True)
		#self.cvf3cwSlider.setDisabled(True)

		#for i in range(0,len(self.flowedit)):
		#	MainWindow.findChild(QtWidgets.QLineEdit,self.flowedit[i]).setDisabled(True)
		#	MainWindow.findChild(QtWidgets.QSlider,self.flowedit[i]+'Slider').setDisabled(True)
	
		#Create default data array for plotting from
		#self.plotdata = np.c_[[-9999]*(self.dropdownlist.count()+1)]#np.c_[[np.nan]*4]
		#self.tabledata = np.c_[[-9999]*(len(self.tablerowlabels)),[-9999]*(len(self.tablerowlabels)),[-9999]*len(self.tablerowlabels)]
		#self.rawInOutData = np.c_[[-9999]*(len(self.rawtablerowlabels)),[-9999]*(len(self.rawtablerowlabels))]
		#self.dim = self.plotdata.shape
		
		#Force selection change on the plot to the default to
		#Initialize title and axes
		#self.CVIreplot()
		
		#Create server loop
		#self.server_loop = asyncio.get_event_loop()
	
	def flashing(self, MainWindow):
		if self.timerPosition:
			if self.connectFlash:	self.connect.setStyleSheet("background-color: lightgreen")
			self.timerPosition = False

			for i in range(0,len(self.rawtablerowlabels)):
				if self.rawTableErrorTracker[i,1] == 2:
					ui.rawtableWidget.item(i,0).setBackground(QtGui.QColor(255,0,0))
					ui.rawtableWidget.item(i,1).setBackground(QtGui.QColor(255,0,0))
					#ui.rawtableWidget.item(i,1).setText(_translate("MainWindow",str(self.rawInOutData[i,1])))
					ui.rawtableWidget.verticalHeaderItem(i).setBackground(QtGui.QColor(255,0,0))

		else:
			self.connect.setStyleSheet("background-color: lightblue")
			self.timerPosition = True

			for i in range(0,len(self.rawtablerowlabels)):
				if self.rawTableErrorTracker[i,1] == 2:
					ui.rawtableWidget.item(i,0).setBackground(QtGui.QColor(1,125,125))
					ui.rawtableWidget.item(i,1).setBackground(QtGui.QColor(1,125,125))
					ui.rawtableWidget.verticalHeaderItem(i).setBackground(QtGui.QColor(1,125,125))

	
	def tdlCalUpdateGUI(self, MainWindow, widget = ''):
		try: min = float(self.tdlCalRampMin.text())
		except: 
			self.tdlCalRampMin.setText('0.0')
			min = 0.0
			
		try: max = float(self.tdlCalRampMax.text())
		except: 
			self.tdlCalRampMax.setText('20.0')
			max = 20.0
			
		try: steps = int(self.tdlCalRampSteps.text())
		except:
			self.tdlCalRampSteps.setText('10')
			steps = 10
			
		#self.tdlCalRampMin.setDisabled(True)
		#self.tdlCalRampMax.setDisabled(True)
		#self.tdlCalRampSteps.setDisabled(True)

		#self.tdlCalRampSteps = QtWidgets.QLineEdit(self.tab_4)

		#self.tdlCalRampTimeStep = QtWidgets.QLineEdit(self.tab_4)

		#self.tdlCalRampTimeout = QtWidgets.QLineEdit(self.tab_4)

		#self.tdlCalRampVariation = QtWidgets.QLineEdit(self.tab_4)
			
		#self.tdlCalRamp = QtWidgets.QTextBrowser(self.tab_4)#QTextEdit()
	
		#print('tdlCalRampToggle')
		widget = MainWindow.findChild(QtWidgets.QPushButton,'tdlCalRampToggle')
		if not self.tdlCalInProgress:
			if widget.isChecked(): 
				widget.setText('Ramp: User Defined ---->')
				self.tdlCalRampMin.setDisabled(True)
				self.tdlCalRampMax.setDisabled(True)
				self.tdlCalRampSteps.setDisabled(True)
				self.tdlCalRamp.setDisabled(False)
				self.tdlCalRampDivToggle.setDisabled(True)
			else: 
				widget.setText('Ramp: Calculated')
				self.tdlCalRampMin.setDisabled(False)
				self.tdlCalRampMax.setDisabled(False)
				self.tdlCalRampSteps.setDisabled(False)
				self.tdlCalRamp.setDisabled(True)
				self.tdlCalRampDivToggle.setDisabled(False)
		
				widget = MainWindow.findChild(QtWidgets.QPushButton,'tdlCalRampDivToggle')
				tmparray = []
				if widget.isChecked(): 
					widget.setText('Ramp: Exponential')
					#if min <= 0:
					#	min = 1
					#	steps = steps-1
					#	tmparray = ['0.0']
					#if max <= 0:
					#	max = 1
					#	steps = steps-1
					coef = np.polyfit([0,1],np.log([min,max]), 1)
					for i in np.linspace(0,1,steps):#np.arange(0,1,1/(steps-1)):
						tmparray.append(str(np.round(float(np.exp(coef[1])*np.exp(i*coef[0])),3)))
					#if max == 1:
					#	tmparray.append('0.0')
					self.tdlCalRamp.setText(', '.join(tmparray))
				else: 
					widget.setText('Ramp: Linear')
					for i in np.linspace(min,max,steps):#np.arange(min,max,(max-min)/steps):
						tmparray.append(str(np.round(float(i),3)))
					self.tdlCalRamp.setText(', '.join(tmparray))
		
		#elif widget == 'tdlCalSave':
		#	print('tdlCalSave')

			

		#tmpobject.setStyleSheet("QPushButton {color:black; background-color:red}"
		#	"QPushButton:checked {color:black; background-color: lightgreen}")
		#tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

	def startTDLCal(self,MainWindow):
		self.tdlCalArray = self.tdlCalRamp.toPlainText().replace(' ','').split(',')

		#self.tdlCalArray = list(reversed(self.tdlCalArray)) #For reversing order of array

		try: self.tdlCalArray = [float(x)/10.0 for x in self.tdlCalArray]
		except: return
		
		self.connect.click()
		
		MainWindow.findChild(QtWidgets.QSlider,self.flowedit[1]+'Slider')\
			.setValue(int(float(self.tdlCalFlow.text())*100.0))
		MainWindow.findChild(QtWidgets.QSlider,self.flowedit[0]+'Slider').setValue(0)
		MainWindow.findChild(QtWidgets.QSlider,self.flowedit[2]+'Slider').setValue(0)
		MainWindow.findChild(QtWidgets.QSlider,self.flowedit[3]+'Slider').setValue(0)
		MainWindow.findChild(QtWidgets.QSlider,'cvf3cwSlider').setValue(0)
			
		
		#MainWindow.findChild(QtWidgets.QSlider,widget+'Slider')\
		#	.setValue(int(float(MainWindow.findChild(QtWidgets.QLineEdit,widget).text())*100.0))
		#float(MainWindow.findChild(QtWidgets.QSlider, self.flowedit[i]+'Slider')\
		#				.value()/100.0)
		
		#self.tdlCalArray.extend(self.tdlCalArray[::-1]) #For appending backwards array onto end. Requires double :: for reversing
		self.tdlCalArray.extend([self.tdlCalArray[0]]) #For going back to initial step....
		self.tdlCalArraySize = len(self.tdlCalArray)
		self.tdlCalInProgress = True
		
		#Disable ALL Widgets except for cancel and plotting
		self.tdlCalRampToggle.setDisabled(True)
		self.tdlCalRampDivToggle.setDisabled(True)
		self.tdlCalRamp.setDisabled(True)
		self.tdlCalStart.setDisabled(True)
		self.tdlCalFlow.setDisabled(True)
		self.tdlCalRampMin.setDisabled(True)
		self.tdlCalRampMax.setDisabled(True)
		self.tdlCalRampSteps.setDisabled(True)
		self.tdlCalRampTimeStep.setDisabled(True)
		self.tdlCalRampTimeout.setDisabled(True)
		self.tdlCalRampVariation.setDisabled(True)
		self.tdlCalCancel.setDisabled(False)
		
		#ALSO DISABLE OTHER TABS
		
	def continueTDLCal(self,MainWindow):
		self.tdlCalStart.setText("Begin TDL Ramps")
		self.tdlCalIndex = 0
		self.tdlCalStart.setDisabled(True)
	
	def stopTDLCal(self,MainWindow):
		#Revert parameters to defaults
		self.tdlCalInProgress = False
		self.tdlCalIndex = 0
		self.tdlCalArray = []
		self.tdlCalArraySize = 0
		self.tdlCalDeviation = 0
		self.tdlTime = ''
		
		self.tdlCalUpdateGUI(MainWindow)
	
		if (self.tdlCalIndex == self.tdlCalArraySize - 1):
			self.tdlCalRampTimeStep.setText(str(float(self.tdlCalRampTimeStep.text())/2.0))
	
		self.tdlCalStart.setText("Begin TDL Ramps")
		self.tdlCalStart.disconnect()
		self.tdlCalStart.clicked.connect(lambda: self.startTDLCal(MainWindow))
		
		self.tdlCalStart.setDisabled(False)
		self.tdlCalFlow.setDisabled(False)
		self.tdlCalRampToggle.setDisabled(False)
		self.tdlCalRampTimeStep.setDisabled(False)
		self.tdlCalRampTimeout.setDisabled(False)
		self.tdlCalRampVariation.setDisabled(False)
		
		self.tdlCalCancel.setDisabled(True)
		
	#def processData(self, datain, client_sock = ''):
	def processTDLCal(self, input):
		if self.tdlTime == '':
			self.tdlTime = time.time()

		if (time.time() - self.tdlTime) >= float(self.tdlCalRampTimeStep.text())*60.0 and self.tdlCalStart.text() != "Continue TDL Cal":#self.tdlCalIndex != self.tdlCalArraySize:
			#Compute deviation of previous however many points
			#Potentially make it to where it only moves on once the standard deviation of given points does not grow?
			if 1==1:#self.tdlCalDeviation < float(self.tdlCalRampVariation.text()):
				self.tdlCalIndex+=1
				self.tdlTime = ''
		
			#Make larger time step
			if (self.tdlCalIndex == self.tdlCalArraySize - 1):
				self.tdlCalRampTimeStep.setText(str(float(self.tdlCalRampTimeStep.text())*2.0))

			#For reverting back to smaller time step
			if self.tdlCalIndex == self.tdlCalArraySize:
				self.tdlCalRampTimeStep.setText(str(float(self.tdlCalRampTimeStep.text())/2.0))
				#self.tdlCalInProgress = False
				
				#Query the to press continue or cancel for if they want to set a new pressure
				reply = QtGui.QMessageBox.warning(MainWindow, 'WARNING', \
                     "Would you like to change to a new pressure? If so, click yes, monitor pressure on plot, and then press continue", \
					 QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)#, QtGui.QMessageBox.Warning)

				if reply == QtGui.QMessageBox.Yes:	
					self.tdlCalIndex = 0
					self.tdlCalStart.setText("Continue TDL Cal")
					self.tdlCalStart.setDisabled(False)
					self.tdlCalStart.disconnect()
					self.tdlCalStart.clicked.connect(lambda: self.continueTDLCal(MainWindow))
				else:
					#If cancelled, know what to do, if 
					self.stopTDLCal(MainWindow)#self.tdlCalInProgress = False

		if self.tdlCalStart.text() == "Continue TDL Cal":
			self.tdlTime = ''

		if 	len(self.tdlData)==0:
			self.tdlData = input
		else:
			self.tdlData = np.c_[self.tdlData,input]
			#try:
			self.tdlData = np.c_[self.tdlData[:,-899:], input]
			#except:
			#	self.tdlData = np.c_[self.tdlData, newdata]
	
		tdlHeader = 'dsmtime, cvfx2wr, cvfx2R,  cvfx2wrc, cvfx2C, dewPointSet(V), dewPointRead (V), dewPointSet (C), dewPoint (C), H2O_TDL, pTDL, tTDL, TDLsignalL, TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec,TDLtrans, opcc, opcco, opcnts, opcflow, opcc_Pcor, opcco_Pcor, opcc_pres_mb'#, H2O_PIC_cvrtd, 180, HDO' #REMOVED Picarro headers
		tdlHeader += '\n'	
		
		output = np.array(input)
		output = np.around(output,decimals=5)
		saveString = list(map(str, output))
		saveString = ','.join(saveString)
		saveString += '\n'
			
		self.dataSave(3, saveString, tdlHeader)
			
		#Order is dsm time, flow set voltage, flow return voltage, flor set (real), flow return calibrated
		#	dewpoint setpoint voltage, dewpoint return voltage, dewpoint set, dewpoint return, H20 parameters...
		#ui.processTDLCal.emit(np.r_[input[0],dataout[3],input[6],self.internalFlows[2],
			#	calibrated[3],dataout[4],input[7],dataout[4]*10.0,input[7]*10.0,input[19:29])
			
		#Linking protocols for dual lines on each plot
		self.tdlCalPlotline2.setGeometry(self.tdlCalPlot.plotItem.vb.sceneBoundingRect())
		self.tdlCalPlotline2.linkedViewChanged(self.tdlCalPlot.plotItem.vb,self.tdlCalPlotline2.XAxis)
		self.tdlCalPlot2line2.setGeometry(self.tdlCalPlot2.plotItem.vb.sceneBoundingRect())
		self.tdlCalPlot2line2.linkedViewChanged(self.tdlCalPlot2.plotItem.vb,self.tdlCalPlot2line2.XAxis)

		#enableAutoRange(axis=None, enable=True, x=None, y=None)
		#self.tdlCalPlot.enableAutoRange(axis=ViewBox.XAxis)
		#self.tdlCalPlot.setMouseEnabled(x=False, y=True)
		#self.tdlCalPlot2.enableAutoRange(axis=ViewBox.XAxis)
		#self.tdlCalPlot.setMouseEnabled(x=False, y=True)		

#		if (self.dropdownlist2line2.currentIndex() != 0) : 
#			self.tdlCalPlot2.showAxis('right')
#			self.tdlCalPlot2.setTitle(self.plottitles[self.dropdownlist2.currentIndex()]+' & '+self.plottitles[self.dropdownlist2line2.currentIndex()-1])
#			self.tdlCalPlot2.getAxis('right').setLabel(self.ylabels[self.dropdownlist2line2.currentIndex()-1])#, color = (150,150,255))#'#0000ff')
		#self.tdlCalPlot2.hideAxis('right')
		
		try:
			#Update base plots based on first dropdown list positions
			self.tdlCalPlot.plot(self.tdlData[0,:], self.tdlData[7,:], clear = True,pen=pyqtgraph.mkPen(color=(255,255,255), width=1))
			self.tdlCalPlot2.plot(self.tdlData[0,:], self.tdlData[9,:], clear = True,pen=pyqtgraph.mkPen(color=(255,255,255), width=1))
			#self.tdlCalPlot2.plot(self.tdlData[0,:], np.array(self.tdlData[9,:])+np.array(self.tdlData[7,:]), clear = True,pen=pyqtgraph.mkPen(color=(255,255,255), width=1))
			self.tdlCalPlotline2.clear()
			self.tdlCalPlot2line2.clear()
		
			#Form dual lines on each plot if opted for
			self.tdlCalPlotline2.addItem(pyqtgraph.PlotCurveItem(self.tdlData[0,:], self.tdlData[8,:],clear = True,pen=pyqtgraph.mkPen(color=(0,255,0), width=1)))#,clear=True))

#			if (self.dropdownlist2line2.currentIndex() != 0) : 
#				self.tdlCalPlot2line2.addItem(pyqtgraph.PlotCurveItem(self.plotdata[0,:], self.plotdata[self.dropdownlist2line2.currentIndex(),:],clear=True,pen=pyqtgraph.mkPen(color=(0,255,0), width=1)))#,pen='b',clear=True))
		except: pass
		
		_translate = QtCore.QCoreApplication.translate

		# Fit a 3rd order, 2d polynomial
		try:
			m = self.polyfit2d(self.tdlData[10,:],self.tdlData[9,:],self.tdlData[8,:], [3,3])
			#m = self.polyfit2d(self.tdlData[10,:],np.array(self.tdlData[9,:])+np.array(self.tdlData[7,:]),self.tdlData[7,:], [3,3])
		except: pass
		#cxy where x is water dependent and y is pressure dependent
		#so 
		#= 	c00 		+ 	c01*q 		+ 	c02*q2 		+ 	c03*q3
		#+ 	c10*p 		+ 	c11*p*q 	+ 	c12*p*q2 	+	c13*p*q3
		#+	c20*p2		+	c21*p2*q	+	c22*p2*q2	+	c23*p2*q3
		#+	c30*p3		+	c31*p3*q	+	c32*p3*q2	+	c33*p3*q3
		#polyvander2d returns cij*x^i*y^j where coef is cij for i,j in matrix
		#Python uses rise over run for matrix indexing so the top row will be j0...j3
		#		corresponding to signal.... So i is pressure, j is 
		
		#Updates calibration tables for the TDL Coefficients
		computedDewPoint = []
		for i in range(0, len(self.tdlcaltablerowlabels)):
			for j in range(0,len(self.tdlcaltablecolumnlabels)):
				item = self.tdlCalTableDerived.item(i,j)
				#try:
				#	item.setText(_translate("MainWindow",str(m[i,j])))# = float(item.text())
				#except:# ValueError:
				#	item.setText(_translate("MainWindow",str(0.0)))
				try:
					#print(tdlData[10,:])
					if len(computedDewPoint)==0:
						computedDewPoint = m[i,j]*np.power(self.tdlData[10,:],i)*np.power(self.tdlData[9,:],j)
						#computedDewPoint = m[i,j]*np.power(self.tdlData[10,:],i)*np.power(np.array(self.tdlData[9,:])+np.array(self.tdlData[7,:]),j)
						#np.array(self.tdlData[10,:])+np.array(self.tdlData[7,:])/10
					else:
						computedDewPoint += m[i,j]*np.power(self.tdlData[10,:],i)*np.power(self.tdlData[9,:],j)
						#computedDewPoint += m[i,j]*np.power(self.tdlData[10,:],i)*np.power(np.array(self.tdlData[9,:])+np.array(self.tdlData[7,:]),j)

				except: pass
				
		try: 
			#self.tdlCalPlotline2.addItem(pyqtgraph.PlotCurveItem(self.tdlData[0,:], self.tdlData[8,:],clear = True,pen=pyqtgraph.mkPen(color=(0,255,0), width=1)))#,clear=True))
			#self.tdlCalPlot2line2.addItem(pyqtgraph.PlotCurveItem(self.tdlData[0,:], computedDewPoint,clear=True,pen=pyqtgraph.mkPen(color=(0,255,0), width=1)))#,pen='b',clear=True))
			self.tdlCalPlot2line2.addItem(pyqtgraph.PlotCurveItem(self.tdlData[0,:], self.tdlData[10,:],clear=True,pen=pyqtgraph.mkPen(color=(0,255,0), width=1)))#,pen='b',clear=True))
		except: pass
		
		#Force GUI to update display
		app.processEvents()


	def polyfit2d(self, x, y, f, deg):
		x = np.asarray(x)
		y = np.asarray(y)
		f = np.asarray(f)
		deg = np.asarray(deg)
		vander = polynomial.polyvander2d(x, y, deg)
		vander = vander.reshape((-1,vander.shape[-1]))
		f = f.reshape((vander.shape[0],))
		c = np.linalg.lstsq(vander, f)[0]
		return c.reshape(deg+1)
	
	def addCommonNote(self, MainWindow):
		#self.commonNoteDropdown.activated.connect(lambda: self.addCommonNote(MainWindow))
		if self.commonNoteDropdown.currentIndex() != 0:
			self.logSignal.emit(self.commonNoteDropdown.currentText())
			self.commonNoteDropdown.setCurrentIndex(0)
		
	def userNote(self, MainWindow):
		userNote, contupdate = QInputDialog.getText(MainWindow, 'Custom Note', 'Please enter a note to be added to the log file .... or press cancel')
		if contupdate:
			self.logSignal.emit(userNote)

	def preflightChecklist(self, MainWindow):
		preflighttext, contupdate = QInputDialog.getText(MainWindow, 'Updating Preflight Prefix', 'Please enter a directory prefix for the flight (e.g. RF01)')		
		if contupdate:
			self.preflightPrefix = '/'+preflighttext+'/'
		self.preflightButton.setDisabled(True)
		self.dataSave()
		
	#Old formatting code: %x %X
	#New formatting code: %H:%M:%S

	def errorLog(self, errorString):#errorCode):
		#Code for populating error status on first tab
		if self.mainerrorlist[0] in self.errorstatus.toPlainText():
			self.errorstatus.setText(time.strftime("%H:%M:%S")+' ('+str(self.outputTracker[0])+')\t'+errorString)
		else:#elif not errorString in self.errorstatus.toPlainText():#self.mainerrorlist[errorCode] in self.errorstatus.toPlainText():
			self.errorstatus.append(time.strftime("%H:%M:%S")+' ('+str(self.outputTracker[0])+')\t'+errorString)
		self.dataSave(2, time.strftime("%H:%M:%S")+' ('+str(self.outputTracker[0])+')\t'+errorString+'\n')					

	def mainLog(self, logString):#logCode):
		if self.mainstatuslist[0] in self.mainstatus.toPlainText():
			self.mainstatus.setText(time.strftime("%H:%M:%S")+' ('+str(self.outputTracker[0])+')\t'+logString+'\n')
		else:
			self.mainstatus.append(time.strftime("%H:%M:%S")+' ('+str(self.outputTracker[0])+')\t'+logString+'\n')#self.mainstatuslist[logCode])
		self.dataSave(1, time.strftime("%H:%M:%S")+' ('+str(self.outputTracker[0])+')\t'+logString+'\n')#self.mainstatuslist[logCode]+'\n')
		
	def dataSave(self, saveCode = -1, data = '', header=''):
		if saveCode == 0: saveFile = self.dataFile
		if saveCode == 1: saveFile = self.logFile
		if saveCode == 2: saveFile = self.errorFile
		if saveCode == 3: saveFile = self.tdlFile
		
		oldDir = self.basedir+'/'+self.project+'/'#+saveFile
		newDir = self.basedir+'/'+self.project+'/'+self.preflightPrefix+'/'#+saveFile
		
		oldDir = oldDir.replace('\\','/')
		newDir = newDir.replace('\\','/')
		while True:
			if oldDir.replace('//','/') == oldDir and newDir.replace('//','/') == newDir : break
			oldDir = oldDir.replace('//','/')
			newDir = newDir.replace('//','/')
		
		if (len(self.preflightPrefix) != 0):
			if not os.path.exists(os.path.dirname(newDir)):
				os.makedirs(os.path.dirname(newDir))
			if os.path.isfile(oldDir+self.dataFile):
				shutil.move(oldDir+self.dataFile,newDir+self.dataFile) #os.rename
			if os.path.isfile(oldDir+self.logFile):
				shutil.move(oldDir+self.logFile, newDir+self.logFile)
			if os.path.isfile(oldDir+self.errorFile):
				shutil.move(oldDir+self.errorFile, newDir+self.errorFile)
				
		if saveCode != -1:
			newDir = newDir + saveFile
			if not os.path.isfile(newDir):
				if not os.path.exists(os.path.dirname(newDir)):
					os.makedirs(os.path.dirname(newDir))
				if(header != ''):
					with open(newDir, 'a') as f:
						f.write(header)		
			with open(newDir,'a') as f:
				f.write(data)
			
		if saveCode == 0:
			self.currentfile.setText(str(newDir))


	def syncSliders(self, MainWindow, widget = None):
	
		if widget != None:
			MainWindow.findChild(QtWidgets.QLineEdit,widget)\
				.setText(str(MainWindow.findChild(QtWidgets.QSlider,widget+'Slider')\
				.value()/100.0))
				
		if widget == 'cvf3cw':
			MainWindow.findChild(QtWidgets.QLineEdit,widget)\
				.setText(str(MainWindow.findChild(QtWidgets.QSlider,widget+'Slider')\
				.value()/100.0))
			self.cfexcess = MainWindow.findChild(QtWidgets.QSlider,widget+'Slider').value()/100.0

			MainWindow.findChild(QtWidgets.QLineEdit,widget+'Indicator')\
				.setText(str(MainWindow.findChild(QtWidgets.QSlider,widget+'Slider')\
				.value()/100.0))

				
	def updateSliders(self, MainWindow, widget = None):
	
		if widget != None:
			try:
				MainWindow.findChild(QtWidgets.QSlider,widget+'Slider')\
					.setValue(int(float(MainWindow.findChild(QtWidgets.QLineEdit,widget).text())*100.0))
			except: pass

				
	#Function for loading program defaults from base path
	def loadprogramdefaults(self, MainWindow):
		#Checks if defaults file exists at the specified path and name
		#	If found, the program begins loading parameters, otherwise it creates a template
		#	file and displays an error message
		if not os.path.isfile(ui.basedir+ui.programdefaults):
			#self.errorLog(self.mainerrorlist[2])
			self.errorSignal.emit(self.mainerrorlist[2])
			
			#Template default file that is saved if file is not found
			inputstring = ('#\tProgram Defaults for Python Code\r\n'
				+'#\r\n'
				+'#\r\n'+'#\tDirectory for which all branching directories form (DO NOT CHANGE)\r\n'+'Base Directory: ~/CVI/\r\n'
				+'#\r\n'+'#\tA directory name which contains project data\r\n'+'Project Name: Testing\r\n'
				+'#\r\n'+'#\tA directory name which contains calibration data\r\n'+'Calibration Directory: Calibrations\r\n'
				+'#\r\n'+'#\tIP of DSM for communications FROM Laptop TO DSM\r\n'+'DSM IP Address: 192.168.184.145\r\n'
				+'#\r\n'+'#\tNetwork port for receiving data FROM DSM TO Laptop\r\n'+'Incoming Port: 30005\r\n'
				+'#\r\n'+'#\tNetwork port for sending data FROM Laptop TO DSM\r\n'+'Outgoing Port: 30006\r\n'
				+'#\r\n'+'#\tDefault valve positions (0: closed, 1: open)\r\n'+'Default Valves: 0, 0, 0, 0\r\n'
				+'#\r\n'+'#\tDefault flows for cvfx0, cvfx2, cvfx3, cvfx4\r\n'+'Default Flows: 0.0, 2.0, 5.0, 2.0\r\n'
				+'#\r\n'+'#\tValve source (0: User controlled (testing), 1: Program controlled)\r\n'+'Valve Source: 1\r\n'
				+'#\r\n'+'#\tFlow source (0: User controlled (testing), 1: Program controlled)\r\n'+'Flow Source: 1\r\n'
				+'#\r\n'+'#\tExcess flow amount to avoid pulling cabin air\r\n'+'counterflow excess: 0.5\r\n'
				+'#\r\n'+'#\tFlow offset amount before beginning instrument add/remove routine\r\n'+'flow increase amount: 3.0\r\n'
				+'#\r\n'+'#\tDelay (in seconds) after flow increase to allow system to settle\r\n'+'pause after flow increase: 1.0\r\n'
				+'#\r\n'+'#\tFlow options written in the form of: \r\n'
				+'#\t\tlabel (name of instrument)\r\n'
				+'#\t\tmode (0: User input flow, 1: calculated), \r\n'
				+'#\t\tUser Input Flow, Data Type (0: Mass, 1: Volume), \r\n'
				+'#\t\tTemperature Source (0: User Input Temp, 1: cnt1), \r\n'
				+'#\t\tUser Input Temperature\r\n'
				+'cvfx5options: WIBS, 1, 0.00, 0, 1, 20.00\r\n'
				+'cvfx6options: cvfx6, 1, 0.00, 0, 1, 20.00\r\n'
				+'cvfx7options: cvfx7, 1, 0.00, 0, 1, 20.00\r\n'
				+'cvfx8options: cvfx8, 1, 0.00, 0, 1, 20.00\r\n'
				+'#\r\n'+'#\tDefault nulls for voiding channels from flow (or other calculations) in the order:\r\n'
				+'#\t\tcvf1, cvfx0, cvfx1, cvfx2, cvfx3, cvfx4, cvfx5, cvfx6, cvfx7, cvfx8\r\n'
				+'#\t\tccvpcn, cvtt, cvtp, cvts, cvtcn, cvtai\r\n'
				+'nulls: 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0\r\n'
				)

			#Creation of directory and writing of template file
			os.makedirs(os.path.dirname(self.basedir+self.programdefaults), exist_ok=True)
			with open(self.basedir+self.programdefaults, "w") as f:
				f.write(inputstring)
				f.close()
		
		#If file has been found originally, begin loading data
		else:
			with open(ui.basedir + ui.programdefaults, "rb") as f:
				#Iterates through lines in file
				for lines in f:
					lines = lines.decode('utf-8')
					#If line does not appear to be a comment and is not empty
					#	then recognize it as a line of data
					if (lines[0] != '#' and len(lines[0].replace(" ","")) != 0) :
						#Creates and dynamically builds the array
						try: lines = lines.split(':',1)[1]
						except: pass
						while True:
							if lines.replace(" ","").replace("\n","").replace("\r","") == lines:
								break
							lines = lines.replace(" ","").replace("\n","").replace("\r","")							
						try:
							programdefaultstrings.extend([lines])
						except:
							programdefaultstrings = [lines]

			#Populates front panel and appropriate variables with default data
			#Directory and network information

			self.basedir = os.path.expanduser(programdefaultstrings[0]).replace("\\","/")
			while True:
				if self.basedir.replace("//","/") == self.basedir: break
				self.basedir = self.basedir.replace("//","/")
			self.basedirval.setText(self.basedir)
			
			self.project = programdefaultstrings[1]
			self.projectdirval.setText(self.project)
			self.calname = programdefaultstrings[2]
			self.caldirval.setText(self.calname)
			self.ipaddress.setText(programdefaultstrings[3])
			self.portin.setText(programdefaultstrings[4])
			self.portout.setText(programdefaultstrings[5])
			
			#Default valve and flow information
			self.valvepositions = programdefaultstrings[6].split(',')
			self.valvepositions = [float(x) for x in self.valvepositions]
			self.internalFlows = programdefaultstrings[7].split(',')
			self.internalFlows = [float(x) for x in self.internalFlows]
			for i in range(0,len(self.flowedit)):
				MainWindow.findChild(QtWidgets.QLineEdit,self.flowedit[i])\
					.setText(str(self.internalFlows[i]))
				MainWindow.findChild(QtWidgets.QSlider,self.flowedit[i]+'Slider')\
					.setValue(int(self.internalFlows[i]*100.0))
				
			self.valvesource.setChecked(int(programdefaultstrings[8]))
			self.flowsource.setChecked(int(programdefaultstrings[9]))

			#External instrument addition/removal parameters
			self.cvf3cw.setText(programdefaultstrings[10])
			self.cvf3cwSlider.setValue(int(float(programdefaultstrings[10])*100.0))
			self.offset.setText(programdefaultstrings[11])
			self.offsetSlider.setValue(int(float(programdefaultstrings[11])*100.0))
			self.delay.setText(programdefaultstrings[12])
			self.delaySlider.setValue(int(float(programdefaultstrings[12])*100.0))
			
			#Full external instrument configurations
			for i in range(0,4):
				for j in range(0, len(self.auxdevtoggleslist)):
					if j in [0,2,5]:
						MainWindow.findChild(QtWidgets.QLineEdit,\
							"cvfx"+str(i+5)+self.auxdevtoggleslist[j])\
							.setText(programdefaultstrings[13+i].split(',')[j])
					else:
						MainWindow.findChild(QtWidgets.QPushButton,\
							"cvfx"+str(i+5)+self.auxdevtoggleslist[j])\
							.setChecked(int(programdefaultstrings[13+i].split(',')[j]))

						
			#Null channel configurations
			for i in range(0, len(self.signalnulls)):
				MainWindow.findChild(QtWidgets.QPushButton,"Null"+str(i))\
					.setChecked(int(programdefaultstrings[17].split(',')[i]))
	
	def devChangeRoutine(self, conn,  stage = 0, canc = False):
			
		if stage == 0:

			if conn: self.logSignal.emit("Ancillary device connection routine started")
			else: self.logSignal.emit("Ancillary device disconnection routine started")

			#Increment the number of external instrument changes
			self.numchanges += 1

			#Hides original buttons to prevent redundancy
			self.devconnect.hide()
			self.devdisconnect.hide()
		
			#Disables other tabs to prevent interference
			self.tabWidget.setTabEnabled(0, False)
			self.tabWidget.setTabEnabled(1, False)
			
			#Updates temporary instrument i/o buttons with actual states, labels and colors
			for i in range(1,5):
				tmpobject = self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))
				tmpobject.setChecked(self.MainWindow.findChild(QtWidgets.QPushButton,'valve'+str(i)).isChecked())
				tmpobject.setText(self.MainWindow.findChild(QtWidgets.QLineEdit,'cvfx'+str(i+4)+'Label').text())
				#if tmpobject.isChecked(): tmpobject.setStyleSheet("background-color: green")
				#else:	tmpobject.setStyleSheet("background-color: red")

			#Stores the initial counterflow value to reference to		
			self.initialcfexcess = float(self.cvf3cwSlider.value())/100.0
		
			#Stores the initial valve positions (just in case something is cancelled)
			self.initialValvePositions = [int(self.v1.isChecked()),int(self.v2.isChecked()),int(self.v3.isChecked()),int(self.v4.isChecked())]
		
			#Offsets counterflow to allow external instrument changes
			#	This also updates a parameter that is used within a parallel
			#	routine so that it is responds to function changes
			self.cfexcess = self.initialcfexcess + float(self.offsetSlider.value())/100.0

			#Waits for specified amount of time before allowing further input
			time.sleep(float(self.delaySlider.value())/100.0)

			if conn:
				#Display instructions, force program to respond, and show continue/cancel buttons
				self.devinstruct.setText("The Counterflow has been increased... \nPlease select the instruments that are to be connected and press continue")
		
				#Need to show each of the device addition toggles (Should be hidden by default)
				for i in range(1,5):
					self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))\
						.setDisabled(False)

			else:
				#Display instructions, force program to respond, and show continue/cancel buttons
				self.devinstruct.setText("The Counterflow has been increased!\n\nAncillary valves can be switched off. \n\nPress continue once completed")

			app.processEvents()
			self.devcontinue.show()
			self.devcancel.show()

			#Link signal/slots for connect/cancel buttons
			self.devcontinue.clicked.connect(lambda: self.devChangeRoutine(conn,1))
			self.devcancel.clicked.connect(lambda: self.devChangeRoutine(conn,2,True))

		if stage == 1:
			#Disable continue button to prevent rushing program
			self.devcontinue.disconnect()
		
			#Boolean for deciding how to update the instruments.
			#	If connecting, run connection routine,
			#	otherwise, run disconnection routine
			for i in range(1,5):
				self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))\
					.setDisabled(conn)

			if(conn) :
				#Set valve positions based on selection. Emit signal for log file
				tmparr = []
				for i in range(1,5):
					tmpobject = self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))
					self.MainWindow.findChild(QtWidgets.QPushButton,'valve'+str(i)).setChecked(tmpobject.isChecked())
					#if tmpobject.isChecked():
					#	tmparr.append(str(tmpobject.text()))#+','
				
					if int(tmpobject.isChecked()) != self.initialValvePositions[i-1]: tmparr.append(str(tmpobject.text()))
				
				tmparr = ', '.join(tmparr)
				if len(tmparr) == 0: self.logSignal.emit('No valves opened')
				else:	self.logSignal.emit(tmparr+' valves opened')		


				#Wait for valves to change and then provide instructional interface
				time.sleep(3)
				self.devinstruct.setText("The CVI valves have been switched... \n\nAncillary valves can be opened. Once operators are finished, press continue")
			else: 
				#Display instructional interface
				self.devinstruct.setText("Please deselect the instruments that are to be disconnected. Then press continue and wait for flow to return to normal")

			#Force gui events to be processed and connect continue signal/slots
			app.processEvents()
			self.devcontinue.clicked.connect(lambda: self.devChangeRoutine(conn, 2))

		if stage == 2:
			#Disconnect button signal/slots to prevent rushing
			self.devcontinue.disconnect()
			self.devcancel.disconnect()

			if canc:
				self.logSignal.emit('Connection routine cancelled, valves reverting if changed')	
				for i in range(0,4):
					self.MainWindow.findChild(QtWidgets.QPushButton,'valve'+str(i+1))\
						.setChecked(self.initialValvePositions[i])
					#self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i+1))\
					#	.setChecked(self.initialValvePositions[i])

				time.sleep(3)
				self.devinstruct.setText("The valves have been reverted to their original state")
		
			#If disconnecting instruments, this is the final routine to process
			if(not conn):#connecting): 
				tmparr = []
				for i in range(1,5):
					#Disabling of temporary valve i/o toggles
					self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))\
						.setDisabled(True)
					#Updating Actual Valves
					tmpobject = self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))
					self.MainWindow.findChild(QtWidgets.QPushButton,'valve'+str(i)).setChecked(tmpobject.isChecked())
					
					if int(tmpobject.isChecked()) != self.initialValvePositions[i-1]: tmparr.append(str(tmpobject.text()))
				
				tmparr = ', '.join(tmparr)
				if len(tmparr) == 0: ui.logSignal.emit('No valves closed')
				else:	ui.logSignal.emit(tmparr+' valves closed')	

				

				#Updating actual valve controls with temporary toggles
				time.sleep(3)
			
			#ADD NONBLOCKING SLEEP TIMER FOR LOOP BELOW

			#Begin slowly stepping down the counterflow excess
			#	back to the original level to prevent flow gulps
			while self.cfexcess > self.initialcfexcess + 0.5:
				#Step down flow
				self.cfexcess = self.cfexcess - 0.5
			
				#Update instructional interface with new flow step
				#	Force gui update and pause to allow instrument response
				self.devinstruct.setText("Flow is returning to normal. \n\nDO NOT PRESS ANY BUTTONS \n  Current Flow: "+str(self.cfexcess)+"\n  Goal: "+str(self.initialcfexcess))
				app.processEvents()
				time.sleep(2)
		
			#Check to make sure flow is back to where it originally was
			#	If it is, then great; otherwise, make final step
			if self.cfexcess != self.initialcfexcess:
				#Force final step
				self.cfexcess = self.initialcfexcess	

				#Update instructional interface with new flow step
				#	Force gui update and pause to allow instrument response
				self.devinstruct.setText("Flow is returning to normal. \n\nDO NOT PRESS ANY BUTTONS \n  Current Flow: "+str(self.cfexcess)+"\n  Goal: "+str(self.initialcfexcess))
				app.processEvents()
				time.sleep(2)		
		
			#Provide final display information and allow gui to respond
			self.devinstruct.setText("Flow has returned to normal.\n\nYou may now resume normal operation")
			app.processEvents()
		
			#Disable temporary valve i/o toggles
			for i in range(1,5):
				self.MainWindow.findChild(QtWidgets.QPushButton,'auxdev'+str(i))\
					.setDisabled(True)

			ui.logSignal.emit('Ancillary valve change routine complete')
		
			#Re-enable tabs and reset buttons to original states
			self.tabWidget.setTabEnabled(0, True)
			self.tabWidget.setTabEnabled(1, True)
			self.devcontinue.hide()
			self.devcancel.hide()	
			self.devconnect.show()
			self.devdisconnect.show()
		
			#Reset instructional interface with default text
			self.devinstruct.setText(self.defaultdevinstruct)



	#Function for loading calibration coefficients from NIDAS files
	#	Will run once when the program is first started and populate
	#	all calibration tables and will carry a 3 dimensional array
	#	with each calibration versions for changing whenever
	def readcalsfromfiles(self, MainWindow):	
		self.calversionlist.clear()
		_translate = QtCore.QCoreApplication.translate
		#Defining calibration coefficients path
		self.calpath = self.basedir + '/' + self.calname + '/' 

		#Exception handling to ensure that all files are read as they should.
		#	If exception is found, an error message is presented and
		#	recommendations are made
		try:
			#Iteration through each of the known separate calibration files
			for i in range(0,len(self.calarray)):
				#Open indexed file with reference
				with open(self.calpath + self.calarray[i]+'.dat',"rb") as f:
					#Counters to determine current line in file and
					#	current number of calibration versions
					tmpcounter = 0
					calcounter = 0
					
					#Initialize array to None for temporary use				
					tmparray = None
					
					#Iterate through the lines in the file
					for lines in f:
						lines = lines.decode('utf-8')
						#If the line does not contain a comment and is not empty
						#	then proceed as if it is a calibration entry
						if (lines[0] != '#' and len(lines.replace(" ","").replace("\n","").replace("\r","")) != 0) :
							#Archive each calibration line from the file
							#	If first line, create array, otherwise
							#	add to the array
							try:
								tmparray.extend([lines])
							except:
								tmparray = [lines]
							#After archive, pull out calibration coefficients
							finally:
								calinput = lines.split()#('\t')
								calinput = [float(i) for i in calinput[-4:]]
								#Load calibration coefficients into array and extend
								#	into third dimension based on how many versions are found
								try:
									self.calvalues[i,:,calcounter] = calinput
								except:
									self.calvalues = np.repeat(self.calvalues[:, :, None], 20, axis=2)
									self.calvalues[i,:,calcounter] = calinput
								#if (i==0):	print(self.calvalues[i,:])
							#Increment counter to indicate that a new calibration version
							#	has been found
							calcounter+=1
							#Begin array for archiving version comments
							#	if i==0 ensures that this is only run for the first file
							if (i == 0):
								try:	desclist.extend([''])
								except:	desclist = ['']
						#If not a calibration coefficient data entry and not partition
						#	of the header, then archive as a version comment until new entry
						#	is found
						elif (tmpcounter>3 and i == 0):
							try:
								desclist[-1] = desclist[-1]+lines.replace("#","").replace("\r",".").replace("\n",".")
							except:
								desclist = [lines.replace("#","").replace("\r",".").replace("\n",".")]

						#Increment counter for knowing how many total lines have been read		
						tmpcounter += 1
				
			#Archive final file for retrieving time stamps
			try:
				tmptwo.extend(tmparray)
			except:
				tmptwo = tmparray

			#Add times stamps and descriptions to calibration 
			#	version selectable drop down list
			for i in range(0,len(tmptwo)):
				self.calversionlist.addItem(('Calibration Version: '+tmptwo[i].split('\t')[0]+': '+desclist[i]))
				
			#Set index of calibration version dropdown list to the
			#	most recent calibration by default. This will incite
			#	the "calVersionChange" function to populate tables
			self.calversionlist.setCurrentIndex(self.calversionlist.count()-1)
			
		#Exception throws error message and instructions to the front panel
		except:
			#self.errorLog(self.mainerrorlist[1])
			self.errorSignal.emit(self.mainerrorlist[1])

	def deleteCalibrations(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		
		#Defining calibration coefficients path
		self.calpath = self.basedir + '/' + self.calname + '/' 
 
		reply = QtGui.QMessageBox.warning(MainWindow, 'WARNING', 
                     "Are you sure you want to delete the currently selected calibration?", 
					 QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)#, QtGui.QMessageBox.Warning)

		if reply == QtGui.QMessageBox.Yes:		
			#Exception handling to ensure that all files are read as they should.
			#	If exception is found, an error message is presented and
			#	recommendations are made
			try:
				#Iteration through each of the known separate calibration files
				for i in range(0,len(self.calarray)):
					#Open indexed file with reference
					with open(self.calpath + self.calarray[i]+'.dat',"rb") as f:
						#Counters to determine current line in file and
						#	current number of calibration versions
						tmpcounter = 0
						calcounter = 0
					
						#Initialize array to for temporary use				
						tmparray = None
					
						#Iterate through the lines in the file
						for lines in f:
							#If the line does not contain a comment and is not empty
							#	then proceed as if it is a calibration entry
							lines = lines.decode('utf-8')
							if (calcounter!=self.calversionlist.currentIndex()):
								#Archive each calibration line from the file
								#	If first line, create array, otherwise
								#	add to the array
								try:
									tmparray.extend([lines.replace('\r','')])
								except:
									tmparray = [lines.replace('\r','')]
							#Increment counter to indicate that a new calibration version
							#	has been found
							if(lines[0] != '#' and len(lines.replace(" ","").replace("\n","").replace("\r","")) != 0) :
								calcounter+=1
						with open(self.calpath + self.calarray[i]+'.dat',"w+") as f:
							for lines in tmparray:
								f.write(lines)

						tmparray = None
						calcounter = 0
			
			#Exception throws error message and instructions to the front panel
			except:
				#self.errorLog(self.mainerrorlist[1])
				self.errorSignal.emit(self.mainerrorlist[1])

			self.readcalsfromfiles(MainWindow)
			
	#Function that updates calibration coefficients within the GUI tables
	def calVersionChange(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		
		#Updates calibration tables for the 16 main channels
		for i in range(0,len(self.caltablerowlabels)):
			for j in range(0, len(self.caltablecolumnlabels)):
				item = self.caltableWidget.item(i,j)
				try:
					item.setText(_translate("MainWindow","{:.5E}".format(self.calvalues[i,j,self.calversionlist.currentIndex()])))# = float(item.text())
				except ValueError:
					item.setText(_translate("MainWindow","{:.5E}".format(0.0)))
		
		#Updates calibration tables for the extra parameters
		#	RHOD, CVTBL, CVTBR, CVOFF1, LTip
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.item(0,i)
			try:
				item.setText(_translate("MainWindow","{:.5E}".format(self.calvalues[len(self.caltablerowlabels)+i,0,self.calversionlist.currentIndex()])))# = float(item.text())
			except ValueError:
				item.setText(_translate("MainWindow","{:.5E}".format(0.0)))
				
		#Updates calibration tables for the TDL Coefficients
		for i in range(0, len(self.tdlcaltablerowlabels)):
			for j in range(0,len(self.tdlcaltablecolumnlabels)):
				item = self.tdlcaltableWidget.item(i,j)
				try:
					item.setText(_translate("MainWindow","{:.5E}".format(self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels),j,self.calversionlist.currentIndex()])))# = float(item.text())
				except ValueError:
					item.setText(_translate("MainWindow","{:.5E}".format(0.0)))
			
		#Updates calibration table for the OPC Pressure calibrations
		for i in range(0, len(self.opccaltablerowlabels)):
			for j in range(0,len(self.opccaltablecolumnlabels)):
				item = self.opccaltableWidget.item(i,j)
				try:
					item.setText(_translate("MainWindow","{:.5E}".format(self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels)+len(self.tdlcaltablecolumnlabels),j,self.calversionlist.currentIndex()])))# = float(item.text())
				except ValueError:
					item.setText(_translate("MainWindow","{:.5E}".format(0.0)))
			
	#Function for updating (appending) NIDAS calibration files based on what exists
	#	within the tables on the graphical display.
	def savecalibrations(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		
		#Forming calibration data path from base path
		self.calpath = self.basedir + '/' + self.calname + '/' 

		'''
			REQUIRES UPDATE TO APPEND NEW VALUE TO CALVALUES AND DROPDOWN
		'''
		for i in range(0,len(self.caltablerowlabels)):
			for j in range(0, len(self.caltablecolumnlabels)):
				item = self.caltableWidget.item(i,j)
				try:
					self.calvalues[i,j,self.calversionlist.currentIndex()] = float(item.text())
				except ValueError:
					self.calvalues[i,j,self.calversionlist.currentIndex()] = 0.0
		
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.item(0,i)
			try:
				self.calvalues[len(self.caltablerowlabels)+i,0,self.calversionlist.currentIndex()] = float(item.text())
			except ValueError:
				self.calvalues[len(self.caltablerowlabels)+i,0,self.calversionlist.currentIndex()] = 0.0
				
		for i in range(0, len(self.tdlcaltablerowlabels)):
			for j in range(0,len(self.tdlcaltablecolumnlabels)):
				item = self.tdlcaltableWidget.item(i,j)
				try:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels),j,self.calversionlist.currentIndex()] = float(item.text())
				except ValueError:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels),j,self.calversionlist.currentIndex()] = 0
					
		for i in range(0, len(self.opccaltablerowlabels)):
			for j in range(0,len(self.opccaltablecolumnlabels)):
				item = self.opccaltableWidget.item(i,j)
				try:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels)+len(self.tdlcaltablecolumnlabels),j,self.calversionlist.currentIndex()] = float(item.text())
				except ValueError:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels)+len(self.tdlcaltablecolumnlabels),j,self.calversionlist.currentIndex()] = 0
		
		calupdatetext, contupdate = QInputDialog.getText(MainWindow, 'Updating Calibrations', 'Please provide update comment. Press cancel to abort update')		
		#If cancel is clicked, ('', False)
		
		#Checks if user chose to continue with save or not
		if contupdate:
			#Determines a timestamp of update
			caltimestamp = 	time.strftime("%Y %b %d %H:%M:%S",time.gmtime())
			#Iterates through the calibration files, formats the data
			#	And appends to each NIDAS file
			for i in range(0,len(self.calarray)):
				caloutput = [ "{:.5E}".format(x) for x in self.calvalues[i,:,self.calversionlist.currentIndex()] ]
				caloutput = '\t'.join(caloutput)
				caloutput = '\n\n# '+ str(calupdatetext) + '\n' + caltimestamp+'\t'+caloutput
				if not os.path.isfile(self.calpath+self.calarray[i]+'.dat'):
					os.makedirs(os.path.dirname(self.calpath+self.calarray[i]+'.dat'), exist_ok=True)
					with open(self.calpath+self.calarray[i]+'.dat', "w") as f:
						f.write(self.NIDASHeader)#outputstring)	
						f.write(caloutput)
						f.close()
				#If NIDAS file does not exist, it will be created.
				else:
					with open(self.calpath+self.calarray[i]+'.dat', "a") as f:
						f.write(caloutput)
						f.close()
		
		self.readcalsfromfiles(MainWindow)
			
	#Global updating function for toggles. Various toggles have different text
	#	depending on state of toggle. Therefore, whenever anything is toggled,
	#	the text will be updated for all of the toggles to ensure accuracy
	#	and to avoid many reredundant functions
	def toggleswitched(self,MainWindow):
		if self.autopilot.isChecked() : self.autopilot.setText("Autopilot: ON")
		else: self.autopilot.setText("Autopilot: OFF")
	
		if self.flowsource.isChecked() : self.flowsource.setText("Calculated")
		else: self.flowsource.setText("User Input")
		
		for i in range(0,len(self.cvfManVoltLabels)):
			MainWindow.findChild(QtWidgets.QSlider,self.cvfManVoltLabels[i]+'Slider').setDisabled(self.flowsource.isChecked())
			MainWindow.findChild(QtWidgets.QLineEdit,self.cvfManVoltLabels[i]).setDisabled(self.flowsource.isChecked())

		if self.flowio.isChecked() : 
			self.flowio.setText("Flow ON")
			self.flowio.setStyleSheet("background-color: lightgreen")
		else: 
			self.flowio.setText("Flow OFF")
			self.flowio.setStyleSheet("background-color: red")
		if self.cvimode.isChecked() : 
			self.cvimode.setText("Mode: Total")
		else: 
			self.cvimode.setText("Mode: CVI")
		if self.valvesource.isChecked(): 
			self.valvesource.setText("Calculated")
		else: 
			self.valvesource.setText("User Input")
		self.v1.setDisabled(self.valvesource.isChecked())
		self.v2.setDisabled(self.valvesource.isChecked())
		self.v3.setDisabled(self.valvesource.isChecked())
		self.v4.setDisabled(self.valvesource.isChecked())
				
		#Naming of toggles for external instruments
		self.auxdevtoggleoptions = [['Input Below', 'Mass','Input Below'],['DSM Input','Volume','cnt1']]
		for i in range(0,4):
			for j in range(0,len(self.auxdevtoggles)):
				tmpobject = MainWindow.findChild(QtWidgets.QPushButton,'cvfx'+str(i+5)+self.auxdevtoggles[j])
				if not tmpobject.isChecked(): tmpobject.setText(self.auxdevtoggles[j]+' : '+self.auxdevtoggleoptions[0][j] )
				else: tmpobject.setText(self.auxdevtoggles[j]+' : '+self.auxdevtoggleoptions[1][j] )		

		for i in range(0,len(self.signalnulls)):
			tmpobject = MainWindow.findChild(QtWidgets.QPushButton,'Null'+str(i))
			if not tmpobject.isChecked(): 
				tmpobject.setText("Active")
				tmpobject.setStyleSheet("background-color: lightgreen")
			else: 
				tmpobject.setText("Disabled")
				tmpobject.setStyleSheet("background-color: red")
			
	#Function runs when the "connect" button is clicked
	#Establishes server in separate thread for receiving data
	#	from DSM. Once established, it initializes a slot for
	#	replotting the data ~3 times a second.
	def connecting(self, MainWindow):
		#Check to make sure that connection was not attempted multiple times in succession
		#self.disconnecting(MainWindow)
		try:
			if self.runconnection:
				return
		except: pass
		
		self.statusindicatorlabel.setText("Ensuring Disconnection . . . . . . . ")
		self.statusindicatorlabel.setText("Initiating Connection . . . . . . . .")
		self.runconnection = True
		
		self.CVI_Server = QServer(self.ipaddress.text(),int(self.portin.text()),int(self.portout.text()))
		self.CVI_Server.start()
	
		#Update network status indicator
		self.statusindicatorlabel.setText("Incoming data server has been established")	
		
		#Timer for establishing plotting frequency
		#timer.timeout.connect(self.CVIreplot)
		#timer.start(300)		

	#Code run when "disconnect" button is clicked.
	#	Once clicked, server thread is joined and closed
	def disconnecting(self, MainWindow):
		if not self.runconnection :
			self.statusindicatorlabel.setText("No connection to disconnect")
		else :
			self.statusindicatorlabel.setText("Initiating Disconnect . . . . . . .")
			
			try:
				self.CVI_Server.stop()
			except: pass
		
			#Display success message
			self.statusindicatorlabel.setText("Disconnect Successful")
			self.runconnection = False
						
			self.flowio.setDisabled(True)
			self.cvimode.setDisabled(True)
			self.disconnect.setDisabled(True)
			self.connect.setDisabled(False)
			self.connectFlash = True
		
	#function for replotting the data based on which data
	#selection has been chosen
	def CVIreplot(self):	
		#Linking protocols for dual lines on each plot
		self.CVIplotline2.setGeometry(self.CVIplot.plotItem.vb.sceneBoundingRect())
		self.CVIplotline2.linkedViewChanged(self.CVIplot.plotItem.vb,self.CVIplotline2.XAxis)
		self.CVIplot2line2.setGeometry(self.CVIplot2.plotItem.vb.sceneBoundingRect())
		self.CVIplot2line2.linkedViewChanged(self.CVIplot2.plotItem.vb,self.CVIplot2line2.XAxis)

		#enableAutoRange(axis=None, enable=True, x=None, y=None)
		self.CVIplot.enableAutoRange(axis=ViewBox.XAxis)
		self.CVIplot.setMouseEnabled(x=False, y=True)
		self.CVIplot2.enableAutoRange(axis=ViewBox.XAxis)
		self.CVIplot.setMouseEnabled(x=False, y=True)		

		_translate = QtCore.QCoreApplication.translate
		#Update table in first tab displaying raw, calibrated, and crunched data
		#	for each of the 16 main input channels
		
		try:
			for i in range(0,len(self.tablerowlabels)):
				item = ui.tableWidget.item(i, 0)
				item.setText(_translate("MainWindow",str(self.tabledata[i,0])))
				item = ui.tableWidget.item(i, 1)
				item.setText(_translate("MainWindow",str(self.tabledata[i,1])))
				item = ui.tableWidget.item(i, 2)
				item.setText(_translate("MainWindow",str(self.tabledata[i,2])))
				item = ui.tableWidget.item(i, 3)
				item.setText(_translate("MainWindow",str(self.tableErrorTracker[i,0])))

			for i in range(0,len(self.rawtablerowlabels)):
				ui.rawtableWidget.item(i,0).setText(_translate("MainWindow",str(self.rawInOutData[i,0])))
				ui.rawtableWidget.item(i,1).setText(_translate("MainWindow",str(self.rawTableErrorTracker[i,0])))
				#ui.rawtableWidget.item(i,1).setText(_translate("MainWindow",str(self.rawInOutData[i,1])))
		except: pass
				
		#Set appropriate titles and axes labels
		self.CVIplot.setTitle(self.plottitles[self.dropdownlist.currentIndex()])
		self.CVIplot.setLabel('left',text = self.ylabels[self.dropdownlist.currentIndex()])
		self.CVIplot2.setTitle(self.plottitles[self.dropdownlist2.currentIndex()])
		self.CVIplot2.setLabel('left',text = self.ylabels[self.dropdownlist2.currentIndex()])

		#Form dual lines on each plot if opted for
		if (self.dropdownlistline2.currentIndex() != 0) : 
			self.CVIplot.showAxis('right')
			self.CVIplot.setTitle(self.plottitles[self.dropdownlist.currentIndex()]+' & '+self.plottitles[self.dropdownlistline2.currentIndex()-1])
			self.CVIplot.getAxis('right').setLabel(self.ylabels[self.dropdownlistline2.currentIndex()-1])#, color = (150,150,255))#'#0000ff')
		else: self.CVIplot.hideAxis('right')
		if (self.dropdownlist2line2.currentIndex() != 0) : 
			self.CVIplot2.showAxis('right')
			self.CVIplot2.setTitle(self.plottitles[self.dropdownlist2.currentIndex()]+' & '+self.plottitles[self.dropdownlist2line2.currentIndex()-1])
			self.CVIplot2.getAxis('right').setLabel(self.ylabels[self.dropdownlist2line2.currentIndex()-1])#, color = (150,150,255))#'#0000ff')
		else: self.CVIplot2.hideAxis('right')
		
		
		try:
			#Update base plots based on first dropdown list positions
			self.CVIplot.plot(self.plotdata[0,:], self.plotdata[self.dropdownlist.currentIndex()+1,:], clear = True,pen=pyqtgraph.mkPen(color=(255,255,255), width=1))
			self.CVIplot2.plot(self.plotdata[0,:], self.plotdata[self.dropdownlist2.currentIndex()+1,:], clear = True,pen=pyqtgraph.mkPen(color=(255,255,255), width=1))
			self.CVIplotline2.clear()
			self.CVIplot2line2.clear()
		
			#Form dual lines on each plot if opted for
			if (self.dropdownlistline2.currentIndex() != 0) : 
				self.CVIplotline2.addItem(pyqtgraph.PlotCurveItem(self.plotdata[0,:], self.plotdata[self.dropdownlistline2.currentIndex(),:],clear = True,pen=pyqtgraph.mkPen(color=(0,255,0), width=1)))#,clear=True))
			if (self.dropdownlist2line2.currentIndex() != 0) : 
				self.CVIplot2line2.addItem(pyqtgraph.PlotCurveItem(self.plotdata[0,:], self.plotdata[self.dropdownlist2line2.currentIndex(),:],clear=True,pen=pyqtgraph.mkPen(color=(0,255,0), width=1)))#,pen='b',clear=True))
		except: pass
		
		#Force GUI to update display
		app.processEvents()
		
		
	def processData(self, datain, client_sock = ''):
		try: self.statusindicatorlabel.setText('Data is being received from {}'.format(self.peername))
		except: pass
	
		self.flowio.setDisabled(False)
		self.cvimode.setDisabled(False)
		self.disconnect.setDisabled(False)
		self.connect.setDisabled(True)
		self.connectFlash = False

		try:	
			if datain[0] == 'N' :
				self.dsmheader.setText(str(datain))
				return
		except:	
			self.errorSignal.emit("Fatal error in trying to parse DSM header")
			return

		#Update front panel with data that has just been received
		try: 
		#	testoutput = str(datain).replace(' ','').replace('\n','').replace('\r','').split(',')
			#print(testoutput)
		#	testoutput = np.around(np.r_[testoutput],decimals=4)
		#	print(testoutput)
		#	testoutput = ', '.join(testoutput)
		#	print(testoutput)
			self.datafromdsm.setText(str(datain).replace("\n","").replace("\r","").replace(",","\t"))#str(datain).replace(",", ", "))
		except: pass
		
		#Null string just in case
		dataout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		
		#If data looks does not produce error (i.e. not a header) then proceed. 
		#	Otherwise, print header or error prone input to graphical interface
		#try: #if datain[0] != 'N' :
		calcError = False
		#NESTED TRY STATEMENTS ARE PROBLEMATIC
		#if datain[0] != 'N':
		#if datain[0] == 'N': raise Exception('This is the exception you expect to handle')

		try:
			input = datain.replace(" ","").replace("\n","").replace("\r","").split(',')
			input = [float(i) for i in input]
		except:
			self.errorSignal.emit("Fatal error in tcp string")
			return
			#	calcError = True
			#if calcError: break
		
		try:
			#self.calvalues is the array with all of the calibrations
			#	The first 16 rows contain C0, C1, C2 in their respective columns
			#	The next 5 rows contain RHOD, CVTBL, CVTBR, cvoff1, and LTip in the first column
			#	The next 4 rows contain C0, C1, C2, and C3
			C0 = np.r_[self.calvalues[:16,0,self.calversionlist.currentIndex()]]
			C1 = np.r_[self.calvalues[:16,1,self.calversionlist.currentIndex()]]
			C2 = np.r_[self.calvalues[:16,2,self.calversionlist.currentIndex()]]
			more = np.r_[self.calvalues[16:21,0,self.calversionlist.currentIndex()]]
			tdl_cals = np.c_[self.calvalues[21:25,0,self.calversionlist.currentIndex()], self.calvalues[21:25,1,self.calversionlist.currentIndex()], self.calvalues[21:25,2,self.calversionlist.currentIndex()], self.calvalues[21:25,3,self.calversionlist.currentIndex()]]
			opc_cals = np.r_[self.calvalues[25,0,self.calversionlist.currentIndex()],self.calvalues[25,1,self.calversionlist.currentIndex()]]
			tdl_cals = np.transpose(tdl_cals)
		except:
			self.errorSignal.emit("Fatal error in parsing calibration tables")
			return
				
		####MAY NEED TO TRANSPOSE TDL_CALS######
		
		#File operations for "rollover" file. File is used to carry previous data
		#	from prior program runs to replace "bad" data with previously "good" data
		try:
			if not os.path.isfile(self.basedir+self.tmpfile):
				#Formats data in a good way to be saved
				rolloverinput = input
				inputstring = [ "{:11.10g}".format(x) for x in rolloverinput ]
				inputstring = ','.join(inputstring)
				inputstring += '\n'
				#Create rollover file since it does not already exist
				os.makedirs(os.path.dirname(self.basedir+self.tmpfile), exist_ok=True)
				with open(self.basedir+self.tmpfile, "w") as f:
					f.write(inputstring)
					f.close()
			#If file already exists, grab previous data to potentially overwrite with
			else:
				with open(self.basedir + self.tmpfile, "rb") as f:
					first = f.readline()      # Read the first line.
					f.close()
				rolloverinput = first.decode('utf-8').split(',')#('\t')			
			#Format rollover data in preparation for overwriting of "bad" data
			rolloverinput = [float(x) for x in rolloverinput]
			#Conditional checks for "bad" data. If data is "bad",
			#	it is replaced with the rollover data
			for i in range(3,19):
				if input[i] <= -99: 
					input[i] = (rolloverinput[i])
					self.tableErrorTracker[i-3,0] += 1
					self.tableErrorTracker[i-3,1] = 1
					self.rawTableErrorTracker[i,0] += 1
					self.rawTableErrorTracker[i,1] = 1
				else:
					self.tableErrorTracker[i-3,0] = 0
					self.tableErrorTracker[i-3,1] = 0
					self.rawTableErrorTracker[i,0] = 0
					self.rawTableErrorTracker[i,1] = 0
			#if tdl_data <= -1, use stored value from before, except for TDLzero which if equal to -99.99, use stored value.
			#	TDL_ZERO is index 6 (index 25 of input)
			for i in [19,20,21,22,23,24,26,27,28] :
				if input[i] <= -1: 
					input[i] = (rolloverinput[i])
					self.rawTableErrorTracker[i,0] += 1
					self.rawTableErrorTracker[i,1] = 1
				else:
					self.rawTableErrorTracker[i,0] = 0
					self.rawTableErrorTracker[i,1] = 0
			if input[25] == -99.99: 
				input[25] = (rolloverinput[25])
				self.rawTableErrorTracker[25,0] += 1
				self.rawTableErrorTracker[25,1] = 1
			else:
				self.rawTableErrorTracker[25,0] = 0
				self.rawTableErrorTracker[25,1] = 0
			
			#Windspeed (WSPD) overwrite
			if input[1] < 4 or input[1] > 300 :
				input[1] = rolloverinput[1]
				self.rawTableErrorTracker[1,0] += 1
				self.rawTableErrorTracker[1,1] = 1
				if self.rawTableErrorTracker[1,0] >= 5:
					self.rawTableErrorTracker[1,1] = 2
			else:
				self.rawTableErrorTracker[0,0] = 0
				self.rawTableErrorTracker[0,1] = 0
			#Formatting corrected new data into string to be ready to 
			#	overwrite as new rollover data for future use
			rolloverinput = input
			inputstring = [ "{:11.10g}".format(x) for x in rolloverinput ]
			inputstring = ','.join(inputstring)
			inputstring += '\n'
			#Open file and write rollover data
			with open(self.basedir+self.tmpfile, "w") as f:
				f.write(inputstring)
				f.close()
		except:
			#Potentially add removal of old rollowver data to refresh
			self.errorSignal.emit("Fatal error in parsing rollover data")
			return	
			
		'''
		Code just in case we want to add a timestamp to the rollover data.
		tmptimestamp = 	time.strftime("%Y %b %d %H:%M:%S",time.gmtime())
		'''
		#Taking the null signals from the display
		nullsignals = [0]*16
		for i in range(0,len(self.signalnulls)):
			nullsignals[i] = int(self.MainWindow.findChild(QtWidgets.QPushButton,"Null"+str(i)).isChecked())

		try:
			#Taking the instrument configuration data from the display
			for i in range(0,4):
				for j in range(1,len(self.auxdevtoggleslist)):
					if j in [0,2,5]:
						tmpobject = self.MainWindow.findChild(QtWidgets.QLineEdit,'cvfx'+str(i+5)+self.auxdevtoggleslist[j])
						if tmpobject.text() != '': self.cvfxoptions[j][i] = float(tmpobject.text())
					else:
						tmpobject = self.MainWindow.findChild(QtWidgets.QPushButton,'cvfx'+str(i+5)+self.auxdevtoggleslist[j])
						self.cvfxoptions[j][i] = int(tmpobject.isChecked())
		except:
			self.errorSignal.emit("Fatal error in parsing external instrument configurations")
			return
							
		#Connection status of individual channels	
		self.cvfxoptions[0][0] = int(self.v1.isChecked())
		self.cvfxoptions[0][1] = int(self.v2.isChecked())
		self.cvfxoptions[0][2] = int(self.v3.isChecked())
		self.cvfxoptions[0][3] = int(self.v4.isChecked())

		'''
			PRIMARY COMPUTATION
		'''
		
		#############################################################################
		#############################################################################
		#############################################################################
		#########################BEGIN COMPUTATION ROUTINE###########################
		#############################################################################
		#############################################################################
		#############################################################################
			
		#OLD REFERENCE FOR WHEN COMPUTATION ROUTINE WAS SEPARATE
		#output, calibrated = cvioutput( input , self.flowlimits, self.cfexcess, self.cvfxoptions, nullsignals, self.flowio.isChecked(), self.cvimode.isChecked(), C0, C1, C2, more, tdl_cals, opc_cals)
			
		'''
		#INPUT array is of the form
		#	time, cvtas, counts, cvf1, cvfx0, cvfx1, cvfx2, cvfx3, cvfx4, 
		#	cvfx5, cvfx6, cvfx7, cvfx8, cvpcn, cvtt, cvtp, cvts, cvtcn, cvtai, 
		#	H2OR, ptdlR, ttdlR, TDLsignal, TDLlaser, TDLline, TDLzero, TTDLencl, 
		#	TTDLtec, TDLtrans, opc_cnts, opc_flow_raw, opc_pres_raw, ext1, ext2, 
		#	H2O-PIC, 18O, HDO
	
	
		#"data" and "calibrated" arrays are of the form:
		#	cvf1, cvfx0, cvfx1, cvfx2, cvfx3, cvfx4, 
		#	cvfx5, cvfx6, cvfx7, cvfx8, cvpcn, cvtt, 
		#	cvtp, cvts, cvtcn, cvtai

	
		#calcoeffs array is of the form (23 elements), parenthesis denote separate naming
		#	C0cvf1, C1cvf1, C2cvf1, C0cvfx0, C1cvfx0, C2cvfx0, 
		#	C0cvfx1, C1cvfx1, C2cvfx1, C0cvfx2, C1cvfx2, C2cvfx2, 
		#	C0cvfx3, C1cvfx3, C2cvfx3, C0cvfx4, C1cvfx4, C2cvfx4, 
		#	RHOD (rhod), CVTBL (cvtbl), CVTBR (cvtbr), CVOFF1 (cvoff1), CVOFF2 (LTip)	
	
		#tdl_data is as follows
		#	H2OR, ptdlR, ttdlR, TDLsignal, TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec, TDLtrans
	
		#opc_data is as follows:
		#	opc_cnts, opc_flow_raw, opc_pres_raw, ext1
	
		#zerocorrectedflows are the pressure and temperature corrected flows of the form.
		#	cvfx0c, cvfx1c, cvfx2c, cvfx3c, cvfx4c, 
		#	cvfx5c, cvfx6c, cvfx7c, cvfx8c, cvf1Z
		'''

		try:
			#Input values 3 -> 18 is composed of the "data" values abovei
			data = input[3:19] ; tdl_data = input[19:29] ; opc_data = input[29:33]
		
			#opc_cal input from files
			opc_press = opc_cals[0] + opc_cals[1]*opc_data[2] #opc_data[2] corresponds to opc_pres_raw	
	
			#Array to hold calibration coefficients for flows from inputs
			calcoeffs = [0]*23
			for i in range(0,6):
				calcoeffs[i*3] = C0[i]; calcoeffs[(i*3)+1] = C1[i]; calcoeffs[(i*3)+2] = C2[i]
				#clusters of three are, #c0cvf1...c2cvf1, #c0cvfx0..c2cvfx0, 
				#	.............., #c0cvfx4..c2cvfx4
		
			#Append "more" calibration coefficients to array
			#	This is RHOD, CVTBL, ...
			for i in range(18,23): calcoeffs[i] = more[i-18]
		
			#Perform default calibration of flows, pressures, temps, etc.
			calibrated = [0]*16	
			for i in range(0,16): calibrated[i] = C0[i] + C1[i]*data[i] + C2[i]*data[i]**2

	
			#cvfxtemp ~ default temps; #cvfxtempsource ~ 1 is cnt1, 0 usrinput; 
			#	cvfsw ~ is instrument connected; cvfxmode ~ 1 is calculated, 0 is usrinput;  
			#	cvfxdatatype ~ 0 is Mass, 1 is Volume; #cvfxalt ~ USER INPUT FLOWS		
			cvfxtemp = self.cvfxoptions[5][:]; cvfxtempsource = self.cvfxoptions[4][:]; cvfxsw = self.cvfxoptions[0][:]
			cvfxmode = self.cvfxoptions[1][:]; cvfxalt = self.cvfxoptions[2][:]; cvfxdatatype = self.cvfxoptions[3][:]	

			#Modifications to the flow based on if there are data, mass vs. volume input, etc.
			for i in [0,2,3]:#range(0,4): # Changed so that cvfx6 is not nulled by valve control
				if cvfxtempsource[i] == 1 : cvfxtemp[i] = calibrated[14]
				if cvfxsw[i] == 0 : calibrated[i+6] = 0
				else:
					if cvfxmode[i] == 1 : calibrated[i+6] = C0[i+6] + C1[i+6]*data[i+6] + C2[i+6]*data[i+6]**2
					else: calibrated[i+6] = cvfxalt[i] #USER ENTERED FLOW
					if cvfxdatatype[i] == 1 : calibrated[i+6] = calibrated[i+6]*(calibrated[10]/1013.23)*(294.26/(cvfxtemp[i]+273.15)) #calibrated[10] is cvpcn				


			#print(calibrated)
			#Calibration of opc_data parameters and cvfx4
			#opc_flow = C0[5] + opc_data[1]*C1[5] #opc_data[1] corresponds to opc_flow_raw	
			#calibrated[5] = opc_flow*(calibrated[10]/1013.23)*(294.26/(cvfxtemp[1]+273.15)) #cvfxtemp[i] corresponds to cvfx6temp (user input)

			calibrated[5] = C0[5]+C1[5]*data[5]+C2[5]*data[5]**2

			#For nulling of signals
			for i in range(0,16):
				if nullsignals[i] == 1: calibrated[i] = 0
	
			#H is the upper limit of airspeed, L is the lower limit
			shroud = 1; H = 300; L = 4; location = 1
	
			#Pull windspeed from dsm string
			wspd = input[1]
	
			#cvtascc appears to be the corrected total airspeed
			cvtascc = 0
	
			#If the wspd adjusted for the shroud is within the bounds of H and L
			#	then proceed with corrected total airspeed (TAS) calculation
			if shroud*location*wspd >= L and shroud*location*wspd <= H : cvtascc = shroud*location*wspd*100
		
			#Added to prevent dividing by zero
			#	NEEDS MODIFICATION TO JUST USE DEFAULT?
			if cvtascc <= 0 : cvtascc = 0.0001
	
			#Zero Corrected Flows are the flows that have been corrected for
			#	Temp and Pres AND have been filtered for values less than 0.
			zerocorrectedflows = [0]*10
	
			#Initialization of flow summing parameters
			summedzerocorrectedflow = 0; summedflow = 0	
		except: 
			self.errorSignal.emit("Fatal error in separating input data")
			return

		try:
			self.cvpcnRunAvgArr = np.roll(self.cvpcnRunAvgArr,1)
			if calibrated[10] > -99 : self.cvpcnRunAvgArr[0] = calibrated[10]
			self.cvpcnRunAvg = np.nanmean(self.cvpcnRunAvgArr)

			self.cvtcnRunAvgArr = np.roll(self.cvtcnRunAvgArr,1)
			if calibrated[14] > -99: self.cvtcnRunAvgArr[0] = calibrated[14]
			self.cvtcnRunAvg = np.nanmean(self.cvtcnRunAvgArr)

			#print(self.cvpcnRunAvgArr, self.cvtcnRunAvgArr)
		except:
			self.errorSignal.emit("NonFatal error in pressure and temperature running averages")
			self.cvpcnRunAvg = calibrated[10]
			self.cvtcnRunAvg = calibrated[14]	

	
		try:
			#Iteration of flows to correct for pressure and temperature
			#	IF the pressure is reported correctly.
			#	ALSO performs the flow summations.
			for i in range(1,10):
				#if calibrated[10] > 0 : 
				if self.cvpcnRunAvg > 0 : 
					#zerocorrectedflows[i] = ( calibrated[i]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
					zerocorrectedflows[i] = ( calibrated[i]*(1013.25/self.cvpcnRunAvg)*((self.cvtcnRunAvg+273.15)/294.26))
				else : 
					#zerocorrectedflows[i] = ( calibrated[i]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
					zerocorrectedflows[i] = ( calibrated[i]*(1013.25/0.0001)*((self.cvtcnRunAvg+273.15)/294.26))
					self.errorSignal.emit("Pressure reading invalid")
				if zerocorrectedflows[i] < 0 : zerocorrectedflows[i] = 0.0001
				summedflow = summedflow + calibrated[i]
				summedzerocorrectedflow = summedzerocorrectedflow + zerocorrectedflows[i]	
		
			#Shift in index to place cvf1c at the beginning
			#	DOES NOT REQUIRE PRESSURE AND TEMP CORRECTION
			zerocorrectedflows[0] = calibrated[0]
			if zerocorrectedflows[0] < 0 : zerocorrectedflows[0] = 0.0001

			#IF the pressure is greater than 0,
			#	THEN perform calculation of cvftc, otherwise use 0.0001 for pressure
			#if calibrated[10] > 0 : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
			#if calibrated[10] > 0 : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/cvpcnRunAvg)*((cvtcnRunAvg+273.15)/294.26))
			if self.cvpcnRunAvg > 0 : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/self.cvpcnRunAvg)*((self.cvtcnRunAvg+273.15)/294.26))
			else : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/0.0001)*((self.cvtcnRunAvg+273.15)/294.26))
			#else : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
			
		except: 
			self.errorSignal.emit("Fatal error in calibrated flow calculations")
			return

		try:
			#Calculation of the enhancement factor?
			cvcfact=(cvtascc*math.pi*(calcoeffs[20]**2))/(cvftc*1000.0/60) #calcoeffs[20] corresponds to cvtbr;
		except: 
			cvcfact = -9999

		if cvcfact<1 : 
			cvcfact=1
			self.errorSignal.emit("Enhancement factor set to 1")
	
		#cutsize (NOT SURE IF NECESSARY))
		cutsize = 0#5	
	
		try:	
			#Miscellaneous calculations, #NEEDS DEFINITIONS
			rhoa=calibrated[10]/(2870.12*(calibrated[11]+273.15)) #calibrated[10 & 11] correspond to cvpcn and cvtt respectively
			gnu=(0.0049*calibrated[11]+1.718)*0.0001
			cvrNw=cutsize*10**(-4)
			reNw=(2*cvrNw*cvtascc*rhoa)/gnu	
		except: 
			rhoa = -9999
			gnu = -9999
			cvrNw = -9999
			reNw = -9999
			self.errorSignal.emit("Nonfatal error in rhoa,gnu,cvrNw,and/or reNw Calculation")
	
		#NEEDS DEFINITIONS
		try: cvl = calcoeffs[19]*(zerocorrectedflows[0] - summedflow)/zerocorrectedflows[0]
		except: 
			cv1 = -9999
			self.errorSignal.emit("Nonfatal error in cvl calculation")
		
		#Prevent calculation of greater cut size radii
		cutsizelooplimit = 10
	
		try:
			#Code for presumably calculating cut size radius
			for cvrad in range(1,cutsizelooplimit*10+1):
				cvri=(cvrad/10)*10**(-4); rei= 2 * cvtascc * cvri * rhoa/gnu
				if rei <= 0 : rei = 0.0001
				cvli=(cvri*14.6969*calcoeffs[18] * ((0.408248*rei**(1/3)) + math.atan(2.44949*rei**(-1/3)) - 0.5*math.pi)/(3*rhoa))-calcoeffs[22]
				if cvli >= cvl:
					break
			cvrad = cvrad/10
			cvft=summedflow-calcoeffs[21]
				
		except: 
			cvri = -9999
			cvli = -9999
			cvrad = -9999
			cvft = -9999
			self.errorSignal.emit("Nonfatal error in cvrad,cvri,cvli computation")
			
		try:
			#tdl_data[1] corresponds to press, #tdl_data[2] corresponds to temp, 
			#	calcoeffs[20] corresponds to cvtbr;
			cvcfact_tdl=(cvtascc*math.pi*(calcoeffs[20]**2))/((cvft*1000.0/60)*(1013.23/tdl_data[1])*((tdl_data[2]+273.15)/294.26))
			if cvcfact_tdl<1 : cvcfact_tdl=1;
		except:
			self.errorSignal.emit("Nonfatal error in cvcfact_tdl calculation")
			cvcfact_tdl = -9999


		try:
			#calibration of tdl coefficients based on temperature and pressure
			#tdl_cals[x][y] where x is C0...C3, and y is param_0...3 (May be reversed)
			tdl_poly_coeffs = [0]*4
			tdl_poly_coeffs[0]=tdl_cals[0][0]+tdl_cals[0][1]*tdl_data[1]+tdl_cals[0][2]*tdl_data[1]*tdl_data[1]+tdl_cals[0][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			tdl_poly_coeffs[1]=tdl_cals[1][0]+tdl_cals[1][1]*tdl_data[1]+tdl_cals[1][2]*tdl_data[1]*tdl_data[1]+tdl_cals[1][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			tdl_poly_coeffs[2]=tdl_cals[2][0]+tdl_cals[2][1]*tdl_data[1]+tdl_cals[2][2]*tdl_data[1]*tdl_data[1]+tdl_cals[2][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			tdl_poly_coeffs[3]=tdl_cals[3][0]+tdl_cals[3][1]*tdl_data[1]+tdl_cals[3][2]*tdl_data[1]*tdl_data[1]+tdl_cals[3][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	
			#NEEDS DEFINITION
			cvrho_tdl=tdl_poly_coeffs[0]+tdl_poly_coeffs[1]*tdl_data[0]+tdl_poly_coeffs[2]*tdl_data[0]*tdl_data[0]+tdl_poly_coeffs[3]*tdl_data[0]*tdl_data[0]*tdl_data[0]
			RHOO_TDL=cvrho_tdl/cvcfact_tdl	
	
			#FIRST CALCULATION (CVRH just goes to output file) , 
			#	CVRH is CVI relative humidity in the TDL line
			TTDLK=tdl_data[2]+273.15
			#SATVP is saturation vapor pressure (g/m3) from Goff-Gratch and RAF Bull. 9
			SATVP=10**(23.832241-5.02808*math.log10(TTDLK)-1.3816E-7*(10**(11.334-0.0303998*TTDLK))+0+8.1328E-2*(10**(3.49149-1302.8844/TTDLK))-2949.076/TTDLK)
	
			#NEED DEFINITION
			cvrh=100*cvrho_tdl*TTDLK/(SATVP*216.68)

			#NEEDS DEFINITION
			if cvrho_tdl<=  0.0 : Z= -10
			else : Z = math.log(((tdl_data[2]+273.15))*cvrho_tdl/1322.3)

			#CVDP is CVI Dew Point, Z is intermediate variable
			cvdp = 273.0*Z/(22.51-Z) 
			
			#Indicator in LabView
			cvrhoo_tdl=cvrho_tdl/cvcfact_tdl
			if cvrhoo_tdl>50  : cvrhoo_tdl=99
			if cvrhoo_tdl<-50 : cvrhoo_tdl=-99
			
		except: 
			self.errorSignal.emit("Nonfatal error in tdl computations")
			cvrho_tdl = -9999
			TTDLK = -9999
			SATVP = -9999
			cvrh = -9999
			Z = -9999
			cvdp = -9999
			cvrhoo_tdl = -9999

		try:
			#NEEDS DEFINITION
			opc_press_mb = (opc_press*10)
			opcc = (opc_data[0]*60)/(opc_data[1]); opcc_Pcor = opcc*calibrated[10]/opc_press
			opcco = opcc/cvcfact; opcco_Pcor = opcco*calibrated[10]/opc_press
		except:
			self.errorSignal.emit("Nonfatal error in opcc calcaulations")
			opc_press_mb = -9999
			opcc = -9999
			opcc_Pcor = -9999
			opcco = -9999
			opcco_Pcor = -9999		

		try:
		#NEEDS DEFINITION
			cvf3 = calibrated[0] - summedflow
		except: 
			self.errorSignal.emit("Nonfatal error in cvf3 calculation")
			cvf3 = -9999

		try:
			#NEEDS DEFINITION
			cvcnc1 = (input[2]/(zerocorrectedflows[2]*1000/60))
			cvcnc1 = cvcnc1*math.exp(cvcnc1*zerocorrectedflows[2]*4.167*10**(-6))
	
			#NEEDS DEFINITION
			cvcnc01 = cvcnc1/cvcfact
		except: 
			self.errorSignal.emit("Nonfatal error in cvcnc01 calculation")
			cvcnc1 = -9999
			cvcnc01 = -9999
		
		try:
			#If lower <= flow <= Upper, flow set point from before, #	Otherwise, recalculate
			if self.flowio.isChecked():
				for i in range(0, len(self.flowedit)):
					self.internalFlows[i] = float(MainWindow.findChild(QtWidgets.QSlider, self.flowedit[i]+'Slider')\
						.value()/100.0)

				#Defualt flow bounds were 0.05 (i.e. self.internalFlows[i] + 0.05).
				#	These were changed to 0.01 to add more sensitivity in flow adjustments

				#print(self.internalFlows)
				if (zerocorrectedflows[1] > (self.internalFlows[0] + 0.05)) or (zerocorrectedflows[1] < (self.internalFlows[0] - 0.05)) :
					#cvfxnw = self.internalFlows[0]*(calibrated[10]/1013.25)*(294.26/(calibrated[14]+273.15))
					cvfxnw = self.internalFlows[0]*(self.cvpcnRunAvg/1013.25)*(294.26/(self.cvtcnRunAvg+273.15))
					self.internalflowsetpts[0] = (cvfxnw-calcoeffs[3])/calcoeffs[4] #will be 6 and 7 on next iteration.
				#else: #cvfxwr[0] = 0.0 #Needs to be left as older value. #Nothing is done so flow is as before.
				#Starting at cvfx2 to cvfx4 (index 2 to 3 on calibrated)
				for i in range(1,3) : # int i = 1 ; i < 4; i++ ) {
					if (zerocorrectedflows[i+2] > self.internalFlows[i] + 0.05) or (zerocorrectedflows[i+2] < self.internalFlows[i] - 0.05) :
						#cvfxnw = self.internalFlows[i] * (calibrated[10]/1013.25)*(294.26/(calibrated[14] + 273.15))
						cvfxnw = self.internalFlows[i] * (self.cvpcnRunAvg/1013.25)*(294.26/(self.cvtcnRunAvg + 273.15))
						#cvfx0wr = ( cvfxnw – c0cvfx0) / c1cvfx0;
						self.internalflowsetpts[i] = ( cvfxnw - calcoeffs[(i+2)*3] ) / calcoeffs[(i+2)*3+1] #will be 9 (12) and 10 (13) on next iteration.			
					#else : 	#cvfxwr[i] = 0.0; #REPLACE WITH OLDER VALUE
	
				if (zerocorrectedflows[5] > self.internalFlows[3] + 0.01) or (zerocorrectedflows[5] < self.internalFlows[3] - 0.01) :
					#cvfxnw = self.internalFlows[3] * (calibrated[10]/1013.25)*(294.26/(calibrated[14] + 273.15))
					cvfxnw = self.internalFlows[3] * (self.cvpcnRunAvg/1013.25)*(294.26/(self.cvtcnRunAvg + 273.15))
					#cvfx0wr = ( cvfxnw – c0cvfx0) / c1cvfx0;
					self.internalflowsetpts[3] = ( cvfxnw - calcoeffs[(5)*3] ) / calcoeffs[(5)*3+1] #will be 9 (12) and 10 (13) on next iteration.			
				#else : 	#cvfxwr[i] = 0.0; #REPLACE WITH OLDER VALUE

			else: self.internalflowsetpts = [0.00]*4

			#self.internalflowsetpts is an array to hold old values. Only changed if outside of flow margins
	
			#CVI MODE AND FLOW ON/OFF OPTIONS
			if self.flowio.isChecked() and not self.cvimode.isChecked() :
				#cfexcess_cor=self.cfexcess*(calibrated[10]/1013.25)*294.26/(calibrated[14]+273.15)
				cfexcess_cor=self.cfexcess*(self.cvpcnRunAvg/1013.25)*294.26/(self.cvtcnRunAvg+273.15)
				cfsummed=cfexcess_cor + summedflow + calcoeffs[21]# - calibrated[5]  #cvoff1 is equivalent to calcoeffs[21]
				cvf1wr=( cfsummed - calcoeffs[0])/calcoeffs[1]
				if calcoeffs[2] != 0 :
					cvf1wr = -(np.sqrt(-4*calcoeffs[2]*calcoeffs[0] + 4*calcoeffs[2]*cfsummed + calcoeffs[1]*calcoeffs[1]) + calcoeffs[1])/(2*calcoeffs[2])
					if cvf1wr < 0 or cvf1wr > 5:
						cvf1wr = (np.sqrt(-4*calcoeffs[2]*calcoeffs[0] + 4*calcoeffs[2]*cfsummed + calcoeffs[1]*calcoeffs[1]) - calcoeffs[1])/(2*calcoeffs[2])
						#print(cvf1wr)	
			else: cvf1wr = 0.0

			#Checks to make sure counterflow voltage is not greater than 5
			if cvf1wr >= 5.0 : cvf1wr = 5.0
		
		except: 
			self.errorSignal.emit("Fatal error in calculation of flow set points")
			return
			
		#try:
		#	if( input[34] != -99.99 ) : input[34] = calibrated[10]/(calibrated[14]+273.15) * 0.000217 * input[34]
		#except:	 self.errorSignal.emit("Size of array messed up")

		try:			
			#Creates large data array that will be later saved after minor updates
			output = np.r_[input[0], 0, 0, 0, input[3:19], calibrated[10:16], zerocorrectedflows[:], #ENDS AT INDEX 35, next line is 36
				cvl, cvrhoo_tdl, cvrho_tdl, cvrad, cvcfact_tdl,  #ENDS AT 40, next line 41
				cvf3, input[1], cvcnc1, cvcnc01, cvcfact,  cvftc, cvrh, cvdp, #ENDS at 48, next line 49
				self.internalflowsetpts[0:4], cvf1wr, input[2], tdl_data[:], opcc, opcco, opc_data[0:2], #Ends at 68, next line 69?
				opcc_Pcor, opcco_Pcor, opc_press_mb]#, input[34:37]] #REMOVED Picarro variables			


			#############################################################################
			#############################################################################
			#############################################################################
			###########################END COMPUTATION ROUTINE###########################
			#############################################################################
			#############################################################################
			#############################################################################


			#CVI mode indicator (0 for CVI, 1 for Total)
			output[1] = int(self.cvimode.isChecked())

			#Adjustment to parameter based on number of external
			#	instrument addition/removals have been made
			output[3] = self.numchanges

			#cvl is at index 36?, #cvf3 is at index 41, 
			#	cvfxwr0 is at index 49, #opcc_Pcor is at index 69
			flowbyte = (2*int(self.v1.isChecked()))**3+(2*int(self.v2.isChecked()))**2+(2*int(self.v3.isChecked()))**1+int(self.v4.isChecked())
			output[2] = flowbyte
		
			#FLOW OUTPUTS ARE DECIDED IN THE CONNECTION SEQUENCE
			dataout = np.round(np.r_[ output[0], output[49:54], 
				int(self.v1.isChecked()), int(self.v2.isChecked()), int(self.v3.isChecked()), int(self.v4.isChecked()), 
				int(self.cvimode.isChecked()), flowbyte, self.numchanges, 
				output[39], output[45], output[47:49], output[37] ],3)
			
			zerocorrectedflows = output[26:36]
			#calibrated = np.r_[output[26:36], output[20:26]]
			
			extra = np.r_[output[41], output[43:45], output[38], output[37], output[65:67]]
			#extra = [cvf3, cvcnc1, cvcnc01, cvrho_tdl, cvrhoo_tdl, opcc, opcco]		
			
			#Checked to see if user input or calculated mode is selected
			#	and proceed to populate output array accordingly
			#	IF FLOW IS CHECKED, THEN EVERYTHING IS CALCULATED!!!!
			if self.flowsource.isChecked():
				for i in range(0,len(self.cvfManVoltLabels)):
					MainWindow.findChild(QtWidgets.QLineEdit,self.cvfManVoltLabels[i]).setText(str(dataout[i+1]))
					MainWindow.findChild(QtWidgets.QSlider,self.cvfManVoltLabels[i]+'Slider').setValue(int(dataout[i+1]*100.0))
			else:
				for i in range(0,len(self.cvfManVoltLabels)):
					dataout[i+1] = float(MainWindow.findChild(QtWidgets.QSlider,self.cvfManVoltLabels[i]+'Slider').value())/100.0
					#else:
					#	dataout[i+1] = 0.00
			
			#Added for populating raw input/output data table
			_translate = QtCore.QCoreApplication.translate
			#for i in range(0,min(len(self.rawtablerowlabels),len(input))):
	
		except: 
			self.errorSignal.emit("Fatal error in output array parsing")
			return
			
		try:	
			if self.tdlCalInProgress:
				dataout[1] = 0.000
				dataout[2] = float(self.tdlCalFlow.text())
				dataout[3] = self.tdlCalArray[self.tdlCalIndex]#0.000#setpoint
				dataout[4] = 0.000
				dataout[5] = 0.000
				dataout[6:13] = 0
				dataout[13:] = 0.000
				#ui.processTDLCal.emit(datain, self.tcpOut)
				ui.tdlReturn.emit(np.r_[input[0],dataout[2],input[6],self.internalFlows[2],
					calibrated[3],dataout[3],input[7],dataout[3]*10.0,input[7]*10.0,input[19:29]])
					
		except: 
			self.errorSignal.emit("Fatal error in tdl calibration routine value swapping")
			return
	
		try:
			self.rawInOutData = (np.c_[input, input])
			self.rawInOutData = np.around(self.rawInOutData,decimals=3)
			for i in range(0,len(dataout)):
				self.rawInOutData[i,1] = np.around(dataout[i],decimals=3)
			for i in range(len(dataout),len(input)):
				self.rawInOutData[i,1] = np.nan
		except: 
			self.errorSignal.emit("Nonfatal error in values to front panel tables")
		
		#Sample dataout for testing
		#dataout = [dataout[0],-0.081,1.059,1.968,79.022,0.029,0,1,0,1,0,0,0,10.000,1.000,0.000,-83.974,0.000]

		#Convert array back into a byte string with an
		#	endline character
		
		try:	
			dataout = [ "{:.3f}".format(x) for x in dataout ]
			dataout = ','.join(dataout)
			dataout+='\n'			
			dataout = bytes(dataout,'utf_8')			
		except: 
			self.errorSignal.emit("Fatal error in parsing string to be sent back to dsm")
			return


		#float_formatter = lambda x: "%.3f" % x
		
		#Command formats all elements in array to a string
		#array of specified precision.
		#[ "{:0.2f}".format(elem) for elem in array ]
		#[ "{:11.5g}".format(x) for x in a ]
		
		'''
		Order of file save?
		Header = 'dsmtime, INLET, FXflows,  valve_changes, cvf1R, cvfx0R, cvfx1R, cvfx2R,  cvfx3R, cvfx4R, cvfx5R, cvfx6R, cvfx7R, cvfx8R, cvpcnR, cvttR, cvtpR, cvtsR, cvtcnR, cvtaiR, cvpcnC, cvttC, cvtpC, cvtsC, cvtcnC, cvtaiC, cvf1, cvfx0c, cvfx1c, cvfx2c,  cvfx3c, cvfx4c, cvfx5c, cvfx6c,  cvfx7c, cvfx8c, cvl, cvrhoo_tdl,   cvrho_tdl, cvrad, cvcfact_tdl,  cvf3, cvtas, cvcnc1, cvcno1, cvcfact,  cvftc, cvrh, cvdp, cvfx0WR, cvfx2WR, cvfx3WR,  cvfx4WR, cvfx1WR, cnt1, H2O_TDL,  pTDL, tTDL, TDLsignalL,TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec,TDLtrans, opcc, opcco, opcnts, opcflow, opcc_Pcor, opcco_Pcor, opcc_pres_mb, H2O_PIC_cvrtd, 180, HDO'
			
		File order sould be
		[input[0], input[3:19], calibrated[10:16], calibrated[0:10], 
			
		dsmtime, INLET, FXflows, valve_changes, 
		cvf1R, cvfx0R, cvfx1R, cvfx2R, cvfx3R, cvfx4R, cvfx5R, cvfx6R, cvfx7R, cvfx8R, cvpcnR, 
		cvttR, cvtpR, cvtsR, cvtcnR, cvtaiR, cvpcnC, cvttC, 
		cvtpC, cvtsC, cvtcnC, cvtaiC, cvf1, cvfx0c, 
		cvfx1c,	cvfx2c,	cvfx3c,	cvfx4c,	cvfx5c,	cvfx6c,	cvfx7c,	cvfx8c,	cvl, 
		cvrhoo_tdl,	cvrho_tdl, cvrad, cvcfact_tdl, cvf3, cvtas, cvcnc1, 
		cvcno1, cvcfact, cvftc, cvrh, cvdp, cvfx0WR, cvfx2WR, cvfx3WR, cvfx4WR, cvfx1WR, cnt1, 
		H2O_TDL, pTDL, tTDL, TDLsignalL, TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec, TDLtrans, 
		opcc, opcco, opcnts, opcflow, opcc_Pcor, opcco_Pcor, opcc_pres_mb, H2O_PIC_cvrtd, 180, HDO 
		'''
			
		#Send off the new data to the DSM
		#print(client_sock)
		try: 
			client_sock.send(dataout)
			self.CVI_Server.sendSuccess = True
		except: 
			self.errorSignal.emit("Failed to send feedback signal to DSM")
			#print('client socket failed')#		if client_sock != '': client_sock.send(dataout)	
			self.CVI_Server.sendSuccess = False
	
		#self.logSignal.emit('No valves closed')
		#self.outputTracker(dsmtime,flowio,cvimode,cvfx0,2,3,4,cvf3)
			
		try:
			tmpdata = [input[0], bool(self.flowio.isChecked()),bool(self.cvimode.isChecked())]
			for i in range(0,4):
				tmpdata.append(self.internalFlows[i])
			tmpdata.append(self.cfexcess)
			tmparr = []
			if self.outputTracker[1] != tmpdata[1]: 
				if tmpdata[1]: self.logSignal.emit("Flow has been turned on")
				else: self.logSignal.emit("Flow has been turned off")
			if self.outputTracker[2] != tmpdata[2]:
				if tmpdata[2]: self.logSignal.emit("CVI Mode set to Total")
				else: self.logSignal.emit("CVI Mode set to CVI")
			tmplabels = ['cvfx0','cvfx2','cvfx3','cvfx4','cvf3']
			for i in range(3,len(self.outputTracker)):
				if self.outputTracker[i] != tmpdata[i]: 
					tmparr.append(str(tmplabels[i-3])+' set to '+str(tmpdata[i])+' vlpm')
			for i in range(0,len(self.outputTracker)):
				self.outputTracker[i] = tmpdata[i]
			tmparr = ', '.join(tmparr)
			if len(tmparr)!= 0: self.logSignal.emit(str(tmparr))
		
		except: 
			self.errorSignal.emit("Nonfatal error in deducing prior state of toggles")
		
		try:								
			#Update front panel with data sent to dsm
			self.datatodsm.setText(str(dataout).replace(",", ", "))	
		
			self.tabledata = np.c_[input[3:19], calibrated[0:16], np.r_[zerocorrectedflows[:], [np.nan]*6]]
			self.tabledata = np.around(self.tabledata,decimals=3)		
		except: 
			self.errorSignal.emit("Nonfatal error in organizing table data")
			#print('client socket failed')#		if client_sock != '': client_sock.send(dataout)	

		#self.tabledata = ["{:.3f}".format(x) for x in self.tabledata]
		#formattedList = ["%.2f" % member for member in theList]
		try:
			#When this is changed, also change the dropdown lists from above (~ line 1000, self.plottitles)
			#H2O, ptdl, ttdl, cvf3, cvcnc1, cvcnc01, cvrho_tdl, cvrhoo_tdl, opcc, opcco
			#New 2-24-17 	--- Added cvfx5r, cvfx5c, cvts, cvtai, cvcfact 
			#		--- corresponding to input[9],cal[6],cal[13],cal[15], 
			newdata = np.r_[input[0],input[19:22], extra[:],input[9],calibrated[6],calibrated[13],calibrated[15], cvcfact]
			newdata = np.around(newdata,decimals=3)
			try:
				try:
					self.plotdata = np.c_[self.plotdata[:,-899:], newdata]
				except:
					self.plotdata = np.c_[self.plotdata, newdata]
			except:
				self.plotdata = np.c_[newdata]
		except:# NameError:
			self.errorSignal.emit("There was an error in the plotting data")
			#print ("There was a problem in the plotting")
				
		try:	
			#Originally had C:\data\
			#	Appended to project title (i.e. IDEAS2013\)
			#	The file name then listed as
			#	YYMMDDHH.MM with 'q' on the end
			#	Full file name could be YYMMDDHH.MMq
			#	In certain directory.
			#outputstring = [ "{:11.5g}".format(x) for x in output ]
			output = np.array(output)
			output = np.around(output,decimals=5)
			outputstring = list(map(str, output))
			outputstring = ','.join(outputstring)
			outputstring += '\n'

			#Save data to project path
			self.dataSave(0, outputstring, self.header)
		except: self.errorSignal.emit("Error in saving data")
			
		try: self.CVIreplot()
		except: self.errorSignal.emit("Error in plotting")

	#Exception to print data header or error data to DSM
	#	header text box on display
	#except:
	#	if datain[0] == 'N' :
	#		self.dsmheader.setText(str(datain))
	#	else:
	#		self.errorSignal.emit("General error in flow calculation")

class QServer(QThread):

	def __init__(self, host, portin, portout, parent=None):#(self, socketDescriptor, fortune, parent):
		super(QServer, self).__init__(parent)
		self.host = host
		self.portin = portin
		self.portout = portout
		
		#Flag to stop server loop
		self.stopFlag = False
		
		#Flag to know whether or not to reconnect to client
		self.sendSuccess = False

		# Create a TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		# Bind the socket to the port
		self.server_address = ('',self.portin)
		self.client_address = (self.host, self.portout)		
		#print(sys.stderr, 'starting up on %s port %s' % self.server_address)
		ui.logSignal.emit(str('Starting up local server on %s port %s' % self.server_address))
		
		self.sock.bind(self.server_address)

		# Listen for incoming connections
		self.sock.listen(1)
		self.sock.setblocking(False)
		
	def run(self):		
		server_socket = self.sock
		read_list = [server_socket]
		write_list = []
		
		#Initialize output socket
		self.tcpOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		#Begin server loop
		#	For establishing in and outbound connections
		while not self.stopFlag:
			readable, writable, errored = select.select(read_list, write_list, [], 0)
			
			for s in readable:		
				if s is server_socket:
					client_socket, address = server_socket.accept()
					read_list.append(client_socket)
					ui.logSignal.emit("Connection from"+str(address))
					break
					break
				else:
					#Read data and emit signal for processing if valid
					data = s.recv(1024)
					if data: 
						datain = data.decode(encoding='utf-8')
						ui.dataReceived.emit(datain, self.tcpOut)
					else:
						ui.logSignal.emit("Connection FROM CVI DSM was lost")
						ui.errorSignal.emit("Connection FROM CVI DSM was lost")
						s.close()
						read_list.remove(s)
				if not self.sendSuccess:
					try:
						self.tcpOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						self.tcpOut.connect(self.client_address)
						self.tcpOut.setblocking(0)
						ui.logSignal.emit("Successful client connection TO CVI DSM at %s port %s" % self.client_address)
						#The following line presents a potential threading conflict
						#	It is used to prevent a double client connection to DSM
						# 	before the calculation thread can catch up
						self.sendSuccess = True
					except:
						ui.logSignal.emit("Client connection TO CVI DSM Failed")#Failed to connect to CVI server")
						ui.errorSignal.emit("Client connection TO CVI DSM Failed")
					
		#Close all connections once the server loop has halted
		for w in write_list:
			w.close()
		for r in read_list:
			r.close()
		
	def stop(self):
		self.stopFlag = True
		ui.logSignal.emit("Local server closed by user")
	
	def __del__(self):
		self.quit()
		self.wait()		
		
#Class for allowing a window close event to be intercepted
class MyWindow(QtGui.QMainWindow):
	def closeEvent(self,event):
		result = QtGui.QMessageBox.warning(MainWindow, 'WARNING',\
			 "Are you sure you want to close the program?", QtGui.QMessageBox.Yes, \
			QtGui.QMessageBox.No)
		event.ignore()

		if result == QtGui.QMessageBox.Yes:
			event.accept()	
			
if __name__ == "__main__":

	#Create time for plot updating
	#timer = QTimer();
	
	#Initialize GUI
	app = QtWidgets.QApplication(sys.argv)
	#MainWindow = QtWidgets.QMainWindow()#QMainWindow()
	MainWindow = MyWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.showMaximized()
	sys.exit(app.exec_())

		
