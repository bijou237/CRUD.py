import mysql.connector as mysql

"""
    CRUD: - Create -> Création d'un utilisateur     -> INSERT INTO
          - Read   -> lister les utilisateurs       -> SELECT
          - Update -> Mise à jour d'un utilisateur  -> UPDATE --- WHERE ID=
          - Delete -> Suppression d'un utilisateur  -> DELETE --- WHERE ID=
          
          UPDATE utilisateur set nom='Bijou' WHERE ID=1
          DELETE users WHERE ID=1


"""

# On crée une foction de connexion à la base de données MySQL
def connexion_db():
    connexion = mysql.connect(
        user='root',
        password='',
        host='localhost',
        database='ecole'
    )
    return connexion

connexion = connexion_db()

# Cration d'un utilisateur
def create_utilisateur(email, password, nom):
    
    cursor = connexion.cursor()

    sql = "INSERT INTO users(email, password, nom) VALUES(%s,%s,%s)"
    cursor.execute(sql, (email,password,nom))
    connexion.commit()

    return (nom, email)

# Lister utilisateur
def read_utilisateur():
    cursor = connexion.cursor()

    sql = "SELECT * FROM utilisateur"
    cursor.execute(sql)
    utilisateur = cursor.fetchall()
    for user in utilisateur:
        print(user)

# update user
# UPDATE `ecole`.`users` SET `password` = '12345' WHERE (`id` = '1');        
def update_user(ID, email, password, nom):
    cursor = connexion.cursor()

    sql = "UPDATE utilisateur SET email=%s, password=%s, nom=%s WHERE id=%s"
    cursor.execute(sql, (email, password, nom, ID))
    connexion.commit()


# DELETE USER
def delete_utilisateur(ID):
    cursor = connexion.cursor()

    sql = "DELETE FROM users WHERE id=%s"
    cursor.execute(sql, (ID,))
    connexion.commit()
1

class Utilisateur:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

class GestionUtilisateurs:
    def __init__(self):
        self.utilisateurs = []

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def lister_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(f"Nom: {utilisateur.nom}, Age: {utilisateur.age}, Email: {utilisateur.email}")

    def mettre_a_jour_utilisateur(self, index, nouvel_utilisateur):
        self.utilisateurs[index] = nouvel_utilisateur

    def supprimer_utilisateur(self, index):
        del self.utilisateurs[index]

def afficher_menu():
    print("Menu :")
    print("1. Ajouter un utilisateur")
    print("2. Mettre à jour un utilisateur")
    print("3. Supprimer un utilisateur")
    print("4. Lister les utilisateurs")
    print("5. Quitter")

def main():
    gestion_utilisateurs = GestionUtilisateurs()

    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom de l'utilisateur : ")
            age = input("Âge de l'utilisateur : ")
            email = input("Email de l'utilisateur : ")
            utilisateur = Utilisateur(email, password, nom)
            gestion_utilisateurs.ajouter_utilisateur(utilisateur)

        elif choix == "2":
            index = int(input("Indiquez l'index de l'utilisateur à mettre à jour : "))
            nom = input("Nouveau nom de l'utilisateur : ")
            age = input("Nouvel âge de l'utilisateur : ")
            email = input("Nouvel email de l'utilisateur : ")
            nouvel_utilisateur = Utilisateur(email, password, nom)
            gestion_utilisateurs.mettre_a_jour_utilisateur(index, nouvel_utilisateur)

        elif choix == "3":
            index = int(input("Indiquez l'index de l'utilisateur à supprimer : "))
            gestion_utilisateurs.supprimer_utilisateur(index)

        elif choix == "4":
            gestion_utilisateurs.lister_utilisateurs()

        elif choix == "5":
            print("Merci d'avoir utilisé le programme.")
            break

        else:
            print("Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()