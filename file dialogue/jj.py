import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QStackedWidget, QHBoxLayout, QLabel, QFileDialog
)
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure
import numpy as np

class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Matplotlib Figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Plot data
        self.plot_graph()

        # Download button
        download_btn = QPushButton("Download Graph")
        download_btn.clicked.connect(self.download_graph)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(download_btn)

        self.setLayout(layout)

    def plot_graph(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(x, y)
        ax.set_title("Sine Wave")
        self.canvas.draw()

    def download_graph(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Graph", "", "PNG Files (*.png);;All Files (*)")
        if file_path:
            self.figure.savefig(file_path)

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("<h1>Welcome to the Graph App</h1>")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Graph App")

        # Stack for multiple pages
        self.stack = QStackedWidget()
        self.home_page = HomePage()
        self.graph_page = GraphWidget()

        self.stack.addWidget(self.home_page)   # Index 0
        self.stack.addWidget(self.graph_page)  # Index 1

        # Navigation buttons
        nav_layout = QHBoxLayout()
        home_btn = QPushButton("Home")
        graph_btn = QPushButton("Graph")

        home_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        graph_btn.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(graph_btn)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
