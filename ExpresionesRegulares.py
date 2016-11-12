# -*- coding: utf-8 -*-

import urllib
import re

def leer_pagina():
    Pagina = urllib.urlopen("http://www.finanzas.com/cotizaciones/telefonica/")
    ContenidoPagina = Pagina.read()
    Pagina.close()
    return ContenidoPagina

def obtener_cotizacion(ContenidoPagina):
    pattern = re.compile('title=.TELEFONICA.>TELEFONICA<.a> .TEF.*\n      .*\n    .*\n    .*</time><span>[0-9],[0-9][0-9]')
    info_pagina = re.findall(pattern,ContenidoPagina)
    array_cotizacion = re.split('</time><span>',info_pagina[0])
    return array_cotizacion

def obtener_fecha(ContenidoPagina):
    pattern = re.compile('<div class="date">\n.*<span>[0-9]* de \w*, [0-2]\d:[0-5]\d \wm')
    info_pagina = re.findall(pattern,ContenidoPagina)
    array_hora = re.split(',',info_pagina[0])
    array_dia = re.split('<span>',array_hora[0])
    return array_hora,array_dia

def cotizacion():
    ContenidoPagina = leer_pagina()
    array_hora,array_dia = obtener_fecha(ContenidoPagina)
    array_cotizacion = obtener_cotizacion(ContenidoPagina)
    cotizacion = array_cotizacion[1:]
    hora = array_hora[1:]
    dia = array_dia[1:]
    return cotizacion,hora,dia
    
    