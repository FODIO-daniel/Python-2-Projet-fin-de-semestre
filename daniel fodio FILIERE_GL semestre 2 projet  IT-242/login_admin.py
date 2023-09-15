from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
from gestion_stock import stock
from creation_compte_admin import compte_admin
from modification_admin import modif2
class Login_ad:
    def __init__(self,window):
        self.window=window
        self.window.title("login ADMIN")
        self.window.geometry("1080x720")
        self.window.resizable(width=0, height=0)
        self.var1_texte=StringVar()
        self.var2_texte=StringVar()
        self.var3_texte=StringVar()

        titre=Label(window,text="/  PARTIE ADMIN /                                                                                                                                                        ",font=("Arial",25),bg="#fb6001",fg="white")
        titre.place(x=0,y=0)

        def com_admin():
            self.compte_fenetre=Toplevel(self.window)
            self.app =compte_admin(self.compte_fenetre)
        def pass_admin():
            self.pass_fenetre=Toplevel(self.window)
            self.app =modif2(self.pass_fenetre)
            

        def connexion():
            #connexion
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT * FROM administrateur"
            my_db.execute(requete)
            resultat=my_db.fetchall()
            self.var1_texte.get()
            self.var2_texte.get()
            self.var3_texte.get()
            verification1="access 1"
            verification2="access 2"
            verification3="access 3"
            
            
            for i in enumerate(resultat):
                print(i)
            if self.var1_texte.get() in i[1]:
                
                verification1=True
            if self.var2_texte.get() in i[1]:
                
                verification2=True
            if self.var3_texte.get() in i[1]:
                
                verification3=True
            if verification1==True and verification2==True and verification3==True:
                messagebox.showinfo("success","BIENVENU  "+self.var1_texte.get())
                self.stock_fenetre=Toplevel(self.window)
                self.app =stock(self.stock_fenetre)
            else:
                messagebox.showinfo("success","ACCESS REFUSER")
                
               
                

            #connexion

        nom_utilisateur=Label(window,text="NOM du client:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=70)
        
        champ_nom=Entry(window,textvariable=self.var1_texte,width=20,font=("Arial",20))
        champ_nom.place(x=350,y=100)


        nom_utilisateur=Label(window,text="PRENOM:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=200)


        champ_prenom=Entry(window,textvariable=self.var2_texte,width=20,font=("Arial",20))
        champ_prenom.place(x=350,y=230)


        nom_utilisateur=Label(window,text="MOT DE PASS:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=320)


        champ_password=Entry(window,textvariable=self.var3_texte,width=20,font=("Arial",20))
        champ_password.place(x=350,y=350)


        login=Button(window,text="IDENTIFIER",bg="green",fg="white",command=connexion)
        login.place(x=350,y=430)

        nom_utilisateur=Label(window,text="OU",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=437,y=430)

        nouveau_compte=Button(window,text="CREER UN COMPTE CLIENT",bg="green",fg="white",command=com_admin)
        nouveau_compte.place(x=480,y=430)

        oubli=Label(window,text="vous avez oubliez votre mot de passe ?",font=("Arial",10),bg="#f0f0f0",fg="black")
        oubli.place(x=350,y=500)

        nouveau_PASS=Button(window,text="RENISIALISER LE MOT DE PASS",bg="WHITE",fg="green",command=pass_admin)
        nouveau_PASS.place(x=350,y=550)


        nom_utilisateur=Label(window,text="IMPORTANT: VEUILLEZ REMPLIR TOUS LES CHAMPS ",font=("Arial",8),bg="#f0f0f0",fg="black")
        nom_utilisateur.place(x=0,y=700)


       





if __name__== "__main__":
    window=Tk()
    faire=Login_ad(window)
    window.mainloop()
    
    
