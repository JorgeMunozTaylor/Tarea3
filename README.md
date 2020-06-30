# Tarea 3: Variables aleatorias múltiples

## Autor
```
Jorge Muñoz Taylor 
A53863
jorge.munoztaylor@ucr.ac.cr
```

## Como ejecutar el código
```
>>python3 tarea3 xy.csv
```

En el archivo xy.csv está el registro de la frecuencia relativa de dos variables aleatorias conjuntas en forma de tabla. También está el archivo xyp.csv donde vienen todos los pares (x, y) y su probabilidad asociada sin embargo el código se creó en base al archivo xy.csv.


## Bibliotecas necesarias

```
* numpy
* Matplotlib
* Scipy
* math
```

## Solución


#### 1. A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

A partir de los datos, analíticamente se puede observar que la curva que mejor se ajusta a los datos (tanto para X como para Y) es la correspondiente a la función de densidad Normal (Gaussiana), note de las gráficas como el modelo tiene prácticamente el mismo recorrido de los datos -tome en cuenta que los datos presentan ruido-. En el código se mostrarán los valores de la media y la desviación estándar del modelo normal para X e Y.

![image info](imagenes/pmf_x_dist.png)
![image info](imagenes/pmf_y_dist.png)

---
#### 2. Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?

 Como asumimos que X e Y son independientes entonces la función de densidad conjunta 
 

 ![fxfy](https://latex.codecogs.com/gif.latex?f_%7BX%2CY%7D%28x%2Cy%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csigma%5Csqrt%7B2%5Cpi%7D%7De%5E%7B%20-%5Cfrac%7B%28x-%5Cmu%29%5E2%7D%7B2%5Csigma%5E2%7D%20%7D%20%5Ccdot%20%5Cfrac%7B1%7D%7B%5Csigma%5Csqrt%7B2%5Cpi%7D%7De%5E%7B%20-%5Cfrac%7B%28y-%5Cmu%29%5E2%7D%7B2%5Csigma%5E2%7D%20%7D)

 ![final](https://latex.codecogs.com/gif.latex?%5Crightarrow%20f_%7BX%2CY%7D%28x%2Cy%29%20%3D%20%5Cfrac%7B1%7D%7B2%5Cpi%20%5Csigma%5E2%7D%20e%5E%7B%20-%5Cfrac%7B1%7D%7B2%5Csigma%5E2%7D%20%28%20%28x-%5Cmu%29%5E2&plus;%28y-%5Cmu%29%5E2%20%29%20%7D)

 
\frac{1}{2}
 $$
 
 fX,Y(x,y) = fX(x) * fY(y)

---
#### 3. Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.



---
#### 4. Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).

![image info](imagenes/pmf_x.png)
![image info](imagenes/pmf_y.png)
![image info](imagenes/3d.png)