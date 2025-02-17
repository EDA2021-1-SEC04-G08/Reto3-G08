﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def init():
    catalogo = model.newCatalog()
    return catalogo

# Funciones para la carga de datos


def loadSongs(catalog, songsFile):
    songsFile = cf.data_dir + songsFile
    input_file = csv.DictReader(open(songsFile, encoding="utf-8"),
                                delimiter=",")
    for song in input_file:
        model.addSong(catalog, song)
    return catalog


def loadHashtags(catalog, hashtagFile):
    hashtagFile = cf.data_dir + hashtagFile
    input_file = csv.DictReader(open(hashtagFile, encoding="utf-8"),
                                delimiter=",")
    for hashtag in input_file:
        model.addHashtag(catalog, hashtag)
    return catalog


def loadSentiments(catalog, sentimentFile):
    sentimentFile = cf.data_dir + sentimentFile
    input_file = csv.DictReader(open(sentimentFile, encoding="utf-8"),
                                delimiter=",")
    for sentiment in input_file:
        model.addSentiment(catalog, sentiment)
    return catalog

# Funciones para creacion de datos


def countReproductions(catalog, carac, req):
    return model.countReproductions(catalog, carac, req)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo


def indexHeight(catalog):
    return model.indexHeight(catalog)


def indexSize(catalog):
    return model.indexSize(catalog)


def getRankByCarac(map, keylo, keyhi):
    return model.getRankByCarac(map, keylo, keyhi)


def musicToCelebrate(catalog, minE, maxE, minD, maxD):
    return model.musicToCelebrate(catalog, minE, maxE, minD, maxD)


def musicToStudy(catalog, minI, maxI, minT, maxT):
    return model.musicToStudy(catalog, minI, maxI, minT, maxT)


def StudyGenders(catalog, lista, dic):
    return model.StudyGenders(catalog, lista, dic)


def counReproductionsByHour(catalog, minH, maxH):
    return model.counReproductionsByHour(catalog, minH, maxH)


def getUniqueTracks(catalog, lista):
    return model.getUniqueTracks(catalog, lista)
