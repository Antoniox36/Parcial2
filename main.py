import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QLabel, QHeaderView, QTextEdit
)
from PyQt5.QtCore import Qt

from generador_datos import generar_o_cargar_inventario, obtener_resumen_estadistico
from graficos import CanvasGrafico

class DashboardInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Análisis de Inventario - Empresa Salvadoreña")
        self.resize(1100, 700)

        self.df = generar_o_cargar_inventario()
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # Panel Izquierdo: Tabla y botones
        left_layout = QVBoxLayout()
        
        lbl_titulo = QLabel("Inventario General de Productos")
        lbl_titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        left_layout.addWidget(lbl_titulo)

        self.table = QTableWidget()
        self.cargar_tabla()
        left_layout.addWidget(self.table)

        btn_barras = QPushButton("Ver Stock por Sucursal")
        btn_barras.clicked.connect(self.mostrar_grafico_barras)
        left_layout.addWidget(btn_barras)

        btn_pie = QPushButton("Ver Precio Promedio por Categoría")
        btn_pie.clicked.connect(self.mostrar_grafico_pie)
        left_layout.addWidget(btn_pie)

        btn_stats = QPushButton("Mostrar Inspección de Datos (Pandas)")
        btn_stats.clicked.connect(self.mostrar_estadisticas)
        left_layout.addWidget(btn_stats)

        main_layout.addLayout(left_layout, stretch=2)

        # Panel Derecho: Gráficos Matplotlib e inspección
        right_layout = QVBoxLayout()

        self.canvas = CanvasGrafico(self)
        right_layout.addWidget(self.canvas, stretch=3)

        lbl_stats = QLabel("Resumen de Inspección (Pandas):")
        lbl_stats.setStyleSheet("font-weight: bold;")
        right_layout.addWidget(lbl_stats)

        self.txt_stats = QTextEdit()
        self.txt_stats.setReadOnly(True)
        right_layout.addWidget(self.txt_stats, stretch=2)

        main_layout.addLayout(right_layout, stretch=3)

        self.mostrar_grafico_barras()

    def cargar_tabla(self):
        self.table.setRowCount(len(self.df))
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(self.df.columns)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(len(self.df)):
            for j in range(len(self.df.columns)):
                item = QTableWidgetItem(str(self.df.iloc[i, j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(i, j, item)

    def mostrar_grafico_barras(self):
        self.canvas.graficar_stock_sucursal(self.df)

    def mostrar_grafico_pie(self):
        self.canvas.graficar_categoria_precio(self.df)

    def mostrar_estadisticas(self):
        resumen = obtener_resumen_estadistico(self.df)
        self.txt_stats.setText(resumen)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardInventario()
    window.show()
    sys.exit(app.exec_())