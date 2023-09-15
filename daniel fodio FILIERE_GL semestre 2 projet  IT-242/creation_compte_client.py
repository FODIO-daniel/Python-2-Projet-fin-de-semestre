from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox




class compte_client:
    def __init__(self,client):
        self.client=client
        self.client.title("creation compte client")
        self.client.geometry("1080x720")
        self.var1_texte=StringVar()
        self.var2_texte=StringVar()
        self.var3_texte=StringVar()
        self.var4_texte=StringVar()
        self.var5_texte=StringVar()
        self.var6_texte=StringVar()
        self.var7_texte=StringVar()

        

        def login_client():
            self.retour_fenetre=Toplevel(self.client)
            self.app =login_client(self.retour_fenetre)
        def creer_compte():
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT mot_de_pass,email FROM administrateur"
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                o=i[1]
            for t in range(0,1):
                if self.var7_texte.get() in o:
                    messagebox.showinfo("success","MOT DE PASS DEJA UTILISER") 
                if self.var4_texte.get() in o:
                    messagebox.showinfo("success","UN COMPTE EST DEJA LIE A CET EMAIL")
                else:
                    my_db.execute("insert into client(nom_client,prenom_client, email,contact,question_securite_client,champ_securite_client,mot_de_pass) values(%s,%s,%s,%s,%s,%s,%s)",(self.var1_texte.get(),
                                                                                                                                                 self.var2_texte.get(),
                                                                                                                                                 self.var4_texte.get(),
                                                                                                                                                 self.var3_texte.get(),
                                                                                                                                                 self.var5_texte.get(),
                                                                                                                                                 self.var6_texte.get(),              
                                                                                                                                                 self.var7_texte.get()))
                    connect.commit()
                    connect.close()
                    
                    champ_nom.delete(0,END)
                    champ_prenom.delete(0,END)
                    champ_tel.delete(0,END)
                    champ_mail.delete(0,END)
                    champ_pass.delete(0,END)
                    champ_quiz.delete(0,END)

                    messagebox.showinfo("success","COMPTE CREER!")

            

            
            
            
            
            

        nom_utilisateur=Label(client, text="NOM:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=10)

        champ_nom=Entry(client,textvariable=self.var1_texte,width=20,font=("Arial",15))
        champ_nom.place(x=350,y=50)

        nom_utilisateur=Label(client, text="PRENOM:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=100)

        champ_prenom=Entry(client,textvariable=self.var2_texte,width=20,font=("Arial",15))
        champ_prenom.place(x=350,y=140)

        nom_utilisateur=Label(client, text="CONTACT:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=190)

        champ_tel=Entry(client,textvariable=self.var3_texte,width=20,font=("Arial",15))
        champ_tel.place(x=350,y=230)

        nom_utilisateur=Label(client, text="EMAIL:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=280)


        champ_mail=Entry(client,textvariable=self.var4_texte,width=20,font=("Arial",15))
        champ_mail.place(x=350,y=320)

        nom_utilisateur=Label(client, text="QUESTION DE SECURITE:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=370)


        self.combo_security=ttk.Combobox(client, font=("Arial",15),textvariable=self.var5_texte)
        self.combo_security["values"]=("votre couleur préféré","le nom de votre meilleur ami","le nom de votre animal de compagie")
        self.combo_security.place(x=350,y=410)

        nom_utilisateur=Label(client, text="QUESTION DE SECURITE:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=460)

        champ_quiz=Entry(client,textvariable=self.var6_texte,width=20,font=("Arial",15))
        champ_quiz.place(x=350,y=500)

        nom_utilisateur=Label(client, text="MOT DE PASS:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=350,y=550)

        champ_pass=Entry(client,textvariable=self.var7_texte,width=20,font=("Arial",15))
        champ_pass.place(x=350,y=590)

        check=Checkbutton(client,text="J'ACCEPTE LES TERMS ET CONDITION",font=("ARIAL",10))
        check.place(x=350,y=650)

        login=Button(client,text="CREER LE COMPTE",bg="green",fg="white",command=creer_compte)
        login.place(x=350,y=690)

        

        












if __name__== "__main__":
    client=Tk()
    faire=compte_client(client)
    client.mainloop()



