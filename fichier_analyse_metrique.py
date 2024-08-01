#!/usr/bin/env python3

import os,sys,os.path


def fichier_analyse_metrique_PE():
    
    #Lecture du chemin contenant la base de données et intégration du chemin dans une variable
    BDD= open("cheminBUSCOBDD.txt","r")
    for j in BDD:
        Basedonnée=j.split("\n")
        newBDD=Basedonnée[0]
        #Récupération du nom du fichier à analyser
        dicofic=newBDD.split("/")
        nomfic=dicofic[-1]    
    
    
    #Ouverture du fichier d'analyse bash brut 
    lect= open("analyse_cluster/analyse_metrique.sh","r")

    #Création d'un fichier d'analyse bash copiant le fichier brut et intégrant les modifications utilisateurs
    metrique= open("fich_modif_analyse/analyse_metriquemodif.sh","w+")
    
    for i in lect:
        if i!="modifvariable\n" and i!="variablemodif\n":
            metrique.write(i)
        else:
            if i=="modifvariable\n":
                metrique.write(f"scp -r {newBDD} busco/{nomfic}")
            else:
                #options du programme:
                #   -i: fichier à analyser
                #   -m: type des données (transcriptome ou genome)
                #   -c: nombre de coeurs à utiliser pour l'analyse
                #   -o: nom de la sortie
                #   -l: base de données utilisée
                metrique.write(f"busco -i Trinity.fasta -m transcriptome -c 2 -o busco/busco_resultat -l busco/{nomfic}")

fichier_analyse_metrique_PE()
    
