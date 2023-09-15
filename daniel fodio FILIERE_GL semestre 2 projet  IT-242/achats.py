from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox



class acheter:
    def __init__(self,achat):
        self.achat=achat
        self.achat.title("achat medicaments")
        self.achat.geometry("1080x720")
        self.achat.config(background='green')
        self.var1_texte=StringVar()
        self.var2_texte=StringVar()
        self.var3_texte=StringVar()

        tva = ttk.Treeview(achat)
        tva['columns']=('NOM', 'FABRIQUANT', 'PRIX')
        tva.column('#0', width=0, stretch=NO)
        tva.column('NOM', anchor=CENTER, width=200)
        tva.column('FABRIQUANT', anchor=CENTER, width=200)
        tva.column('PRIX', anchor=CENTER, width=200)
        

        tva.heading('#0', text='', anchor=CENTER)
        tva.heading('NOM', text='NOM', anchor=CENTER)
        tva.heading('FABRIQUANT', text='FABRIQUANT', anchor=CENTER)
        tva.heading('PRIX', text='PRIX', anchor=CENTER)
        tva.place(x=50,y=70)

        connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
        my_db=connect.cursor()
        requete="SELECT nom_medicament,nom_fabricant,prix_medicament FROM medicament"
        my_db.execute(requete)
        resultat=my_db.fetchall()
        for i in enumerate(resultat):
            tva.insert(parent='', index=END, text='', values=(i[1]))
        def facture():
            self.var2_texte.get()
            messagebox.showinfo("success","PRIX TOTAL DES ACHATS EFFECTUER: \n"+self.var2_texte.get()+"  franc")
            

        def INFORMATIONS():
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT nom_medicament  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                prix=i[1]
                for s in prix:
                    
                    r=prix[0]
                    r=str(r)
                    ligne_texteA.insert(END,"MEADICAMENT ACHETE:"+r)
            connect.commit()

            connect.close()

            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT date_expiration  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                prix=i[1]
                for s in prix:
                    
                    r=prix[0]
                    r=str(r)
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END,"DATE D'EXPIRATION:"+r)
            connect.commit()

            connect.close()

            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT maladie  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                prix=i[1]
                for s in prix:
                    
                    r=prix[0]
                    r=str(r)
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END,"MALADIE TRAITER:"+r)
            connect.commit()

            connect.close()

            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT posologie  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                prix=i[1]
                for s in prix:
                    
                    r=prix[0]
                    r=str(r)
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END,"POSOLOGIE:"+r)
            connect.commit()

            connect.close()
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT avertissement  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                prix=i[1]
                for s in prix:
                    
                    r=prix[0]
                    r=str(r)
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END,"avertissement:"+r)
            connect.commit()

            connect.close()
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT effets_secondaire  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                prix=i[1]
                for s in prix:
                    
                    r=prix[0]
                    r=str(r)
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END," ")
                    ligne_texteA.insert(END,"effets_secondaire:"+r)
                    ligne_texteA.insert(END,"--------------------------------------------------------------------------------------------------------------------------------")
            connect.commit()

            connect.close()
                

        def ajout_tableau2():
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT nom_medicament,prix_medicament  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                prix=i[1]
        
                tv.insert(parent='', index=END, text='', values=(i[1]))
                connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
                my_db=connect.cursor()
                requete="SELECT nom_medicament,type,date_expiration,nom_fabricant,maladie,posologie,avertissement,effets_secondaire  FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
                my_db.execute(requete)
                resultat=my_db.fetchall()
                for i in enumerate(resultat):
                    t=i[1]
                    for s in prix:
                        
        
                        f=open('facture.txt','r',encoding='utf8')
                        m=f.read()
                        f.close()
                    if m!="":
                        
                        f=open('facture.txt','a',encoding='utf8')
                        f.write("\n")
                        f.write("NOM DU MEDICAMENT: ")
                        f.write(t[0])
                        f.write("\n")
                        f.write("TYPE: ")
                        f.write(t[1])
                        f.write("\n")
                        f.write("DATE D'EXPIRATION: ")
                        f.write(t[2])
                        f.write("\n")
                        f.write("NOM DU FABRIQUANT: ")
                        f.write(t[3])
                        f.write("\n")
                        f.write("MALADIE TRAITER: ")
                        f.write(t[4])
                        f.write("\n")
                        f.write("POSOLOGIE: ")
                        f.write(t[5])
                        f.write("\n")
                        f.write("CONSIGNES: ")
                        f.write(t[6])
                        f.write("\n")
                        f.write("EFFETS SECONDAIRE: ")
                        f.write(t[7])
                        f.write("\n")
                        f.write("PRIX TOTAL DES ACHATS:")
                        f.write(self.var2_texte.get())
                        f.write("\n")
                        
                        
                        
                        
                        f.close()
                    
            connect.commit()

            connect.close()
                
            
        def ajouter():
            ajout_tableau2()
            self.var1_texte.get()
            result=self.var1_texte.get()
            result=int(result)
            
            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT prix_medicament FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                
                prix=i[1]
                for s in prix:
                    if self.var2_texte.get()=="":
                        
                        achat1=result*prix[0]
                        
                        
                            
                        champ_prix.delete(0,END)
                        champ_prix.insert(END,achat1)
                    elif self.var2_texte.get()!="":
                        self.var2_texte.get()
                        
                        r=self.var2_texte.get()
                        r=int(r)
                        connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
                        my_db=connect.cursor()
                        requete="SELECT prix_medicament FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            
                        my_db.execute(requete)
                        resultat=my_db.fetchall()
                        for i in enumerate(resultat):
                            prix=i[1]
                            for s in prix:
                                if self.var2_texte.get()!="":
                                    
                                    achat1=result*prix[0]
                                    

                                   
                                    total=r+achat1
                                    champ_prix.delete(0,END)
                                    champ_prix.insert(END,total)
                                    
                                    
                            
        
            
            connect.commit()

            connect.close()

            connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
            my_db=connect.cursor()
            requete="SELECT quantite FROM medicament WHERE nom_medicament='{}'".format(self.var3_texte.get())
            my_db.execute(requete)
            resultat=my_db.fetchall()
            for i in enumerate(resultat):
                
                quant=i[1]
                for s in quant:
                    g=quant[0]
                    if self.var1_texte.get()!="" and g!=0:
                       r=self.var1_texte.get()
                       r=int(r)
                       val=g-r
                       connect=mysql.connect(host='localhost',user='root',password='',database='projet pharmacie')
                       my_db=connect.cursor()
                       requete=("UPDATE medicament  SET  quantite=%s WHERE  nom_medicament=%s")
                       value=(val,self.var3_texte.get())
                       my_db.execute(requete,value)
                        
                       
                        
                       connect.commit()
                       connect.close()

                       if r>g:
                           messagebox.showinfo("success","LA QUANTITE RENSEIGNER  DEPASSE LE STOCK")
                           if g==0 or g<0:
                               messagebox.showinfo("success","PRODUIT EN RUPTURE")
                               
                    
                        
                       
            

            


        nom_utilisateur=Label(achat,text="LISTE DES MEDICAMENT DISPONIBLES",font=("Arial",20),bg="white",fg="green")
        nom_utilisateur.place(x=50,y=20)

        nom_utilisateur=Label(achat,text="NOM DU MEDICAMENT ",font=("Arial",12),bg="green",fg="white")
        nom_utilisateur.place(x=50,y=300)

        champ_qte=Entry(achat,textvariable=self.var3_texte,width=20,font=("Arial",12))
        champ_qte.place(x=230,y=300)

        nom_utilisateur=Label(achat,text="QTE",font=("Arial",12),bg="green",fg="white")
        nom_utilisateur.place(x=50,y=350)

        nom_utilisateur=Label(achat,text="PRIX TOTAL",font=("Arial",12),bg="green",fg="white")
        nom_utilisateur.place(x=50,y=690)


        champ_qte=Entry(achat,textvariable=self.var1_texte,width=10,font=("Arial",12))
        champ_qte.place(x=100,y=350)

        champ_prix=Entry(achat,textvariable=self.var2_texte,width=10,font=("Arial",12))
        champ_prix.place(x=150,y=690)


        nom_utilisateur=Label(achat,text="INFORMATIONS",font=("Arial",20),bg="white",fg="green")
        nom_utilisateur.place(x=835,y=20)

        

        var_texte=StringVar()
        ligne_texteA=Listbox(achat,height=38,width=100)
        ligne_texteA.place(x=670,y=70)



        


        ajout=Button(achat,text="AJOUTER",bg="green",fg="white",command=ajouter)
        ajout.place(x=50,y=380)

        ajout=Button(achat,text="INFORMATIONS",bg="green",fg="white",command=INFORMATIONS)
        ajout.place(x=150,y=380)

        ajout=Button(achat,text="FACTURE",bg="green",fg="white",command=facture)
        ajout.place(x=270,y=380)


        tv = ttk.Treeview(achat)
        tv['columns']=('NOM','PRIX UNITAIRE')
        tv.column('#0', width=0, stretch=NO)
        tv.column('NOM', anchor=CENTER, width=200)
        tv.column('PRIX UNITAIRE', anchor=CENTER, width=200)
        
        

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('NOM', text='NOM', anchor=CENTER)
        tv.heading('PRIX UNITAIRE', text='PRIX UNITAIRE', anchor=CENTER)
        
        tv.place(x=50,y=456)



        


        
       












if __name__== "__main__":
    achat=Tk()
    faire=acheter(achat)
    achat.mainloop()



