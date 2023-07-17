from window import *



def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.setStyleSheet("""
                    QMainWindow {background-color: #C5FAD5;}

                    QPushButton {
                        font: bold 14pt Times New Roman;
                        color: #013f5e;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 5px;
                        background-color: #F1AC88;
                        min-width: 100px;
                        min-height: 70px;
                    }
                    QLabel {
                        font: bold 12pt Times New Roman;
                        color: #150b4a;
                        qproperty-alignment: AlignCenter;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 10;
                        background-color: #c5aefc;
                    }
                    QComboBox {
                        font:  10pt Arial;
                        color: #234E70;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 5px;
                        background-color: #FBF8BE;
                    }
                    QLineEdit {
                        font:  10pt Arial;
                        color: #381d06;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 5px;
                        background-color: #FFFFD2;
                    }
                """)
    app.exec_()






if __name__ == "__main__":
    main()