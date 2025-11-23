import matplotlib.pyplot as plt
import numpy as np

# Datos simulados para el reporte
def generar_graficos():
    # 1. Gráfico de Distribución (Pastel)
    labels = ['Débiles (Comunes)', 'Medias (Solo letras)', 'Fuertes (Seguras)']
    sizes = [45, 30, 25]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    explode = (0.1, 0, 0)  # resaltar las débiles

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Distribución de Seguridad de Contraseñas Analizadas')
    plt.savefig('grafico_distribucion.png')
    print("Generado: grafico_distribucion.png")

    # 2. Gráfico de Entropía (Barras)
    tipos = ['"123456"', '"password"', '"Juan123"', '"Tr0ub4dor&3"', '"Xy9#mK2$pL"']
    entropias = [10, 15, 35, 60, 95] # Bits aproximados

    plt.figure(figsize=(10, 6))
    bars = plt.bar(tipos, entropias, color=['red', 'red', 'orange', 'blue', 'green'])
    plt.ylabel('Entropía (Bits)')
    plt.title('Comparación de Entropía por Tipo de Contraseña')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Añadir valores encima de las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 1), ha='center', va='bottom')

    plt.savefig('grafico_entropia.png')
    print("Generado: grafico_entropia.png")

if __name__ == "__main__":
    try:
        generar_graficos()
        print("¡Gráficos listos para el reporte!")
    except ImportError:
        print("Error: matplotlib no está instalado. No se pueden generar gráficos.")
    except Exception as e:
        print(f"Error generando gráficos: {e}")
