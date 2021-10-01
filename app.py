import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_games")
def get_games():
    games = list(mongo.db.games.find())
    return render_template("games.html", games=games)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    games = list(mongo.db.games.find({"$text": {"$search": query}}))
    return render_template("games.html", games=games)


@app.route("/register", methods=["GET", "POST"])
def register():
    # check if user is in the DB
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if registered_user:
            flash("Sorry, That username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Thanks for Registering, Welcome to the Family!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking username's existsance in db
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if registered_user:
            # checks if password matches user input
            if check_password_hash(
                registered_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Unfortunately your Username and/or Password is incorrect")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Unfortunately your Username and/or Password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # obtaining the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session['user']:
        return render_template("profile.html", username=username)
    
    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/add_games", methods=["GET", "POST"])
def add_games():
    if request.method == "POST":
        game = {
            "genre_name": request.form.get("genre_name"),
            "game_name": request.form.get("game_name"),
            "game_description": request.form.get("game_description"),
            "release_date": request.form.get("release_date"),
            "img_url": request.form.get("img_url"),
            "created_by": session["user"]
        }
        mongo.db.games.insert_one(game)
        flash("Thanks for adding a game!")
        return redirect(url_for('get_games'))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_games.html", genres=genres)


@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "game_name": request.form.get("game_name"),
            "game_description": request.form.get("game_description"),
            "release_date": request.form.get("release_date"),
            "img_url": request.form.get("img_url"),
            "created_by": session["user"]
        }
        mongo.db.games.update({"_id": ObjectId(game_id)}, submit)
        flash("Game Successfully Updated")

    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_game.html", game=game, genres=genres)


@app.route("/delete_game/<game_id>")
def delete_game(game_id):
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Game Successfully Deleted")
    return redirect(url_for("get_games"))


if __name__ == "__main__":
   app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
