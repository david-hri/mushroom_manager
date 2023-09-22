import tkinter as tk
from tkinter import ttk
from pythonmax import *
from PIL import Image, ImageTk

default_taille=30
fonction_inutile()

def creer_batch1():
    ajd= get_date_jour()
    data=csv('assets/data/etageres.txt')

    try:
        taille = float(entry1a.get())
        type=entry1b.get()
        champi=csv('assets/data/liste_champis.txt')
        try:
            num = champi.loc[champi['Type_name'] == type, 'Type_id'].iloc[0]
        except:
            result1.delete("1.0", tk.END)
            result1.insert(tk.END, "Veuillez entrer un type valide.")

        if True:
            batch=max(data['num_batch'])+1
            L=remplir_newbatch(data,batch,taille,False,num)
            phrase=""
            for j in range(len(L)):
                et=""
                if L[j]!=[]:
                    for i in L[j]:
                        et+=str(i)+" "
                    phrase+="Dans l'étagère "+str(j) + " remplissez les étages \n "+et +"\n"

            phrase+="Id_batch: "+str(get_date_jour_format_ddmmaa())+num
        result1.delete("1.0", tk.END)
        result1.insert(tk.END, phrase.format(batch))
        dataframe_to_txt(data,'assets/data/etageres.txt')
    except ValueError:
        result1.delete("1.0", tk.END)
        result1.insert(tk.END, "Veuillez entrer un nombre valide.")


def virer_sacs():
    ajd = get_date_jour()
    data = csv('assets/data/etageres.txt')
    B = trop_vieux(data, time_room1)
    
    phrase2 = "Les sacs suivants ont été lardés il y a plus de 2 semaines :\n"
    for i in B:
        phrase2 += "Le Batch " + str(i[1]) + " il y a " + str(difference_dates(ajd, i[0])) + " jours\n Il contient l'espèce "+str(type_champi(i[2]))
    result2.insert(tk.END, phrase2)

    try:
        rep = float(entry2.get())
        phrase3 = ""
        A=[[] for i in range(max(data["num_etagere"])+1)]
        if int(rep) in [i[1] for i in B]:
            for i in range(len(data)):
                if data.loc[i,"num_batch"]==int(rep):
                        A[data.loc[i,"num_etagere"]]+=[data.loc[i,"etage"]]
                        data.loc[i,"num_batch"]=0
            phrase3=""
            for j in range(len(A)):
                et=""
                for i in A[j]:
                        et+=str(i)+ " "
                if et!="":
                        phrase3+="Dans l'étagère "+str(j)+" retirez les étages "+ et +"\n"
        result2.delete("1.0", tk.END)
        result2.insert(tk.END, phrase3.format(rep))
        dataframe_to_txt(data,'assets/data/etageres.txt')

    except ValueError:
        result2.delete("1.0", tk.END)
        result2.insert(tk.END, "Veuillez entrer un nombre valide.")
     
    
def reset_window():
    entry1a.delete(0, tk.END)
    entry1b.delete(0, tk.END)
    entry2.delete(0,tk.END)
    result1.delete("1.0", tk.END)
    result2.delete("1.0",tk.END)
    ajd = get_date_jour()
    data = csv('assets/data/etageres.txt')
    label1.config(text="Taille du nouveau batch "+ "(Il y a "+str(sum_column_with_condition(data))+" places libres) :")
    B = trop_vieux(data, time_room1)
    phrase2 = "Les sacs suivants ont été lardés il y a plus de 2 semaines :\n"
    for i in B:
        phrase2 += "Le Batch " + str(i[1]) + " il y a " + str(difference_dates(ajd, i[0])) + " jours\n"

    result2.insert(tk.END, phrase2)


# Création de la fenêtre principale
window = tk.Tk()
window.iconbitmap("assets/ico/logo.ico")
window.title("CHAMBRE DE CROISSANCE CHAMPIPOTE")
window.geometry("800x500")

img=Image.open("assets/img/img_champote.png")
img=img.resize((800,500))
photo=ImageTk.PhotoImage(img)
label=tk.Label(window,image=photo)
label.pack


# Création de la première section
frame1 = tk.Frame(window, padx=20, pady=20,)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

label1 = tk.Label(frame1, text="Taille du nouveau batch "+ "(Il y a "+str(sum_column_with_condition(data))+" places libres) :")
label1.pack()

entry1a = tk.Entry(frame1)
entry1a.insert(tk.END, str(default_taille))
entry1a.pack()

# Remplacer l'entrée "Type du nouveau batch" par un Combobox avec les options "1" et "2"
label1b = tk.Label(frame1, text="Type du nouveau batch :")
label1b.pack()

# Créer le Combobox avec les options "1" et "2"
entry1b_var = tk.StringVar()
entry1b = ttk.Combobox(frame1, textvariable=entry1b_var, values=["Pleurotes_jaunes","Pleurotes_du_panicaut"])
entry1b.set("Pleurotes_jaunes")  # Définir la valeur par défaut (1 dans ce cas)
entry1b.pack()

button1 = tk.Button(frame1, text="Créer un nouveau batch", command=creer_batch1)
button1.pack()

result1 = tk.Text(frame1, height=10, width=40)
result1.pack()


# Création de la deuxième section
frame2 = tk.Frame(window, bg="gray", padx=20, pady=20)
frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

label2 = tk.Label(frame2, text="Quel batch voulez vous passer en salle de fructification :")
label2.pack()

entry2 = tk.Entry(frame2)
entry2.pack()

button2 = tk.Button(frame2, text="Entrer", command=virer_sacs)
button2.pack()

result2 = tk.Text(frame2, height=10, width=40)
result2.pack()

ajd = get_date_jour()
data = csv('assets/data/etageres.txt')
B = trop_vieux(data, time_room1)

phrase2 = "Les sacs suivants ont été lardés il y a plus de 2 semaines :\n"
for i in B:
    phrase2 += "Le Batch " + str(i[1]) + " il y a " + str(difference_dates(ajd, i[0])) + " jours\nIl contient l'espèce "+str(type_champi(i[2]))+"\n"

result2.insert(tk.END, phrase2)
result2.configure(width=50)

reset_button = tk.Button(frame2, text="Réinitialiser", command=reset_window)
reset_button.pack(side=tk.RIGHT, padx=10, pady=10)


# Ajustement des options pour avoir la même taille des sections
frame1.pack_propagate(False)
frame2.pack_propagate(False)


# Lancement de la boucle principale
window.mainloop()