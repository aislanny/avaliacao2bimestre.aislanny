from flask import Flask, Blueprint, flash, redirect, render_template, abort, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from jinja2 import TemplateNotFound

import database

app = Flask(__name__)
auth_bp = Blueprint('auth_bp', __name__,
template_folder='templates')

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("auth.registro"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Implemente o login com session.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("auth.logout"))

def show(bp):
    try:
        return render_template('templates')
    except TemplateNotFound:
        abort(404)
        
# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#
# - a rota /registro;
# - a rota /login;
# - a rota /logout.
