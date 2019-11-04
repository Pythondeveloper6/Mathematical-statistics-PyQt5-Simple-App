'''
    simple GUI to calculate
     [ Mode , Mean , Median , Variance , Five Number Summary ,Standered deviation ] 
    developed by : Mahmoud Ahmed - pythondeveloper6@gmail.com

'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import math
import os
from os import path
import statistics
import numpy as np
from PyQt5.uic import loadUiType

FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__), "UI.ui"))

class Main(QMainWindow,FORM_CLASS):
    ''' simple pyqt5 app to calculate Median ,Mean , Mode , Variance ,
                   Five Number Summary , Standered deviation '''
    def __init__(self , parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()


    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Get_Median)
        self.pushButton_2.clicked.connect(self.Clear)

    def Clear(self):
        self.lineEdit.setText(' ')

    def Get_Median(self):
        numbers = self.lineEdit.text()
        numbers = numbers.split(' ')
        numbers = list(filter(None, numbers))
        # numbers = [int(i) for i in numbers]


        if self.comboBox.currentIndex() == 0 :
            numbers = list(map(float, numbers))
            result = self.median(numbers)
            QMessageBox.information(self, 'Result', "The Median = %s" %(result), QMessageBox.Ok )


        if self.comboBox.currentIndex() == 1 :
            if len(numbers) == len(set(numbers)):
                QMessageBox.information(self, 'Result', "The Values Are Equal", QMessageBox.Ok)
            else:
                result = self.mode(numbers)
                QMessageBox.information(self, 'Result', "The Mode = %s" %(result), QMessageBox.Ok )

        if self.comboBox.currentIndex() == 2 :
            numbers = list(map(float, numbers))
            result = self.mean(numbers)
            QMessageBox.information(self, 'Result', "The Mean = %s" %(result), QMessageBox.Ok )



        if self.comboBox.currentIndex() == 3 :
            numbers = list(map(float, numbers))
            result = self.variance(numbers)
            QMessageBox.information(self, 'Result', "The Variance = %s" %(result), QMessageBox.Ok )


        if self.comboBox.currentIndex() == 4 :
            numbers = list(map(float, numbers))
            result = self.standard_deviation(numbers)
            QMessageBox.information(self, 'Result', "The Standerd Deviation = %s" %(result[0]), QMessageBox.Ok )



        if self.comboBox.currentIndex() == 5 :
            numbers = list(map(float, numbers))
            result = self.five_number_summary(numbers)
            # print(result)
            # QMessageBox.information(self, 'Result', "The Result = %s" %(result), QMessageBox.Ok )






    def mean(self , data):
        return float(sum(data) / len(data))


    def median(self , data):
        if type(data) is int:
            return (float(data))
        elif type(data) is list:
            data.sort()

            if len(data) == 1:
                return (float(data[0]))
            elif len(data) % 2 == 1:
                return (float(data[int(len(data) / 2)]))

            # else
            middleIndex = len(data) / 2
            return ((data[int(middleIndex - .5)] + data[int(middleIndex + .5)]) / 2)


    def mode(self , data):
        max_count = 0
        modes = []
        number_counter = {}

        if type(data) is int:
            return (data)
        elif type(data) is list and len(data) > 0:
            data.sort()

            for ii in data:
                if ii in number_counter.keys():
                    number_counter[ii] = number_counter[ii] + 1
                else:
                    number_counter[ii] = 1
                if number_counter[ii] == max_count:
                    modes.append(ii)
                elif number_counter[ii] > max_count:
                    modes = [ii]
                    max_count = number_counter[ii]

            modes.sort()
            return (modes)


    def variance(self , data , sample=True):
        if len(data) < 2:
            return(None)

        m = self.mean(data)
        if sample:
            return(float(sum([pow(x - m, 2) for x in data]) / (len(data) - 1)))
        else:
            return(float(self.mean([pow(x - m, 2) for x in data])))

    def standard_deviation(self , data, sample=True):
        return math.sqrt(self.variance(data, sample))


    def five_number_summary(self , data):
        print('Max Value %s ' %(max(data)))
        print('Min Value %s ' % (min(data)))
        print('Median Value %s ' % (self.median((data))))
        return



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()    


if __name__ == '__main__':
        main()
