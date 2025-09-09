import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):

    DEFAULT_SIZE = (700, 500)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TriScope")
        self.resize(*self.DEFAULT_SIZE)

        self.view = TriangleView()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.view)

        container = QtWidgets.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

class TriangleView(QtWidgets.QGraphicsView):

    VIEW_SIZE = (700, 500)

    def __init__(self):
        super().__init__()

        self.scene = QtWidgets.QGraphicsScene(0, 0, *self.VIEW_SIZE)
        self.setScene(self.scene)

        triangle = [
            QtCore.QPointF(100, 400),
            QtCore.QPointF(250, 100),
            QtCore.QPointF(400, 400) 
            ]
        self.triangle_item = QtWidgets.QGraphicsPolygonItem(triangle)

        triangle_pen = QtGui.QPen()
        triangle_pen.setWidth(5)
        self.triangle_item.setPen(triangle_pen)

        self.scene.addItem(self.triangle_item)

        self.handles = []
        for point in triangle:
            handle = TriangleHandle(point.x(), point.y())
            self.handles.append(handle)
            self.scene.addItem(handle)

class TriangleHandle(QtWidgets.QGraphicsEllipseItem):

    HANDLE_SIZE = 25

    def __init__(self, x, y):
        super().__init__(x - TriangleHandle.HANDLE_SIZE / 2, y - TriangleHandle.HANDLE_SIZE / 2, TriangleHandle.HANDLE_SIZE, TriangleHandle.HANDLE_SIZE)
        handle_brush = QtGui.QBrush(QtGui.QColor('#ff9900'))
        self.setBrush(handle_brush)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()