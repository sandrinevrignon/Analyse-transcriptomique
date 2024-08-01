#!/usr/bin/env python3

import os,sys,os.path


def fichier_analyse_diff():
    
    #Ouverture du fichier chemtranscrit et mise de l'information dans une variable
    chem= open("chemtranscrit.txt","r")
    for i in chem:
        chemin =i
    
    #Lecture du fichier d'analyse brut
    lect=open("analyse_cluster/analyse_diff.sh","r")
    
    #Création d'un fichier d'analyse bash copiant le fichier brut et contenant les modifications du chemin et des données 
    # demandées à l'utilisateur qui seront transférées ultérieurement sur le cluster
    diff= open("fich_modif_analyse/analyse_diffmodif.sh","w+")
    for j in lect:
        if j!="modifvariable\n":
            diff.write(j)
        else:
            if j=="modifvariable\n":
                diff.write(f"scp -r Expressiondif {chemin}\n")
    
        
fichier_analyse_diff ()