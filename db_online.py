from beebotte import *

def base_dato_write(valor,hora,dia):
	bclient = BBT("4ee2f7d5b165b37642267fff5ee0eb96","4beeb951593ad542b76bed501e3c4cd8237045e0050da534137fca163b3d9ee9")
	#Lectura_numero = bclient.read("Canal", "numero", 1)
	#Lectura_numero = Lectura_numero[0]
	#Lectura_serie = bclient.read("Canal", "serie", 1)
	#Lectura_serie = Lectura_serie[0]
	#if dato!=Lectura_numero['data'] or dato!=Lectura_serie['data']:
	bclient.write("BD_Cotizaciones", "Valor", valor)
	bclient.write("BD_Cotizaciones", "Hora", hora)
	bclient.write("BD_Cotizaciones", "Dia", dia)


def base_dato_read():
	Lectura=[]
	sum = count = 0
	bclient = BBT("4ee2f7d5b165b37642267fff5ee0eb96","4beeb951593ad542b76bed501e3c4cd8237045e0050da534137fca163b3d9ee9")
	resource = Resource(bclient, "BD_Cotizaciones", "Valor")
	Lectura_valor = bclient.read("BD_Cotizaciones", "Valor",limit= 300)


	Lectura_hora = bclient.read("BD_Cotizaciones", "Hora",300)
	#Lectura_hora = Lectura_hora[0]
	#Lectura_hora = Lectura_hora ['data']
	Lectura_dia = bclient.read("BD_Cotizaciones", "Dia",300)
	#Lectura_dia = Lectura_dia[0]
	#Lectura_dia = Lectura_dia ['data']
	return Lectura_valor, Lectura_hora,Lectura_dia



	