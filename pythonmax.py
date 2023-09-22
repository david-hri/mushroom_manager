from datetime import datetime
from fonctions_principales import *


class Etagere:
    def __init__(self,num):
            self.num = num
            self.batch = None


class Batch:
    def __init__(self,name,date):
            self.name = name
            self.etagere=None
            self.date=date
            self.state="None"
            

# Obtenir le numéro du jour actuel
numero_jour = datetime.now().day

#print("Le numéro du jour actuel est :", numero_jour)          
time_cook=1
time_room1=14
time_room2=14

'''
def creer_batch():
    ajd= get_date_jour()
    data=csv('etageres_init.txt')

    a=input("Voulez vous lancer un batch sachant qu'il y a actuellement "+str(sum_column_with_condition(data))+" places de libre ")

    if a=="oui":
            batch=max(data['num_batch'])+1
            remplir_newbatch(data,batch,taille=30)
    dataframe_to_txt(data,'etageres.txt')
'''

def virer_sacs():
    ajd= get_date_jour()
    data=csv(folder/'assets/data/etageres_init.txt')
    B=trop_vieux(data,time_room1)
    print("Les sacs suivants ont été lardés il y a plus de 2 semaines")
    for i in B:
          print("Le Batch "+str(i[1])+" il y a "+str(difference_dates(ajd,i[0]))+ " jours ")
    print(B)
    rep="truc"

    while rep!="" :
        try:
            rep=int(input("Donnez le numéro des Batch à retirer "))
            if int(rep) in [i[1] for i in B]:
                for i in range(len(data)):
                    if data.loc[i,"num_batch"]==int(rep):
                            print("Supprimez l'étage "+ str(data.loc[i,"etage"])+ " de la l'étagère " +str(data.loc[i,"num_etagere"]))
                            data.loc[i,"num_batch"]=0
        except:
            rep=""
     
    dataframe_to_txt(data,folder/'assets/data/etageres.txt')


def taches_semaine():
    ajd= get_date_jour()
    data=csv(folder/'assets/data/etageres_init.txt')

    a=input("Voulez vous lancer un batch sachant qu'il y a actuellement "+str(sum_column_with_condition(data))+" places de libre ")
    if a=="oui":
            batch=max(data['num_batch'])+1
            remplir_newbatch(data,batch,taille=30)
    B=trop_vieux(data,time_room1)
    print("Les sacs suivants ont été lardés il y a plus de 2 semaines")
    for i in B:
          print("Le Batch "+str(i[1])+" il y a "+str(difference_dates(ajd,i[0]))+ " jours ")
    print(B)
    rep="truc"
    while rep!="":
        try:
            A=[[] for i in range(max(data["num_etagere"])+1)]
            rep=int(input("Donnez le numéro des Batch à retirer "))
            if int(rep) in [i[1] for i in B]:
                for i in range(len(data)):
                    if data.loc[i,"num_batch"]==int(rep):
                            A[data.loc[i,"num_etagere"]]+=[data.loc[i,"etage"]]
                            print("Supprimez l'étage "+ str(data.loc[i,"etage"])+ " de la l'étagère " +str(data.loc[i,"num_etagere"]))
                            data.loc[i,"num_batch"]=0
                for j in range(len(A)):
                    et=""
                    for i in A[j]:
                            et+=str(i)+ " "
                    if et!="":
                            print("Dans l'étagère "+str(j)+" retirez les étages "+ et)          
        except:
            rep=""

    '''
    while rep!="":
        try:
            rep=int(input("Donnez le numéro des Batch à retirer "))
            if int(rep) in [i[1] for i in B]:
                for i in range(len(data)):
                    A=[""]*(max(data.loc["num_etagere"])+1)
                    if data.loc[i,"num_batch"]==int(rep):
                            A[data.loc[i,"num_etagere"]]=data.loc[i,"etage"]
                            print("Supprimez l'étage "+ str(data.loc[i,"etage"])+ " de la l'étagère " +str(data.loc[i,"num_etagere"]))
                            data.loc[i,"num_batch"]=0
                    for j in range(len(A)):
                        et=""
                        for i in A[j]:
                              et+=str(i)+ " "
                        if et!="":
                             print("Dans l'étagère "+str(j)+" retirez les étages "+ et)
                              
        except:
            rep=""
     '''
    # print(data)
    dataframe_to_txt(data, folder/'assets/data/etageres.txt')


#taches_semaine()