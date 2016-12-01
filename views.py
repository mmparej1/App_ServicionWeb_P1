from flask import render_template,flash,redirect,request,make_response,session 
from app import app
from flask_pymongo import PyMongo
from ExpresionesRegulares import cotizacion
from .forms import LoginForm
from calculosFlask import calc_media_local, umbral_local,umbral_remota,calc_media_remota
 

@app.route('/', methods=['GET', 'POST'])
def inicio():
	form = LoginForm()
	session['media'] = 'Remota'
	session['umbral'] = 'Local'
	return render_template('inicio.html', title='Inicio', form=form)


@app.route('/Telefonica', methods=['GET', 'POST'])
def Telefonica():
    form = LoginForm()
    if 'media' in session:
        bd_media = session['media']
    if 'umbral' in session:
        bd_umbral = session['umbral']

    try:
	boton = request.form

        if 'n_media' in boton:
	    boton=""

	    if bd_media=='Local':
		avg = calc_media_local()
	        session['media'] = 'Remota'

            elif bd_media=='Remota':
  		avg = calc_media_remota()
		session['media'] = 'Local'

	    else:
		avg='' 
  
            return render_template('Telefonica.html', title='',form=form,avg=avg,bd_media=bd_media) 

        elif 'n_umbral' in boton:
   	    boton=""  

	    if form.validate_on_submit():
		if bd_umbral=='Local':
		    comparacion = umbral_local(form.openid.data)

	            session['umbral'] = 'Remota'
		    
		    return render_template('Telefonica.html', title='',form=form,avg='',comp=comparacion,bd_umbral=bd_umbral)
            	elif bd_umbral=='Remota':
		    v,h,d = umbral_remota(form.openid.data)

		    session['umbral'] = 'Local'

		    return render_template('Telefonica.html', title='',form=form,avg='',v=v,h=h,d=d,bd_umbral=bd_umbral)

	        else:
		    comparacion='' 

	        return render_template('Telefonica.html', title='',form=form,avg='')
 
            return render_template('Telefonica.html', title='',form=form,avg='',comp='')

        elif 'n_graficas' in boton:
	    boton=""   
            return render_template('Telefonica.html', title='',form=form,avg='') 

        else:
            return render_template('Telefonica.html', title='Sign In', form=form,avg='')

    except:
        return render_template('Telefonica.html', title='Sign In', form=form,avg='')
