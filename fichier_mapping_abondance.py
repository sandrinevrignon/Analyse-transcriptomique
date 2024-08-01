#!/usr/bin/env python3

import os,sys,os.path


def fichier_mapping_abondance_PE():
    #Lecture du chemin contenant sample.txt et mise du chemin dans une variable
    sample=open("chemsample.txt","r")
    for i in sample:
        chemsample=i
        
    #Lecture du fichier contenant le chemin des données permettant la création du transcriptome denovo
    chem= open("chemtranscrit.txt","r")
    #Mise de l'information dans une variable
    for j in chem:
        chemin =j
        
    #Lecture du fichier contenant le chemin des données permettant le mapping
    chemmap=open("chemmapp.txt","r")
    #Mise de l'information dans une variable
    for l in chemmap:
        cheminmap=l
        
    #Lecture du fichier d'analyse brut
    lect=open("analyse_cluster/mapping_abondance.sh","r")
    
    #Création d'un fichier d'analyse bash copiant le fichier brut et contenant les modifications du chemin et des données 
    # demandées à l'utilisateur qui seront transférées ultérieurement sur le cluster
    mapping= open("fich_modif_analyse/mapping_abondancemodif.sh","w+")
    for k in lect:
        if k!="variablemodif\n" and k!="modifvariable\n" and k!="vmodif\n":
            mapping.write(k)
        else:
            if k=="variablemodif\n":
                mapping.write(f"scp -r {chemsample}/sample.txt assemblage_$SLURM_JOB_USER/\n")
            else:
                if k=="modifvariable\n":
                    mapping.write(f"scp -r Mapping {chemin}\n")
                else:
                    mapping.write(f"scp -r {cheminmap}/* assemblage_$SLURM_JOB_USER/\n")
    

        
        
        
fichier_mapping_abondance_PE()
