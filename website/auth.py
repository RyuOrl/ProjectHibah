from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
  return render_template("login.html")

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
  return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
  return redirect(url_for("views.login"))

