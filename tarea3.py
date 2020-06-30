#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tarea 3: Variables aleatorias múltiples
"""

""" 
Autor: Jorge Muñoz Taylor
Carné: A53863
Curso: Modelos probabilísticos de señales y sistemas para ingeniería
Grupo: 01
Fecha: 29/06/2020
"""

import sys
import numpy as np

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D #Permite generar gráficos en 3D.
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter 

from scipy.optimize import curve_fit #Modulo que sirve para encontrar la curva de mejor ajuste.
from math import sqrt #Raíz cuadrada.
import warnings
#Elimina el overflow que ocurre en la exponencial con Y, no afecta a la gráfica es sólo por
#estética.
warnings.filterwarnings("ignore") 

#Define la función de densidad de Rayleigh.
#[in] x: variable independiente.
#[in] sigma: desviación estándar.
#[out]: Devuelve el valor de la función de densidad.
def rayleigh ( x, sigma ):
    return ( x * np.exp( -x**2/(2*sigma**2) ) ) / (sigma**2)

#Define la función de densidad Normal (Gaussiana).
#[in] x: variable independiente.
#[in] sigma: desviación estándar.
#[in] mu: media
#[out]: Devuelve el valor de la función de densidad.
def normal ( x, sigma, mu ):
    return ( 1/ (sigma*sqrt(2*np.pi) ) ) * ( np.exp ( - (x-mu)**2 / (2* sigma**2) ) )

#Define la función de densidad Uniforme. 
#[in] a: primer punto de la función.
#[in] b: segundo punto de la función.
#[out]: Devuelve el valor de la función de densidad.
def uniforme ( a, b ):
    return 1 / (b -a)

#Define la función de densidad Exponencial.
#[in] lamb: parámetro que indica el grado de inclinación de la función.
#[in] x: variable independiente.
#[out]: Devuelve el valor de la función de densidad.
def exponencial( x, lamb ):
    return 1 - np.exp(-lamb*x)



if __name__=="__main__":

    archivo = sys.argv #Abre el archivo en base a la dirección dada como primer argumento. 


#****************************************
#************** PREGUNTA 1 **************
#****************************************
    
    print ("\n\n******** PREGUNTA 1 ********\n")

    #Se lee el archivo xp.csv y se coloca en un array tipo numpy. 
    DATOS = np.genfromtxt (archivo[1], delimiter=',')

    #Se eliminan la primera fila y la primera columna.
    DATOS = np.delete (DATOS,0,0)
    DATOS = np.delete (DATOS,0,1)

    #Creamos los vectores X e Y con sus respectivos valores.
    X = np.linspace (5,15,11,dtype="int")
    Y = np.linspace (5,25,21,dtype="int")
    
    #Calcula la densidad marginal de cada fila X.
    pmf_X = np.sum (DATOS, axis=1) # axis=1 son filas

    #Ajusta la curva rayleig a la densidad marginal de X.
    X_ray_fit_vals, _    = curve_fit (rayleigh, X ,pmf_X )
    #Ajusta la curva normal a la densidad marginal de X.
    X_normal_fit_vals, _ = curve_fit (normal, X ,pmf_X )
    #Ajusta la curva uniforme a la densidad marginal de X.
    X_uni_fit_vals, _    = curve_fit (uniforme, X ,pmf_X )
    #Ajusta la curva exponencial a la densidad marginal de X.
    X_exp_fit_vals, _    = curve_fit (exponencial, X ,pmf_X )
    
    #Calcula la densidad marginal de cada columna Y.
    pmf_Y = np.sum (DATOS, axis=0) # axis=0 son columnas

    #Ajusta la curva rayleig a la densidad marginal de Y.
    Y_ray_fit_vals, _    = curve_fit (rayleigh, Y ,pmf_Y )
    #Ajusta la curva normal a la densidad marginal de Y.
    Y_normal_fit_vals, _ = curve_fit (normal, Y ,pmf_Y )
    #Ajusta la curva uniforme a la densidad marginal de Y.
    Y_uni_fit_vals, _    = curve_fit (uniforme, Y ,pmf_Y )
    #Ajusta la curva exponencial a la densidad marginal de X.
    Y_exp_fit_vals, _    = curve_fit (exponencial, Y ,pmf_Y )    

    print ("Datos para la función de distribución NORMAL:\n")
    print ("-> Media de X: ", X_normal_fit_vals[1] )
    print ("-> Desviación estándar de X: ", X_normal_fit_vals[0], "\n" )
    print ("-> Media de Y: ", Y_normal_fit_vals[1] )
    print ("-> Desviación estándar de Y: ", Y_normal_fit_vals[0], "\n" )


    #--- Para X ---

    #Crea una figura con 4 subdivisiones, una por imágen.
    fig,axs = plt.subplots (2,2)

    #Primero se creará la curva de mejor ajuste con una línea roja punteada, encima de esta
    #se colocará el modelo que se esté analizando: rayleigh, normal, uniforme o exponenical.
    axs[0,0].plot   (X, pmf_X, 'r--', alpha=0.5, label='pmf de X')
    axs[0,0].set_title ('Rayleigh')
    axs[0,0].plot   (X, rayleigh( X, *X_ray_fit_vals ), lw=4, label='Rayleigh' )
    axs[0,0].legend ()
    
    axs[0,1].plot   (X, pmf_X, 'r--', alpha=0.5, label='pmf de X')
    axs[0,1].set_title ('Normal')
    axs[0,1].plot   (X, normal( X, *X_normal_fit_vals ), lw=4, label='Normal' )
    axs[0,1].legend ()
    
    axs[1,0].plot   (X, pmf_X, 'r--', alpha=0.5, label='pmf de X')
    axs[1,0].set_title ('Uniforme')
    axs[1,0].plot   (X, uniforme( X, *X_uni_fit_vals ), lw=4, label='Uniforme' )
    axs[1,0].legend ()
    
    axs[1,1].plot   (X, pmf_X, 'r--', alpha=0.5, label='pmf de X')
    axs[1,1].set_title ('Exponencial')
    axs[1,1].plot   (X, exponencial( X, *X_exp_fit_vals ), lw=4, label='Exponencial' )
    axs[1,1].legend ()
    
    #Coloca los ejes a cada figura.
    for ax in axs.flat:
        ax.set(xlabel='Datos X', ylabel='Probabilidad')

    for ax in axs.flat:
        ax.label_outer()

    #Imprime la imágen y la guarda.
    plt.savefig("imagenes/pmf_x_dist.png")
    plt.show()

  
    #--- Para Y ---

    #Crea una figura con 4 subdivisiones, una por imágen.
    fig,axs = plt.subplots (2,2)

    #Primero se creará la curva de mejor ajuste con una línea roja punteada, encima de esta
    #se colocará el modelo que se esté analizando: rayleigh, normal, uniforme o exponenical.
    axs[0,0].plot    (Y, pmf_Y, 'r--', alpha=0.5, label='pmf de Y')
    axs[0,0].set_title ('Rayleigh')
    axs[0,0].plot    (Y, rayleigh( Y, *Y_ray_fit_vals ), lw=4, label='Rayleigh' )
    axs[0,0].legend  ()

    axs[0,1].plot    (Y, pmf_Y, 'r--', alpha=0.5, label='pmf de Y')
    axs[0,1].set_title ('Normal')
    axs[0,1].plot    (Y, normal( Y, *Y_normal_fit_vals ), lw=4, label='Normal' )
    axs[0,1].legend  ()  
#
    axs[1,0].plot    (Y, pmf_Y, 'r--', alpha=0.5, label='pmf de Y')
    axs[1,0].set_title ('Uniforme')
    axs[1,0].plot    (Y, uniforme( Y, *Y_uni_fit_vals ), lw=4, label='Uniforme' )
    axs[1,0].legend  ()

    axs[1,1].plot   (Y, pmf_Y, 'r--', alpha=0.5, label='pmf de Y')
    axs[1,1].set_title ('Exponencial')
    axs[1,1].plot   (Y, exponencial( Y, *Y_exp_fit_vals ), lw=4, label='Exponencial' )
    axs[1,1].legend ()

    #Coloca los ejes a cada figura.
    for ax in axs.flat:
        ax.set(xlabel='Datos Y', ylabel='Probabilidad')

    for ax in axs.flat:
        ax.label_outer()

    #Imprime la imágen y la guarda.
    plt.savefig("imagenes/pmf_y_dist.png")
    plt.show()


    #****************************************
    #************** PREGUNTA 2 **************
    #****************************************

    #En el reporte está la solución a esta pregunta.


    #****************************************
    #************** PREGUNTA 3 **************
    #****************************************

    print ("******** PREGUNTA 3 ********\n")

    #--- Correlación ---

    COLUMNA     = 0 #Variable que llevará el conteo de columnas.
    FILA        = 0 #Variable que llevará el conteo de filas.
    CORRELACION = 0 #Variable, sumará el resultado de multiplicar Fila*Columna*Probabilidad.

    for i in Y: #Recorre por columnas
        for j in X: #Recorre por filas
            CORRELACION = CORRELACION + i*j*DATOS [FILA][COLUMNA] #Fila*Columna*Probabilidad.
            FILA = FILA+1

        COLUMNA = COLUMNA+1
        FILA    = 0        

    print ("-> Correlación: ", CORRELACION)


    #--- Covarianza ---

    COLUMNA    = 0 #Variable que llevará el conteo de columnas.
    FILA       = 0 #Variable que llevará el conteo de filas.
    COVARIANZA = 0 #Variable, dará el valor final de la covarianza.

    for i in Y: #Recorre por columnas
        for j in X: #Recorre por filas
            COVARIANZA = COVARIANZA + (i-Y_normal_fit_vals[1])*(j-X_normal_fit_vals[1])*DATOS [FILA][COLUMNA]
            FILA = FILA+1

        COLUMNA = COLUMNA+1
        FILA    = 0        

    print ("-> Covarianza: ", COVARIANZA)


    #--- Coeficiente de correlación (Pearson) ---

    #El coeficiente de Pearson es igual a la covarianza entre la multiplicación
    #de la desviación estándar de los modelos.
    pearson = COVARIANZA / ( X_normal_fit_vals[0] * Y_normal_fit_vals[0] )
    print ("-> Coeficiente de correlación (Pearson): ", pearson)


#****************************************
#************** PREGUNTA 4 **************
#****************************************

    #--- Genera los gráficos de distribución marginal para X e Y ---

    print ("\n******** PREGUNTA 4 ********\n")
    print ("-> Generando el gráfico de distribución marginal de X ...")

    plt.plot    (X, pmf_X, 'b', lw=5, alpha=1, label='pmf de X')
    plt.xlabel  ('X')
    plt.ylabel  ('Densidad marginal de X')
    plt.legend  ()
    plt.savefig("imagenes/pmf_x.png")
    plt.show()

    print ("-> Generando el gráfico de distribución marginal de Y ...")
    plt.plot    (Y, pmf_Y, 'b', lw=5, alpha=1, label='pmf de Y')
    plt.xlabel  ('Y')
    plt.ylabel  ('Densidad marginal de Y')
    plt.legend  ()
    plt.savefig("imagenes/pmf_y.png")
    plt.show()

    #--- Genera el gráfico 3D ---

    print ("-> Generando la gráfica de la función de densidad conjunta ...")
    fig = plt.figure()
    ax = fig.gca(projection='3d') #Indica que se generará un gráfico en 3D.
    X, Y = np.meshgrid(X, Y) #Transforma los vectores x,y al formato usado por el módulo.

    # Se generan los datos que se usarán para colocar los puntos en Z.
    Z = normal( X, *X_normal_fit_vals ) * normal( Y, *Y_normal_fit_vals )
    
    # Crea la superficie en base a las coordenadas X, Y y Z.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)

    # Tunea el eje Z.
    ax.set_zlim(0, 0.009)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.03f'))

    # Colores para que se vea chiva :3
    fig.colorbar(surf, shrink=0.5, aspect=5)

    # Muestra el gráfico.
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("imagenes/3d.png")
    plt.show()

    print ("\n\n -- Fin del programa --\n\n")