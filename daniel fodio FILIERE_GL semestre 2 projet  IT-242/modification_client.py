from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox



class modif1:
    def __init__(self,mod):
        self.mod=mod
        self.mod.title("reset mot de pass client")
        self.mod.geometry("1080x720")
        self.mod.resizable(width=0, height=0)
        self.var1_texte=StringVar()
        self.var2_texte=StringVar()
        self.var3_texte=StringVar()
        self.var4_texte=StringVar()
        self.var5_texte=StringVar()
        self.var6_texte=StringVar()
        

        def modif():
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
            verification4="access 4"
            verification5="access 5"
            verification6="access 6"
            
            
            
            
            for i in enumerate(resultat):
                print(i)
                print(i[1])
                if self.var1_texte.get() in i[1]:
                    print(verification1)
                    verification1=True
                if self.var2_texte.get() in i[1]:
                    print(verification2)
                    verification2=True
                if self.var3_texte.get() in i[1]:
                    print(verification3)
                    verification3=True
                if self.var4_texte.get() in i[1]:
                    print(verification4)
                    verification4=True
                if verification1==True and verification2==True and verification3==True and verification4==True :
                    print("premiere partie")
                    verification5=True
                if self.var5_texte.get()==self.var6_texte.get():
                    print(verification6)
                    verification6=True
                if verification5==True and verification6==True:
                    connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
                    my_db=connect.cursor()
                    requete=("UPDATE client  SET  mot_de_pass=%s WHERE  nom_client=%s")
                    value=(self.var6_texte.get(),self.var1_texte.get())
                    my_db.execute(requete,value)
                    
                    messagebox.showinfo("success","MOT DE PASS MODIFIER")
                    
                    connect.commit()
                    connect.close()
                    
                    
                else:
                    messagebox.showinfo("success","ACCESS REFUSER")
                
               
                

            #connexion

        nom_utilisateur=Label(mod, text="NOM:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=450,y=100)


        champ_nom=Entry(mod,textvariable=self.var1_texte,width=20,font=("Arial",15))
        champ_nom.place(x=450,y=140)


        nom_utilisateur=Label(mod, text="EMAIL:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=450,y=180)

        champ_nom=Entry(mod,textvariable=self.var2_texte,width=20,font=("Arial",15))
        champ_nom.place(x=450,y=220)


        nom_utilisateur=Label(mod, text="QUESTION DE SECURITE:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=450,y=270)

        self.combo_security=ttk.Combobox(mod, font=("Arial",15),textvariable=self.var3_texte)
        self.combo_security["values"]=("selectionner","votre couleur préféré","le nom de votre meilleur ami","le nom de votre animal de compagie")
        self.combo_security.place(x=450,y=320)


        nom_utilisateur=Label(mod, text="QUESTION DE SECURITE:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=450,y=360)


        champ_nom=Entry(mod,textvariable=self.var4_texte,width=20,font=("Arial",15))
        champ_nom.place(x=450,y=400)


        nom_utilisateur=Label(mod, text="NOUVEAU MOT DE PASS:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=450,y=440)

        champ_nom=Entry(mod,textvariable=self.var5_texte,width=20,font=("Arial",15))
        champ_nom.place(x=450,y=480)

        nom_utilisateur=Label(mod, text="REPETER MOT DE PASS:",font=("Arial",15),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=450,y=520)

        champ_nom=Entry(mod,textvariable=self.var6_texte,width=20,font=("Arial",15))
        champ_nom.place(x=450,y=560)

        check=Checkbutton(mod,text="RENITIALISER LE MOT DE PASS ?",font=("ARIAL",10))
        check.place(x=450,y=620)

        login=Button(mod,text="RENITIALISER",bg="green",fg="white",command=modif)
        login.place(x=450,y=670)

        

        


        











if __name__== "__main__":
    mod=Tk()
    faire=modif1(mod)
    mod.mainloop()



