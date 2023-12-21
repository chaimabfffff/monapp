from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)


#inscrire + met donnes dans base de donnees
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        motdepasse = request.form['motdepasse']
        
        # Connexion à la base de données
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Vérification si l'email existe déjà
        cursor.execute('SELECT id FROM Utilisateurs WHERE email = ?', (email,))
        user = cursor.fetchone()
        if user:
            return render_template('registration.html', error='L\'email existe déjà')
        
        # Insertion des données de l'utilisateur dans la base de données
        cursor.execute('INSERT INTO Utilisateurs(nom, prenom, email, motdepasse) VALUES (?, ?, ?, ?)', (nom, prenom, email, motdepasse))
        conn.commit()
    
        
        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()
        
        return redirect(url_for('login'))
    
    return render_template('registration.html')


#verif si l'utilsateur est bien inscrit lors de la connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Connexion à la base de données
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Vérification si l'utilisateur existe dans la base de données
        cursor.execute('SELECT * FROM Utilisateurs WHERE email = ? AND motdepasse = ?', (email, password))
        user = cursor.fetchone()
        if user:
            # Fermeture de la connexion à la base de données
            cursor.close()
            conn.close()
            return redirect(url_for('home'))
        else:
            # Fermeture de la connexion à la base de données
            cursor.close()
            conn.close()
          
    return render_template('login.html')






