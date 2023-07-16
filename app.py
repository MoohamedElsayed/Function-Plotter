import sys
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QIntValidator,QRegExpValidator
from PySide2.QtWidgets import QApplication, QMainWindow,QMessageBox, QLineEdit,QPushButton, QLabel ,QWidget,QGridLayout,QVBoxLayout 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")

        # creating input box for the function and a restricting the user to specific input characters
        self.f_x = QLineEdit()
        self.f_x.setPlaceholderText('Please Enter the Function')
        accepted_inputs = QRegExp("[xX0-9()*/^+-]+")
        input_validator = QRegExpValidator(accepted_inputs, self.f_x)
        self.f_x.setValidator(input_validator)

        # creating input box for min x and restricting the user for int only
        self.min_x = QLineEdit()
        self.min_x.setPlaceholderText('Please Enter min value of x')
        self.min_x.setValidator(QIntValidator())

        # creating input box for max x and restricting the user for int only
        self.max_x = QLineEdit()
        self.max_x.setPlaceholderText('Please Enter max value of x')
        self.max_x.setValidator(QIntValidator())

        # creating grid layout and adding the previous widgets to it
        user_input = QGridLayout()
        user_input.addWidget(QLabel("Function"),0,0)
        user_input.addWidget(self.f_x,1,0)

        user_input.addWidget(QLabel("Min x"),0,1)
        user_input.addWidget(self.min_x,1,1)

        user_input.addWidget(QLabel("Max x"),0,2)
        user_input.addWidget(self.max_x,1,2)

        # creating a button and adding it to the user input layout
        
        self.button = QPushButton("Plot")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        final_layout = QVBoxLayout()
        final_layout.addLayout(user_input)
        final_layout.addWidget(self.button)


        widget = QWidget()
        widget.setLayout(final_layout)
        self.setCentralWidget(widget)


    def the_button_was_clicked(self):
        func = self.f_x.text()
        minimum_x = self.min_x.text()
        maximum_x = self.max_x.text()

        try:
            self.w = plot_win(func,int(minimum_x),int(maximum_x))
            self.w.show()
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Wrong Input")
            dlg.setText("Please input a valid function and limits")
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec_() 


class plot_win(QWidget):
    """
    class to make a new window with the plotted function
    """
    def __init__(self,fun_str,min_x,max_x):
        super().__init__()

        def f_x(x):
            #checking if the input is constant
            try:
                y = float(eval(fun_str))
                return np.full_like(x, y)
            # if not return the expression
            except:         
                return eval(fun_str)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        x = np.linspace(min_x,max_x,1000)
        sc.axes.plot(x,f_x(x))

        toolbar = NavigationToolbar(sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        self.setLayout(layout)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()