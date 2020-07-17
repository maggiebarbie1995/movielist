from flask import render_template
from . import app

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404

    @app.errorhandler(500)
def five_hun(error):
    '''
    Function to render the 500 error page
    '''
    return render_template('fivehun.html'),500