#!flask/bin/python
# -*- coding: utf-8 -*-

import pymongo
from ExpresionesRegulares import cotizacion
from db_online import base_dato_write,base_dato_read
from calculos import media


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

#Borrar toda la coleccion
#db.coll.remove()



valor,hora,dia = cotizacion()
print valor
# Insertamos un documento creandolo en el momento
result = db.coll.insert_one(
    {
        "valor": valor,
        "fecha": 
            {
                "dia": dia[0],
                "hora": hora[0]
            }
    }
)



################ DB ONLINE ########################

base_dato_write(valor,hora[0],dia[0])
