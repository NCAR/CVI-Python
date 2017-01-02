# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CVI_Python_Interface_Config.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

#CVI code for performing all of the data manipulation
from crunchcvi import *

#GUI imports
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#For creating parallel thread for server
import threading

#Following three imports appear to be the "newer" version of asyncore
#Implemented; however, needs to be implemented as asynchronous I/O
#As opposed to its current threading implementation
import asyncio
import asyncio.streams

#For the simple non blocking tcp client output
#Incorporates Select()
from eventlet.green import socket

#For plotting within pyqt
import pyqtgraph
from pyqtgraph import PlotWidget, ViewBox
import numpy as np

#For File WRiting
import os

#for scheduling replot (NO LONGER USED) 
#from apscheduler.schedulers.background import BackgroundScheduler

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		self.MainWindow = MainWindow
						
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
			
		#Creation of Tabs for program	
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)#MainWindow)
		#self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1800, 925))
		self.tabWidget.setObjectName("tabWidget")		
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.tabWidget.addTab(self.tab, "")

		self.tabLayout_1 = QtWidgets.QGridLayout(self.tab)
		self.tabLayout_1.setContentsMargins(10, 10, 10, 10)
		self.tabLayout_1.setObjectName("tabLayout_1")
		
		self.tabLayout_1.setSpacing(10)
		
		#Create corresponding Tabs?
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tabWidget.addTab(self.tab_2, "")

		self.tabLayout_2 = QtWidgets.QGridLayout(self.tab_2)
		self.tabLayout_2.setContentsMargins(10, 10, 10, 10)
		self.tabLayout_2.setObjectName("tabLayout_2")	

		self.tabLayout_2.setSpacing(10)

		#self.tabWidget.addTab(self.tab, "")
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.tabWidget.addTab(self.tab_3, "Connect Auxiliary Instruments")
		
		self.tabLayout_3 = QtWidgets.QGridLayout(self.tab_3)
		self.tabLayout_3.setContentsMargins(10, 10, 10, 10)
		self.tabLayout_3.setObjectName("tabLayout_3")
		
		self.tabLayout_3.setSpacing(10)
		
		for i in range(0, 101):
			#self.tabLayout_1.setColumnMinimumWidth(i,1) 
			self.tabLayout_1.setColumnStretch(i,1)
			#self.tabLayout_2.setColumnMinimumWidth(i,1) 
			self.tabLayout_2.setColumnStretch(i,1)
			#self.tabLayout_3.setColumnMinimumWidth(i,1) 
			self.tabLayout_3.setColumnStretch(i,1)
			
		for i in range(0, 51):
			#self.tabLayout_1.setRowMinimumHeight(i,1)
			self.tabLayout_1.setRowStretch(i,1)
			#self.tabLayout_2.setRowMinimumHeight(i,1)
			self.tabLayout_2.setRowStretch(i,1)
			#self.tabLayout_3.setRowMinimumHeight(i,1)
			self.tabLayout_3.setRowStretch(i,1)
		
				
		#Push buttons for establishing (or cancel) server to receive data
		self.connect = QtWidgets.QPushButton(self.tab)#MainWindow)
		self.connect.setObjectName("connect")
		self.tabLayout_1.addWidget(self.connect, 0, 0, 1, 25)
		self.disconnect = QtWidgets.QPushButton(self.tab)#MainWindow)
		self.disconnect.setObjectName("disconnect")
		self.tabLayout_1.addWidget(self.disconnect, 0, 25, 1, 25)			
		
				
		self.flowio = QtWidgets.QPushButton(self.tab)#MainWindow)
		self.flowio.setObjectName("flowio")
		self.tabLayout_1.addWidget(self.flowio, 3, 0, 4, 10)
		self.flowio.setCheckable(True)
		
		self.cvimode = QtWidgets.QPushButton(self.tab)#MainWindow)
		self.cvimode.setObjectName("cvimode")
		self.tabLayout_1.addWidget(self.cvimode, 7, 0, 4, 10)
		self.cvimode.setCheckable(True)
		
		
		tmpobject = QtWidgets.QLabel(self.tab)
		tmpobject.setObjectName("flowoptionslabel")
		self.tabLayout_1.addWidget(tmpobject, 2, 0, 1, 10)
		tmpobject.setText("FLOW OPTIONS")
		tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		

		
		self.flowlabels = ['cvfx0label','cvfx2label','cvfx3label','cvfx4label']
		self.flowedit = ['cvfx0','cvfx2','cvfx3','cvfx4']
		for i in range(0,len(self.flowedit)):
			tmpobject = QtWidgets.QLabel(self.tab)
			tmpobject.setObjectName(self.flowlabels[i])
			self.tabLayout_1.addWidget(tmpobject, 11+3*i, 0, 3, 5)
			tmpobject = QtWidgets.QLineEdit(self.tab)
			tmpobject.setObjectName(self.flowedit[i])
			self.tabLayout_1.addWidget(tmpobject, 11+3*i, 5, 3, 5)
			
		#webView.sizePolicy.setHorizontalStretch(1)
		#graphicsView.sizePolicy.setHorizontalStretch(1)		
				
				
		self.currentfilelabel = QtWidgets.QLabel(self.tab)#MainWindow)
		self.currentfilelabel.setObjectName("currentfilelabel")
		self.tabLayout_1.addWidget(self.currentfilelabel, 23, 0, 1, 50)
		self.currentfile = QtWidgets.QLineEdit(self.tab)#MainWindow)
		self.currentfile.setObjectName("currentfile")
		self.tabLayout_1.addWidget(self.currentfile, 24, 0, 1, 50)
		self.currentfile.setDisabled(True)		
					
				
		self.mainstatus = QtWidgets.QTextEdit()#Label()#self.tab)#MainWindow)
		self.mainstatus.setObjectName("mainstatus")
		#self.tabLayout_1.addWidget(self.mainstatus, 3, 15, 20, 30)
		#self.mainstatus.setWordWrap(True)
		#self.mainstatus.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")		
		#self.mainstatus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.mainstatus.setAlignment(Qt.AlignTop)
		self.mainstatus.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))	

		self.scrollArea = QtWidgets.QScrollArea(self.tab)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setWidget(self.mainstatus)
		self.scrollArea.setObjectName("scrollArea")
		#self.scrollArea.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")		
		self.scrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.tabLayout_1.addWidget(self.scrollArea, 3, 15, 20, 30)
		
		#self.Voltage_Label[i].setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))		
		'''
		QFont font;
		font.setPointSize(32);
		font.setBold(true);
		'''		
		###############################################################################
		###############################################################################
		
		#Create Table for Viewing Parameters
		self.tableWidget = QtWidgets.QTableWidget(self.tab)
		self.tableWidget.setObjectName("tableWidget")
		self.tabLayout_1.addWidget(self.tableWidget, 25, 0, 25, 30)
		
		self.rawtableWidget = QtWidgets.QTableWidget(self.tab)
		self.rawtableWidget.setObjectName("rawtablewidget")
		self.tabLayout_1.addWidget(self.rawtableWidget, 25, 30, 25, 20)
		
		#Plotting Widget
