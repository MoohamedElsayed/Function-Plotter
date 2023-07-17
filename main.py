from window import *



def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.setStyleSheet("""
                    QPushButton {
                        font: bold 12pt Times New Roman;
                        color: #ab0202;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 5px;
                        background-color: #ecf0d8;
                    }
                    QLabel {
                        font: bold 12pt Times New Roman;
                        color: #0824fc;
                        qproperty-alignment: AlignCenter;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 10;
                        background-color: #ecf0d8;
                    }
                    QComboBox {
                        font:  10pt Arial;
                        color: #333333;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 5px;
                        background-color: #e0f0ff;
                    }
                    QLineEdit {
                        font:  10pt Arial;
                        color: #333333;
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        padding: 5px;
                        background-color: #e0f0ff;
                    }
                """)
    app.exec_()






if __name__ == "__main__":
    main()