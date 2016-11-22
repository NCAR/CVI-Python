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
from pyqtgraph import PlotWidget
import numpy as np

#For File WRiting
import os

#for scheduling replot (NO LONGER USED) 
#from apscheduler.schedulers.background import BackgroundScheduler

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		
		#Qt.WindowMinimizeButtonHint#|Qt.WindowMaximizeButtonHint
		#Dialog.resize(1800,535)#657, 535)
		
		
		#ADDED FOR POTENTIALLY RESIZING
		#self.h_layout = QtWidgets.QHBoxLayout()
		#Dialog.setLayout(self.h_layout)

        # Create the QTabWidget.
       # self.tabWidget = QTabWidget()
        #self.tabWidget.setEnabled(True)
        #self.tabWidget.setGeometry(QRect(20, 40, 601, 501))
        #self.tabWidget.setTabPosition(QTabWidget.North)
        #self.tabWidget.setObjectName('tabWidget')
        
		# Add the QTabWidget to the created layout and set the 
        # layout on the QWidget.
				
		#Creation of Tabs for program	
		self.tabWidget = QtWidgets.QTabWidget(Dialog)
		self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1800, 925))
		self.tabWidget.setObjectName("tabWidget")		
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")

		#Create corresponding Tabs?
		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tabWidget.addTab(self.tab_2, "")		
				
		#Host and Port Configuration Labels and inputs
		self.dsmiplabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.dsmiplabel.setGeometry(QtCore.QRect(30, 20, 121, 19))
		self.dsmiplabel.setObjectName("label")
		self.ipaddress = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.ipaddress.setGeometry(QtCore.QRect(30, 40, 141, 25))
		self.ipaddress.setObjectName("ipaddress")
		self.portin = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.portin.setGeometry(QtCore.QRect(210, 40, 113, 25))
		self.portin.setObjectName("portin")
		self.portout = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.portout.setGeometry(QtCore.QRect(360, 40, 113, 25))
		self.portout.setObjectName("portout")
		self.portinlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.portinlabel.setGeometry(QtCore.QRect(210, 20, 121, 19))
		self.portinlabel.setObjectName("portinlabel")
		self.portoutlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.portoutlabel.setGeometry(QtCore.QRect(360, 20, 121, 19))
		self.portoutlabel.setObjectName("portoutlabel")
		
		#Push buttons for establishing (or cancel) server to receive data
		self.connect = QtWidgets.QPushButton(self.tab)#Dialog)
		self.connect.setGeometry(QtCore.QRect(30, 80, 141, 34))
		self.connect.setObjectName("connect")
		self.disconnect = QtWidgets.QPushButton(self.tab)#Dialog)
		self.disconnect.setGeometry(QtCore.QRect(30, 120, 141, 34))
		self.disconnect.setObjectName("disconnect")
		self.connectedlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.connectedlabel.setGeometry(QtCore.QRect(210, 80, 113, 41))
		self.connectedlabel.setObjectName("connectedlabel")
		
		#Text Boxes for displaying the data to and from the DSM
		self.datafromdsmlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.datafromdsmlabel.setGeometry(QtCore.QRect(30, 170, 121, 19))
		self.datafromdsmlabel.setObjectName("datafromdsmlabel")
		self.datatodsmlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.datatodsmlabel.setGeometry(QtCore.QRect(30, 300, 121, 19))
		self.datatodsmlabel.setObjectName("datatodsmlabel")
		self.datafromdsm = QtWidgets.QLabel(self.tab)#Dialog)
		self.datafromdsm.setGeometry(QtCore.QRect(30, 190, 601, 107))
		self.datafromdsm.setObjectName("datafromdsm")
		self.datafromdsm.setWordWrap(True)
		#.setAlignment(AlignCenter)
		#.font.setFamily("Sans Serif")
		#.font.setPointSize(20)
		#.setFont(...)
		#.setStyleSheet("QLabel { background-color : gray; color : black; }")
		self.datafromdsm.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")
		self.datafromdsm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.datafromdsm.setAlignment(Qt.AlignTop)
		self.datatodsm = QtWidgets.QLabel(self.tab)#Dialog)
		self.datatodsm.setGeometry(QtCore.QRect(30, 320, 601, 107))
		self.datatodsm.setObjectName("datafromdsm")
		self.datatodsm.setWordWrap(True)
		self.datatodsm.setStyleSheet("""QLabel { border: 3px inset palette(dark); border-radius: 10px; background-color: white; color: #545454; }""")		
		self.datatodsm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.datatodsm.setAlignment(Qt.AlignTop)

		#Status indicator at bottom of GUI
		self.statusindicatorlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.statusindicatorlabel.setGeometry(QtCore.QRect(30, 425, 500, 19))
		self.statusindicatorlabel.setObjectName("statusindicatorlabel")

		#Label and checkboxes for the four controllable valves
		self.valveiolabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.valveiolabel.setGeometry(QtCore.QRect(535, 20, 121, 19))
		self.valveiolabel.setObjectName("valveiolabel")
		self.v1 = QtWidgets.QCheckBox(self.tab)#Dialog)
		self.v1.setGeometry(QtCore.QRect(550, 50, 500, 20))
		self.v1.setObjectName("valve1")
		self.v2 = QtWidgets.QCheckBox(self.tab)#Dialog)
		self.v2.setGeometry(QtCore.QRect(550, 75, 500, 20))
		self.v2.setObjectName("valve2")
		self.v3 = QtWidgets.QCheckBox(self.tab)#Dialog)
		self.v3.setGeometry(QtCore.QRect(550, 100, 500, 20))
		self.v3.setObjectName("valve3")
		self.v4 = QtWidgets.QCheckBox(self.tab)#Dialog)
		self.v4.setGeometry(QtCore.QRect(550, 125, 500, 20))
		self.v4.setObjectName("valve4")
		
		#Toggle button/label for determining whether valves and 
		#flows are controlled by the user or by the calculation
		self.flowsourcelabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.flowsourcelabel.setGeometry(QtCore.QRect(650, 20, 121, 19))
		self.flowsourcelabel.setObjectName("flowsourcelabel")
		self.flowsource = QtWidgets.QPushButton(self.tab)#Dialog)
		self.flowsource.setGeometry(QtCore.QRect(650, 50, 100, 34))
		self.flowsource.setObjectName("flowsource")
		self.flowsource.setCheckable(True)

		self.flowio = QtWidgets.QPushButton(self.tab)#Dialog)
		self.flowio.setGeometry(QtCore.QRect(360, 80, 113, 34))
		self.flowio.setObjectName("flowio")
		self.flowio.setCheckable(True)
		
		self.cvimode = QtWidgets.QPushButton(self.tab)#Dialog)
		self.cvimode.setGeometry(QtCore.QRect(360, 120, 113, 34))
		self.cvimode.setObjectName("cvimode")
		self.cvimode.setCheckable(True)
		
		#User input flows and labels for cvfx0,cvfx2,cvfx3,cvfx4,cvf1
		self.cvfx0wrlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.cvfx0wrlabel.setGeometry(QtCore.QRect(650, 100, 121, 19))
		self.cvfx0wrlabel.setObjectName("cvfx0wrlabel")		
		self.cvfx0wr = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.cvfx0wr.setGeometry(QtCore.QRect(650, 125, 100, 25))
		self.cvfx0wr.setObjectName("cvfx0wr")
		self.cvfx2wrlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.cvfx2wrlabel.setGeometry(QtCore.QRect(650, 175, 121, 19))
		self.cvfx2wrlabel.setObjectName("cvfx2wrlabel")			
		self.cvfx2wr = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.cvfx2wr.setGeometry(QtCore.QRect(650, 200, 100, 25))
		self.cvfx2wr.setObjectName("cvfx2wr")
		self.cvfx3wrlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.cvfx3wrlabel.setGeometry(QtCore.QRect(650, 250, 121, 19))
		self.cvfx3wrlabel.setObjectName("cvfx3wrlabel")			
		self.cvfx3wr = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.cvfx3wr.setGeometry(QtCore.QRect(650, 275, 100, 25))
		self.cvfx3wr.setObjectName("cvfx3wr")
		self.cvfx4wrlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.cvfx4wrlabel.setGeometry(QtCore.QRect(650, 325, 121, 19))
		self.cvfx4wrlabel.setObjectName("cvfx4wrlabel")			
		self.cvfx4wr = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.cvfx4wr.setGeometry(QtCore.QRect(650, 350, 100, 25))
		self.cvfx4wr.setObjectName("cvfx4wr")
		self.cvf1wrlabel = QtWidgets.QLabel(self.tab)#Dialog)
		self.cvf1wrlabel.setGeometry(QtCore.QRect(650, 400, 121, 19))
		self.cvf1wrlabel.setObjectName("cvf1wrlabel")			
		self.cvf1wr = QtWidgets.QLineEdit(self.tab)#Dialog)
		self.cvf1wr.setGeometry(QtCore.QRect(650, 425, 100, 25))
		self.cvf1wr.setObjectName("cvf1wr")
	
		#Colored box for showing green if connected, red if disconnected
		self.graphicsView = QtWidgets.QGraphicsView(self.tab)#Dialog)
		self.graphicsView.setGeometry(QtCore.QRect(210, 120, 113, 34))
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
		
		#Plotting Widget