#		pyqtgraph.setConfigOption('background', 'w')
#		pen=pyqtgraph.mkPen(color=C,width=10)
		self.CVIplot = PlotWidget(self.tab)#MainWindow)
		self.CVIplot.setObjectName("CVIplot")
		self.tabLayout_1.addWidget(self.CVIplot, 1, 50, 24, 50)
		self.CVIplot.show()
		self.CVIplot.setTitle("CVI Data")
		self.CVIplot.setLabel('bottom',text = 'time (seconds)')
		self.CVIplot.setLabel('left',text = 'y')
		
		self.CVIplotline2 = ViewBox()
		self.CVIplot.showAxis('right')
		self.CVIplot.scene().addItem(self.CVIplotline2)
		self.CVIplot.getAxis('right').linkToView(self.CVIplotline2)
		self.CVIplotline2.setXLink(self.CVIplot)
		self.CVIplot.getAxis('right').setLabel('axis2', color = '#0000ff')
		
		self.CVIplot.getAxis('left').setPen(pyqtgraph.mkPen(color=(255,255,255), width=2))#, size=10))
		self.CVIplot.getAxis('bottom').setPen(pyqtgraph.mkPen(color=(255,255,255), width=2))
		self.CVIplot.getAxis('right').setPen(pyqtgraph.mkPen(color=(0,0,255), width=2))
		#self.CVIplot.AxisItem('title').setPen(pyqtgraph.mkPen(color=(255,255,0), width=2))
		
		#a=window.getAxis('bottom')
		#a.font.setPixelSize(10)
		#but a.font.pixelSize() doesn't change and the font size on the plot doesn't change

		#I then tried 
		#b=QtGui.QFont()
		#b.setPixelSize(10)
		#a.setFont(b)
		
		
		#b=QtGui.QFont().setPixelSize(20)
		#b.setPixelSize(20)
		#x_axisitem.tickFont = b
		
		#self.CVIplot.getAxis('left').tickFont = QtGui.QFont().setPixelSize(200)
		#self.CVIplot.getAxis('left').setFont(QtGui.QFont("Times",100,QtGui.QFont.Bold))
		#self.CVIplot.setFont(QtGui.QFont("Times",100,QtGui.QFont.Bold))	
		
		'''
		p1.setLabels(left='axis 1')
		p1.getAxis('right').setLabel('axis2', color='#0000ff')
		'''
		
		self.CVIplot2 = PlotWidget(self.tab)#MainWindow)
		self.CVIplot2.setObjectName("CVIplot")
		self.tabLayout_1.addWidget(self.CVIplot2, 26, 50, 24, 50)
		self.CVIplot2.setTitle("CVI Data")
		self.CVIplot2.setLabel('bottom',text = 'time (seconds)')
		self.CVIplot2.setLabel('left',text = 'y')
		
		self.CVIplot2line2 = ViewBox()
		self.CVIplot2.showAxis('right')
		self.CVIplot2.scene().addItem(self.CVIplot2line2)
		self.CVIplot2.getAxis('right').linkToView(self.CVIplot2line2)
		self.CVIplot2line2.setXLink(self.CVIplot2)
		self.CVIplot2.getAxis('right').setLabel('axis2', color = '#0000ff')
		
		
		#Dropdown list for selecting data to plot
		self.dropdownlist = QtWidgets.QComboBox(self.tab)#MainWindow)
		self.dropdownlist.setObjectName("dropdownlist")
		self.tabLayout_1.addWidget(self.dropdownlist, 0, 50, 1, 25)

		self.dropdownlistline2 = QtWidgets.QComboBox(self.tab)#MainWindow)
		self.dropdownlistline2.setObjectName("dropdownlistline2")
		self.tabLayout_1.addWidget(self.dropdownlistline2, 0, 75, 1, 25)
		
		self.dropdownlist2 = QtWidgets.QComboBox(self.tab)#MainWindow)
		self.dropdownlist2.setObjectName("dropdownlist2")
		self.tabLayout_1.addWidget(self.dropdownlist2, 25, 50, 1, 25)
		
		self.dropdownlist2line2 = QtWidgets.QComboBox(self.tab)#MainWindow)
		self.dropdownlist2line2.setObjectName("dropdownlist2line2")
		self.tabLayout_1.addWidget(self.dropdownlist2line2, 25, 75, 1, 25)	
		
		###############################################################################
		###############################################################################		
		
				
		#Host and Port Configuration Labels and inputs
		self.dsmiplabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.dsmiplabel.setObjectName("label")
		self.tabLayout_2.addWidget(self.dsmiplabel, 0, 0, 1, 10)
		self.ipaddress = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.ipaddress.setObjectName("ipaddress")
		self.tabLayout_2.addWidget(self.ipaddress, 1, 0, 1, 10)
		self.portin = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.portin.setObjectName("portin")
		self.tabLayout_2.addWidget(self.portin, 3, 0, 1, 10)
		self.portout = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.portout.setObjectName("portout")
		self.tabLayout_2.addWidget(self.portout, 5, 0, 1, 10)
		self.portinlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.portinlabel.setObjectName("portinlabel")
		self.tabLayout_2.addWidget(self.portinlabel, 2, 0, 1, 10)
		self.portoutlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.portoutlabel.setObjectName("portoutlabel")
		self.tabLayout_2.addWidget(self.portoutlabel, 4, 0, 1, 10)
		
		#Base File Path
		self.basedirlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.basedirlabel.setObjectName("basedirlabel")
		self.tabLayout_2.addWidget(self.basedirlabel, 0, 20, 1, 10)
		self.basedirval = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.basedirval.setObjectName("basedirval")
		self.tabLayout_2.addWidget(self.basedirval, 1, 20, 1, 10)
		self.basedirval.setDisabled(True)
		
		self.projectdirlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.projectdirlabel.setObjectName("projectdirlabel")
		self.tabLayout_2.addWidget(self.projectdirlabel, 2, 20, 1, 10)
		self.projectdirval = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.projectdirval.setObjectName("projectdirval")
		self.tabLayout_2.addWidget(self.projectdirval, 3, 20, 1, 10)
		self.projectdirval.setDisabled(True)
		
		self.caldirlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.caldirlabel.setObjectName("caldirlabel")
		self.tabLayout_2.addWidget(self.caldirlabel, 4, 20, 1, 10)
		self.caldirval = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.caldirval.setObjectName("caldirval")
		self.tabLayout_2.addWidget(self.caldirval, 5, 20, 1, 10)
		self.caldirval.setDisabled(True)
	
		#Text Boxes for displaying the data to and from the DSM
		self.datafromdsmlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.datafromdsmlabel.setObjectName("datafromdsmlabel")
		self.tabLayout_2.addWidget(self.datafromdsmlabel, 6, 0, 1, 40)
		
		self.datafromdsm = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.datafromdsm.setObjectName("datafromdsm")
		self.tabLayout_2.addWidget(self.datafromdsm, 7, 0, 8, 40)
		self.datafromdsm.setWordWrap(True)
		#.setAlignment(AlignCenter)
		#.font.setFamily("Sans Serif")
		#.font.setPointSize(20)
		#.setFont(...)
		#.setStyleSheet("QLabel { background-color : gray; color : black; }")
		self.datafromdsm.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")
		self.datafromdsm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.datafromdsm.setAlignment(Qt.AlignTop)
	
		self.datatodsmlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.datatodsmlabel.setObjectName("datatodsmlabel")
		self.tabLayout_2.addWidget(self.datatodsmlabel, 15, 0, 1, 40)
		self.datatodsm = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.datatodsm.setObjectName("datafromdsm")
		self.tabLayout_2.addWidget(self.datatodsm, 16, 0, 6, 40)
		self.datatodsm.setWordWrap(True)
		self.datatodsm.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")		
		self.datatodsm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.datatodsm.setAlignment(Qt.AlignTop)

		#Status indicator at bottom of GUI
		self.statusindicatorlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.statusindicatorlabel.setObjectName("statusindicatorlabel")
		self.tabLayout_2.addWidget(self.statusindicatorlabel, 22, 0, 1, 30)

		
		#Toggle button/label for determining whether valves and 
		#flows are controlled by the user or by the calculation
		self.valvesourcelabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.valvesourcelabel.setObjectName("valvesourcelabel")
		self.tabLayout_2.addWidget(self.valvesourcelabel, 24, 0, 1, 40)
		self.valvesource = QtWidgets.QPushButton(self.tab_2)#MainWindow)
		self.valvesource.setObjectName("valvesource")
		self.tabLayout_2.addWidget(self.valvesource, 25, 0, 2, 40)
		self.valvesource.setCheckable(True)

		self.valvesourcelabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
		
		#Label and checkboxes for the four controllable valves!
		self.v1 = QtWidgets.QPushButton(self.tab_2)#MainWindow)
		self.v1.setObjectName("valve1")
		self.tabLayout_2.addWidget(self.v1, 27, 0, 2, 10)
		self.v2 = QtWidgets.QPushButton(self.tab_2)#MainWindow)
		self.v2.setObjectName("valve2")
		self.tabLayout_2.addWidget(self.v2, 27, 10, 2, 10)
		self.v3 = QtWidgets.QPushButton(self.tab_2)#MainWindow)
		self.v3.setObjectName("valve3")
		self.tabLayout_2.addWidget(self.v3, 27, 20, 2, 10)
		self.v4 = QtWidgets.QPushButton(self.tab_2)#MainWindow)
		self.v4.setObjectName("valve4")
		self.tabLayout_2.addWidget(self.v4, 27, 30, 2, 10)
		self.v1.setCheckable(True)
		self.v2.setCheckable(True)
		self.v3.setCheckable(True)
		self.v4.setCheckable(True)
		
		#Toggle button/label for determining whether valves and 
		#flows are controlled by the user or by the calculation
		self.flowsourcelabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.flowsourcelabel.setObjectName("flowsourcelabel")
		self.tabLayout_2.addWidget(self.flowsourcelabel, 30, 0, 1, 40)
		self.flowsource = QtWidgets.QPushButton(self.tab_2)#MainWindow)
		self.flowsource.setObjectName("flowsource")
		self.tabLayout_2.addWidget(self.flowsource, 31, 0, 2, 40)
		self.flowsource.setCheckable(True)
		
		self.flowsourcelabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		
		
		#User input flows and labels for cvfx0,cvfx2,cvfx3,cvfx4,cvf1
		self.cvfx0wrlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.cvfx0wrlabel.setObjectName("cvfx0wrlabel")		
		self.tabLayout_2.addWidget(self.cvfx0wrlabel, 33, 0, 1, 8)
		self.cvfx0wr = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.cvfx0wr.setObjectName("cvfx0wr")
		self.tabLayout_2.addWidget(self.cvfx0wr, 34, 0, 1, 8)
		self.cvfx2wrlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.cvfx2wrlabel.setObjectName("cvfx2wrlabel")			
		self.tabLayout_2.addWidget(self.cvfx2wrlabel, 33, 8, 1, 8)
		self.cvfx2wr = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.cvfx2wr.setObjectName("cvfx2wr")
		self.tabLayout_2.addWidget(self.cvfx2wr, 34, 8, 1, 8)
		self.cvfx3wrlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.cvfx3wrlabel.setObjectName("cvfx3wrlabel")			
		self.tabLayout_2.addWidget(self.cvfx3wrlabel, 33, 16, 1, 8)
		self.cvfx3wr = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.cvfx3wr.setObjectName("cvfx3wr")
		self.tabLayout_2.addWidget(self.cvfx3wr, 34, 16, 1, 8)
		self.cvfx4wrlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.cvfx4wrlabel.setObjectName("cvfx4wrlabel")			
		self.tabLayout_2.addWidget(self.cvfx4wrlabel, 33, 24, 1, 8)
		self.cvfx4wr = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.cvfx4wr.setObjectName("cvfx4wr")
		self.tabLayout_2.addWidget(self.cvfx4wr, 34, 24, 1, 8)
		self.cvf1wrlabel = QtWidgets.QLabel(self.tab_2)#MainWindow)
		self.cvf1wrlabel.setObjectName("cvf1wrlabel")			
		self.tabLayout_2.addWidget(self.cvf1wrlabel, 33, 32, 1, 8)
		self.cvf1wr = QtWidgets.QLineEdit(self.tab_2)#MainWindow)
		self.cvf1wr.setObjectName("cvf1wr")
		self.tabLayout_2.addWidget(self.cvf1wr, 34, 32, 1, 8)
	
		#Colored box for showing green if connected, red if disconnected
		self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)#MainWindow)
		#self.tabLayout_2.addWidget(self.graphicsView, 3, 10, 2, 7)
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
		#brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
		self.graphicsView.setPalette(palette)
		self.graphicsView.setObjectName("graphicsView")
		
		self.graphicsView.hide()
		
		#Functions for adding scalable graphics to program
		'''
		self.radioButton = QtWidgets.QRadioButton(self.tab_2)
		self.radioButton.setObjectName("radioButton")
		self.tabLayout_1.addWidget(self.radioButton, 0, 0, 1, 1)
		'''
		
		self.updatecals = QtWidgets.QPushButton(self.tab_2)#MainWindow)
		self.updatecals.setObjectName("updatecals")
		self.tabLayout_2.addWidget(self.updatecals, 0, 50, 2, 50)
		#self.flowio.setCheckable(True)
		
		#Create Table for OPC Calibration Coefficients
		self.opccaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.opccaltableWidget.setObjectName("opccaltableWidget")
		self.tabLayout_2.addWidget(self.opccaltableWidget, 2, 50, 3, 50)
		
		self.opccaltablerowlabels = ['OPC Pressure Cals']
		self.opccaltablecolumnlabels = ['OPC_C0','OPC_C1']

		self.opccaltableWidget.setColumnCount(len(self.opccaltablecolumnlabels))
		self.opccaltableWidget.setRowCount(len(self.opccaltablerowlabels))
		
		for i in range(0,len(self.opccaltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.opccaltableWidget.setVerticalHeaderItem(i,item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setVerticalHeaderItem(0, item)
		
		for i in range(0,len(self.opccaltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.opccaltableWidget.setHorizontalHeaderItem(i, item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setHorizontalHeaderItem(1, item)
		for i in range(0,len(self.opccaltablerowlabels)):
			for j in range(0, len(self.opccaltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.opccaltableWidget.setItem(i, j, item)	
		
		#Create Table for More Calibration Coefficients
		self.morecaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.morecaltableWidget.setObjectName("morecaltableWidget")
		self.tabLayout_2.addWidget(self.morecaltableWidget, 5, 50, 3, 50)

		self.morecaltablecolumnlabels = ['RHOD','CVTBL','CVTBR','CVOFF1','LTip']
		self.morecaltablerowlabels = ['Coefficients']

		self.morecaltableWidget.setColumnCount(len(self.morecaltablecolumnlabels))
		self.morecaltableWidget.setRowCount(len(self.morecaltablerowlabels))
		
		for i in range(0,len(self.morecaltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.morecaltableWidget.setVerticalHeaderItem(i,item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setVerticalHeaderItem(0, item)
				
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.morecaltableWidget.setHorizontalHeaderItem(i, item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setHorizontalHeaderItem(1, item)
		for i in range(0,len(self.morecaltablerowlabels)):
			for j in range(0, len(self.morecaltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.morecaltableWidget.setItem(i, j, item)			

		self.morecaltableWidget.verticalHeader().setVisible(False)		

		self.tablerowlabels = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4','cvfx5','cvfx6','cvfx7','cvfx8','cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai']
		self.tablecolumnlabels = ['raw','calibrated','crunched']
		
		self.tableWidget.setColumnCount(len(self.tablecolumnlabels))
		self.tableWidget.setRowCount(len(self.tablerowlabels))
		for i in range(0,len(self.tablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setVerticalHeaderItem(i,item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setVerticalHeaderItem(0, item)
		
		for i in range(0,len(self.tablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setHorizontalHeaderItem(i, item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setHorizontalHeaderItem(1, item)
		for i in range(0,len(self.tablerowlabels)):
			for j in range(0, len(self.tablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.tableWidget.setItem(i, j, item)
				
				
				
		#table for raw input output parameters
		#self.rawtablerowlabels = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4','cvfx5','cvfx6','cvfx7','cvfx8','cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai']
		self.rawtablecolumnlabels = ['Input','Output']
		
		self.rawtableWidget.setColumnCount(len(self.rawtablecolumnlabels))
		self.rawtableWidget.setRowCount(100)#len(self.tablerowlabels))
		for i in range(0,100):#len(self.rawtablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.rawtableWidget.setVerticalHeaderItem(i,item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setVerticalHeaderItem(0, item)
		for i in range(0,len(self.rawtablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.rawtableWidget.setHorizontalHeaderItem(i, item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setHorizontalHeaderItem(1, item)
		for i in range(0,100):#len(self.tablerowlabels)):
			for j in range(0, len(self.rawtablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.rawtableWidget.setItem(i, j, item)	

		self.rawtableWidget.verticalHeader().setVisible(False)					
				
				
		
		#Create Table for Calibration Coefficients
		self.caltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.caltableWidget.setObjectName("caltableWidget")
		self.tabLayout_2.addWidget(self.caltableWidget, 8, 50, 17, 50)

		self.caltablerowlabels = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4','cvfx5','cvfx6','cvfx7','cvfx8','cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai']
		self.caltablecolumnlabels = ['C0','C1','C2','UNUSED']

		self.caltableWidget.setColumnCount(len(self.caltablecolumnlabels))
		self.caltableWidget.setRowCount(len(self.caltablerowlabels))
		
		for i in range(0,len(self.caltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.caltableWidget.setVerticalHeaderItem(i,item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setVerticalHeaderItem(0, item)
		
		for i in range(0,len(self.caltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.caltableWidget.setHorizontalHeaderItem(i, item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setHorizontalHeaderItem(1, item)
		for i in range(0,len(self.caltablerowlabels)):
			for j in range(0, len(self.caltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.caltableWidget.setItem(i, j, item)
				
								
		#Create Table for TDL Calibration Coefficients
		self.tdlcaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.tdlcaltableWidget.setObjectName("tdlcaltableWidget")
		self.tabLayout_2.addWidget(self.tdlcaltableWidget, 25, 50, 10, 50)

		self.tdlcaltablerowlabels = ['param_0','param_1','param_2','param_3']
		self.tdlcaltablecolumnlabels = ['TDL_C0','TDL_C1','TDL_C2','TDL_C3']

		self.tdlcaltableWidget.setColumnCount(len(self.tdlcaltablecolumnlabels))
		self.tdlcaltableWidget.setRowCount(len(self.tdlcaltablerowlabels))
		
		for i in range(0,len(self.tdlcaltablerowlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tdlcaltableWidget.setVerticalHeaderItem(i,item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setVerticalHeaderItem(0, item)
		
		for i in range(0,len(self.tdlcaltablecolumnlabels)):
			item = QtWidgets.QTableWidgetItem()
			self.tdlcaltableWidget.setHorizontalHeaderItem(i, item)
		#item = QtWidgets.QTableWidgetItem()
		#self.tableWidget.setHorizontalHeaderItem(1, item)
		for i in range(0,len(self.tdlcaltablerowlabels)):
			for j in range(0, len(self.tdlcaltablecolumnlabels)):
				item = QtWidgets.QTableWidgetItem()
				self.tdlcaltableWidget.setItem(i, j, item)	
				
				
		
		
		
		###############################################################################
		###############################################################################
		
		
		
		#Push buttons for connecting or disconnecting instruments
		self.devconnect = QtWidgets.QPushButton(self.tab_3)#MainWindow)
		#self.devconnect.setGeometry(QtCore.QRect(30, 80, 141, 34))
		self.devconnect.setObjectName("devconnect")
		self.tabLayout_3.addWidget(self.devconnect, 0, 0, 1, 10)
		self.devdisconnect = QtWidgets.QPushButton(self.tab_3)#MainWindow)
		self.devdisconnect.setObjectName("devdisconnect")
		self.tabLayout_3.addWidget(self.devdisconnect, 0, 10, 1, 10)
		
		#Text Box for displaying instructions for instrument connections
		#self.devinstructlabel = QtWidgets.QLabel(self.tab_3)#MainWindow)
		#self.devinstructlabel.setObjectName("devinstructlabel")
		#self.tabLayout_3.addWidget(self.devinstructlabel, 4, 0, 1, 20)
		self.devinstruct = QtWidgets.QLabel(self.tab_3)#MainWindow)
		self.devinstruct.setObjectName("devinstruct")
		self.tabLayout_3.addWidget(self.devinstruct, 4, 0, 14, 20)
		self.devinstruct.setWordWrap(True)
		self.devinstruct.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")
		self.devinstruct.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.devinstruct.setAlignment(Qt.AlignTop)		
		self.devinstruct.setFont(QtGui.QFont("Times",10,QtGui.QFont.Bold))	
		
		self.defaultdevinstruct = "The connection and disconnection routine above is used to add or remove instrumentation from the flow. Upon either button press, counterflow will be raised and an instructional sequence will be displayed"
		self.devinstruct.setText(self.defaultdevinstruct)
		
		
		self.devcontinue = QtWidgets.QPushButton(self.tab_3)
		self.devcontinue.setObjectName("devcontinue")
		self.tabLayout_3.addWidget(self.devcontinue, 0, 0, 1, 10)
		self.devcontinue.hide()
		
		self.devcancel = QtWidgets.QPushButton(self.tab_3)
		self.devcancel.setObjectName("devcancel")
		self.tabLayout_3.addWidget(self.devcancel, 0, 10, 1, 10)
		self.devcancel.hide()
		
		'''
		self.Voltage_Label = []
		self.Voltage_Label.append(QtGui.QLabel("voltage1 ")) # i need to have diff Font & size for these 
		self.Voltage_Label.append(QtGui.QLabel("voltage2 "))   
		self.Voltage_Label.append(QtGui.QLabel("voltage3 "))
		'''
		
					
		#USER INPUTS FOR DELAY, OFFSET, and CVF3CW
		self.delaylabel = QtWidgets.QLabel(self.tab_3)#MainWindow)
		self.delaylabel.setObjectName("delaylabel")		
		self.tabLayout_3.addWidget(self.delaylabel, 1, 0, 1, 6)
		self.delay = QtWidgets.QLineEdit(self.tab_3)#MainWindow)
		self.delay.setObjectName("delay")
		self.tabLayout_3.addWidget(self.delay, 2, 0, 1, 6)
		self.delaylabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		

		
		self.offsetlabel = QtWidgets.QLabel(self.tab_3)#MainWindow)
		self.offsetlabel.setObjectName("offsetlabel")		
		self.tabLayout_3.addWidget(self.offsetlabel, 1, 7, 1, 6)
		self.offset = QtWidgets.QLineEdit(self.tab_3)#MainWindow)
		self.offset.setObjectName("offset")
		self.tabLayout_3.addWidget(self.offset, 2, 7, 1, 6)
		self.offsetlabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		
		
		self.cvf3cwlabel = QtWidgets.QLabel(self.tab_3)#MainWindow)
		self.cvf3cwlabel.setObjectName("cvf3cwlabel")		
		self.tabLayout_3.addWidget(self.cvf3cwlabel, 1, 14, 1, 6)
		self.cvf3cw = QtWidgets.QLineEdit(self.tab_3)#MainWindow)
		self.cvf3cw.setObjectName("cvf3cw")
		self.tabLayout_3.addWidget(self.cvf3cw, 2, 14, 1, 6)	
		self.cvf3cwlabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		

		
		self.auxdev1 = QtWidgets.QPushButton(self.tab_3)#MainWindow)
		self.auxdev1.setObjectName("auxdev1")
		self.tabLayout_3.addWidget(self.auxdev1, 3, 0, 1, 5)
		self.auxdev1.setCheckable(True)
		
		self.auxdev2 = QtWidgets.QPushButton(self.tab_3)#MainWindow)
		self.auxdev2.setObjectName("auxdev2")
		self.tabLayout_3.addWidget(self.auxdev2, 3, 5, 1, 5)
		self.auxdev2.setCheckable(True)		
		
		self.auxdev3 = QtWidgets.QPushButton(self.tab_3)#MainWindow)
		self.auxdev3.setObjectName("auxdev3")
		self.tabLayout_3.addWidget(self.auxdev3, 3, 10, 1, 5)
		self.auxdev3.setCheckable(True)

		self.auxdev4 = QtWidgets.QPushButton(self.tab_3)#MainWindow)
		self.auxdev4.setObjectName("auxdev4")
		self.tabLayout_3.addWidget(self.auxdev4, 3, 15, 1, 5)
		self.auxdev4.setCheckable(True)
			
		#Creating toggles for external instruments
		#for i in range(0,4):
			#self.tmpobject.setCheckable(True)	
			
		self.signalnulls = self.caltablerowlabels
		
		tmpobject = QtWidgets.QLabel(self.tab_3)
		tmpobject.setObjectName("NullLabel")
		self.tabLayout_3.addWidget(tmpobject, 0, 25, 2, 10)
		tmpobject.setText("NULL SIGNALS")
		tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)		
		tmpobject.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		
		
		for i in range(0,len(self.signalnulls)):
			tmpobject = QtWidgets.QLabel(self.tab_3)
			tmpobject.setObjectName("NullLabel"+str(i))
			self.tabLayout_3.addWidget(tmpobject, 2+i, 25, 1, 5)	
		
			tmpobject = QtWidgets.QPushButton(self.tab_3)
			tmpobject.setObjectName("Null"+str(i))
			self.tabLayout_3.addWidget(tmpobject, 2+i, 30, 1, 5)
			tmpobject.setCheckable(True)			
		
		
		tmpobject = QtWidgets.QLabel(self.tab_3)
		tmpobject.setObjectName("AuxDevLabel")
		self.tabLayout_3.addWidget(tmpobject, 0, 50, 2, 40)
		tmpobject.setText("AUXILIARY DEVICE CONFIGURATIONS")
		tmpobject.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)				
		tmpobject.setFont(QtGui.QFont("Times",8,QtGui.QFont.Bold))
		
		
		self.auxdevtoggles = ['mode','datatype','tmpsrc']
		self.auxdevtoggleslist = ['title','mode','dataval','datatype','tmpsrc','tempval']
		for i in range(0,4):
			for j in range(0,len(self.auxdevtoggleslist)):
				if j in [0,2,5]:
					self.tmpobject = QtWidgets.QLineEdit(self.tab_3)#MainWindow)
					self.tmpobject.setObjectName("cvfx"+str(i+5)+self.auxdevtoggleslist[j])
					self.tabLayout_3.addWidget(self.tmpobject, j+2, 50+i*10, 1, 10)
				else:
					self.tmpobject = QtWidgets.QPushButton(self.tab_3)
					self.tmpobject.setObjectName("cvfx"+str(i+5)+self.auxdevtoggleslist[j])
					self.tabLayout_3.addWidget(self.tmpobject, j+2, 50+i*10, 1, 10)
					self.tmpobject.setCheckable(True)

		self.auxoptions = QtWidgets.QLabel(self.tab_3)#MainWindow)
		self.auxoptions.setObjectName("auxoptions")
		self.tabLayout_3.addWidget(self.auxoptions, 8, 50, 10, 40)
		self.auxoptions.setWordWrap(True)
		self.auxoptions.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")
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
				
		###############################################################################
		###############################################################################
			
		'''
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		'''
		
		self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		
		self.retranslateUi(MainWindow)
		
#		self.layout = QVBoxLayout(self)
#		self.layout.add(everything)
		
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "CVI Interface"))
		
		self.dsmiplabel.setText(_translate("MainWindow", "DSM IP Address"))
		self.ipaddress.setText(_translate("MainWindow", "192.168.184.145"))#"localhost"))#"192.168.184.145"))#"192.168.0.1"))#"192.168.184.145"))
		self.portin.setText(_translate("MainWindow", "30005"))
		self.portout.setText(_translate("MainWindow", "30006"))
		self.portinlabel.setText(_translate("MainWindow", "Incoming Port"))
		self.portoutlabel.setText(_translate("MainWindow", "Outgoing Port"))
		self.connect.setText(_translate("MainWindow", "Start"))
		self.disconnect.setText(_translate("MainWindow", "Stop"))
		self.datafromdsmlabel.setText(_translate("MainWindow", "Data From DSM"))
		self.datatodsmlabel.setText(_translate("MainWindow", "Data To DSM"))

		self.devconnect.setText(_translate("MainWindow", "Device Connect"))
		self.devdisconnect.setText(_translate("MainWindow", "Device Disconnect"))
		
		self.devcontinue.setText(_translate("MainWindow", "Continue"))
		self.devcancel.setText(_translate("MainWindow", "Cancel"))
		
		self.statusindicatorlabel.setText(_translate("MainWindow", "Status Indicator"))

		self.v1.setText(_translate("MainWindow", "1"))
		self.v2.setText(_translate("MainWindow", "2"))
		self.v3.setText(_translate("MainWindow", "3"))
		self.v4.setText(_translate("MainWindow", "4"))
		
		self.basedirlabel.setText(_translate("MainWindow","Base Directory"))
		self.basedirval.setText(_translate("MainWindow","C:/CVI/"))
		self.projectdirlabel.setText(_translate("MainWindow","Project Path"))
		self.projectdirval.setText(_translate("MainWindow","Testing"))
		self.caldirlabel.setText(_translate("MainWindow","Calibrations Path"))
		self.caldirval.setText(_translate("MainWindow","Calibrations"))
				
		self.currentfilelabel.setText(_translate("MainWindow","Current Saved File"))
		self.currentfile.setText(_translate("MainWindow","Not Yet Implemented"))
				
		self.delaylabel.setText(_translate("MainWindow","Delay"))
		self.delay.setText(_translate("MainWindow", "1"))
		self.offsetlabel.setText(_translate("MainWindow","Flow Offset"))
		self.offset.setText(_translate("MainWindow", "3"))
		self.cvf3cwlabel.setText(_translate("MainWindow", "Counterflow Excess"))
		self.cvf3cw.setText(_translate("MainWindow", "0.5"))
				
		self.auxdev1.setText(_translate("MainWindow", "Dev1"))
		self.auxdev2.setText(_translate("MainWindow", "Dev2"))
		self.auxdev3.setText(_translate("MainWindow", "Dev3"))
		self.auxdev4.setText(_translate("MainWindow", "Dev4"))

		for i in range(0,4):
			MainWindow.findChild(QtWidgets.QLineEdit, "cvfx"+str(i+5)+"dataval").setText("3.00")
			MainWindow.findChild(QtWidgets.QLineEdit, "cvfx"+str(i+5)+"tempval").setText("20.00")

		for i in range(0,len(self.signalnulls)):
			MainWindow.findChild(QtWidgets.QLabel,"NullLabel"+str(i)).setText(_translate("MainWindow",self.signalnulls[i]))
			MainWindow.findChild(QtWidgets.QPushButton,"Null"+str(i)).clicked.connect(lambda: self.toggleswitched(MainWindow))

				
		self.flowio.setText(_translate("MainWindow", "Flow OFF"))
		
		self.cvimode.setText(_translate("MainWindow", "Mode: CVI"))

		self.valvesourcelabel.setText(_translate("MainWindow","Valve Source"))
		self.flowsourcelabel.setText(_translate("MainWindow", " Flow Source"))
		self.cvfx0wrlabel.setText(_translate("MainWindow", "    cvfx0wr"))
		self.cvfx2wrlabel.setText(_translate("MainWindow", "    cvfx2wr"))
		self.cvfx3wrlabel.setText(_translate("MainWindow", "    cvfx3wr"))
		self.cvfx4wrlabel.setText(_translate("MainWindow", "    cvfx4wr"))
		self.cvf1wrlabel.setText(_translate("MainWindow", "     cvf1wr"))
		self.cvfx0wr.setText(_translate("MainWindow","0.00"))
		self.cvfx2wr.setText(_translate("MainWindow","0.00"))
		self.cvfx3wr.setText(_translate("MainWindow","0.00"))
		self.cvfx4wr.setText(_translate("MainWindow","0.00"))
		self.cvf1wr.setText(_translate("MainWindow","0.00"))	
		
		flowvalues = [0.00,2.00,5.00,2.00]
		for i in range(0,len(self.flowlabels)):
			MainWindow.findChild(QtWidgets.QLabel,self.flowlabels[i]).setText(_translate("MainWindow",str(self.flowedit[i])))
			MainWindow.findChild(QtWidgets.QLineEdit, self.flowedit[i]).setText(_translate("MainWindow",str(flowvalues[i])))
	
		MainWindow.findChild(QtWidgets.QLineEdit,self.flowedit[i]).setDisabled(True)
		
		#self.cvfx4.setDisabled(True)
				
		self.datafromdsm.setText(_translate("MainWindow", "Awaiting Data to be received. . . . ."))
		self.datatodsm.setText(_translate("MainWindow", "Awaiting Data to be sent. . . . ."))

		
		self.plottitles = ['H2O','ptdl','ttdl','cvf3','cvcnc1','cvcnc01','cvrho_tdl','cvrhoo_tdl','opcc','opcco']
		self.ylabels = ['Concentration (g/m^3)','Pressure (mbar)','Temperature (C)','y','y','y','y','y','y','y']
		self.dropdownlist.addItems(self.plottitles)
		
		#self.dropdownlistline2.addItem("")
		self.dropdownlistline2.addItems([""]+self.plottitles)
		
		self.dropdownlist2.addItems(self.plottitles)
		
		#self.dropdownlist2line2.addItem("")
		self.dropdownlist2line2.addItems([""]+self.plottitles)
		
		
		#Labeling Tabs on screen
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Operations"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Configuration"))
		
		for i in range(0,len(self.tablerowlabels)):
			item = self.tableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("MainWindow", "This is the new row"))
		for i in range(0,len(self.tablecolumnlabels)):
			item = self.tableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("MainWindow", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tableWidget.setSortingEnabled(False)
		#item = self.tableWidget.item(0, 0)
		#item.setText(_translate("MainWindow", "This is item 1,1"))
		
		#Cal Coeffs Table
		for i in range(0,len(self.caltablerowlabels)):
			item = self.caltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.caltablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("MainWindow", "This is the new row"))
		for i in range(0,len(self.caltablecolumnlabels)):
			item = self.caltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.caltablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("MainWindow", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.caltableWidget.setSortingEnabled(False)

		#More Cal Coeffs Table
		for i in range(0,len(self.morecaltablerowlabels)):
			item = self.morecaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.morecaltablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("MainWindow", "This is the new row"))
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.morecaltablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("MainWindow", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.morecaltableWidget.setSortingEnabled(False)
		
		
		
		#TDL Cal Coeffs Table
		for i in range(0,len(self.tdlcaltablerowlabels)):
			item = self.tdlcaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tdlcaltablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("MainWindow", "This is the new row"))
		for i in range(0,len(self.tdlcaltablecolumnlabels)):
			item = self.tdlcaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.tdlcaltablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("MainWindow", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tdlcaltableWidget.setSortingEnabled(False)
		
		
		#OPC Cal Coeffs Table
		for i in range(0,len(self.opccaltablerowlabels)):
			item = self.opccaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("MainWindow",self.opccaltablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("MainWindow", "This is the new row"))
		for i in range(0,len(self.opccaltablecolumnlabels)):
			item = self.opccaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("MainWindow",self.opccaltablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("MainWindow", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.opccaltableWidget.setSortingEnabled(False)
		
		self.updatecals.setText(_translate("MainWindow", "Press to SAVE new calibrations"))
		
		
		#Starting index for which data is plotted
		self.dropdownindices = [0,0,0,0]
		#self.dropdownindex = 0
		#self.dropdownindex2 = 0
		self.dropdownlist.currentIndexChanged.connect(self.CVIreplot)#self.selectionchange)
		self.dropdownlistline2.currentIndexChanged.connect(self.CVIreplot)#selectionchange)
		self.dropdownlist2.currentIndexChanged.connect(self.CVIreplot)#selectionchange)
		self.dropdownlist2line2.currentIndexChanged.connect(self.CVIreplot)#selectionchange)
#		self.dropdownlist2.currentIndexChanged.connect(self.selectionchange2)

		#connect the signal 'clicked' to the slot 'connecting'
		self.connect.clicked.connect(self.connecting)
		self.disconnect.clicked.connect(self.disconnecting)
		#how to perform a programmatic click
		#self.connect.click()
		
		#Counterflow excess to always be referenced to
		self.cfexcess = 0.5
		
		self.devconnect.clicked.connect(self.addinstruments)
		self.devdisconnect.clicked.connect(self.removeinstruments)	
		
		self.calarray = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4','cvfx5','cvfx6','cvfx7','cvfx8',
			'cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai',
			'RHOD','CVTBL','CVTBR','CVOFF1','LTip',
			'tdl_param_0','tdl_param_1','tdl_param_2','tdl_param_3','opc_pressure']
		self.calvalues = np.c_[[0.0]*len(self.calarray),[0.0]*len(self.calarray),[0.0]*len(self.calarray),[0.0]*len(self.calarray)]
		self.NIDASHeader = '#\n# dateFormat="%Y %b %d %H:%M:%S"\n# timeZone = "UTC"\n#'
		
		#Create filenaming structure
		self.basedir = 'C:/CVI/'
		self.project = 'Testing'
		
		self.tmpfile = 'rollovervalues.txt'
		
		self.path = self.basedir + '/' + self.project + '/'
		self.calpath = self.basedir + '/Calibrations' + '/' 
		self.file = time.strftime("%y%m%d%H.%Mq")
						
		self.header = 'dsmtime, INLET, FXflows,  valve_changes, cvf1R, cvfx0R, cvfx1R, cvfx2R,  cvfx3R, cvfx4R, cvfx5R, cvfx6R, cvfx7R, cvfx8R, cvpcnR, cvttR, cvtpR, cvtsR, cvtcnR, cvtaiR, cvpcnC, cvttC, cvtpC, cvtsC, cvtcnC, cvtaiC, cvf1, cvfx0c, cvfx1c, cvfx2c,  cvfx3c, cvfx4c, cvfx5c, cvfx6c,  cvfx7c, cvfx8c, cvl, cvrhoo_tdl,   cvrho_tdl, cvrad, cvcfact_tdl,  cvf3, cvtas, cvcnc1, cvcno1, cvcfact,  cvftc, cvrh, cvdp, cvfx0WR, cvfx2WR, cvfx3WR,  cvfx4WR, cvfx1WR, cnt1, H2O_TDL,  pTDL, tTDL, TDLsignalL,TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec,TDLtrans, opcc, opcco, opcnts, opcflow, opcc_Pcor, opcco_Pcor, opcc_pres_mb, H2O_PIC_cvrtd, 180, HDO'
		self.header += '\n'
		
		self.readcalsfromfiles(MainWindow)
		
		self.updatecals.clicked.connect(lambda: self.savecalibrations(MainWindow))
		
		#connect the signal 'clicked' to the slot 'flowsourcechanged'
		self.flowsource.clicked.connect(lambda: self.toggleswitched(MainWindow))
		self.flowio.clicked.connect(lambda: self.toggleswitched(MainWindow))
		self.cvimode.clicked.connect(lambda: self.toggleswitched(MainWindow))
		self.valvesource.clicked.connect(lambda: self.toggleswitched(MainWindow))
		
		self.auxdev1.setDisabled(True)
		self.auxdev2.setDisabled(True)
		self.auxdev3.setDisabled(True)
		self.auxdev4.setDisabled(True)
		
		for i in range(0,4):
			for j in range(0,len(self.auxdevtoggles)):
				MainWindow.findChild(QtWidgets.QPushButton,'cvfx'+str(i+5)+self.auxdevtoggles[j]).clicked.connect(lambda: self.toggleswitched(MainWindow))
		
		###REMOVE ONCE TEXT FILE DEFAULTS ARE LOADED###
		self.flowsource.click()
		self.valvesource.click()
		
		self.numchanges = 0 #Number for tracking how many times a connection or disconnection routine has been run.
		
		self.flowlimits = [0]*4
		
		self.cvfxoptions = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,[0]*4]
		#First index is the option, second index is the instrument
		#mode,modeval,datatype,tmpsource,tempval,i/o
		self.internalflowsetpts = [0.00]*4
		
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
			'Instructional message 2'
			,
			'Instructional message 3'
			,
			'Instructional message 4'
			,
			'Instructional message 5']
		self.mainstatus.setText(self.mainstatuslist[0])

			
			
			#'To begin operations, press the START button at the upper portion of the screen and ]
		
		# creates a server and starts listening to TCP connections
		self.runconnection = False
		
		#Create default data array for plotting from
		self.plotdata = np.c_[[-9999]*(self.dropdownlist.count()+1)]#np.c_[[np.nan]*4]
		self.tabledata = np.c_[[-9999]*(len(self.tablerowlabels)),[-9999]*(len(self.tablerowlabels)),[-9999]*len(self.tablerowlabels)]
		self.dim = self.plotdata.shape
		
		#Force selection change on the plot to the default to
		#Initialize title and axes?
		#self.selectionchange(0)
		#self.selectionchange2(0)
		
		#timer.timeout.connect(self.CVIreplot)
		#timer.timeout.connect(lambda: self.CVIreplot(0))
		#timer.start(300)
		
		#Create server loop
			
		self.server_loop = asyncio.get_event_loop()				

		
	def addinstruments(self, MainWindow):		
		self.devconnect.hide()
		self.devdisconnect.hide()
		#self.tabWidget.setTabEnabled(0, False)
		#self.tabWidget.setTabEnabled(1, False)
		
		self.auxdev1.setChecked(self.v1.isChecked())
		self.auxdev2.setChecked(self.v2.isChecked())
		self.auxdev3.setChecked(self.v3.isChecked())
		self.auxdev4.setChecked(self.v4.isChecked())
		
		
		self.initialcfexcess = float(self.cvf3cw.text())
		self.cfexcess = self.initialcfexcess + float(self.offset.text())
		#The above should allow the other thread to begin updating cfexcess
		time.sleep(float(self.delay.text()))

		self.devinstruct.setText("The Counterflow has been increased... \nPlease select the instruments that are to be connected and press continue")
		app.processEvents()
		self.devcontinue.show()
		self.devcancel.show()
		
		#Need to show each of the device addition toggles (Should be hidden by default)
		self.auxdev1.setDisabled(False)
		self.auxdev2.setDisabled(False)
		self.auxdev3.setDisabled(False)
		self.auxdev4.setDisabled(False)
		
		self.devcontinue.clicked.connect(lambda: self.updateinstruments(True))
		self.devcancel.clicked.connect(lambda: self.gradualflowreduction(True))		
		
	def removeinstruments(self, MainWindow):
		self.devconnect.hide()
		self.devdisconnect.hide()
		#self.tabWidget.setTabEnabled(0, False)
		#self.tabWidget.setTabEnabled(1, False)
		
		self.auxdev1.setChecked(self.v1.isChecked())
		self.auxdev2.setChecked(self.v2.isChecked())
		self.auxdev3.setChecked(self.v3.isChecked())
		self.auxdev4.setChecked(self.v4.isChecked())
		
		self.initialcfexcess = float(self.cvf3cw.text())
		self.cfexcess = self.initialcfexcess + float(self.offset.text())
		#The above should allow the other thread to begin updating cfexcess
		time.sleep(float(self.delay.text()))

		self.devinstruct.setText("The Counterflow has been increased!\n\nOperators may now begin performing operations. \n\nPress continue once completed")
		app.processEvents()
		self.devcontinue.show()
		self.devcancel.show()
		self.devcontinue.clicked.connect(lambda: self.updateinstruments(False))
		self.devcancel.clicked.connect(self.gradualflowreduction)
		
	def updateinstruments(self, connecting):
		self.devcontinue.disconnect()
		#time.sleep(3)
		self.numchanges += 1
		if(connecting) : 
			#ui.MainWindow.findChild(QtWidgets.QPushButton,'cvfx'+str(i+5)+self.auxdevtoggles[j]).clicked.connect(lambda: self.toggleswitched(MainWindow))
			self.auxdev1.setDisabled(True)
			self.auxdev2.setDisabled(True)
			self.auxdev3.setDisabled(True)
			self.auxdev4.setDisabled(True)
			
			self.v1.setChecked(self.auxdev1.isChecked())
			self.v2.setChecked(self.auxdev2.isChecked())
			self.v3.setChecked(self.auxdev3.isChecked())
			self.v4.setChecked(self.auxdev4.isChecked())
			time.sleep(3)
			self.devinstruct.setText("The Valves have been switched... \n\nOnce operators are finished, press continue")
		else: 
			self.auxdev1.setDisabled(False)
			self.auxdev2.setDisabled(False)
			self.auxdev3.setDisabled(False)
			self.auxdev4.setDisabled(False)
			self.devinstruct.setText("Please select the instruments that are to be disconnected and press continue")
		app.processEvents()
		self.devcontinue.clicked.connect(lambda: self.gradualflowreduction(connecting))

	def gradualflowreduction(self, connecting):		
	
		self.devcontinue.disconnect()
		self.devcancel.disconnect()
		
		if(not connecting): 
			self.auxdev1.setDisabled(True)
			self.auxdev2.setDisabled(True)
			self.auxdev3.setDisabled(True)
			self.auxdev4.setDisabled(True)
			self.v1.setChecked(self.auxdev1.isChecked())
			self.v2.setChecked(self.auxdev2.isChecked())
			self.v3.setChecked(self.auxdev3.isChecked())
			self.v4.setChecked(self.auxdev4.isChecked())
			time.sleep(3)
		
		
		while self.cfexcess > self.initialcfexcess:
			self.cfexcess = self.cfexcess - 0.5
			self.devinstruct.setText("Flow is returning to normal. \n\nDO NOT PRESS ANY BUTTONS \n  Current Flow: "+str(self.cfexcess)+"\n  Goal: "+str(self.initialcfexcess))
			app.processEvents()
			time.sleep(2)
		
		if self.cfexcess != self.initialcfexcess:
			self.cfexcess = self.initialcfexcess	
			self.devinstruct.setText("Flow is returning to normal. \n\nDO NOT PRESS ANY BUTTONS \n  Current Flow: "+str(self.cfexcess)+"\n  Goal: "+str(self.initialcfexcess))
			app.processEvents()
			time.sleep(2)		
		
		self.devinstruct.setText("Flow has returned to normal.\n\nYou may now resume normal operation")
		app.processEvents()
		
		self.auxdev1.setDisabled(True)
		self.auxdev2.setDisabled(True)
		self.auxdev3.setDisabled(True)
		self.auxdev4.setDisabled(True)
		
		self.tabWidget.setTabEnabled(0, True)
		self.tabWidget.setTabEnabled(1, True)
		self.devcontinue.hide()
		self.devcancel.hide()	
		self.devconnect.show()
		self.devdisconnect.show()
		
		self.devinstruct.setText(self.defaultdevinstruct)
		
	def loadprogramdefaults(self, MainWindow):
		print("Hi")
	
	def saveprogramdefaults(self, MainWindow):
		print("Hi")

		
	def readcalsfromfiles(self, MainWindow):	
		_translate = QtCore.QCoreApplication.translate

		for i in range(0,len(self.calarray)):
			with open(self.calpath + self.calarray[i]+'.dat', "rb") as f:
				first = f.readline()      # Read the first line.
				f.seek(-2, 2)             # Jump to the second last byte.
				while f.read(1) != b"\n": # Until EOL is found...
					f.seek(-2, 1)         # ...jump back the read byte plus one more.
				last = f.readline() 
				f.close()
			calinput = last.decode('utf-8').split()#('\t')
			calinput = [float(i) for i in calinput[-4:]]
			for j in range(0,4):
				self.calvalues[i,j] = calinput[j]

		#print(self.calvalues)
			
			
		for i in range(0,len(self.caltablerowlabels)):
			for j in range(0, len(self.caltablecolumnlabels)):
				item = self.caltableWidget.item(i,j)
				try:
					item.setText(_translate("MainWindow",str(self.calvalues[i,j])))# = float(item.text())
				except ValueError:
					item.setText(_translate("MainWindow",str(0.0)))
		
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.item(0,i)
			try:
				item.setText(_translate("MainWindow",str(self.calvalues[len(self.caltablerowlabels)+i,0])))# = float(item.text())
			except ValueError:
				item.setText(_translate("MainWindow",str(0.0)))
				
		for i in range(0, len(self.tdlcaltablerowlabels)):
			for j in range(0,len(self.tdlcaltablecolumnlabels)):
				item = self.tdlcaltableWidget.item(i,j)
				try:
					item.setText(_translate("MainWindow",str(self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels),j])))# = float(item.text())
				except ValueError:
					item.setText(_translate("MainWindow",str(0.0)))
			
		for i in range(0, len(self.opccaltablerowlabels)):
			for j in range(0,len(self.opccaltablecolumnlabels)):
				item = self.opccaltableWidget.item(i,j)
				try:
					item.setText(_translate("MainWindow",str(self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels)+len(self.tdlcaltablecolumnlabels),j])))# = float(item.text())
				except ValueError:
					item.setText(_translate("MainWindow",str(0.0)))

	def savecalibrations(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate

		for i in range(0,len(self.caltablerowlabels)):
			for j in range(0, len(self.caltablecolumnlabels)):
				item = self.caltableWidget.item(i,j)
				try:
					self.calvalues[i,j] = float(item.text())
				except ValueError:
					self.calvalues[i,j] = 0.0
		
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.item(0,i)
			try:
				self.calvalues[len(self.caltablerowlabels)+i,0] = float(item.text())
			except ValueError:
				self.calvalues[len(self.caltablerowlabels)+i,0] = 0.0
				
		for i in range(0, len(self.tdlcaltablerowlabels)):
			for j in range(0,len(self.tdlcaltablecolumnlabels)):
				item = self.tdlcaltableWidget.item(i,j)
				try:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels),j] = float(item.text())
				except ValueError:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels),j] = 0
					
		for i in range(0, len(self.opccaltablerowlabels)):
			for j in range(0,len(self.opccaltablecolumnlabels)):
				item = self.opccaltableWidget.item(i,j)
				try:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels)+len(self.tdlcaltablecolumnlabels),j] = float(item.text())
				except ValueError:
					self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels)+len(self.tdlcaltablecolumnlabels),j] = 0
		
		calupdatetext, contupdate = QInputDialog.getText(MainWindow, 'Text Input MainWindow', 'Please provide update comment. Press cancel to abort update')		
		#If cancel is clicked, ('', False)
		
		if contupdate:
			caltimestamp = 	time.strftime("%Y %b %d %H:%M:%S",time.gmtime())
			for i in range(0,len(self.calarray)):
				caloutput = [ "{:.6f}".format(x) for x in self.calvalues[i,:] ]
				caloutput = '\t'.join(caloutput)
				caloutput = '\n\n# '+ str(calupdatetext) + '\n' + caltimestamp+'\t'+caloutput
				if not os.path.isfile(self.calpath+self.calarray[i]+'.dat'):
					os.makedirs(os.path.dirname(self.calpath+self.calarray[i]+'.dat'), exist_ok=True)
					with open(self.calpath+self.calarray[i]+'.dat', "w") as f:
						f.write(self.NIDASHeader)#outputstring)	
						f.write(caloutput)
						f.close()
				else:
					with open(self.calpath+self.calarray[i]+'.dat', "a") as f:
						f.write(caloutput)
						f.close()
		
			
			
	def toggleswitched(self,MainWindow):
		if self.flowsource.isChecked() : self.flowsource.setText("Calculated")
		else: self.flowsource.setText("User Input")
		self.cvfx0wr.setDisabled(self.flowsource.isChecked())
		self.cvfx2wr.setDisabled(self.flowsource.isChecked())
		self.cvfx3wr.setDisabled(self.flowsource.isChecked())
		self.cvfx4wr.setDisabled(self.flowsource.isChecked())
		self.cvf1wr.setDisabled(self.flowsource.isChecked())
		
		
		
		if self.flowio.isChecked() : self.flowio.setText("Flow ON")
		else: self.flowio.setText("Flow OFF")
		if self.cvimode.isChecked() : self.cvimode.setText("Mode: Total")
		else: self.cvimode.setText("Mode: CVI")

		if self.valvesource.isChecked(): self.valvesource.setText("Calculated")
		else: self.valvesource.setText("User Input")
		self.v1.setDisabled(self.valvesource.isChecked())
		self.v2.setDisabled(self.valvesource.isChecked())
		self.v3.setDisabled(self.valvesource.isChecked())
		self.v4.setDisabled(self.valvesource.isChecked())
				
		#Naming toggles for external instruments
		self.auxdevtoggleoptions = [['User Input Below', 'Mass','User Input Below'],['DSM Input','Volume','cnt1']]
		for i in range(0,4):
			#tmpobject = MainWindow.findChild(QtWidgets.QLineEdit,'cvfx'+str(i+5)+'title')
			#tmpobject.setText('cvfx'+str(i+5))
			for j in range(0,len(self.auxdevtoggles)):
				tmpobject = MainWindow.findChild(QtWidgets.QPushButton,'cvfx'+str(i+5)+self.auxdevtoggles[j])
				if not tmpobject.isChecked(): tmpobject.setText(self.auxdevtoggles[j]+' : '+self.auxdevtoggleoptions[0][j] )
				else: tmpobject.setText(self.auxdevtoggles[j]+' : '+self.auxdevtoggleoptions[1][j] )		
		
		for i in range(0,len(self.signalnulls)):
			tmpobject = MainWindow.findChild(QtWidgets.QPushButton,'Null'+str(i))
			if not tmpobject.isChecked(): tmpobject.setText("Active")
			else: tmpobject.setText("Disabled")
			
	#Function runs when the "connect" button is clicked
	#Establishes server in separate thread for receiving data
	#	from DSM. Once established, it initializes a slot for
	#	replotting the data ~3 times a second.
	def connecting(self, MainWindow):
		#Check to make sure that connection was not attempted multiple times in succession
		self.disconnecting(MainWindow)
		self.statusindicatorlabel.setText("Ensuring Disconnection . . . . . . . ")
		self.statusindicatorlabel.setText("Initiating Connection . . . . . . . .")
		self.runconnection = True
		
		#asyncio.ensure_future(self.server_loop_in_thread)
		#implement parallel thread for server
		self.server_thread = threading.Thread(target=self.server_loop_in_thread, args = ())#args = (self,))#, args=(loop,))
		self.server_thread.start()			
		
		self.statusindicatorlabel.setText("Incoming data server has been established")	

		#counter for testing purposes to increment plot asbcissa
		self.counter = 0
		
		#Timer for establishing plotting frequency
		timer.timeout.connect(self.CVIreplot)
		timer.start(300)

	#Server code to be established in parallel thread
	def server_loop_in_thread(self):
		asyncio.set_event_loop(self.server_loop)
		self.server_coro = self.server_loop.create_server(IncomingServer, '', int(self.portin.text()))#(self.hostin.text()),int(self.portin.text()))#'127.0.0.1',8888)
		self.server = self.server_loop.run_until_complete(self.server_coro)#greet_every_two_seconds)#self.coro)#greet_every_two_seconds())
	#	server_loop.run_until_complete(server.wait_closed())
		self.server_loop.run_forever() #Is this necessary?
			
	#Code run when "disconnect" button is clicked.
	#Once clicked, server thread is joined and closed
	#and connected indicator is reset to red
	def disconnecting(self, MainWindow):
		if not self.runconnection :
			self.statusindicatorlabel.setText("No connection to disconnect")
			#print('No connection sequence has been run')
		else :
			self.statusindicatorlabel.setText("Initiating Disconnect . . . . . . .")

			# Close the server
			self.server_loop.stop()
			self.server.close()
			self.server_thread.join()
			self.server_loop.run_until_complete(self.server.wait_closed())
			
			self.statusindicatorlabel.setText("Disconnect Successful")
			self.runconnection = False
			
			#Resets the connected? indicator to red
			palette = QtGui.QPalette()
			brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
			palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
			palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
			palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
			#palette.setColor(QtGui.QPalette.Background,QtGui.QColor(255,255,0))
			self.graphicsView.setPalette(palette)
		
	#this is the function that is run when the plot data
	#selection is changed. It then changes plot titles and axes
	#and plots the new set of data.
	#def selectionchange(self,i):

	#program for replotting the data based on which data
	#selection has been chosen
	def CVIreplot(self):#,plotnumber):		
	
		self.CVIplotline2.setGeometry(self.CVIplot.plotItem.vb.sceneBoundingRect())
		self.CVIplotline2.linkedViewChanged(self.CVIplot.plotItem.vb,self.CVIplotline2.XAxis)

		self.CVIplot2line2.setGeometry(self.CVIplot2.plotItem.vb.sceneBoundingRect())
		self.CVIplot2line2.linkedViewChanged(self.CVIplot2.plotItem.vb,self.CVIplot2line2.XAxis)
		
		_translate = QtCore.QCoreApplication.translate
		for i in range(0,len(self.tablerowlabels)):
			item = ui.tableWidget.item(i, 0)
			item.setText(_translate("MainWindow",str(self.tabledata[i,0])))
			item = ui.tableWidget.item(i, 1)
			item.setText(_translate("MainWindow",str(self.tabledata[i,1])))
			item = ui.tableWidget.item(i, 2)
			item.setText(_translate("MainWindow",str(self.tabledata[i,2])))
		
		#derp = [x for x in range(0,10)]
		#derpy = [x for x in range(100,110)]
		#derpyy = [x for x in range(200,210)]
		#derpyy = derpyy[::-1]
		#derpyyy = [x for x in range(300,310)]

		#self.plotdata = np.c_[derp,derpy,derpyy,derpyyy,derp,derpy,derpyy,derpyyy,derp,derpy]
		#self.plotdata = np.transpose(self.plotdata)

		self.CVIplot.plot(self.plotdata[0,:], self.plotdata[self.dropdownlist.currentIndex()+1,:], clear = True)
		self.CVIplot2.plot(self.plotdata[0,:], self.plotdata[self.dropdownlist2.currentIndex()+1,:], clear = True)
		#self.CVIplot.plot([0,1,2,3],[0,1,2,3])
		#self.CVIplotline2.addItem(pyqtgraph.PlotCurveItem([0,1,2,3],[10,2,1,0],pen='b'))
		self.CVIplotline2.clear()
		self.CVIplot2line2.clear()
		
		self.CVIplot.setTitle(self.plottitles[self.dropdownlist.currentIndex()])
		self.CVIplot.setLabel('left',text = self.ylabels[self.dropdownlist.currentIndex()])
		
		self.CVIplot2.setTitle(self.plottitles[self.dropdownlist2.currentIndex()])
		self.CVIplot2.setLabel('left',text = self.ylabels[self.dropdownlist2.currentIndex()])

		if (self.dropdownlistline2.currentIndex() != 0) : 
			self.CVIplotline2.addItem(pyqtgraph.PlotCurveItem(self.plotdata[0,:], self.plotdata[self.dropdownlistline2.currentIndex(),:],pen='b',clear=True))
			self.CVIplot.setTitle(self.plottitles[self.dropdownlist.currentIndex()]+' & '+self.plottitles[self.dropdownlistline2.currentIndex()-1])
			self.CVIplot.getAxis('right').setLabel(self.ylabels[self.dropdownlistline2.currentIndex()-1], color = '#0000ff')
			#self.CVIplot.setLabel('right',text = self.ylabels[self.dropdownlistline2.currentIndex()])
		if (self.dropdownlist2line2.currentIndex() != 0) : 
			self.CVIplot2line2.addItem(pyqtgraph.PlotCurveItem(self.plotdata[0,:], self.plotdata[self.dropdownlist2line2.currentIndex(),:],pen='b',clear=True))
		
		#if(self.dropdownlist.currentIndex() != self.dropdownlistline2.currentIndex()):
		#	self.CVIplot2.setLabel('right',text = self.ylabels[self.dropdownlistline2.currentIndex()])
		'''
		if plotnumber == 1 or plotnumber == 0:
			self.CVIplot.plot(self.plotdata[0,:] , self.plotdata[self.dropdownindex+1,:], clear = True)
		if plotnumber == 2 or plotnumber == 0 :
			x = [0,1,2,3,4,5]
			y = [1,2,3,4,5,6]
			z = [2,3,4,5,6,7]
			self.CVIplot2.plot(x,y, pen=(255,0,0), clear = True)
			self.CVIplot2.plot(x,z, pen=(0,255,0))
#			self.CVIplot2.plot(self.plotdata[0,:] , self.plotdata[self.dropdownindex2+1,:], clear = True)
		'''	
		app.processEvents()

#Class for listening for client connections from the DSM
class IncomingServer(asyncio.Protocol):
	def connection_made(self, transport):
		'''
		Called when a connection is made.
		The argument is the transport representing the pipe connection.
		To receive data, wait for data_received() calls.
		When the connection is closed, connection_lost() is called.
		'''
		self.peername = transport.get_extra_info('peername')
		#print('Connection from {}'.format(peername))
		self.transport = transport
		
		#Changes connected? indicator to green!!
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
		ui.graphicsView.setPalette(palette)
		
		#Now that the DSM has connected, a client can be established
		#to send data back to the DSM
		self.client_sock = socket.socket()
		self.client_sock.connect((ui.ipaddress.text(), int(ui.portout.text())))	

		
	def data_received(self, data):
		'''
		Called when some data is received.
		The argument is a bytes object.		
		'''
		#data is the byte string that came from DSM
		
		#Update status indicator to show connection
		#print('Data received: {!r}'.format(message))
		ui.statusindicatorlabel.setText('Data is being received from {}'.format(self.peername))
		
		#Decode data into a string
		datain = data.decode(encoding='utf-8')
		
		#Update front panel with data that has just been received
		ui.datafromdsm.setText(str(datain).replace(",", ", "))
		
		#Null string just in case
		dataout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		
		#If data looks normal (i.e. not a header) then proceed.
		if(datain[0] != 'N'):
			#Flow boolean for deciding if flow is on or off
			#flowonoff = True
			
			#These are the valve positions selected from the
			#front panel.
			
			'''
			valvepositions = [0]*4
			
			if ui.v1.isChecked() : valvepositions[0] = 1
			else: valvepositions[0] = 0
			if ui.v2.isChecked() : valvepositions[1] = 1
			else: valvepositions[1] = 0			
			if ui.v3.isChecked() : valvepositions[2] = 1
			else: valvepositions[2] = 0
			if ui.v4.isChecked() : valvepositions[3] = 1
			else: valvepositions[3] = 0
			'''
			
			
			#CVI mode corresponding to "CVI"(false) and "total"(true)
			#NOT YET IMPLEMENTED
			#cvimode = False
			
			#Take input string and convert to float array for 
			#	crunchcvi code to process
			#input = data.decode(encoding='utf-8')
			input = datain.split(',')
			input = [float(i) for i in input]
			
			
			
			#self.calvalues is the array with all of the calibrations
			#The first 16 rows contain C0, C1, C2 in their respective columns
			#The next 5 rows contain RHOD, CVTBL, CVTBR, cvoff1, and LTip in the first column
			#The next 4 rows contain C0, C1, C2, and C3
			C0 = np.r_[ui.calvalues[:16,0]]
			C1 = np.r_[ui.calvalues[:16,1]]
			C2 = np.r_[ui.calvalues[:16,2]]
			more = np.r_[ui.calvalues[16:21,0]]
			#tdl_cals
			tdl_cals = np.c_[ui.calvalues[21:25,0], ui.calvalues[21:25,1], ui.calvalues[21:25,2], ui.calvalues[21:25,3]]
			opc_cals = np.r_[ui.calvalues[25,0],ui.calvalues[25,1]]
			
			tdl_cals = np.transpose(tdl_cals)
			
			####MAY NEED TO TRANSPOSE TDL_CALS######
			
			
			#tdl_cals = [[0.00000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
			#myArray=[[1,2],[3,4]]
			#tdl_poly_coeffs = [0]*4
	
			#tdl_poly_coeffs[0]=tdl_cals[0][0]+tdl_cals[0][1]*tdl_data[1]+tdl_cals[0][2]*tdl_data[1]*tdl_data[1]+tdl_cals[0][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			#tdl_poly_coeffs[1]=tdl_cals[1][0]+tdl_cals[1][1]*tdl_data[1]+tdl_cals[1][2]*tdl_data[1]*tdl_data[1]+tdl_cals[1][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			#tdl_poly_coeffs[2]=tdl_cals[2][0]+tdl_cals[2][1]*tdl_data[1]+tdl_cals[2][2]*tdl_data[1]*tdl_data[1]+tdl_cals[2][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			#tdl_poly_coeffs[3]=tdl_cals[3][0]+tdl_cals[3][1]*tdl_data[1]+tdl_cals[3][2]*tdl_data[1]*tdl_data[1]+tdl_cals[3][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]

			'''
			#Input values 3 -> 18 is composed of the "data" values above
			data = input[3:19] 
			tdl_data = input[19:29] 
			opc_data = input[29:33]
	
			#if data <= -99, use stored value from before
			#NEEDS IMPLEMENTATION, CURRENTLY USING SAMPLE VALUES
			data_default = [-0.071,-0.050,-0.025,-0.497,0.008,0.019,0.025,0.016,-0.025,2.463,2.365,0.766,0.715,0.956,0.110,0.881]
			for i in range(0,15):
				if data[i]<=-99 : data[i] = data_default[i]#0#0.0001

			#if tdl_data <= -1, use stored value from before, except for TDLzero which if equal to -99.99, use stored value.
			#NEEDS IMPLEMENTATION, CURRENTLY USING SAMPLE VALUES
			tdl_default = [0.402,817.033,43.943,1680.670,10840.300,272,-4115.330,35.093,43.267,35.093]
			for i in range(0,10):
				if tdl_data[i]<=-1: tdl_data[i] = tdl_default[i]#tdl_data[i] = 0.0001#0.0001#0.0001
			'''
			
			if not os.path.isfile(ui.basedir+ui.tmpfile):
				rolloverinput = input#[78470.5,-99.99,0,-0.0681376,-0.0563926,0.00943004,-0.485442,0.00214072,0.022746,0.0242618,0.0143435,-0.0278935,2.46137,2.36268,0.697071,0.410852,0.670648,0.108651,0.12196,5.086,821.973,33.8967,19949.7,11266.7,282,-4126,26.2067,30.2633,0.886,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
				#inputdefault = [78470.5,-99.99,0,-0.0681376,-0.0563926,0.00943004,-0.485442,0.00214072,0.022746,0.0242618,0.0143435,-0.0278935,2.46137,2.36268,0.697071,0.410852,0.670648,0.108651,0.12196,5.086,821.973,33.8967,19949.7,11266.7,282,-4126,26.2067,30.2633,0.886,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
				inputstring = [ "{:11.10g}".format(x) for x in rolloverinput ]
				inputstring = ','.join(inputstring)
				inputstring += '\n'
							#if not os.path.isfile(ui.basedir+ui.tmpfile):
				os.makedirs(os.path.dirname(ui.basedir+ui.tmpfile), exist_ok=True)
				with open(ui.basedir+ui.tmpfile, "w") as f:
									#f.write(ui.header)#outputstring)	
					f.write(inputstring)
					f.close()
			else:
				with open(ui.basedir + ui.tmpfile, "rb") as f:
					first = f.readline()      # Read the first line.
					f.close()
				rolloverinput = first.decode('utf-8').split(',')#('\t')
			
			rolloverinput = [float(x) for x in rolloverinput]
			
			for i in range(3,19):
				if input[i] <= -99: input[i] = (rolloverinput[i])#inputdefault[i] #NEEDS TO USE PREVIOUS VALUE
			#if tdl_data <= -1, use stored value from before, except for TDLzero which if equal to -99.99, use stored value.
			#TDL_ZERO is index 6 (index 25 of input)
			for i in [19,20,21,22,23,24,26,27,28] :
				if input[i] <= -1: input[i] = (rolloverinput[i])#inputdefault[i] #Needs to use previous value.
			if input[25] == -99.99: input[25] = (rolloverinput[25])#inputdefault[25]
			
			#WSPD
			if input[1] < 4 or input[1] > 300 :
				input[1] = rolloverinput[1]
			
			rolloverinput = input#[78470.5,-99.99,0,-0.0681376,-0.0563926,0.00943004,-0.485442,0.00214072,0.022746,0.0242618,0.0143435,-0.0278935,2.46137,2.36268,0.697071,0.410852,0.670648,0.108651,0.12196,5.086,821.973,33.8967,19949.7,11266.7,282,-4126,26.2067,30.2633,0.886,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
			#inputdefault = [78470.5,-99.99,0,-0.0681376,-0.0563926,0.00943004,-0.485442,0.00214072,0.022746,0.0242618,0.0143435,-0.0278935,2.46137,2.36268,0.697071,0.410852,0.670648,0.108651,0.12196,5.086,821.973,33.8967,19949.7,11266.7,282,-4126,26.2067,30.2633,0.886,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99,-99.99]
			inputstring = [ "{:11.10g}".format(x) for x in rolloverinput ]
			inputstring = ','.join(inputstring)
			inputstring += '\n'
						#if not os.path.isfile(ui.basedir+ui.tmpfile):
			#os.makedirs(os.path.dirname(ui.basedir+ui.tmpfile), exist_ok=True)
			with open(ui.basedir+ui.tmpfile, "w") as f:
								#f.write(ui.header)#outputstring)	
				f.write(inputstring)
				f.close()
			
			'''
			Code just in case we want to add a timestamp to the rollover data.
#			if contupdate:
			tmptimestamp = 	time.strftime("%Y %b %d %H:%M:%S",time.gmtime())
			for i in range(0,len(self.calarray)):
				#caloutput = [ "{:.6f}".format(x) for x in self.calvalues[i,:] ]
				#caloutput = '\t'.join(caloutput)
				#caloutput = '\n\n# '+ str(calupdatetext) + '\n' + caltimestamp+'\t'+caloutput
				if not os.path.isfile(self.calpath+self.calarray[i]+'.dat'):
					os.makedirs(os.path.dirname(self.calpath+self.calarray[i]+'.dat'), exist_ok=True)
					with open(self.calpath+self.calarray[i]+'.dat', "w") as f:
						f.write(self.NIDASHeader)#outputstring)	
						f.write(caloutput)
						f.close()
			'''
			
			#Taking the null signals from the instrument panel.....
			nullsignals = [0]*16
			for i in range(0,len(ui.signalnulls)):
				nullsignals[i] = int(ui.MainWindow.findChild(QtWidgets.QPushButton,"Null"+str(i)).isChecked())
			#print(nullsignals)
				
			#flowedit ===== ['cvfx0','cvfx2','cvfx3','cvfx4']	
			#flowlimits = [0,2,5,2]
			for i in range(0,4):
				if ui.MainWindow.findChild(QtWidgets.QLineEdit,ui.flowedit[i]).text() != '': 
					ui.flowlimits[i] = float(ui.MainWindow.findChild(QtWidgets.QLineEdit,ui.flowedit[i]).text())
				
				
				
			#self.auxdevtoggles = ['mode','datatype','tmpsrc']
			#self.auxdevtoggleslist = ['title','mode','dataval','datatype','tmpsrc','tempval']
			#cvfxoptions = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4]
			#First index is the option, second index is the instrument
			for i in range(0,4):
				for j in range(1,len(ui.auxdevtoggleslist)):
					if j in [0,2,5]:
						tmpobject = ui.MainWindow.findChild(QtWidgets.QLineEdit,'cvfx'+str(i+5)+ui.auxdevtoggleslist[j])
						if tmpobject.text() != '': ui.cvfxoptions[j][i] = float(tmpobject.text())
					else:
						tmpobject = ui.MainWindow.findChild(QtWidgets.QPushButton,'cvfx'+str(i+5)+ui.auxdevtoggleslist[j])
						ui.cvfxoptions[j][i] = int(tmpobject.isChecked())
				
			#Connection status of individual channels	
			ui.cvfxoptions[0][0] = int(ui.v1.isChecked())
			ui.cvfxoptions[0][1] = int(ui.v2.isChecked())
			ui.cvfxoptions[0][2] = int(ui.v3.isChecked())
			ui.cvfxoptions[0][3] = int(ui.v4.isChecked())

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
			
			#output, calibrated = cvioutput( input , ui.flowlimits, ui.cfexcess, ui.cvfxoptions, nullsignals, ui.flowio.isChecked(), ui.cvimode.isChecked(), C0, C1, C2, more, tdl_cals, opc_cals)
			
			#def cvioutput( input, ui.flowlimits, cfexcess, cvfxoptions, nullsignals, flowonoff, cvimode, C0, C1, C2, more, tdl_cals, opc_cal):
			
			#input = input
			#ui.flowlimits = ui.flowlimits
			#cfexcess = ui.cfexcess
			#nullsignals = nullsignals
			#flowonoff = ui.flowio.isChecked()
			#cvimode = ui.cvimode.isChecked()
			#C0 = C0; C1 = C1; C2 = C2
			#more = more; tdl_cals = tdl_cals; opc_cal = opc_cals
			
			
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

			#Input values 3 -> 18 is composed of the "data" values above
			data = input[3:19] ; tdl_data = input[19:29] ; opc_data = input[29:33]
	
			#opc_cal input from files
			#NEEDS TO BE ADDED TO CALIBRATION SPACE, #opc_cal = [10.55600, 22.22200]
	
			opc_press = opc_cals[0] + opc_cals[1]*opc_data[2] #opc_data[2] corresponds to opc_pres_raw	
	
			#Array to hold calibration coefficients for flows from inputs
			calcoeffs = [0]*23
			for i in range(0,6):
				calcoeffs[i*3] = C0[i]; calcoeffs[(i*3)+1] = C1[i]; calcoeffs[(i*3)+2] = C2[i]
				#clusters of three are, #c0cvf1...c2cvf1, #c0cvfx0..c2cvfx0, #.............., #c0cvfx4..c2cvfx4
		
			#Append "more" calibration coefficients to array
			for i in range(18,23): calcoeffs[i] = more[i-18]
		
			#Perform default calibration of flows, pressures, temps, etc., #based on calibtraion arrays
			calibrated = [0]*16	
			for i in range(0,16): calibrated[i] = C0[i] + C1[i]*data[i] + C2[i]*data[i]**2
		
			#cvfxtemp ~ default temps; #cvfxtempsource ~ 1 is cnt1, 0 usrinput; #cvfsw ~ is instrument connected
			#cvfxmode ~ 1 is calculated, 0 is usrinput;  #cvfxdatatype ~ 0 is Mass, 1 is Volume; #cvfxalt ~ USER INPUT FLOWS	
							
			cvfxtemp = cvfxoptions[5][:]; cvfxtempsource = cvfxoptions[4][:]; cvfxsw = cvfxoptions[0][:]
			cvfxmode = cvfxoptions[1][:]; cvfxalt = cvfxoptions[2][:]; cvfxdatatype = cvfxoptions[3][:]	
	
			#Modifications to the flow based on if there are data,
			#	mass vs. volume input, etc.
			for i in range(0,4):
				if cvfxtempsource[i] == 1 : cvfxtemp[i] = calibrated[14]
				else: cvfxtemp[i] = cvfxtemp[i]
				if cvfxsw[i] == 0 : calibrated[i+6] = 0
				else:
					if cvfxmode[i] == 1 : calibrated[i+6] = C0[i+6] + C1[i+6]*data[i+6] + C2[i+6]*data[i+6]**2
					else: calibrated[i+6] = cvfxalt[i] #USER ENTERED FLOW
					if cvfxdatatype[i] == 1 : calibrated[i+6] = calibrated[i+6]*(calibrated[10]/1013.23)*(294.26/(cvfxtemp[i]+273.15)) #calibrated[10] is cvpcn				

			#Calibration of opc_data parameters and cvfx4
			opc_flow = C0[5] + opc_data[1]*C1[5] #opc_data[1] corresponds to opc_flow_raw	
			calibrated[5] = opc_flow*(calibrated[10]/1013.23)*(294.26/(cvfxtemp[1]+273.15)) #cvfxtemp[i] corresponds to cvfx6temp (user input)

			#For nulling a few of the signals
			for i in range(0,16):
				if nullsignals[i] == 1: calibrated[i] = 0
	
			#Needs to be removed?, #H is the upper limit of airspeed, L is the lower limit
			shroud = 1; H = 300; L = 4; location = 1
	
			#Pull windspeed from dsm string
			wspd = input[1]
	
			#cvtascc appears to be the corrected total airspeed
			cvtascc = 0
	
			#If the wspd adjusted for the shroud is within the bounds of H and L
			#	then proceed with corrected total airspeed (TAS) calculation
			if shroud*location*wspd >= L and shroud*location*wspd <= H : cvtascc = shroud*location*wspd*100
		
			#Added to prevent dividing by zero
			#	NEEDS MODIFICATION TO JUST USE DEFAULT
			if cvtascc <= 0 : cvtascc = 0.0001
	
			#Zero Corrected Flows are the flows that have been corrected for
			#	Temp and Pres AND have been filtered for values less than 0.
			zerocorrectedflows = [0]*10
	
			#Initialization of flow summing parameters
			summedzerocorrectedflow = 0; summedflow = 0
	
			#Iteration of flows to correct for pressure and temperature
			#	IF the pressure is reported correctly.
			#	ALSO performs the flow summations.
			for i in range(1,10):
				if calibrated[10] > 0 : zerocorrectedflows[i] = ( calibrated[i]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
				else : zerocorrectedflows[i] = ( calibrated[i]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
				if zerocorrectedflows[i] < 0 : zerocorrectedflows[i] = 0.0001
				summedflow = summedflow + calibrated[i]
				summedzerocorrectedflow = summedzerocorrectedflow + zerocorrectedflows[i]	
		
			#Shift in index to place cvf1c at the beginning
			#	DOES NOT REQUIRE PRESSURE AND TEMP CORRECTION
			zerocorrectedflows[0] = calibrated[0]#calibrated[i]
			if zerocorrectedflows[0] < 0 : zerocorrectedflows[0] = 0.0001

			#IF the pressure is greater than 0,
			#	THEN perform calculation of cvftc, otherwise use 0.0001 for pressure
			if calibrated[10] > 0 : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/calibrated[10])*((calibrated[14]+273.15)/294.26))
			else : cvftc = summedzerocorrectedflow - ( calcoeffs[21]*(1013.25/0.0001)*((calibrated[14]+273.15)/294.26))
	
			#Calculation of the enhancement factor?
			cvcfact=(cvtascc*math.pi*(calcoeffs[20]**2))/(cvftc*1000.0/60) #calcoeffs[20] corresponds to cvtbr;
			if cvcfact<1 : cvcfact=1
		
			#cutsize (NOT SURE IF NECESSARY))
			cutsize = 0#5	
		
			#Miscellaneous calculations, #NEEDS DEFINITIONS
			rhoa=calibrated[10]/(2870.12*(calibrated[11]+273.15)) #calibrated[10 & 11] correspond to cvpcn and cvtt respectively
			gnu=(0.0049*calibrated[11]+1.718)*0.0001
			cvrNw=cutsize*10**(-4)
			reNw=(2*cvrNw*cvtascc*rhoa)/gnu
	
			#UNSURE OF PRIOR FUNCTION, LEFT TO ENSURE 
			#cvl=CVTBL*cvf3/cvf1Z;
			cvl = calcoeffs[19]*(zerocorrectedflows[0] - summedflow)/zerocorrectedflows[0]

			#Prevent calculation of greater cut size radii
			cutsizelooplimit = 10
	
			#Code for presumably calculating cut size radius
			for cvrad in range(1,cutsizelooplimit*10+1):
				cvri=(cvrad/10)*10**(-4); rei= 2 * cvtascc * cvri * rhoa/gnu
				if rei <= 0 : rei = 0.0001
				cvli=(cvri*14.6969*calcoeffs[18] * ((0.408248*rei**(1/3)) + math.atan(2.44949*rei**(-1/3)) - 0.5*math.pi)/(3*rhoa))-calcoeffs[22]
				if cvli >= cvl:
					break
			cvrad = cvrad/10
			cvft=summedflow-calcoeffs[21]
		
			#tdl_data[1] corresponds to press, #tdl_data[2] corresponds to temp, #calcoeffs[20] corresponds to cvtbr;
			cvcfact_tdl=(cvtascc*math.pi*(calcoeffs[20]**2))/((cvft*1000.0/60)*(1013.23/tdl_data[1])*((tdl_data[2]+273.15)/294.26))
			if cvcfact_tdl<1 : cvcfact_tdl=1;

			#calibration of tdl coefficients based on temperature and pressure
			tdl_poly_coeffs = [0]*4
			tdl_poly_coeffs[0]=tdl_cals[0][0]+tdl_cals[0][1]*tdl_data[1]+tdl_cals[0][2]*tdl_data[1]*tdl_data[1]+tdl_cals[0][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			tdl_poly_coeffs[1]=tdl_cals[1][0]+tdl_cals[1][1]*tdl_data[1]+tdl_cals[1][2]*tdl_data[1]*tdl_data[1]+tdl_cals[1][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			tdl_poly_coeffs[2]=tdl_cals[2][0]+tdl_cals[2][1]*tdl_data[1]+tdl_cals[2][2]*tdl_data[1]*tdl_data[1]+tdl_cals[2][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			tdl_poly_coeffs[3]=tdl_cals[3][0]+tdl_cals[3][1]*tdl_data[1]+tdl_cals[3][2]*tdl_data[1]*tdl_data[1]+tdl_cals[3][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
	
			#cvrho_tdl=C0+C1*TDL_H2O+C2*TDL_H2O*TDL_H2O+C3*TDL_H2O*TDL_H2O*TDL_H2O;
			cvrho_tdl=tdl_poly_coeffs[0]+tdl_poly_coeffs[1]*tdl_data[0]+tdl_poly_coeffs[2]*tdl_data[0]*tdl_data[0]+tdl_poly_coeffs[3]*tdl_data[0]*tdl_data[0]*tdl_data[0]
			RHOO_TDL=cvrho_tdl/cvcfact_tdl	
	
			#FIRST CALCULATION (CVRH just goes to output file) , #CVRH is CVI relative humidity in the TDL line   */
			TTDLK=tdl_data[2]+273.15#;                                /*First, Correct temp in C to K */
			#SATVP is saturation vapor pressure (g/m3) from Goff-Gratch and RAF Bull. 9 */
			SATVP=10**(23.832241-5.02808*math.log10(TTDLK)-1.3816E-7*(10**(11.334-0.0303998*TTDLK))+0+8.1328E-2*(10**(3.49149-1302.8844/TTDLK))-2949.076/TTDLK)
	
			cvrh=100*cvrho_tdl*TTDLK/(SATVP*216.68)

			if cvrho_tdl<=  0.0 : Z= -10
			else : Z = math.log(((tdl_data[2]+273.15))*cvrho_tdl/1322.3)

			cvdp = 273.0*Z/(22.51-Z) #/*CVDP is CVI Dew Point, Z is intermediate variable*/
	
			#Indicator in LabView
			cvrhoo_tdl=cvrho_tdl/cvcfact_tdl
			if cvrhoo_tdl>50  : cvrhoo_tdl=99
			if cvrhoo_tdl<-50 : cvrhoo_tdl=-99
	
			opc_press_mb = (opc_press*10)
			opcc = (opc_data[0]*60)/(opc_data[1]*1000); opcc_Pcor = opcc*calibrated[10]/opc_press
			opcco = opcc/cvcfact; opcco_Pcor = opcco*calibrated[10]/opc_press

			cvf3 = calibrated[0] - summedflow #Indicator in Labview Plot

			cvcnc1 = (input[2]/(zerocorrectedflows[2]*1000/60))
			cvcnc1 = cvcnc1*math.exp(cvcnc1*zerocorrectedflows[2]*4.167*10**(-6))
	
			cvcnc01 = cvcnc1/cvcfact
	
			#USER INPUTS
			#cvfxwr = [0.00]*4
			#cvfxwr array is replaced by ui.internalflowsetpts
		
			#If lower <= flow <= Upper, flow set point from before, #	Otherwise, recalculate
			if ui.flowio.isChecked():
				if (zerocorrectedflows[1] > (ui.flowlimits[0] + 0.05)) or (zerocorrectedflows[1] < (ui.flowlimits[0] - 0.05)) :
					cvfxnw = ui.flowlimits[0]*(calibrated[10]/1013.25)*(294.26/(calibrated[14]+273.15))
					ui.internalflowsetpts[0] = (cvfxnw-calcoeffs[3])/calcoeffs[4] #will be 6 and 7 on next iteration.
				#else: #cvfxwr[0] = 0.0 #Needs to be left as older value. #Nothing is done so flow is as before.
				#Starting at cvfx2 to cvfx4 (index 2 to 3 on calibrated)
				for i in range(1,4) : # int i = 1 ; i < 4; i++ ) {
					if (zerocorrectedflows[i+2] > ui.flowlimits[i] + 0.05) or (zerocorrectedflows[i+2] < ui.flowlimits[i] - 0.05) :
						cvfxnw = ui.flowlimits[i] * (calibrated[10]/1013.25)*(294.26/(calibrated[14] + 273.15))
						#cvfx0wr = ( cvfxnw – c0cvfx0) / c1cvfx0;
						ui.internalflowsetpts[i] = ( cvfxnw - calcoeffs[(i+2)*3] ) / calcoeffs[(i+2)*3+1] #will be 9 (12) and 10 (13) on next iteration.			
					#else : 	#cvfxwr[i] = 0.0; #REPLACE WITH OLDER VALUE
			else: ui.internalflowsetpts = [0.00]*4
	
			if ui.flowio.isChecked() and not ui.cvimode.isChecked() :
				cfexcess_cor=ui.cfexcess*(calibrated[10]/1013.25)*294.26/(calibrated[14]+273.15)
				cfsummed=cfexcess_cor + summedflow + calcoeffs[21] - calibrated[5]  #cvoff1 is equivalent to calcoeffs[21]
				cvf1wr=( cfsummed - calcoeffs[0])/calcoeffs[1]
			else: cvf1wr = 0.0

			if cvf1wr >= 5.0 : cvf1wr = 5.0
			
			if( input[34] != -99.99 ) : input[34] = calibrated[10]/(calibrated[14]+273.15) * 0.000217 * input[34]
	
			output = np.r_[input[0], 0, 0, 0, input[3:19], calibrated[10:16], zerocorrectedflows[:], #ENDS AT INDEX 35, next line is 36
				cvl, cvrhoo_tdl, cvrho_tdl, cvrad, cvcfact_tdl,  #ENDS AT 40, next line 41
				cvf3, input[1], cvcnc1, cvcnc01, cvcfact,  cvftc, cvrh, cvdp, #ENDS at 48, next line 49
				cvfxwr[0:4], cvf1wr, input[2], tdl_data[:], opcc, opcco, opc_data[0:2], 
				opcc_Pcor, opcco_Pcor, opc_press_mb, input[34:37]]		
			
			#############################################################################
			#############################################################################
			#############################################################################
			###########################END COMPUTATION ROUTINE###########################
			#############################################################################
			#############################################################################
			#############################################################################
			
			
			#if( input[34] != -99.99 ) : input[34] = calibrated[10]/(calibrated[14]+273.15) * 0.000217 * input[34]
			output[3] = ui.numchanges

			#cvl is at index 36?, #cvf3 is at index 41, #cvfxwr0 is at index 49, #opcc_Pcor is at index 69
			flowbyte = (2*int(ui.v1.isChecked()))**3+(2*int(ui.v2.isChecked()))**2+(2*int(ui.v3.isChecked()))**1+int(ui.v4.isChecked())
			output[2] = flowbyte
			
			
			#output = np.r_[input[0], int(ui.cvimode.isChecked())*2, flowbyte, 0, input[3:19], calibrated[10:16], zerocorrectedflows[:],
			#	cvl, cvrhoo_tdl, cvrho_tdl, cvrad, cvcfact_tdl,  
			#	cvf3, input[1], cvcnc1, cvcno1, cvcfact,  cvftc, cvrh, cvdp, 
			#	cvfxwr[0:4], cvf1wr, input[2], tdl_data[:], opcc, opcco, opc_data[0:2], 
			#	opcc_Pcor, opcco_Pcor, opc_press_mb, input[34:37]]
			
			#FLOW OUTPUTS ARE ALSO DECIDED IN THE CONNECTION SEQUENCE
			dataout = np.round(np.r_[ output[0], output[49:54], 
				int(ui.v1.isChecked()), int(ui.v2.isChecked()), int(ui.v3.isChecked()), int(ui.v4.isChecked()), 
				int(ui.cvimode.isChecked()), flowbyte, ui.numchanges, 
				output[39], output[45], output[47:49], output[37] ],3)
			
			zerocorrectedflows = output[26:36]
			#calibrated = np.r_[output[26:36], output[20:26]]
			
			extra = np.r_[output[41], output[43:45], output[38], output[37], output[65:67]]
			#extra = [cvf3, cvcnc1, cvcnc01, cvrho_tdl, cvrhoo_tdl, opcc, opcco]

			
#			output = [dsmtime,cvfxwr[0],cvfxwr[1],cvfxwr[2],cvfxwr[3],cvf1wr,
#			valvepositions[0],valvepositions[1],valvepositions[2],valvepositions[3],
#			cvimode,fxflows,usernumchanges,cvrad,cvcfact,cvrh,cvdp,cvrhoo_tdl]
	
			#dataout = [message[0], 0.000, 0.000, 0.000, 0.000, 0.000, valvepositions[0],
			#	valvepositions[1], valvepositions[2], valvepositions[3], 0, 0, 0, 
			#	10.000,1.000,0.000,-83.974,0.000]
			
			#Checked to see if user input or calculated mode is selected
			#and proceed to populate output array accordingly
			#IF FLOW IS CHECKED, THEN EVERYTHING IS CALCULATED!!!!
			if ui.flowsource.isChecked():
				ui.cvfx0wr.setText(str(dataout[1]))
				ui.cvfx2wr.setText(str(dataout[2]))
				ui.cvfx3wr.setText(str(dataout[3]))
				ui.cvfx4wr.setText(str(dataout[4]))
				ui.cvf1wr.setText(str(dataout[5]))
				
			if ui.cvfx0wr.text() != "" : dataout[1] = float(ui.cvfx0wr.text())
			else: dataout[1] = 0.00
			if ui.cvfx2wr.text() != "" : dataout[2] = float(ui.cvfx2wr.text())
			else: dataout[2] = 0.00
			if ui.cvfx3wr.text() != "" : dataout[3] = float(ui.cvfx3wr.text())
			else: dataout[3] = 0.00
			if ui.cvfx4wr.text() != "" : dataout[4] = float(ui.cvfx4wr.text())
			else: dataout[4] = 0.00
			if ui.cvf1wr.text() != "" : dataout[5] = float(ui.cvf1wr.text())
			else: dataout[5] = 0.00		
			
			
			#Added for populating raw input/output data table
			_translate = QtCore.QCoreApplication.translate
			for i in range(0,len(input)):
				item = ui.tableWidget.item(i, 0)
				item.setText(_translate("MainWindow",str(self.input[i])))
			for i in range(0,len(dataout)):
				item = ui.tableWidget.item(i, 1)
				item.setText(_translate("MainWindow",str(self.dataout[i])))
				
			#if not ui.valvesource.isChecked():
			#	dataout[6] = int(ui.v1.isChecked())
			#	dataout[7] = int(ui.v2.isChecked())
			#	dataout[8] = int(ui.v3.isChecked())
			#	dataout[9] = int(ui.v4.isChecked())
			
			#Sample dataout for testing
			#dataout = [dataout[0],-0.081,1.059,1.968,79.022,0.029,0,1,0,1,0,0,0,10.000,1.000,0.000,-83.974,0.000]

			#Convert array back into a byte string with an
			#	endline character
			dataout = [ "{:.3f}".format(x) for x in dataout ]
			dataout = ','.join(dataout)
			#dataout = str(dataout).strip('[]')
			#dataout = dataout.replace(" ","")
			dataout+='\n'			
			dataout = bytes(dataout,'utf_8')
			
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
			self.client_sock.send(dataout)	
			
			#Update front panel with data sent to dsm
			ui.datatodsm.setText(str(dataout).replace(",", ", "))	
			
			ui.tabledata = np.c_[input[3:19], calibrated[0:16], np.r_[zerocorrectedflows[:], [np.nan]*6]]
			try:
				#If array has -9999 in first slot (i.e. initialized
				#	but does not contain data), replace data with
				#	with the new stuff.
				#else if number of data points is greater than 900 (15 minutes)
				#	cut off first value, add new end value
				#else add new value to end
				newdata = np.r_[input[0],input[19:22], extra[:]]
				for i in range(1,len(newdata)):
					if (newdata[i] <= 0): newdata[i] = np.nan
				if( ui.dim[1] == 1 and ui.plotdata[0] == -9999 ):
					ui.plotdata = np.c_[newdata] #Appends the column b onto a
				elif (ui.dim[1] >= 900):
					ui.plotdata = np.c_[ui.plotdata[:,-899:], newdata ]
				else:
					ui.plotdata = np.c_[ui.plotdata,  newdata]
			except NameError:
				print ("There was a problem in the plotting")
			#else:
				#	print ("sure, it was defined.")
					#print(ui.plotdata)
			finally:
				#determine size of new array
				ui.dim = ui.plotdata.shape
				
			#Originally had C:\data\
			#Appended to project title (i.e. IDEAS2013\)
			#The file name then listed as
			#YYMMDDHH.MM with 'q' on the end
			#Full file name could be YYMMDDHH.MMq
			#In certain directory.
		
			outputstring = [ "{:11.5g}".format(x) for x in output ]
			outputstring = ','.join(outputstring)
			outputstring += '\n'
			
			if not os.path.isfile(ui.path+ui.file):
				os.makedirs(os.path.dirname(ui.path+ui.file), exist_ok=True)
				with open(ui.path+ui.file, "w") as f:
					f.write(ui.header)#outputstring)	
					f.write(outputstring)
					f.close()
			else:
				with open(ui.path+ui.file, "a") as f:
					f.write(outputstring)
					f.close()
			
			#os.path.isfile('./file.txt') 
			
			#filename = "./CVI_data/"			
			
			#filename = "/foo/bar/baz.txt"¨
			#os.makedirs(os.path.dirname(filename), exist_ok=True)
			#with open(filename, "w") as f:
			#f.write(outputstring)
			
		#Kept for testing purposes; however, unecessary with DSM
		#Removed because CVI does not need an echo.
		#self.transport.write(data)
		#print('Close the client socket')
		#self.transport.close()
			
	def connection_lost(self, exc): #Added after CVI test worked 11-2-16
		'''
		Called when the connection is lost or closed.
		The argument is an exception object or None (the latter
		meaning a regular EOF is received or the connection was aborted or closed).
		'''
		ui.statusindicatorlabel.setText('Connection Lost!!')
		#ui.server.close()
		#ui.disconnecting(MainWindow)
			
if __name__ == "__main__":

	#Create time for plot updating
	timer = QTimer();
	
	#Initialize GUI
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()#QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	#MainWindow.show()
	MainWindow.show()#Maximized()
	
	#Begin Event Loop
	#loop = asyncio.get_event_loop()
	#asyncio.ensure_future(app.exec_())
	#asyncio.ensure_future(ui.server_loop_in_thread)	
	#loop.run_forever() 
	sys.exit(app.exec_())