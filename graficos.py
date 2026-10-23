import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class CanvasGrafico(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.Figure(figsize=(6, 4))
        super().__init__(self.fig)
        self.setParent(parent)

    def graficar_stock_sucursal(self, df):
        self.fig.clear()  # Limpia la figura completa para resetear el aspecto
        ax = self.fig.add_subplot(111)
        
        resumen = df.groupby("Sucursal")["Stock_Disponible"].sum()
        resumen.plot(kind="bar", ax=ax, color="#2b5c8f", edgecolor="black")
        
        ax.set_title("Stock Total Disponible por Sucursal")
        ax.set_xlabel("Sucursal")
        ax.set_ylabel("Unidades Totales")
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        
        # Rotar etiquetas del eje X para que no se amontonen
        plt.setp(ax.get_xticklabels(), rotation=0, ha="center")
        
        self.fig.tight_layout()
        self.draw()

    def graficar_categoria_precio(self, df):
        self.fig.clear()  # Limpia la figura completa
        ax = self.fig.add_subplot(111)
        
        resumen = df.groupby("Categoria")["Precio_Unitario"].mean()
        resumen.plot(kind="pie", ax=ax, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
        
        ax.set_title("Precio Promedio por Categoría")
        ax.set_ylabel("")
        
        self.fig.tight_layout()
        self.draw()