#!flask/bin/python
# -*- coding: utf-8 -*-

import pymongo
from ExpresionesRegulares import cotizacion
from db_onlineC import base_dato_write

########### DB LOCAL ##########################
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

# Insertamos un documento creandolo en el momento
result = db.coll.insert_one(
    {
        "valor": valor[0],
        "fecha": 
            {
                "dia": dia[0],
                "hora": hora[0]
            }
    }
)

#cursor = db.coll.find()
#for document in cursor:
#    print(document)

################ DB ONLINE ########################

base_dato_write(valor[0],hora[0],dia[0])