#		pyqtgraph.setConfigOption('background', 'w')
#		pen=pyqtgraph.mkPen(color=C,width=10)
		self.CVIplot = PlotWidget(self.tab)#Dialog)
		self.CVIplot.setGeometry(QtCore.QRect(775,50,1000,425))#40, 20, 256, 192))
		self.CVIplot.setObjectName("CVIplot")
		self.CVIplot.setTitle("CVI Data")
		self.CVIplot.setLabel('bottom',text = 'time (seconds)')
		self.CVIplot.setLabel('left',text = 'y')
		
		self.CVIplot2 = PlotWidget(self.tab)#Dialog)
		self.CVIplot2.setGeometry(QtCore.QRect(775,515,1000,425))#40, 20, 256, 192))
		self.CVIplot2.setObjectName("CVIplot")
		self.CVIplot2.setTitle("CVI Data")
		self.CVIplot2.setLabel('bottom',text = 'time (seconds)')
		self.CVIplot2.setLabel('left',text = 'y')
		
		#Dropdown list for selecting data to plot
		self.dropdownlist = QtWidgets.QComboBox(self.tab)#Dialog)
		self.dropdownlist.setGeometry(QtCore.QRect(800,20,450,20))
		self.dropdownlist.setObjectName("dropdownlist")

		self.dropdownlistline2 = QtWidgets.QComboBox(self.tab)#Dialog)
		self.dropdownlistline2.setGeometry(QtCore.QRect(1300,20,450,20))
		self.dropdownlistline2.setObjectName("dropdownlistline2")
	
		self.dropdownlist2 = QtWidgets.QComboBox(self.tab)#Dialog)
		self.dropdownlist2.setGeometry(QtCore.QRect(800,485,450,20))
		self.dropdownlist2.setObjectName("dropdownlist2")
		
		self.dropdownlist2line2 = QtWidgets.QComboBox(self.tab)#Dialog)
		self.dropdownlist2line2.setGeometry(QtCore.QRect(1300,485,450,20))
		self.dropdownlist2line2.setObjectName("dropdownlist2line2")
		
		#Create Table for Viewing Parameters
		self.tableWidget = QtWidgets.QTableWidget(self.tab)
		self.tableWidget.setGeometry(QtCore.QRect(30, 515, 700, 375))
		self.tableWidget.setObjectName("tableWidget")

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
		
		#Create Table for Calibration Coefficients
		self.caltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.caltableWidget.setGeometry(QtCore.QRect(1075, 130, 700, 760))
		self.caltableWidget.setObjectName("caltableWidget")

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
				
				
		#Create Table for More Calibration Coefficients
		self.morecaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.morecaltableWidget.setGeometry(QtCore.QRect(1075, 25, 700, 100))
		self.morecaltableWidget.setObjectName("morecaltableWidget")

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
				
		#Create Table for TDL Calibration Coefficients
		self.tdlcaltableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.tdlcaltableWidget.setGeometry(QtCore.QRect(380, 670, 690, 220))
		self.tdlcaltableWidget.setObjectName("tdlcaltableWidget")

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

		
		self.updatecals = QtWidgets.QPushButton(self.tab_2)#Dialog)
		self.updatecals.setGeometry(QtCore.QRect(380, 600, 690, 34))
		self.updatecals.setObjectName("updatecals")
		#self.flowio.setCheckable(True)
		
		
		'''
			self.tabWidget = QtWidgets.QTabWidget(Dialog)
			self.tabWidget.setGeometry(QtCore.QRect(20, 20, 781, 201))
			self.tabWidget.setObjectName("tabWidget")
			self.tab = QtWidgets.QWidget()
			self.tab.setObjectName("tab")
			self.tableWidget = QtWidgets.QTableWidget(self.tab)
			self.tableWidget.setGeometry(QtCore.QRect(20, 40, 741, 71))
			self.tableWidget.setObjectName("tableWidget")
			self.tableWidget.setColumnCount(2)
			self.tableWidget.setRowCount(1)
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setVerticalHeaderItem(0, item)
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setHorizontalHeaderItem(0, item)
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setHorizontalHeaderItem(1, item)
			item = QtWidgets.QTableWidgetItem()
			self.tableWidget.setItem(0, 0, item)
			self.tabWidget.addTab(self.tab, "")
			self.tab_2 = QtWidgets.QWidget()
			self.tab_2.setObjectName("tab_2")
			self.tabWidget.addTab(self.tab_2, "")

			self.retranslateUi(Dialog)
			self.buttonBox.accepted.connect(Dialog.accept)
			self.buttonBox.rejected.connect(Dialog.reject)
			QtCore.QMetaObject.connectSlotsByName(Dialog)

		def retranslateUi(self, Dialog):
			_translate = QtCore.QCoreApplication.translate
			Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
			item = self.tableWidget.verticalHeaderItem(0)
			item.setText(_translate("Dialog", "This is the new row"))
			item = self.tableWidget.horizontalHeaderItem(0)
			item.setText(_translate("Dialog", "cvfx0wr"))
			item = self.tableWidget.horizontalHeaderItem(1)
			item.setText(_translate("Dialog", "cvfx2wr"))
			__sortingEnabled = self.tableWidget.isSortingEnabled()
			self.tableWidget.setSortingEnabled(False)
			item = self.tableWidget.item(0, 0)
			item.setText(_translate("Dialog", "This is item 1,1"))
			self.tableWidget.setSortingEnabled(__sortingEnabled)
			self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
			self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))

		'''		
		'''
		List of Widgets?
		#Added to allow resizing of windows
		self.h_layout.addWidget(self.tabWidget)
		self.h_layout.addWidget(self.dsmiplabel)
		self.h_layout.addWidget(self.ipaddress)
		self.h_layout.addWidget(self.portin)
		self.h_layout.addWidget(self.portout)
		self.h_layout.addWidget(self.portinlabel)
		self.h_layout.addWidget(self.portoutlabel)
		self.h_layout.addWidget(self.connect)
		self.h_layout.addWidget(self.disconnect)
		self.h_layout.addWidget(self.connectedlabel)
		self.h_layout.addWidget(self.datafromdsmlabel)
		self.h_layout.addWidget(self.datatodsmlabel)
		self.h_layout.addWidget(self.datafromdsm)
		self.h_layout.addWidget(self.datatodsm)
		self.h_layout.addWidget(self.statusindicatorlabel)
		self.h_layout.addWidget(self.valveiolabel)
		self.h_layout.addWidget(self.v1)
		self.h_layout.addWidget(self.v2)
		self.h_layout.addWidget(self.v3)
		self.h_layout.addWidget(self.v4)
		self.h_layout.addWidget(self.flowsourcelabel)
		self.h_layout.addWidget(self.flowsource)
		self.h_layout.addWidget(self.flowio)
		self.h_layout.addWidget(self.cvimode)
		self.h_layout.addWidget(self.cvfx0wrlabel)
		self.h_layout.addWidget(self.cvfx0wr)
		self.h_layout.addWidget(self.cvfx2wrlabel)
		self.h_layout.addWidget(self.cvfx2wr)
		self.h_layout.addWidget(self.cvfx3wrlabel)
		self.h_layout.addWidget(self.cvfx3wr)
		self.h_layout.addWidget(self.cvfx4wrlabel)
		self.h_layout.addWidget(self.cvfx4wr)
		self.h_layout.addWidget(self.cvf1wrlabel)
		self.h_layout.addWidget(self.cvf1wr)
		self.h_layout.addWidget(self.graphicsView)
		self.h_layout.addWidget(self.CVIplot)
		self.h_layout.addWidget(self.CVIplot2)
		self.h_layout.addWidget(self.dropdownlist)
		self.h_layout.addWidget(self.dropdownlistline2)
		self.h_layout.addWidget(self.dropdownlist2)
		self.h_layout.addWidget(self.dropdownlist2line2)
		self.h_layout.addWidget(self.tableWidget)
		self.h_layout.addWidget(self.tab)
		self.h_layout.addWidget(self.tab_2)
		'''
		
		self.retranslateUi(Dialog)
		
