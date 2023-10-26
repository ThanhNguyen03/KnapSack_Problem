from PySide6.QtCore import (QRegularExpression,Qt)
from PySide6.QtGui import (QColor, QRegularExpressionValidator, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,QStyledItemDelegate)

from gui_ui import *

def knapsack_hill_climbing(values, weights, max_weight):
    n = len(values)
    current_state = [0] * n

    def calculate_total_value(state):
        return sum(value * state[i] for i, value in enumerate(values))

    def calculate_total_weight(state):
        return sum(weight * state[i] for i, weight in enumerate(weights))

    def get_neighbors(state):
        neighbors = []
        for i in range(n):
            neighbor = list(state)
            neighbor[i] = 1 - neighbor[i]
            neighbors.append(neighbor)
        return neighbors

    def hill_climbing(state):
        current_value = calculate_total_value(state)
        while True:
            neighbors = get_neighbors(state)
            best_neighbor = max(neighbors, key=lambda x: calculate_total_value(x))

            if calculate_total_weight(best_neighbor) > max_weight:
                break
            state = best_neighbor

        return state

    result_state = hill_climbing(current_state)
    return result_state


values = [3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5,6]
weights = [2, 3, 4, 5,3, 4, 5, 6,3, 4, 5,6]
max_weight = 14


# result = knapsack_hill_climbing(values, weights, max_weight)
# print("Chọn vật phẩm:", result)
# print("Tổng giá trị:", sum(value * result[i] for i, value in enumerate(values)))
# print("Tổng trọng lượng:", sum(weight * result[i] for i, weight in enumerate(weights)))

class ColorDelegate(QStyledItemDelegate):
    def __init__(self, indexes, parent=None):
        super().__init__(parent)
        self.indexes = indexes

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        if index.row()+1 in self.indexes:
            option.backgroundBrush = QColor(0, 255, 0)  # Đặt màu nền cho row

class MainHandle(Ui_MainWindow):
    def __init__(self):
        self.indexes = []
        self.values=[]
        self.weights =[]
        self.max_weight = 0
        # ---------------
        self.setupUi(mainWindow)
        # ---------------
        self.value.setPlaceholderText("Nhập giá trị của túi!")
        self.weight.setPlaceholderText("Nhập khối lượng của túi!")
        self.maxWeight.setPlaceholderText("Nhập khối lượng tối đa có thể mang!")

        regex = QRegularExpression("[0-9]+")  # Chỉ cho phép nhập các ký tự từ 0 đến 9
        validator = QRegularExpressionValidator(regex)
        self.value.setValidator(validator)
        self.weight.setValidator(validator)
        self.maxWeight.setValidator(validator)
        # ---------------
        self.btnSubmit.clicked.connect(self.Submit)
        self.btnReset.clicked.connect(self.Reset)
        self.btnCalc.clicked.connect(self.Calc)

    def Calc(self):
        result_ = knapsack_hill_climbing(self.values, self.weights, self.max_weight)
        # Tạo danh sách để lưu index của các giá trị =1
        
        # Duyệt qua mảng
        for i, value in enumerate(result_):
            if value == 1:
                self.indexes.append(i+1)

        s=', '.join(str(x) for x in self.indexes)        
        # Đặt nội dung của QLineEdit
        self.result.setText(str(s))
        self.valueresult.setText(str(sum(value * result_[i] for i, value in enumerate(self.values))))
        self.weightresult.setText(str(sum(weight * result_[i] for i, weight in enumerate(self.weights))))
        self.updateTableViewColors()
        self.showTable()
    
    def updateTableViewColors(self):
        model = self.tableView.model()
        for row in range(model.rowCount()):
            model.index(row, 0)  # Chọn cell của cột đầu tiên (Value)
            if row+1 in self.indexes:  # Kiểm tra nếu row có vị trí thứ tự trong danh sách indexes
                self.tableView.setRowHidden(row, False)  # Hiển thị row
                # self.tableView.setAlternatingRowColors(QColor(255,0,0)) # Đặt màu xen kẽ cho row
                # Tạo ColorDelegate với danh sách indexes
                delegate = ColorDelegate(self.indexes)
                # Gán delegate cho QTableView
                self.tableView.setItemDelegate(delegate)

    def Reset(self):
        self.values.clear()
        self.weights.clear()
        self.maxWeight_2.clear()

        self.showTable()

    def Submit(self):
        if self.value.text().strip():
            if self.weight.text().strip():
                self.weights.append(self.weight.text())
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle('Lỗi!')
                msg_box.setText('Khối lượng vật phẩm không được để trống!')
                msg_box.addButton(QMessageBox.Close)
                msg_box.exec_()

            self.values.append(self.value.text())
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle('Lỗi!')
            msg_box.setText('Giá trị vật phẩm không được để trống!')
            msg_box.addButton(QMessageBox.Close)
            msg_box.exec_()

        if self.maxWeight.text().strip():
            self.max_weight = int(self.maxWeight.text())
        self.maxWeight_2.setText(str(self.max_weight))

        self.value.clear()
        self.weight.clear()
        self.maxWeight.clear()

        self.showTable()
        
    def showTable(self):
        # Tạo mô hình dữ liệu
        model = QStandardItemModel()
        model.setColumnCount(2)  # Đặt số cột là 2

        # Thêm các cặp giá trị vào mô hình dữ liệu
        for value, weight in zip(self.values, self.weights):
            item_value = QStandardItem(str(value))
            item_weight = QStandardItem(str(weight))
            model.appendRow([item_value, item_weight])

        # Tạo QTableView và đặt mô hình dữ liệu
        self.tableView.setModel(model)

        # Đặt tiêu đề cho các cột
        model.setHeaderData(0, Qt.Horizontal, "Value")
        model.setHeaderData(1, Qt.Horizontal, "Weight")

        
if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    GUI = MainHandle()
    mainWindow.show()
    sys.exit(app.exec_())