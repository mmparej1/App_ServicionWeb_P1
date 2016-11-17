from flask import render_template,flash,redirect,request
from app import app
from flask_pymongo import PyMongo
from ExpresionesRegulares import cotizacion
from .forms import LoginForm
from calculosFlask import leer
 
#cotizacion,hora=cotizacion()

@app.route('/', methods=['GET', 'POST'])
def inicio():
    form = LoginForm()

    try:
	boton = request.form

        if 'n_media' in boton:
	    avg = leer()
            boton=""   
            return render_template('inicio.html', title='',form=form,avg=avg) 

        elif 'n_umbral' in boton:
   	    boton=""  
	    if form.validate_on_submit():
	    #if 'Sing in' in request.form:
               flash('Login requested for OpenID="%s", remember_me=%s' %
                  (form.openid.data, str(form.remember_me.data)))
               return redirect('/index')
 
            return render_template('inicio.html', title='',form=form,avg="")

        elif 'n_graficas' in boton:
	    boton=""   
            return render_template('inicio.html', title='',form=form,avg="") 

        else:
            return render_template('inicio.html', title='Sign In', form=form,avg="")

    except:
        return render_template('inicio.html', title='Sign In', form=form,avg="")
