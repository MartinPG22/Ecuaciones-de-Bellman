# Termostato Óptimo con Programación Dinámica

## Descripción
Este proyecto implementa un **control óptimo de un termostato** utilizando **Ecuaciones de Bellman** para determinar la política óptima de encendido y apagado del sistema de calefacción. La meta es minimizar el **costo de operación** mientras se mantiene la temperatura dentro de un rango deseado.

---
## 📋 Características
- Modelado del problema utilizando **programación dinámica**.
- Implementación de la ecuación de Bellman para encontrar la política óptima.
- Simulación del comportamiento del termostato con diferentes condiciones iniciales.
- Evaluación del impacto de diferentes costos y configuraciones.
  
---
## 💻 Instalación y Uso
### Requisitos
Este proyecto está desarrollado en **Python 3** y requiere las siguientes bibliotecas:
```bash
pip install numpy matplotlib
```
---
### 🚀 Ejecución
Para ejecutar el programa, simplemente corre el script principal:
```bash
python termostato.py
```

Esto generará gráficos y estadísticas sobre la operación del termostato bajo la política óptima determinada.

---
## Explicación Técnica
El problema se modela como un **proceso de decisión de Markov (MDP)** con los siguientes elementos:
- **Estados**: La temperatura actual del sistema.
- **Acciones**: Encender o apagar la calefacción.
- **Recompensas**: Costo asociado a la energía consumida y penalización por desviaciones de la temperatura objetivo.
- **Ecuación de Bellman**: Se usa para calcular los valores óptimos y derivar la política de control óptima.
- 
---
## Resultados Esperados
Al ejecutar el modelo, se obtiene una estrategia óptima que balancea el costo de energía y la estabilidad térmica. Se presentan gráficos de temperatura en función del tiempo y decisiones tomadas en cada instante.

---
## Miembros
- Martín Portugal
- No me acuerdo
