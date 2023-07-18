import sys
from PySide2.QtCore import QRegExp,Qt
from PySide2.QtGui import QIntValidator,QRegExpValidator,QIcon
from PySide2.QtWidgets import QApplication, QMainWindow,QMessageBox,QComboBox, QLineEdit,QPushButton, QLabel ,QWidget,QGridLayout,QVBoxLayout ,QSpacerItem, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")

        # creating input box for the function and a restricting the user to specific input characters
        self.f_x = QLineEdit()
        self.f_x.setPlaceholderText('Please Enter the function')
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

        # creating some optional parameters

        #title
        self.title = QLineEdit()
        self.title.setPlaceholderText('Please Enter the plot title')


        #color
        self.color = QComboBox()
        self.color.addItems(["black","blue", "red", "green", "fuchsia", "gold"])

        #linestyle
        self.linestyle = QComboBox()
        self.linestyle.addItems(["solid", "dashed", "dotted"])    

        #xlabel
        self.x_label = QLineEdit()
        self.x_label.setPlaceholderText('Please Enter x label')

        #xlabel
        self.y_label = QLineEdit()
        self.y_label.setPlaceholderText('Please Enter y label')

        # creating grid layout and adding the previous widgets to it
        user_input = QGridLayout()
        user_input.setContentsMargins(5,5,5,5)
        user_input.setHorizontalSpacing(20)
        spacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        user_input.addWidget(QLabel("Enter the Function"),0,0)
        user_input.addWidget(self.f_x,1,0)

        user_input.addWidget(QLabel("Enter Minimum value of x"),0,1)
        user_input.addWidget(self.min_x,1,1)

        user_input.addWidget(QLabel("Enter Maximum value of x"),0,2)
        user_input.addWidget(self.max_x,1,2)

        user_input.addItem(spacer, 2, 0, 1, user_input.columnCount())


        user_input.addWidget(QLabel("Enter the title for the plot (Optional)"),3,0)
        user_input.addWidget(self.title,4,0)    

        user_input.addWidget(QLabel("Enter X label for the plot (Optional)"),3,1)
        user_input.addWidget(self.x_label,4,1)

        user_input.addWidget(QLabel("Enter Y label for the plot (Optional)"),3,2)
        user_input.addWidget(self.y_label,4,2)   

        user_input.addItem(spacer, 5, 0, 1, user_input.columnCount())

        user_input.addWidget(QLabel("Choose your favourite color"),6,0)
        user_input.addWidget(self.color,7,0)

        user_input.addWidget(QLabel("Choose the plot linestyle"),6,1)
        user_input.addWidget(self.linestyle,7,1)

        # creating a button and adding it to the user input layout
        
        self.button = QPushButton("Plot")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        user_input.addItem(spacer, 8, 0, 1, user_input.columnCount())
        user_input.addWidget(self.button,9,1)


        widget = QWidget()
        widget.setLayout(user_input)
        self.setCentralWidget(widget)


    def the_button_was_clicked(self):
        #collecting the user inputs from the gui
        func = self.f_x.text()
        func = func.replace("**", "$")
        func = func.replace("//", "$")
        func = func.replace("^", "**")
        minimum_x = self.min_x.text()
        maximum_x = self.max_x.text()
        color = self.color.currentText()
        xlabel = self.x_label.text()
        ylabel = self.y_label.text()
        title = self.title.text()
        linestyle = self.linestyle.currentText()

        # Trying to plot the function, if error then the user input is wrong, Display him a message
        try:
            self.w = plot_win(func,int(minimum_x),int(maximum_x),title,color,xlabel,ylabel,linestyle)
            self.w.show()
        except:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Wrong Input")
            dlg.setText("Please input a valid function and limits")
            dlg.setInformativeText("1- Limits must be valid numbers.\n2- Function must be a valid equation.\n3- Supported operators are : +, -, /, *, ^, ()")
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec_() 


class plot_win(QWidget):
    """
    class to make a new window with the plotted function
    """
    def __init__(self,fun_str,min_x,max_x,title,color,xlabel,ylabel,linestyle):
        super().__init__()

        def f_x(x):
            #checking if the input is constant
            try:
                y = float(eval(fun_str))
                return np.full_like(x, y)
            # if not return the expression
            except:         
                return eval(fun_str)

        # ploting the function with the user inputs
        sc = MplCanvas(self, width=10, height=8, dpi=100)
        x = np.linspace(min_x,max_x,1000)

        sc.axes.plot(x,f_x(x),color=color,linestyle=linestyle,linewidth=2)
        sc.axes.tick_params(labelsize=10)
        sc.axes.set_facecolor("aliceblue")
        if xlabel:
            sc.axes.set_xlabel(xlabel,fontsize=16,fontdict={'family':'serif','color':'black','size':16})
        if ylabel:
            sc.axes.set_ylabel(ylabel,fontsize=16,fontdict={'family':'serif','color':'black','size':16})
        if title:
            sc.axes.set_title(title,fontsize=20,fontdict={'family':'serif','color':'black','size':20},pad=10)

        #adding a navigation toolbar to the plot
        toolbar = NavigationToolbar(sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        self.setLayout(layout)
        self.setWindowTitle('Plotted Function')
        self.setWindowIcon(QIcon("icon.png"))


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi,facecolor='lightblue')
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)








