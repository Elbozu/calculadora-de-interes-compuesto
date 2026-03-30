# Calculadora de Interés Compuesto 📈

Este es un script de Python sencillo pero potente diseñado para ayudar a los usuarios a proyectar el crecimiento de sus inversiones a lo largo del tiempo. A diferencia de las calculadoras básicas, esta herramienta tiene en cuenta tanto el **monto inicial** como las **aportaciones mensuales adicionales**, aplicando el interés de forma anual.

## 🚀 Características

* **Proyección Detallada:** Muestra el progreso año tras año.
* **Aportaciones Mensuales:** Permite calcular cómo influye el ahorro constante en el resultado final.
* **Desglose de Ganancias:** Calcula tanto la ganancia específica de cada año como el rendimiento acumulado total.
* **Interfaz Limpia:** Salida de datos organizada en consola para facilitar la lectura.

## 🛠️ Requisitos

* **Python 3.x** instalado en tu sistema.

## 💻 Instalación y Uso

1.  **Clona o descarga** el archivo `calculadora de interes compuesto.py`.
2.  Abre una terminal o consola de comandos.
3.  Navega hasta la carpeta donde se encuentra el archivo.
4.  Ejecuta el script con el siguiente comando:
    ```bash
    python "calculadora de interes compuesto.py"
    ```

## 📝 Datos de Entrada

Al ejecutar el programa, se te solicitarán los siguientes datos:
1.  **Inversión inicial:** El capital con el que comienzas.
2.  **Tasa anual:** El porcentaje de interés esperado (ejemplo: `8` para un 8%).
3.  **Cantidad de años:** El tiempo que planeas mantener la inversión.
4.  **Aportación mensual:** El dinero extra que añadirás cada mes.

## 📊 Ejemplo de Salida

Al final de cada año, el programa generará un resumen como este:

```text
Año 1:
Aportaciones del año: 1200.0
Aportaciones totales acumuladas: 1200.0
Total antes del interés: 2200.00
Monto con el interés aplicado: 2420.00
Ganancias del año: 220.00
Ganancias acumuladas: 220.00
```

## 🔍 Lógica del Cálculo

El script sigue este flujo lógico por cada año:
1.  Suma las **aportaciones mensuales** ($\text{aportación} \times 12$) al capital actual.
2.  Calcula el nuevo total aplicando la tasa de interés:
    $$Total_{final} = Total_{actual} \times (1 + \frac{tasa}{100})$$
3.  Resta el capital invertido (inicial + aportaciones) para mostrar el **beneficio neto** generado por los intereses.

---
*Desarrollado con fines educativos para entender el poder del interés compuesto.*
