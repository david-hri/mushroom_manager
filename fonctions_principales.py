import pandas as pd

from datetime import datetime, timedelta


def csv(fichier):
   data = pd.read_csv(fichier, sep=' ')
   return data


def difference_dates(date1, date2):
    format_date = "%d/%m/%Y"
    try:
        # Convertir les chaînes de caractères en objets de type datetime
        date1_obj = datetime.strptime(date1, format_date)
        date2_obj = datetime.strptime(date2, format_date)

        # Calculer la différence de jours entre les deux dates
        difference = abs((date2_obj - date1_obj).days)

        return difference
    except ValueError:
        return "Format de date invalide. Utilisez le format dd/mm/yyyy."

    
def new_etageres(df, fichier):
    df.to_csv(fichier, sep=' ', index=True)


file='assets/data/etageres.txt'
data=csv(file)
#print(data)


def dataframe_to_txt(df, fichier):
    df.to_csv(fichier, sep=' ', index=False)


def get_lundi_semaine(date):
    # Récupérer le jour de la semaine correspondant à la date fournie (0 = lundi, 6 = dimanche)
    jour_semaine = date.weekday()

    # Soustraire le nombre de jours écoulés depuis le lundi pour obtenir la date du lundi
    lundi_semaine = date - timedelta(days=jour_semaine)

    return lundi_semaine.strftime("%d/%m/%Y")


# Obtenir la date actuelle
date_actuelle = datetime.now().date()

# Obtenir la date du lundi de la semaine
#lundi_semaine = get_lundi_semaine(date_actuelle)

#print("Date du lundi de la semaine :", lundi_semaine)

def sum_column_with_condition(df):
    # Vérifier si les colonnes "place" et "x" existent dans le DataFrame
    if "taille" not in df.columns or "num_batch" not in df.columns:
        print("Les colonnes 'place' et 'x' doivent exister dans le DataFrame.")
        return None

    # Filtrer le DataFrame où la colonne "x" est égale à 0
    filtered_df = df[df["num_batch"] == 0]

    # Calculer la somme des éléments de la colonne "place" dans le DataFrame filtré
    column_sum = filtered_df["taille"].sum()
    return column_sum


def remplir_newbatch(df,batch,taille=30,show=True,type=1):
    t=taille
    i=0
    d=get_date_jour()
    L=[[] for j in range(max(df["num_etagere"])+1)]

    while t>0:
        

        if df.loc[i,"num_batch"]==0:
            L[df.loc[i,"num_etagere"]]+=[df.loc[i,"etage"]]
            
            
            #print("Remplissez l'étagère "+str(df.loc[i,"num_etagere"])+" à l'étage "+ str(df.loc[i,"etage"]))
            t-=df.loc[i,"taille"]
            df.loc[i,"num_batch"]=batch
            df.loc[i,"date_begin"]=d
            df.loc[i,"type"]=type

        i+=1
    if show:
        for j in range(len(L)):
            if L[j]!=[]:
                et=" "
                for i in L[j]:
                    et+=str(i)+" "

                print("Dans l'étagère "+ str(j )+ " remplissez les étages "+et)
    else:
        return L


def get_date_jour():
    today=datetime.today()
    return today.strftime("%d/%m/%Y")


def trop_vieux(df,time):
    d=get_date_jour()
    B=[]
    for i in range(len(data)):
        dd=difference_dates(d, df.loc[i,"date_begin"])
        if dd>=int(time):
            if (df.loc[i,"date_begin"],df.loc[i,"num_batch"],df.loc[i,"type"]) not in B and df.loc[i,"num_batch"]!=0:
                B.append((df.loc[i,"date_begin"],df.loc[i,"num_batch"],df.loc[i,"type"]))
    return B


def type_champi(num):
    champis=csv('assets/data/liste_champis.txt')
    for i in range(len(champis)):
        if str(champis.loc[i,"Type_id"])==str(num):
            return champis.loc[i,"Type_name"]
        

def get_date_jour_format_ddmmaa():
    # Obtenir la date du jour
    date_aujourdhui = datetime.today()

    # Formater la date sous la forme ddmmaa (jour, mois, année)
    date_formatee = date_aujourdhui.strftime('%d%m%y')

    return date_formatee

def fonction_inutile():
    data=csv('assets/data/etageres.txt')
    for i in range(len(data)):
        if data.loc[i,"type"]=="1":
            data.loc[i,"type"]="J"

        if data.loc[i,"type"]=="2":
            data.loc[i,"type"]="P"
    dataframe_to_txt(data,'assets/data/etageres.txt')
