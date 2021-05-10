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
from datetime import datetime
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
                'req1': None,
                'req2': None,
                'req3': None,
                'req4': None,
                'req5': None}

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


def countReproductions(catalog, carac, req):
    carac = carac.lower()
    if carac == 'instrumentalness':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpInstrumentalness)
        addSongByCarac(catalog, carac, req)
        return catalog

    elif carac == 'acousticness':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpAcousticness)
        addSongByCarac(catalog, carac, req)
        return catalog

    elif carac == 'liveness':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpLiveness)
        addSongByCarac(catalog, carac, req)
        return catalog

    elif carac == 'speechiness':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpSpeechiness)
        addSongByCarac(catalog, carac, req)
        return catalog

    elif carac == 'energy':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpEnergy)
        addSongByCarac(catalog, carac, req)
        return catalog

    elif carac == 'danceability':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpDanceability)
        addSongByCarac(catalog, carac, req)
        return catalog

    elif carac == 'valence':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpValence)
        addSongByCarac(catalog, carac, req)
        return catalog

    elif carac == 'tempo':
        catalog[req] = om.newMap(omaptype='RBT',
                                 comparefunction=cmpTempo)
        addSongByCarac(catalog, carac, req)
        return catalog

    else:
        return 'No se encontro la caracteristica solicitada'


def addSongByCarac(catalog, carac, req):
    size = lt.size(catalog['songs'])
    i = 0

    while i < size:
        song = lt.getElement(catalog['songs'], i)
        Updatecarac(catalog[req], song, carac)
        i += 1

    return catalog


def Updatecarac(map, song, carac):
    car = float(song[carac])
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


def createMapByHour(catalog, songList, carac):
    catalog['req5'] = om.newMap(omaptype='RBT',
                                comparefunction=cmpTempo)
    size = lt.size(songList)
    i = 0

    while i < size:
        song = lt.getElement(songList, i)
        Updatecarac(catalog['req5'], song, carac)
        i += 1

    return catalog


# Funciones de consulta


def indexHeight(catalog):
    return om.height(catalog['req1'])


def indexSize(catalog):
    return om.size(catalog['req1'])


def getRankByCarac(map, keylo, keyhi):
    lst = om.values(map, keylo, keyhi)
    size = lt.size(lst)
    i = 0
    artist = lt.newList('ARRAY_LIST')
    songs = 0

    while i < size:
        val = lt.getElement(lst, i)
        size2 = lt.size(val['lstsongs'])
        songs += size2
        j = 0

        while j < size2:
            sub = lt.getElement(val['lstsongs'], j)
            art = sub['artist_id']
            pos = lt.isPresent(artist, art)

            if pos == 0:
                lt.addLast(artist, art)

            j += 1
        i += 1

    num_artist = lt.size(artist)

    return (songs, num_artist, artist)


def musicToCelebrate(catalog, minE, maxE, minD, maxD):
    countReproductions(catalog, 'Energy', 'req2')
    lst = om.values(catalog['req2'], float(minE), float(maxE))
    songs = lt.newList('ARRAY_LIST')
    tracks = lt.newList('ARRAY_LIST')
    size = lt.size(lst)
    i = 0

    while i < size:
        val = lt.getElement(lst, i)
        size2 = lt.size(val['lstsongs'])
        j = 0

        while j < size2:
            sub = lt.getElement(val['lstsongs'], j)
            so = sub['danceability']
            id = sub['track_id']
            pos = lt.isPresent(tracks, id)

            if ((pos == 0) and (float(so) >= float(minD)) and
               (float(so) <= float(maxD))):

                lt.addLast(songs, sub)
                lt.addLast(tracks, id)

            j += 1
        i += 1

    num_songs = lt.size(songs)

    return (songs, num_songs)


def musicToStudy(catalog, minI, maxI, minT, maxT):
    countReproductions(catalog, 'Instrumentalness', 'req3')
    lst = om.values(catalog['req3'], float(minI), float(maxI))
    songs = lt.newList('ARRAY_LIST')
    tracks = lt.newList('ARRAY_LIST')
    size = lt.size(lst)
    i = 0

    while i < size:
        val = lt.getElement(lst, i)
        size2 = lt.size(val['lstsongs'])
        j = 0

        while j < size2:
            sub = lt.getElement(val['lstsongs'], j)
            so = sub['tempo']
            id = sub['track_id']
            pos = lt.isPresent(tracks, id)

            if ((pos == 0) and (float(so) >= float(minT)) and
               (float(so) <= float(maxT))):

                lt.addLast(songs, sub)
                lt.addLast(tracks, id)

            j += 1
        i += 1

    num_songs = lt.size(songs)

    return (songs, num_songs)


def StudyGenders(catalog, lista, dic):
    countReproductions(catalog, 'tempo', 'req4')
    for genero in lista:



def counReproductionsByHour(catalog, minH, maxH):
    h1 = datetime.strptime(minH, '%H:%M:%S')
    H1 = datetime.time(h1)
    h2 = datetime.strptime(maxH, '%H:%M:%S')
    H2 = datetime.time(h2)
    lstByHour = lt.newList('ARRAY_LIST')
    size1 = lt.size(catalog['songs'])
    i = 0

    while i < size1:
        song = lt.getElement(catalog['songs'], i)
        date1 = song['created_at']
        date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
        eventTime = datetime.time(date1)

        if eventTime >= H1 and eventTime <= H2:
            lt.addLast(lstByHour, song)

        i += 1

    size2 = lt.size(lstByHour)

    createMapByHour(catalog, lstByHour, 'tempo')

    listByGender = lt.newList('ARRAY_LIST')

    reggae = countByGender(catalog['req5'], 60.0, 90.0, 'reggae')
    lt.addLast(listByGender, reggae)

    downTempo = countByGender(catalog['req5'], 70.0, 100.0, 'Down Tempo')
    lt.addLast(listByGender, downTempo)

    chillOut = countByGender(catalog['req5'], 90.0, 120.0, 'Chill Out')
    lt.addLast(listByGender, chillOut)

    hipHop = countByGender(catalog['req5'], 85.0, 115.0, 'Hip Hop')
    lt.addLast(listByGender, hipHop)

    jazz = countByGender(catalog['req5'], 120.0, 125.0, 'Jazz and Funk')
    lt.addLast(listByGender, jazz)

    pop = countByGender(catalog['req5'], 100.0, 130.0, 'Pop')
    lt.addLast(listByGender, pop)

    RB = countByGender(catalog['req5'], 60.0, 80.0, 'R&B')
    lt.addLast(listByGender, RB)

    rock = countByGender(catalog['req5'], 110.0, 140.0, 'Rock')
    lt.addLast(listByGender, rock)

    metal = countByGender(catalog['req5'], 100.0, 160.0, 'Metal')
    lt.addLast(listByGender, metal)

    sorted_list = sa.sort(listByGender, cmpReproductions)
    return (sorted_list, size2)


def countByGender(map, minT, maxT, gender):
    lst = om.values(map, minT, maxT)
    size1 = lt.size(lst)
    lst1 = lt.newList('ARRAY_LIST')
    songs = 0
    i = 0

    while i < size1:
        val = lt.getElement(lst, i)
        size2 = lt.size(val['lstsongs'])
        songs += size2
        j = 0

        while j < size2:
            sub = lt.getElement(val['lstsongs'], j)
            lt.addLast(lst1, sub)
            j += 1

        i += 1

    return {'gender': gender, 'songs': lst1, 'count': songs}


def getUniqueTracks(catalog, lista):
    top = lt.getElement(lista, 1)
    songs = top['songs']
    mapa = mp.newMap(4500,
                     maptype='CHAINING',
                     loadfactor=1.2)

    size1 = lt.size(songs)
    i = 0

    while i < size1:
        song = lt.getElement(songs, i)
        t1 = song['track_id']
        existTrack = mp.contains(mapa, t1)
        if existTrack:
            entry = mp.get(mapa, t1)
            dic = me.getValue(entry)
        else:
            dic = newDataEntry(t1)
            mp.put(mapa, t1, dic)
        lt.addLast(dic['lstsongs'], song)
        i += 1

    keySet = mp.keySet(mapa)
    count = lt.size(keySet)
    hashtags = lt.newList('ARRAY_LIST')
    j = 0

    while j < count:
        track = lt.getElement(keySet, j)
        dc = getHashtags(catalog, track)
        lt.addLast(hashtags, dc)
        j += 1

    return (count, hashtags)


def getHashtags(catalog, track):
    dic = {'track_id': track,
           'hashtags': lt.newList('ARRAY_LIST'),
           'vader': None}

    size1 = lt.size(catalog['hashtags'])
    i = 0

    while i < size1:
        song = lt.getElement(catalog['hashtags'], i)
        song_id = song["track_id"]
        if song_id == track:
            lt.addLast(dic['hashtags'], song['hashtag'].lower())
        i += 1

    size2 = lt.size(dic['hashtags'])
    size3 = lt.size(catalog['sentiments'])
    vaderValue = 0
    j = 0

    while j < size2:
        hashtag = lt.getElement(dic['hashtags'], j)
        k = 0
        while k < size3:
            vader = lt.getElement(catalog['sentiments'], k)
            vaderName = vader['hashtag'].lower()
            vaderAvg = vader['vader_avg']
            if vaderName == hashtag and vaderAvg != '':
                vaderValue += float(vaderAvg)
            k += 1
        j += 1

    dic['vader'] = round(vaderValue / float(size2), 2)
    return dic


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


def cmpTempo(temp1, temp2):
    if (temp1 == temp2):
        return 0
    elif (temp1 > temp2):
        return 1
    else:
        return -1


def cmpReproductions(gen1, gen2):
    return (gen1['count'] > gen2['count'])


# Funciones de ordenamiento