#		self.layout = QVBoxLayout(self)
#		self.layout.add(everything)
		
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "CVI Interface"))
		
		self.dsmiplabel.setText(_translate("Dialog", "DSM IP Address"))
		self.ipaddress.setText(_translate("Dialog", "192.168.184.145"))#"localhost"))#"192.168.184.145"))#"192.168.0.1"))#"192.168.184.145"))
		self.portin.setText(_translate("Dialog", "30005"))
		self.portout.setText(_translate("Dialog", "30006"))
		self.portinlabel.setText(_translate("Dialog", "Incoming Port"))
		self.portoutlabel.setText(_translate("Dialog", "Outgoing Port"))
		self.connect.setText(_translate("Dialog", "Connect"))
		self.disconnect.setText(_translate("Dialog", "Disconnect"))
		self.datafromdsmlabel.setText(_translate("Dialog", "Data From DSM"))
		self.datatodsmlabel.setText(_translate("Dialog", "Data To DSM"))
		self.connectedlabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Connected?</span></p></body></html>"))

		self.statusindicatorlabel.setText(_translate("Dialog", "Status Indicator"))

		self.valveiolabel.setText(_translate("Dialog", "Valve I/O"))		
		self.v1.setText(_translate("Dialog", "1"))
		self.v2.setText(_translate("Dialog", "2"))
		self.v3.setText(_translate("Dialog", "3"))
		self.v4.setText(_translate("Dialog", "4"))
		
		self.flowsource.setText(_translate("Dialog", "User Input"))
		
		self.flowio.setText(_translate("Dialog", "Flow OFF"))
		
		self.cvimode.setText(_translate("Dialog", "Mode: CVI"))

		self.flowsourcelabel.setText(_translate("Dialog", " Flow Source"))
		self.cvfx0wrlabel.setText(_translate("Dialog", "    cvfx0wr"))
		self.cvfx2wrlabel.setText(_translate("Dialog", "    cvfx2wr"))
		self.cvfx3wrlabel.setText(_translate("Dialog", "    cvfx3wr"))
		self.cvfx4wrlabel.setText(_translate("Dialog", "    cvfx4wr"))
		self.cvf1wrlabel.setText(_translate("Dialog", "     cvf1wr"))
		self.cvfx0wr.setText(_translate("Dialog","0.00"))
		self.cvfx2wr.setText(_translate("Dialog","0.00"))
		self.cvfx3wr.setText(_translate("Dialog","0.00"))
		self.cvfx4wr.setText(_translate("Dialog","0.00"))
		self.cvf1wr.setText(_translate("Dialog","0.00"))	
		
		self.datafromdsm.setText(_translate("Dialog", "Awaiting Data to be received. . . . ."))
		self.datatodsm.setText(_translate("Dialog", "Awaiting Data to be sent. . . . ."))

		
		self.plottitles = ['H2O','ptdl','ttdl','cvf3','cvcnc1','cvcnc01','cvrho_tdl','cvrhoo_tdl','opcc','opcco']
		self.ylabels = ['Concentration (g/m^3)','Pressure (mbar)','Temperature (C)','y','y','y','y','y','y','y']
		self.dropdownlist.addItems(self.plottitles)
		
		self.dropdownlistline2.addItem("")
		self.dropdownlistline2.addItems(self.plottitles)
		
		self.dropdownlist2.addItems(self.plottitles)
		
		self.dropdownlist2line2.addItem("")
		self.dropdownlist2line2.addItems(self.plottitles)
		
		
		#Labeling Tabs on screen
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Operations"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Configuration"))
	
		'''
		#Which options are available for plotting
		self.dropdownlist.addItem("H2OR")
		self.dropdownlist.addItem("ptdl")
		self.dropdownlist.addItem("ttdl")
		

		#cvf3, cvcnc1, cvcnc01, cvrho_tdl, cvrhoo_tdl, opcc, opcco
		self.dropdownlist.addItem("cvf3")
		self.dropdownlist.addItem("cvcnc1")
		self.dropdownlist.addItem("cvcnc01")
		self.dropdownlist.addItem("cvrho_tdl")
		self.dropdownlist.addItem("cvrhoo_tdl")
		self.dropdownlist.addItem("opcc")
		self.dropdownlist.addItem("opcco")
		'''
		
		for i in range(0,len(self.tablerowlabels)):
			item = self.tableWidget.verticalHeaderItem(i)
			item.setText(_translate("Dialog",self.tablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("Dialog", "This is the new row"))
		for i in range(0,len(self.tablecolumnlabels)):
			item = self.tableWidget.horizontalHeaderItem(i)
			item.setText(_translate("Dialog",self.tablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("Dialog", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tableWidget.setSortingEnabled(False)
		#item = self.tableWidget.item(0, 0)
		#item.setText(_translate("Dialog", "This is item 1,1"))
		
		#Cal Coeffs Table
		for i in range(0,len(self.caltablerowlabels)):
			item = self.caltableWidget.verticalHeaderItem(i)
			item.setText(_translate("Dialog",self.caltablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("Dialog", "This is the new row"))
		for i in range(0,len(self.caltablecolumnlabels)):
			item = self.caltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("Dialog",self.caltablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("Dialog", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.caltableWidget.setSortingEnabled(False)

		#More Cal Coeffs Table
		for i in range(0,len(self.morecaltablerowlabels)):
			item = self.morecaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("Dialog",self.morecaltablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("Dialog", "This is the new row"))
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("Dialog",self.morecaltablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("Dialog", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.morecaltableWidget.setSortingEnabled(False)
		
		
		
		#TDL Cal Coeffs Table
		for i in range(0,len(self.tdlcaltablerowlabels)):
			item = self.tdlcaltableWidget.verticalHeaderItem(i)
			item.setText(_translate("Dialog",self.tdlcaltablerowlabels[i]))
#		item = self.tableWidget.verticalHeaderItem(0)
#		item.setText(_translate("Dialog", "This is the new row"))
		for i in range(0,len(self.tdlcaltablecolumnlabels)):
			item = self.tdlcaltableWidget.horizontalHeaderItem(i)
			item.setText(_translate("Dialog",self.tdlcaltablecolumnlabels[i]))
		#item = self.tableWidget.horizontalHeaderItem(1)
		#item.setText(_translate("Dialog", "corrected"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tdlcaltableWidget.setSortingEnabled(False)
		
		self.updatecals.setText(_translate("Dialog", "Press to SAVE new calibrations"))
		
		
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
		
		
		self.calarray = ['cvf1','cvfx0','cvfx1','cvfx2','cvfx3','cvfx4','cvfx5','cvfx6','cvfx7','cvfx8',
			'cvpcn','cvtt','cvtp','cvts','cvtcn','cvtai',
			'RHOD','CVTBL','CVTBR','CVOFF1','LTip',
			'tdl_param_0','tdl_param_1','tdl_param_2','tdl_param_3']
		self.calvalues = np.c_[[0.0]*len(self.calarray),[0.0]*len(self.calarray),[0.0]*len(self.calarray),[0.0]*len(self.calarray)]
		self.NIDASHeader = '#\n# dateFormat="%Y %b %d %H:%M:%S"\n# timeZone = "UTC"\n#'
		
		#Create filenaming structure
		basedir = 'C:/CVI/'
		project = 'Testing'
		
		self.path = basedir + '/' + project + '/'
		self.calpath = basedir + '/Calibrations' + '/' 
		self.file = time.strftime("%y%m%d%H.%Mq")
						
		self.header = 'dsmtime, INLET, FXflows,  valve_changes, cvf1R, cvfx0R, cvfx1R, cvfx2R,  cvfx3R, cvfx4R, cvfx5R, cvfx6R, cvfx7R, cvfx8R, cvpcnR, cvttR, cvtpR, cvtsR, cvtcnR, cvtaiR, cvpcnC, cvttC, cvtpC, cvtsC, cvtcnC, cvtaiC, cvf1, cvfx0c, cvfx1c, cvfx2c,  cvfx3c, cvfx4c, cvfx5c, cvfx6c,  cvfx7c, cvfx8c, cvl, cvrhoo_tdl,   cvrho_tdl, cvrad, cvcfact_tdl,  cvf3, cvtas, cvcnc1, cvcno1, cvcfact,  cvftc, cvrh, cvdp, cvfx0WR, cvfx2WR, cvfx3WR,  cvfx4WR, cvfx1WR, cnt1, H2O_TDL,  pTDL, tTDL, TDLsignalL,TDLlaser, TDLline, TDLzero, TTDLencl, TTDLtec,TDLtrans, opcc, opcco, opcnts, opcflow, opcc_Pcor, opcco_Pcor, opcc_pres_mb, H2O_PIC_cvrtd, 180, HDO'
		self.header += '\n'
		
		self.readcalsfromfiles(Dialog)
		
		self.updatecals.clicked.connect(lambda: self.savecalibrations(Dialog))
		
		#connect the signal 'clicked' to the slot 'flowsourcechanged'
		self.flowsource.clicked.connect(self.toggleswitched)
		self.flowio.clicked.connect(self.toggleswitched)
		self.cvimode.clicked.connect(self.toggleswitched)
		
		self.flowsource.click()
		
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
		
	def readcalsfromfiles(self, Dialog):	
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
					item.setText(_translate("Dialog",str(self.calvalues[i,j])))# = float(item.text())
				except ValueError:
					item.setText(_translate("Dialog",str(0.0)))
		
		for i in range(0,len(self.morecaltablecolumnlabels)):
			item = self.morecaltableWidget.item(0,i)
			try:
				item.setText(_translate("Dialog",str(self.calvalues[len(self.caltablerowlabels)+i,0])))# = float(item.text())
			except ValueError:
				item.setText(_translate("Dialog",str(0.0)))
				
		for i in range(0, len(self.tdlcaltablerowlabels)):
			for j in range(0,len(self.tdlcaltablecolumnlabels)):
				item = self.tdlcaltableWidget.item(i,j)
				try:
					item.setText(_translate("Dialog",str(self.calvalues[i+len(self.caltablerowlabels)+len(self.morecaltablecolumnlabels),j])))# = float(item.text())
				except ValueError:
					item.setText(_translate("Dialog",str(0.0)))
					
		#for i in range(0,len(self.tablerowlabels)):
		#	item = ui.tableWidget.item(i, 0)
		#	item.setText(_translate("Dialog",str(self.tabledata[i,0])))
		#	item = ui.tableWidget.item(i, 1)
		#	item.setText(_translate("Dialog",str(self.tabledata[i,1])))
		#	item = ui.tableWidget.item(i, 2)
		#	item.setText(_translate("Dialog",str(self.tabledata[i,2])))
		
	def savecalibrations(self, Dialog):
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
					
		#for i in range(0,len(self.tablerowlabels)):
		#	item = ui.tableWidget.item(i, 0)
		#	item.setText(_translate("Dialog",str(self.tabledata[i,0])))
		#	item = ui.tableWidget.item(i, 1)
		#	item.setText(_translate("Dialog",str(self.tabledata[i,1])))
		#	item = ui.tableWidget.item(i, 2)
		#	item.setText(_translate("Dialog",str(self.tabledata[i,2])))		

		#self.tabWidget = QtWidgets.QTabWidget(Dialog)
		#self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1800, 925))
		#self.tabWidget.setObjectName("tabWidget")		
		#self.tab = QtWidgets.QWidget()
		#self.tab.setObjectName("tab")
		
		calupdatetext, contupdate = QInputDialog.getText(Dialog, 'Text Input Dialog', 'Please provide update comment. Press cancel to abort update')		
		
		#('Derpaderp', True)
		#('', True)
		
		#If cancel is clicked, ('', False)
		
		if contupdate:
			#print(text)#self.le1.setText(str(text))
			caltimestamp = 	time.strftime("%Y %b %d %H:%M:%S",time.gmtime())
			for i in range(0,len(self.calarray)):
				#caloutput = '\n'
				#caloutput += caltimestamp
				caloutput = [ "{:.6f}".format(x) for x in self.calvalues[i,:] ]
				caloutput = '\t'.join(caloutput)
				caloutput = '\n\n# '+ str(calupdatetext) + '\n' + caltimestamp+'\t'+caloutput
				#outputstring = [ "{:11.5g}".format(x) for x in output ]
				#outputstring = ','.join(outputstring)
				#outputstring += '\n'
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
	
		#outputstring = [ "{:11.5g}".format(x) for x in output ]
		#outputstring = ','.join(outputstring)
		#outputstring += '\n'
		
			
			
	def toggleswitched(self,Dialog):
		if self.flowsource.isChecked() : self.flowsource.setText("Calculated")
		else: self.flowsource.setText("User Input")
		if self.flowio.isChecked() : self.flowio.setText("Flow ON")
		else: self.flowio.setText("Flow OFF")
		if self.cvimode.isChecked() : self.cvimode.setText("Mode: Total")
		else: self.cvimode.setText("Mode: CVI")

	#Function runs when the "connect" button is clicked
	#Establishes server in separate thread for receiving data
	#	from DSM. Once established, it initializes a slot for
	#	replotting the data ~3 times a second.
	def connecting(self, Dialog):
		#Check to make sure that connection was not attempted multiple times in succession
		self.disconnecting(Dialog)
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
		
		#Removed: code for adding a scheduled job in a different thread.
		#self.sched.add_interval_job(self.CVIreplot(), seconds = 10)
		#self.sched.add_job(ui.CVIreplot, 'interval', seconds = 2)
		#self.sched.shutdown()
		
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
	def disconnecting(self, Dialog):
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

		_translate = QtCore.QCoreApplication.translate
		for i in range(0,len(self.tablerowlabels)):
			item = ui.tableWidget.item(i, 0)
			item.setText(_translate("Dialog",str(self.tabledata[i,0])))
			item = ui.tableWidget.item(i, 1)
			item.setText(_translate("Dialog",str(self.tabledata[i,1])))
			item = ui.tableWidget.item(i, 2)
			item.setText(_translate("Dialog",str(self.tabledata[i,2])))
		
		#self.dropdownlist.currentIndex()
		self.CVIplot.plot(self.plotdata[0,:], self.plotdata[self.dropdownlist.currentIndex()+1,:], clear = True)
		self.CVIplot2.plot(self.plotdata[0,:], self.plotdata[self.dropdownlist2.currentIndex()+1,:], clear = True)
		#if (self.dropdownlistline2.currentIndex() != 0) : self.CVIplot.plot(self.plotdata[0,:], self.plotdata[self.dropdownlistline2.currentIndex()+2:])
		#if (self.dropdownlist2line2.currentIndex() != 0): self.CVIplot2.plot(self.plotdata[0,:], self.plotdata[self.dropdownlist2line2.currentIndex()+2,:])
		
		self.CVIplot.setTitle(self.plottitles[self.dropdownlist.currentIndex()])
		self.CVIplot.setLabel('left',text = self.ylabels[self.dropdownlist.currentIndex()])
		
		self.CVIplot2.setTitle(self.plottitles[self.dropdownlist2.currentIndex()])
		self.CVIplot2.setLabel('left',text = self.ylabels[self.dropdownlist2.currentIndex()])
		
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
		
#		if (self.dropdownindex == 0):	
#			#self.CVIplot.setTitle("H2O")
#			self.CVIplot.plot(self.plotdata[0,:] , self.plotdata[1,:], clear=True)#, pen=None, symbol = 'o')
#		elif (self.dropdownindex == 1): 
#			self.CVIplot.plot( self.plotdata[0,:] , self.plotdata[2,:], clear=True)#, pen=None, symbol = 'o')
#		elif (self.dropdownindex == 2): 
#			self.CVIplot.plot( self.plotdata[0,:] , self.plotdata[3,:], clear=True)#, pen=None, symbol = 'o')
		#May not be necessary; however, it is supposed to force
		#plot to be completed
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
			valvepositions = [0]*4
			
			if ui.v1.isChecked() : valvepositions[0] = 1
			else: valvepositions[0] = 0
			if ui.v2.isChecked() : valvepositions[1] = 1
			else: valvepositions[1] = 0			
			if ui.v3.isChecked() : valvepositions[2] = 1
			else: valvepositions[2] = 0
			if ui.v4.isChecked() : valvepositions[3] = 1
			else: valvepositions[3] = 0
			
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
			tdl_cals = np.c_[ui.calvalues[21:,0], ui.calvalues[21:,1], ui.calvalues[21:,2], ui.calvalues[21:,3]]
			
			#print(C0)
			#print(C1)
			#print(C2)
			#print(more)
			#print(tdl_cals)
			
			#tdl_cals = [[0.00000000000000001,0.00000000000000000,0.00000000000000000,0.00000000000000000],[1.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000],[0.00000000000000000,0.00000000000000000,0.00000000000000000,0.00000000000000000]]
			#myArray=[[1,2],[3,4]]
			#tdl_poly_coeffs = [0]*4
	
			#tdl_poly_coeffs[0]=tdl_cals[0][0]+tdl_cals[0][1]*tdl_data[1]+tdl_cals[0][2]*tdl_data[1]*tdl_data[1]+tdl_cals[0][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			#tdl_poly_coeffs[1]=tdl_cals[1][0]+tdl_cals[1][1]*tdl_data[1]+tdl_cals[1][2]*tdl_data[1]*tdl_data[1]+tdl_cals[1][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			#tdl_poly_coeffs[2]=tdl_cals[2][0]+tdl_cals[2][1]*tdl_data[1]+tdl_cals[2][2]*tdl_data[1]*tdl_data[1]+tdl_cals[2][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]
			#tdl_poly_coeffs[3]=tdl_cals[3][0]+tdl_cals[3][1]*tdl_data[1]+tdl_cals[3][2]*tdl_data[1]*tdl_data[1]+tdl_cals[3][3]*tdl_data[1]*tdl_data[1]*tdl_data[1]

			
			
			
#			dataout, extra, calibrated, zerocorrectedflows = cvioutput( input , ui.flowio.isChecked(), valvepositions, ui.cvimode.isChecked() )
			output, calibrated = cvioutput( input , ui.flowio.isChecked(), valvepositions, ui.cvimode.isChecked(), C0, C1, C2, more, tdl_cals)
			
			#if( input[34] != -99.99 ) : input[34] = calibrated[10]/(calibrated[14]+273.15) * 0.000217 * input[34]

			#cvl is at index 36?
			#cvf3 is at index 41
			#cvfxwr0 is at index 49
			#opcc_Pcor is at index 69
			
			flowbyte = (2*int(ui.v1.isChecked()))**3+(2*int(ui.v2.isChecked()))**2+(2*int(ui.v3.isChecked()))**1+int(ui.v4.isChecked())

			#output = np.r_[input[0], int(ui.cvimode.isChecked())*2, flowbyte, 0, input[3:19], calibrated[10:16], zerocorrectedflows[:],
			#	cvl, cvrhoo_tdl, cvrho_tdl, cvrad, cvcfact_tdl,  
			#	cvf3, input[1], cvcnc1, cvcno1, cvcfact,  cvftc, cvrh, cvdp, 
			#	cvfxwr[0:4], cvf1wr, input[2], tdl_data[:], opcc, opcco, opc_data[0:2], 
			#	opcc_Pcor, opcco_Pcor, opc_press_mb, input[34:37]]
			
			#FLOW OUTPUTS ARE ALSO DECIDED IN THE CONNECTION SEQUENCE
			dataout = np.round(np.r_[ output[0], output[49:54], 0, 0, 0, 0, output[1], 0, 0, output[39], output[45], output[47:49], output[37] ],3)
			
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
			if not ui.flowsource.isChecked():
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
				dataout[6] = int(ui.v1.isChecked())
				dataout[7] = int(ui.v2.isChecked())
				dataout[8] = int(ui.v3.isChecked())
				dataout[9] = int(ui.v4.isChecked())
			
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
			
			dsmtime
			INLET, 				cvimode (CVI = 0, total = 2)
			FXflows,  			flowbinary (binary representation of flows)
			valve_changes, 		Number of changes?
			cvf1R, 				input[3:19]
			cvfx0R, 
			cvfx1R, 
			cvfx2R, 
			cvfx3R, 
			cvfx4R, 
			cvfx5R, 
			cvfx6R, 
			cvfx7R, 
			cvfx8R, 
			cvpcnR, 
			cvttR, 
			cvtpR, 
			cvtsR, 
			cvtcnR, 
			cvtaiR, 
			cvpcnC, 			calibrated[10:16]
			cvttC, 
			cvtpC, 
			cvtsC, 
			cvtcnC, 
			cvtaiC, 
			cvf1, 				calibrated[0:10]
			cvfx0c, 
			cvfx1c, 
			cvfx2c,  
			cvfx3c, 
			cvfx4c, 
			cvfx5c, 
			cvfx6c,  
			cvfx7c, 
			cvfx8c, 
			cvl, 				start extra array from processed
			cvrhoo_tdl,  
			cvrho_tdl, 
			cvrad, 
			cvcfact_tdl,  		same as cfact_tdl
			cvf3, 
			cvtas, 				input[0]
			cvcnc1, 
			cvcno1, 
			cvcfact,  
			cvftc, 
			cvrh, 
			cvdp, 				end extra array from processed
			cvfx0WR, 
			cvfx2WR, 
			cvfx3WR, 
			cvfx4WR, 
			cvfx1WR, 
			cnt1, 
			H2O_TDL,  
			pTDL, 
			tTDL, 
			TDLsignalL,
			TDLlaser, 
			TDLline, 
			TDLzero, 
			TTDLencl, 
			TTDLtec,
			TDLtrans, 
			opcc, 
			opcco, 
			opcnts, 
			opcflow, 
			opcc_Pcor, 
			opcco_Pcor, 
			opcc_pres_mb, 
			H2O_PIC_cvrtd, 
			180, 
			HDO 
			'''
			
			#Send off the new data to the DSM
			self.client_sock.send(dataout)	
			
			#Update front panel with data sent to dsm
			ui.datatodsm.setText(str(dataout).replace(",", ", "))	
			
			#print( zerocorrectedflows )

			#Try to update the data array to accommodate a new column
			#	of data. 
			
			#for i in range(1,len(self.tablerowlabels)):
			#	for j in range(1,len(self.tablerow)
			ui.tabledata = np.c_[input[3:19], calibrated[0:16], np.r_[zerocorrectedflows[:], [np.nan]*6]]
			try:
				#dim = ui.plotdata.shape
				#For testing purposes
				#ui.counter += 1
				#Consider adding to ignore crazy data
				#if (input[19] < 0): input[19] = np.nan
				
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
		#ui.disconnecting(Dialog)
			
if __name__ == "__main__":

	#Create time for plot updating
	timer = QTimer();
	
	#Initialize GUI
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	
	#Begin Event Loop
	#loop = asyncio.get_event_loop()
	#asyncio.ensure_future(app.exec_())
	#asyncio.ensure_future(ui.server_loop_in_thread)	
	#loop.run_forever() 
	sys.exit(app.exec_())