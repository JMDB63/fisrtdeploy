from flask import Flask, render_template

skills_app = Flask(__name__)

countries_list = [
               {"city": "Paris", "country": "France"},
               {"city": "Londres", "country": "Angleterre"},
               {"city": "Munich", "country": "Allemagne"},
               {"city": "Madrid", "country": "Espagne"}
           ]

@skills_app.route("/")
def homepage():
   return render_template('list_for.html', countries=countries_list)

#if __name__ == "__main__":
 #  skills_app.run(debug = True)
