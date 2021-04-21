﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

sys.setrecursionlimit(1000*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Inicializar catalogo")
    print("1- Cargar información en el catálogo")
    print("2- Caracterizar las reproducciones")
    print("3- Encontrar musica para festejar")
    print("4- Encontrar musica para festejar")
    print("5- Estudiar los generos musicales")
    print("6- Indicar el genero musical mas escuchado en el tiempo")


songsFile = 'context_content_features-small.csv'
hashtagFile = 'sentiment_values.csv'
sentimentFile = 'user_track_hashtag_timestamp-small.csv'
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        catalog = controller.init()
        print('Se inicializo el catalogo\n')

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadSongs(catalog, songsFile)
        controller.loadHashtags(catalog, hashtagFile)
        controller.loadSentiments(catalog, sentimentFile)
        print('Se cargo la informacion del catalogo\n')

    elif int(inputs[0]) == 3:
        carac = input('Ingrese la caracteristica de contenido: ')
        lmin = input('Seleccione un limite minimo: ')
        lmax = input('Seleccione un limite maximo: ')
        controller.countReproductions(catalog, carac)
        print('Altura del arbol: ' + str(controller.indexHeight(catalog)))
        print('Elementos en el arbol: ' + str(controller.indexSize(catalog))
              + '\n')

    else:
        sys.exit(0)
sys.exit(0)
