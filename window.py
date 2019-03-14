from PyQt5 import QtGui
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QActionGroup, QFileDialog, \
    QTableWidget, QTableWidgetItem, QVBoxLayout, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect, Qt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.uic.properties import QtCore
from scipy.interpolate import spline
class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 50
        self.top = 50
        self.width = 1500
        self.height = 1500
        self.setScreen()
        loadUi('Screen.ui', self)
        self.actionLoad.triggered.connect(self.load_csv_file)
        self.actionPlot_Data.triggered.connect(self.plot)
        #self.show()
    def setScreen(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def on_click_scatter(self):
        dataset=data.iloc[:,:].values
        x_axis=dataset[:,0]
        y_axis=dataset[:,1]
        plt.scatter(x_axis,y_axis)
        plt.show()

    def on_click_scatter_smooth(self):
        dataset = data.iloc[:, :].values
        x_axis= dataset[:, 0]
        y_axis= dataset[:, 1]
        x_smooth = np.linspace(x_axis.min(), x_axis.max(), 500)
        y_smooth = spline(x_axis,y_axis,x_smooth)
        plt.plot(x_smooth, y_smooth)
        plt.scatter(x_axis,y_axis)
        plt.show()

    def on_click_lines(self):
        dataset = data.iloc[:, :].values
        x_axis= dataset[:, 0]
        y_axis= dataset[:, 1]
        plt.plot(x_axis,y_axis)
        plt.show()
    def plot(self):

        button1 = QPushButton('scatter points ', self)
        button1.move(100, 70)
        button1.clicked.connect(self.on_click_scatter)
        button2 = QPushButton('scatter points with smooth lines', self)
        button2.move(400, 70)
        button2.resize(200, 31)
        button2.clicked.connect(self.on_click_scatter_smooth)
        button3 = QPushButton('lines', self)
        button3.move(800, 70)
        button3.clicked.connect(self.on_click_lines)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.comboBox1= QComboBox(centralWidget)
        self.comboBox1.setGeometry(QRect(3, 3, 600, 31))
        self.comboBox1.setObjectName(("comboBox1"))
        dimension=data.shape
        columns = list(data.head(0))
        self.comboBox1.addItem('please select column1')
        for i in range (0,dimension[1]):
             self.comboBox1.addItem(columns[i])

        self.comboBox2 = QComboBox(centralWidget)
        self.comboBox2.setGeometry(QRect(610, 3, 600, 31))
        self.comboBox2.setObjectName(("comboBox2"))
        self.comboBox2.addItem('please select column2')
        for i in range (0,dimension[1]):
                self.comboBox2.addItem(columns[i])

    def load_csv_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName= QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                       "Python Files (*.csv)", options=options)

        global data

        data=pd.read_csv(self.fileName[0])#reading csv file from the path and storing it into data
        self.size=data.shape
        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()
    def createTable(self):
        df=data.shape
      #  self.setCentralWidget(centralWidget)
        #self.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.tableWidget = QTableWidget(centralWidget)

        self.tableWidget.setRowCount(df[0])
        self.tableWidget.setColumnCount(df[1])

        list=data.values
        for i in range(0,df[0]):
            for j in range(0,df[1]):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(list[i][j])))

        #self.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

       # self.table.setEditTriggers(QWidget.QAbstractItemView.NoEditTriggers)
if __name__ == '__main__':
    application = QApplication(sys.argv)
    start= MainFrame()
    start.show()
    sys.exit(application.exec())
