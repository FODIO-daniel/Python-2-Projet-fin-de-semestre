from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox



class stock:
    def __init__(self,stockage):
        self.stockage=stockage
        self.stockage.title("stock")
        self.stockage.geometry("1550x800")
        self.var1_texte=StringVar()
        self.var2_texte=StringVar()
        self.var3_texte=StringVar()
        self.var4_texte=StringVar()
        self.var5_texte=StringVar()
        self.var6_texte=StringVar()
        self.var7_texte=StringVar()
        self.var8_texte=StringVar()
        self.var9_texte=StringVar()
        self.var10_texte=StringVar()
        self.var11_texte=StringVar()
        self.var12_texte=StringVar()
        self.var13_texte=StringVar()
        self.var14_texte=StringVar()
        self.var100_texte=StringVar()
    
        def ajouter():
            var1=champ_nom_m.get()
            var3=champ_prix.get()
            var4=self.var4_texte.get()
            var5=champ_qte.get()
            var6=champ_date.get()
            var7=champ_expi.get()
            var8=champ_num_serie.get()
            var9=champ_num_m.get()
            var10=champ_nom_f.get()
            var11=champ_fact.get()
        
            tv.insert(parent='', index=END, text='', values=(var1,var3,var4,var5,var6,var7,var9,var10,var11))
            champ_nom_m.get()
            champ_prix.get()

            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            my_db.execute("insert into medicament(nom_medicament,nom_admin, prix_medicament,quantite,type ,date_ajout,date_expiration,numero_medicament,nom_fabricant,numero_facture,maladie,posologie,avertissement,effets_secondaire) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var2_texte.get(),
                                                                                                                                                                                                                                     self.var1_texte.get(),
                                                                                                                                                                                                                                     self.var3_texte.get(),
                                                                                                                                                                                                                                     self.var5_texte.get(),
                                                                                                                                                                                                                                     self.var4_texte.get(),
                                                                                                                                                                                                                                     self.var6_texte.get(),
                                                                                                                                                                                                                                     self.var7_texte.get(),              
                                                                                                                                                                                                                                     self.var9_texte.get(),
                                                                                                                                                                                                                                     self.var10_texte.get(),
                                                                                                                                                                                                                                     self.var11_texte.get(),
                                                                                                                                                                                                                                     self.var8_texte.get(),
                                                                                                                                                                                                                                     self.var12_texte.get(),
                                                                                                                                                                                                                                     self.var13_texte.get(),
                                                                                                                                                                                                                                     self.var14_texte.get()))                                                       
            connect.commit()
            connect.close()
            
            
            champ_qte.delete(0,END)
            champ_date.delete(0,END)
            champ_expi.delete(0,END)
            champ_num_serie.delete(0,END)
            champ_num_m.delete(0,END)
            champ_nom_f.delete(0,END)
            champ_nom_m.delete(0,END)
            champ_prix.delete(0,END)
            champ_nom.delete(0,END)
            champ_fact.delete(0,END)
            champ_pos.delete(0,END)
            champ_aver.delete(0,END)
            champ_efec.delete(0,END)
            

            messagebox.showinfo("success","MEDICAMENT AJOUTER")
        def actualiser():
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT nom_medicament,prix_medicament,type,quantite,date_ajout,date_expiration,numero_medicament,nom_fabricant,numero_facture FROM medicament"
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
    
                tv.insert(parent='', index=END, text='', values=(i[1]))
            
            
       
            
       
        def effacer():
            
            
            
            
                
                
            x=tv.selection()[0]
            tv.delete(x)
                
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="DELETE FROM medicament WHERE numero_medicament= '{}'".format(self.var100_texte.get())
            my_db.execute(requete)
                

            connect.commit()

            connect.close()
        nom_utilisateur=Label(stockage,text=" NUMERO DU MEDICAMENT A SUPPRIMER DU STOCK:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=290,y=380)
        champ_nom=Entry(stockage,textvariable=self.var100_texte,width=20,font=("Arial",15))
        champ_nom.place(x=650,y=375)
            
        nom_utilisateur=Label(stockage,text="NOM ADMINISTRATEUR:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=5,y=0)

        champ_nom=Entry(stockage,textvariable=self.var1_texte,width=20,font=("Arial",15))
        champ_nom.place(x=5,y=25)

        nom_utilisateur=Label(stockage,text="NOM DU MEDICAMENT:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=5,y=60)

        champ_nom_m=Entry(stockage,textvariable=self.var2_texte,width=20,font=("Arial",15))
        champ_nom_m.place(x=5,y=85)

        nom_utilisateur=Label(stockage,text="PRIX DU MEDICAMENT:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=5,y=120)

        champ_prix=Entry(stockage,textvariable=self.var3_texte,width=20,font=("Arial",15))
        champ_prix.place(x=5,y=145)

        nom_utilisateur=Label(stockage,text="TYPE DU MEDICAMENT:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=5,y=180)



        self.combo_security=ttk.Combobox(stockage, font=("Arial",15),textvariable=self.var4_texte)
        self.combo_security["values"]=("comprimé","gelulle","injection"," sirop")
        self.combo_security.place(x=5,y=205)

        nom_utilisateur=Label(stockage,text="QUANTITE DU MEDICAMENT:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=5,y=240)

        champ_qte=Entry(stockage,textvariable=self.var5_texte,width=20,font=("Arial",15))
        champ_qte.place(x=5,y=265)

        nom_utilisateur=Label(stockage,text="DATE D'AJOUT:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=5,y=300)

        champ_date=Entry(stockage,textvariable=self.var6_texte,width=20,font=("Arial",15))
        champ_date.place(x=5,y=325)

        nom_utilisateur=Label(stockage,text="DATE D'EXPIRATION:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=300,y=0)

        champ_expi=Entry(stockage,textvariable=self.var7_texte,width=20,font=("Arial",15))
        champ_expi.place(x=300,y=25)

        nom_utilisateur=Label(stockage,text="MALADIE:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=300,y=60)

        champ_num_serie=Entry(stockage,textvariable=self.var8_texte,width=20,font=("Arial",15))
        champ_num_serie.place(x=300,y=85)

        nom_utilisateur=Label(stockage,text="NUMERO MEDICAMENT:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=300,y=120)

        champ_num_m=Entry(stockage,textvariable=self.var9_texte,width=20,font=("Arial",15))
        champ_num_m.place(x=300,y=145)

        nom_utilisateur=Label(stockage,text="NOM DU FABRICANT:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=300,y=180)

        champ_nom_f=Entry(stockage,textvariable=self.var10_texte,width=20,font=("Arial",15))
        champ_nom_f.place(x=300,y=205)

        nom_utilisateur=Label(stockage,text="NUMERO FACTURE:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=300,y=240)

        champ_fact=Entry(stockage,textvariable=self.var11_texte,width=20,font=("Arial",15))
        champ_fact.place(x=300,y=265)

        login=Button(stockage,text="AJOUTER AU STOCK",bg="green",fg="white",command=ajouter)
        login.place(x=300,y=325)

        login=Button(stockage,text="EFFACER DU STOCK",bg="green",fg="white",command=effacer)
        login.place(x=420,y=325)


        login=Button(stockage,text="ACTUALISER",bg="green",fg="white",command=actualiser)
        login.place(x=540,y=325)

        


        nom_utilisateur=Label(stockage,text="posologie:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=550,y=0)
        champ_pos=Entry(stockage,textvariable=self.var12_texte,width=50,font=("Arial",10))
        champ_pos.place(x=550,y=23)

        
        nom_utilisateur=Label(stockage,text="avertissement:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=550,y=43)

        champ_aver=Entry(stockage,textvariable=self.var13_texte,width=50,font=("Arial",10))
        champ_aver.place(x=550,y=63)

        nom_utilisateur=Label(stockage,text="effets secondaire:",font=("Arial",10),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=550,y=83)

        champ_efec=Entry(stockage,textvariable=self.var14_texte,width=50,font=("Arial",10))
        champ_efec.place(x=550,y=103)

        nom_utilisateur=Label(stockage,text="liste des produits:",font=("Arial",20),bg="#f0f0f0",fg="#222221")
        nom_utilisateur.place(x=5,y=370)


        tv = ttk.Treeview(stockage)
        tv['columns']=('NOM MEDICAMENT', 'PRIX DU MEDICAMENT', 'TYPE DU MEDICAMENT','QUANTITE DU MEDICAMENT','DATE AJOUT','DATE EXPIRATION','NUMERO MEDICAMENT','NOM DU FABRICANT','NUMERO FACTURE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('NOM MEDICAMENT', anchor=CENTER, width=170)
        tv.column('PRIX DU MEDICAMENT', anchor=CENTER, width=170)
        tv.column('TYPE DU MEDICAMENT', anchor=CENTER, width=170)
        tv.column('QUANTITE DU MEDICAMENT', anchor=CENTER, width=170)
        tv.column('DATE AJOUT', anchor=CENTER, width=170)
        tv.column('DATE EXPIRATION', anchor=CENTER, width=170)
        tv.column('NUMERO MEDICAMENT', anchor=CENTER, width=170)
        tv.column('NOM DU FABRICANT', anchor=CENTER, width=170)
        tv.column('NUMERO FACTURE', anchor=CENTER, width=170)
        

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('NOM MEDICAMENT', text='NOM MEDICAMENT', anchor=CENTER)
        tv.heading('PRIX DU MEDICAMENT', text='PRIX DU MEDICAMENT', anchor=CENTER)
        tv.heading('TYPE DU MEDICAMENT', text='TYPE DU MEDICAMENT', anchor=CENTER)
        tv.heading('QUANTITE DU MEDICAMENT', text='QUANTITE DU MEDICAMENT', anchor=CENTER)
        tv.heading('DATE AJOUT', text='DATE AJOUT', anchor=CENTER)
        tv.heading('DATE EXPIRATION', text='DATE EXPIRATION', anchor=CENTER)
        tv.heading('NUMERO MEDICAMENT', text='NUMERO MEDICAMENT', anchor=CENTER)
        tv.heading('NOM DU FABRICANT', text='NOM DU FABRICANT', anchor=CENTER)
        tv.heading('NUMERO FACTURE', text='NUMERO FACTURE', anchor=CENTER)
        tv.place(x=5,y=420)


        
        
















if __name__== "__main__":
    stockage=Tk()
    faire=stock(stockage)
    stockage.mainloop()



