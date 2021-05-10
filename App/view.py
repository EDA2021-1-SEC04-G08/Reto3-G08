"""
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
from random import randint
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
    print("2- Cargar información en el catálogo")
    print("3- Caracterizar las reproducciones")
    print("4- Encontrar musica para festejar")
    print("5- Encontrar musica para Estudiar")
    print("6- Estudiar los generos musicales")
    print("7- Indicar el genero musical mas escuchado en el tiempo")


songsFile = 'context_content_features-small.csv'
hashtagFile = 'user_track_hashtag_timestamp-small.csv'
sentimentFile = 'sentiment_values.csv'
catalog = None


def printSongsToCelebrate(lista):
    size = lt.size(lista)
    count = 0

    while count < 5:
        number = randint(0, size-1)
        song = lt.getElement(lista, number)
        print('Track ' + str(count+1) + ': ' + song['track_id'] +
              ' with energy of ' + song['energy'] + ' and danceability of '
              + song['danceability'])
        count += 1


def printSongsToStudy(lista):
    size = lt.size(lista)
    count = 0

    while count < 5:
        number = randint(0, size-1)
        song = lt.getElement(lista, number)
        print('Track ' + str(count+1) + ': ' + song['track_id'] +
              ' with instrumentalness of ' + song['instrumentalness'] +
              ' and tempo of ' + song['tempo'])
        count += 1


def generos():
    dic = {'reggae': [60, 90],
           'down-tempo': [70, 100],
           'chill-out': [90, 120],
           'hip-hop': [85, 115],
           'jazz and Funk': [120, 125],
           'pop': [100, 130],
           'r&b': [60, 80],
           'rock': [110, 140],
           'metal': [100, 160]}
    return dic


def printTopGenders(lista, answer2):
    hashtags = answer2[1]
    size = lt.size(lista)
    i = 1

    while i <= size:
        gender = lt.getElement(lista, i)
        print('TOP ' + str(i) + ': ' + gender['gender'] + ' with ' +
              str(gender['count']) + ' reps')
        i += 1

    top = lt.getElement(lista, 1)
    print('\nThe TOP GENDER is ' + top['gender'] + ' with ' +
          str(top['count']) + ' reproductions\n')

    print('========================== ' + top['gender'] +
          ' SENTIMENT ANALYSIS =========================')
    print(top['gender'] + ' has ' + str(answer2[0]) + ' unique tracks')
    print('Random 10 tracks are: \n')
    size2 = lt.size(hashtags)
    count = 0

    while count < 10:
        number = randint(0, size2-1)
        track = lt.getElement(hashtags, number)
        numH = lt.size(track['hashtags'])
        print('Track #' + str(count+1) + ': ' + track['track_id'] + ' with ' +
              str(numH) + ' hashtags and VADER = ' + str(track['vader']))
        count += 1


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
        controller.countReproductions(catalog, carac, 'req1')
        print('\nAltura del arbol: ' + str(controller.indexHeight(catalog)))
        print('Elementos en el arbol: ' + str(controller.indexSize(catalog))
              + '\n')
        answer = controller.getRankByCarac(catalog['req1'], float(lmin),
                                           float(lmax))
        print('++++++ Req no.1 results ++++++')
        print('Instrumentalness is between ' + lmin + ' and ' + lmax)
        print('Total of reproduction: ' + str(answer[0]) +
              ' Total of unique artists: ' + str(answer[1]) + '\n')

    elif int(inputs[0]) == 4:
        lminE = input('Seleccione un limite minimo para Energy: ')
        lmaxE = input('Seleccione un limite maximo para Energy: ')

        lminD = input('Seleccione un limite minimo para Danceability: ')
        lmaxD = input('Seleccione un limite maximo para Danceability: ')

        answer = controller.musicToCelebrate(catalog, lminE, lmaxE, lminD,
                                             lmaxD)
        print('\n++++++ Req no.2 results ++++++')
        print('Energy is between ' + lminE + ' and ' + lmaxE)
        print('Danceability is between ' + lminD + ' and ' + lmaxD)
        print('Total of unique tracks in events: ' + str(answer[1]) + '\n')
        print('--- Unique track_id --- ')
        printSongsToCelebrate(answer[0])

    elif int(inputs[0]) == 5:
        lminI = input('Seleccione un limite minimo para Instrumentalness: ')
        lmaxI = input('Seleccione un limite maximo para Instrumentalness: ')

        lminT = input('Seleccione un limite minimo para Tempo: ')
        lmaxT = input('Seleccione un limite maximo para Tempo: ')

        answer = controller.musicToStudy(catalog, lminI, lmaxI, lminT,
                                         lmaxT)
        print('\n++++++ Req no.3 results ++++++')
        print('Instrumentalness is between ' + lminI + ' and ' + lmaxI)
        print('Tempo is between ' + lminT + ' and ' + lmaxT)
        print('Total of unique tracks in events: ' + str(answer[1]) + '\n')
        print('--- Unique track_id --- ')
        printSongsToStudy(answer[0])

    elif int(inputs[0]) == 6:
        dic = generos()
        keys = dic.keys()
        strKeys = str(keys)
        print('Los generos actuales son: ' + strKeys[10:-1])
        agregar = input('¿Desea agregar un genero extra?: ')
        if agregar.lower() == 'si':
            nombre = input('Ingrese un nombre unico para el genero: ')
            Vmin = float(input('Ingrese un valor minimo para el tempo del ' +
                               'nuevo genero: '))
            Vmax = float(input('Ingrese un valor maximo para el tempo del ' +
                               'nuevo genero: '))
            if nombre.lower() in keys:
                print('El genero ingresado ya se encuentra agregado')
            else:
                dic[nombre.lower()] = [Vmin, Vmax]
                keys = dic.keys()
                strKeys = str(keys)
                print('Los generos actuales son: ' + strKeys[10:-1])

        cadena = input('Ingrese los generos a buscar(separados por comas): ')
        cadena = cadena.lower()
        cd = cadena.split(', ')
        conteo = 0
        for genero in cd:
            if genero not in dic:
                conteo += 1

        if conteo > 0:
            print(str(conteo) + ' genero(s) no se encuentran agregados' +
                  ', por favor agregelos e intente nuevamente\n')

        else:
            

    elif int(inputs[0]) == 7:
        hmin = input('Ingrese una hora como limite minimo: ')
        hmax = input('Ingrese una hora como limite maximo: ')

        answer = controller.counReproductionsByHour(catalog, hmin, hmax)
        answer2 = controller.getUniqueTracks(catalog, answer[0])
        print('\n++++++ Req no.5 results ++++++')
        print('There is a total of ' + str(answer[1]) +
              ' reproductions between ' + hmin + ' and ' + hmax)
        print('====================== GENRES SORTED REPRODUCTIONS ' +
              '======================')
        printTopGenders(answer[0], answer2)
        print('\n')

    else:
        sys.exit(0)
sys.exit(0)
