#!/usr/bin/env python3

import os,sys,os.path


def fichier_matrice_Ex90N50_PE():
    
    nomfic=[]
    #Ouverture du fichier sample.txt contenant les conditions d'analyse  
    sample=open('sample.txt','r')
    #Récupération dans un dictionnaire du nom des fichiers donnés à chaque échantillon lors du mapping
    for i in sample:
        sampledico=i.split("\n")
        newsample=sampledico[0]
        newsampledico=newsample.split('\t')
        fic=newsampledico[1]
        nomfic.append(fic)
    
    #Ouverture du fichier chemtranscrit et mise de l'information dans une variable
    chem= open("chemtranscrit.txt","r")
    for j in chem:
        chemin =j
    
    #Lecture du fichier d'analyse brut
    lect=open("analyse_cluster/matrice_Ex90N50.sh","r")
    
    #Création d'un fichier d'analyse bash copiant le fichier brut et contenant les modifications du chemin et des données 
    # demandédes à l'utilisateur qui seront transférées ultérieurement sur le cluster
    matrice= open("fich_modif_analyse/matrice_Ex90N50modif.sh","w+")
    for k in lect:
        if k!="variablemodif\n" and k!="modifvariable\n":
            matrice.write(k)
        else:
            if k=="modifvariable\n":
                for l in nomfic[:-1]:
                    matrice.write(f"\t{l}/quant.sf \\\n")
                matrice.write(f"\t{nomfic[-1]}/quant.sf")
            else:
                matrice.write(f"scp -r ../../trinity_assemblage/Qualite {chemin}/Assemblage\n")
    
    
        
        
        
fichier_matrice_Ex90N50_PE ()
