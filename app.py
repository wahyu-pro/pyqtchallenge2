import requests
from PyQt5.QtWidgets import *
from PyQt5 import *

fetch = requests.get("https://jsonplaceholder.typicode.com/users")
jsonUser = fetch.json()

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.head = ["id", "name", "username", "email", "address"]
        self.createTable()
        self.mainUI()
        self.setWidget()
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Line Edit")

    def mainUI(self):
        # linetext
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Search name here ...")
        # push button
        self.button = QPushButton("Enter")
        # signal slot push button
        self.button.clicked.connect(self.showName)
        # signal slot line edit
        self.lineEdit.returnPressed.connect(self.showName)
        # label
        self.resultInput = QLabel()

    def createTable(self):
        row = len(list(jsonUser))
        self.table = QTableWidget()
        self.table.setRowCount(row)
        self.table.setColumnCount(len(self.head))
        for row in range(len(jsonUser)):
            for col in range(5):
                if col == 0:
                    self.table.setItem(row,col,QTableWidgetItem(str(jsonUser[row]["id"])))
                elif col == 1:
                    self.table.setItem(row,col,QTableWidgetItem(jsonUser[row]["name"]))
                elif col == 2:
                    self.table.setItem(row,col,QTableWidgetItem(jsonUser[row]["username"]))
                elif col == 3:
                    self.table.setItem(row,col,QTableWidgetItem(jsonUser[row]["email"]))
                elif col == 4:
                    self.table.setItem(row,col,QTableWidgetItem("{} {}".format(jsonUser[row]["address"]["city"], jsonUser[row]["address"]["street"])))

        self.table.setHorizontalHeaderLabels(self.head)
        self.table.verticalHeader().hide()

    def setWidget(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.resultInput)
        self.layout.addWidget(self.table)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

    def showName(self):
        name = self.lineEdit.text()
        find = self.table.findItems(name, QtCore.Qt.MatchExactly)
        res = self.table.currentRow()
        if find:
            results = '\n'.join(
                '%d,%d' % (item.row(), item.column())
                for item in find)
            rep = results.split(",")
            row, col = rep
            data = []
            for x in range(len(self.head)):
                res = self.table.item(int(row),int(x)).text()
                data.append(res)
            QMessageBox.information(self, "result", "<b>Name</b> : {} <br> <b>Username</b> : {} <br> <b>Email</b> : {} <br> <b>Address</b> : {}".format(data[1], data[2], data[3], data[4]))
        elif name == "":
            QMessageBox.warning(self, "result", "field don't empty")
        else:
            QMessageBox.warning(self, "result", f"{name} not found")


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()