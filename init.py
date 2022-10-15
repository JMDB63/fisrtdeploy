from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template( 'home.html' ,
                           title="Exemple de templates avec Jinja",
                           description="Mon application avec Flask et Jinja.")

#if __name__ == "__main__":
 #   app.run()