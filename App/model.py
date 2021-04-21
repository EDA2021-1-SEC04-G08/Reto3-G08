"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog():
    catalogo = {"songs": None,
                "hashtags": None,
                "sentiments": None,
                'req1': None}

    catalogo['songs'] = lt.newList('ARRAY_LIST')
    catalogo['hashtags'] = lt.newList('ARRAY_LIST')
    catalogo['sentiments'] = lt.newList('ARRAY_LIST')

    return catalogo

# Funciones para agregar informacion al catalogo


def addSong(catalog, song):
    lt.addLast(catalog['songs'], song)
    return catalog


def addHashtag(catalog, hashtag):
    lt.addLast(catalog['hashtags'], hashtag)
    return catalog


def addSentiment(catalog, sentiment):
    lt.addLast(catalog['sentiments'], sentiment)
    return catalog

# Funciones para creacion de datos


def countReproductions(catalog, carac):
    carac = carac.lower()
    if carac == 'instrumentalness':
        catalog['req1'] = om.newMap(omaptype='RBT',
                                    comparefunction=cmpInstrumentalness)
        addSongByCarac(catalog, carac)
        return catalog

    elif carac == 'acousticness':
        catalog['req1'] = om.newMap(omaptype='RBT',
                                    comparefunction=cmpAcousticness)
        addSongByCarac(catalog, carac)
        return catalog

    elif carac == 'liveness':
        catalog['req1'] = om.newMap(omaptype='RBT',
                                    comparefunction=cmpLiveness)
        addSongByCarac(catalog, carac)
        return catalog

    elif carac == 'speechiness':
        catalog['req1'] = om.newMap(omaptype='RBT',
                                    comparefunction=cmpSpeechiness)
        addSongByCarac(catalog, carac)
        return catalog

    elif carac == 'energy':
        catalog['req1'] = om.newMap(omaptype='RBT',
                                    comparefunction=cmpEnergy)
        addSongByCarac(catalog, carac)
        return catalog

    elif carac == 'danceability':
        catalog['req1'] = om.newMap(omaptype='RBT',
                                    comparefunction=cmpDanceability)
        addSongByCarac(catalog, carac)
        return catalog

    elif carac == 'valence':
        catalog['req1'] = om.newMap(omaptype='RBT',
                                    comparefunction=cmpValence)
        addSongByCarac(catalog, carac)
        return catalog

    else:
        return 'No se encontro la caracteristica solicitada'


def addSongByCarac(catalog, carac):
    size = lt.size(catalog['songs'])
    i = 0

    while i < size:
        song = lt.getElement(catalog['songs'], i)
        Updatecarac(catalog['req1'], song, carac)
        i += 1

    return catalog


def Updatecarac(map, song, carac):
    car = song[carac]
    entry = om.get(map, car)
    if entry is None:
        datentry = newDataEntry(song)
        om.put(map, car, datentry)
    else:
        datentry = me.getValue(entry)

    lst = datentry['lstsongs']
    lt.addLast(lst, song)
    return map


def newDataEntry(song):
    entry = {'lstsongs': None}
    entry['lstsongs'] = lt.newList('SINGLE_LINKED')
    return entry

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpInstrumentalness(isnt1, isnt2):
    if (isnt1 == isnt2):
        return 0
    elif (isnt1 > isnt2):
        return 1
    else:
        return -1


def cmpAcousticness(aco1, aco2):
    if (aco1 == aco2):
        return 0
    elif (aco1 > aco2):
        return 1
    else:
        return -1


def cmpLiveness(liv1, liv2):
    if (liv1 == liv2):
        return 0
    elif (liv1 > liv2):
        return 1
    else:
        return -1


def cmpSpeechiness(spe1, spe2):
    if (spe1 == spe2):
        return 0
    elif (spe1 > spe2):
        return 1
    else:
        return -1


def cmpEnergy(ene1, ene2):
    if (ene1 == ene2):
        return 0
    elif (ene1 > ene2):
        return 1
    else:
        return -1


def cmpDanceability(dan1, dan2):
    if (dan1 == dan2):
        return 0
    elif (dan1 > dan2):
        return 1
    else:
        return -1


def cmpValence(val1, val2):
    if (val1 == val2):
        return 0
    elif (val1 > val2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
