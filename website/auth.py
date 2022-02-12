from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/rules')
def rules():
    return render_template('rules.html')


@auth.route('/about')
def about():
    return render_template('about.html')


@auth.route('/discord')
def discord():
    return render_template('discord.html')


@auth.route('/plugins-datapacks')
def plugins_datapacks():
    return render_template('plugins-datapacks.html')
