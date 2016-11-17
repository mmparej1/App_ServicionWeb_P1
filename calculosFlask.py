# -*- coding: utf-8 -*-

import pymongo
from ExpresionesRegulares import cotizacion
from db_onlineC import base_dato_write
from calculos import media



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


def calc_media():
    db,coll=leer()
    sum = count = 0
    cursor = db.coll.find()
    for document in cursor:
        sum = sum + document['valor']
	count = count + 1
    media=sum/count
    return media


def comparar_umbral(umbral):
    u = 'Cotizaciones que han superado el umbral '
    db,coll=leer()
    cursor = db.coll.find()
    # leer el ultimo
    for document in cursor:
    	ultimo = document['valor']

    # calcular el max y el min
    max = ultimo * (1+ umbral /100.0)
    max = ultimo * (1- umbral /100.0)
    # compararlo con todo
    cursor_comparacion = db.coll.find({"$or": [{"valor": {"$gt": max}}, {"valor": {"$lt": max}}]})

    # devolver los que lo superen 
    for documento in cursor_comparacion:
    	 u = u + str(documento['valor'])

    return u
