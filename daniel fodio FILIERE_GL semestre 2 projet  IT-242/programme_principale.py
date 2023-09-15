from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
from PIL import Image
from login_admin import Login_ad
from login_cl import login_client


                


class principal:
    def __init__(self,first):
        self.first=first
        self.first.title("fenetre principal")
        self.first.geometry("1080x720")
        self.first.resizable(width=0, height=0)
        self.first.config(background='#16c315')
        

        
                
                 


        def client_lien():
            self.client_fenetre=Toplevel(self.first)
            self.app =login_client(self.client_fenetre)
        def admin_lien():
            self.admin_fenetre=Toplevel(self.first)
            self.app =Login_ad(self.admin_fenetre)
        mainmenu=Menu(first)

        first_menu=Menu(mainmenu,tearoff=0)

        first_menu.add_command(label="ADMIN")

        mainmenu.add_cascade(label="CLIENT ",command=client_lien)

        mainmenu.add_cascade(label="ADMIN ",command=admin_lien)

        nom_utilisateur=Label(first, text="GESTIONNAIRE",font=("Arial",50),bg="#16c315",fg="white")
        nom_utilisateur.place(x=300,y=10)

        nom_utilisateur=Label(first, text="DE",font=("Arial",50),bg="#16c315",fg="white")
        nom_utilisateur.place(x=300,y=80)

        nom_utilisateur=Label(first, text="PHARMACIE:",font=("Arial",50),bg="#16c315",fg="white")
        nom_utilisateur.place(x=420,y=80)

        


        first.config(menu=mainmenu)













   

if __name__== "__main__":
    first=Tk()
    faire=principal(first)
    first.mainloop()



