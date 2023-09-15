from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
from achats import acheter
from creation_compte_client import compte_client
from modification_client import modif1
class login_client:
    def __init__(self,window):
        self.window=window
        self.window.title("login client")
        self.window.geometry("1080x720")
        self.window.resizable(width=0, height=0)
        self.var1_texte=StringVar()
        self.var2_texte=StringVar()
        self.var3_texte=StringVar()


        def red_compte():
            self.compte_fenetre=Toplevel(self.window)
            self.app =compte_client(self.compte_fenetre)
        def modif_client():
            self.modif_fenetre=Toplevel(self.window)
            self.app =modif1(self.modif_fenetre)


        def connexion():
            #connexion
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT * FROM client"
            my_db.execute(requete)
            resultat=my_db.fetchall()
            self.var1_texte.get()
            self.var2_texte.get()
            self.var3_texte.get()
            verification1="access 1"
            verification2="access 2"
            verification3="access 3"
            
            
            for i in enumerate(resultat):
                
                print(i[1])
                
                if self.var1_texte.get() in i[1]:
                    
                    verification1=True
                if self.var2_texte.get() in i[1]:
                    
                    verification2=True
                if self.var3_texte.get() in i[1]:
                    
                    verification3=True
            if verification1==True and verification2==True and verification3==True:
                
                messagebox.showinfo("success","BIENVENU  "+self.var1_texte.get())
                self.achat_fenetre=Toplevel(self.window)
                self.app =acheter(self.achat_fenetre)
                connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
                my_db=connect.cursor()
                requete="SELECT nom_client,prenom_client FROM client"
                my_db.execute(requete)
                resultat=my_db.fetchall()
                for i in resultat:
            
                    f=open('facture.txt','w',encoding='utf8')
                    f.write("nom client:  ")
                    f.write(self.var1_texte.get())
                    f.write("\n")
                    f.write("prenom client:  ")
                    f.write(self.var2_texte.get())
                    f.write("\n")

                   
                        
                        
                        
                    f.close()

                    #copie facture
            else:
                messagebox.showinfo("success","ACCESS REFUSER")
                
               
                

            #connexion

        titre=Label(window,text="/  PARTIE CLIENT /                                                                                                                                                     ",font=("Arial",25),bg="green",fg="white")
        titre.place(x=0,y=0)

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

        nouveau_compte=Button(window,text="CREER UN COMPTE CLIENT",bg="green",fg="white",command=red_compte)
        nouveau_compte.place(x=480,y=430)

        oubli=Label(window,text="vous avez oubliez votre mot de passe ?",font=("Arial",10),bg="#f0f0f0",fg="black")
        oubli.place(x=350,y=500)

        nouveau_PASS=Button(window,text="RENISIALISER LE MOT DE PASS",bg="WHITE",fg="green",command=modif_client)
        nouveau_PASS.place(x=350,y=550)

        nom_utilisateur=Label(window,text="IMPORTANT: VEUILLEZ REMPLIR TOUS LES CHAMPS ",font=("Arial",8),bg="#f0f0f0",fg="black")
        nom_utilisateur.place(x=0,y=700)


       





if __name__== "__main__":
    window=Tk()
    faire=login_client(window)
    window.mainloop()
    
    
