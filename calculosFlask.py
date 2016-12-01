# -*- coding: utf-8 -*-

import pymongo
from ExpresionesRegulares import cotizacion
from db_online import base_dato_write,base_dato_read
from calculos import media

bd=0

def leer():
# Connection to Mongo DB
    try:
        conn=pymongo.MongoClient()
        print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e 
    conn


#asignamos la base de datos 'mydb' a la variable 'db'
    db = conn.cotizaciones

#Asignamos la collecion 'mycollection' de la base de datos 'mydb' a la variable 'coll'
    coll= db.telefonica

    valor,hora,dia = cotizacion()

#cursor = db.coll.find()
#for document in cursor:
#    print(document['valor'])
#    media = calc_media(db,coll)
    return db,coll


def calc_media_local():
    db,coll=leer()
    sum = count = 0
    cursor = db.coll.find()
    for document in cursor:
        sum = sum + document['valor']
	count = count + 1
    media=sum/count
    return media

def calc_media_remota():
    valor,hora,dia=base_dato_read()
    sum=count=0
    for i in valor:
	sum = sum + i['data']
	count = count + 1
    media=sum/count

    return media

def umbral_remota(umbral):
    valor,hora,dia=base_dato_read()
    umbral = float(umbral)
    uu=[]
    hh=[]
    dd=[]

    #for document in valor:
    #    ultimo = document['data']
    ultimo=valor[0]

    ultimo=ultimo['data']

    max = ultimo * (1+ umbral /100.0)
    min = ultimo * (1- umbral /100.0)

    for i in range(len(valor)):
        ultimo = valor[i]['data']

        if ultimo>max or ultimo <min:
            uu.append(ultimo)

            hh.append(hora[i]['data'])

            dd.append(dia[i]['data'])
    
    return uu,hh,dd

def umbral_local(umbral):
    u = 'Cotizaciones que han superado el umbral '
    db,coll=leer()
    cursor = db.coll.find()
    # leer el ultimo
    for document in cursor:
    	ultimo = document['valor']
    #ultimo,hora,dia = cotizacion()
        # calcular el max y el min
    print ultimo
    umbral = float(umbral)
    max = ultimo * (1+ umbral /100.0)
    min = ultimo * (1- umbral /100.0)
    # compararlo con todo
    cursor_comparacion = db.coll.find({"$or": [{"valor": {"$gt": max}}, {"valor": {"$lt": min}}]})
	 
    return cursor_comparacion
