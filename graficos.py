import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class CanvasGrafico(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        super().__init__(self.fig)
        self.setParent(parent)

    def graficar_stock_sucursal(self, df):
        self.ax.clear()
        resumen = df.groupby("Sucursal")["Stock_Disponible"].sum()
        resumen.plot(kind="bar", ax=self.ax, color="#2b5c8f", edgecolor="black")
        self.ax.set_title("Stock Total Disponible por Sucursal")
        self.ax.set_xlabel("Sucursal")
        self.ax.set_ylabel("Unidades Totales")
        self.ax.grid(axis="y", linestyle="--", alpha=0.7)
        self.fig.tight_layout()
        self.draw()

    def graficar_categoria_precio(self, df):
        self.ax.clear()
        resumen = df.groupby("Categoria")["Precio_Unitario"].mean()
        resumen.plot(kind="pie", ax=self.ax, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
        self.ax.set_title("Precio Promedio por Categoría")
        self.ax.set_ylabel("")
        self.fig.tight_layout()
        self.draw()