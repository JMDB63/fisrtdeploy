from flask import Flask, render_template,redirect, url_for, request
app = Flask(__name__)


#@app.route('/addition/<int:nombre_1>/<int:nombre_2>')
@app.route('/addition_test/<nbr1>')
def addition(nbr1):

    return render_template("addition_test.html",add="resultat",nombre1=nbr1)



@app.route('/Formulaire_test',methods = ['POST'])
def recuperer_nbr():
    #return render_template("nom.html")
    nombr1 = request.form['nbr1']
    #nombr2 = request.form['nbr2']
    #operande=request.form['operande']

    return redirect(url_for('templates',filename="/addition_test",nbr1=nombr1))

@app.route('/')
def recuperer():
    return render_template("Formulaire_test.html")

if __name__ == "__main__":
    app.run(debug=True)