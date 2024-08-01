#!/usr/bin/env python3

import os,sys,os.path


def fichier_analyse_qualite():
    
    #Création de variable
    chemin=""
    
    #Lecture du fichier contenant le chemin des données permettant la création du transcriptome denovo
    chem= open("chemtranscrit.txt","r")
    #Mise de l'information dans une variable
    for j in chem:
        chemin =j
    
    #Ouverture du fichier d'analyse bash brut 
    lect= open("analyse_cluster/fastqc.sh","r")
    
    #Création d'un fichier d'analyse bash copiant le fichier brut et contenant les modifications du chemin et des données 
    # demandées à l'utilisateur puis qui seront transférés ultérieurement sur le cluster
    qualite= open("fich_modif_analyse/fastqcmodif.sh","w+")
    for i in lect:
        #Ecriture des lignes ne contenant aucune des deux variables ci dessous
        if i!="variablemodif\n" and i!="modifvariable\n":
            qualite.write(i)
        else:
            #Modification de la variable variablemodif par chemin utilisateur
            if i=="variablemodif\n":
                qualite.write(f"scp -r {chemin}/* assemblage_$SLURM_JOB_USER/\n")
            else:
                #Modification de la variable modifvariable par chemin utilisateur
                if i=="modifvariable\n":
                    qualite.write(f"scp -r Fastqc {chemin} \n")
    


fichier_analyse_qualite()
