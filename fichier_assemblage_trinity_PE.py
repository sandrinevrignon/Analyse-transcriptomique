#!/usr/bin/env python3

import os,sys,os.path


def fichier_assemblage_trinity_PE():
    #Création de variable
    chemin=""
    donnees=""
    modifvariableleft=[]
    modifvariableright=[]
    
    #Lecture du fichier contenant le chemin des données permettant la création du transcriptome denovo
    chem= open("chemtranscrit.txt","r")
    #Mise de l'information dans une variable
    for j in chem:
        chemin =j
        
    #Lecture du fichier contenant les données à analyser
    donnees= open("denovo.txt","r")
    
    for i in donnees:
        #Mise des données dans des variables en fonction du sens (forward ou reverse) permettant l'analyse
        sens=i.split("_")
        if sens[1]=="1":
            #Enlèvement du saut de ligne sur les données
            donok=i.split("\n")
            donnew=donok[0]
            #Mise données dans une variable contenant les échantillons forwards
            modifvariableleft.append(donnew)
        else:
            #Enlèvement du saut de ligne sur les données
            donok=i.split("\n")
            donnew=donok[0]
            #Mise données dans une variable contenant les échantillons reverse
            modifvariableright.append(donnew)

    #Ouverture du fichier d'analyse bash brut 
    lect= open("analyse_cluster/assemblage_trinity.sh","r")
    
    #Création d'un fichier d'analyse bash copiant le fichier brut et contenant les modifications du chemin et des données 
    # demandées à l'utilisateur qui seront transférés ultérieurement sur le cluster
    assemblage= open("fich_modif_analyse/assemblage_trinitymodif.sh","w+")
    
    for k in lect:
        #Ecriture des lignes ne contenant aucune des variable ci-dessous
        if k!="modifvariableleft\n" and k!="modifvariableright\n" and k!="modifvariable\n" :
            assemblage.write(k)
        else:
            #Remplacement de la variable par les données échantillons forwards
            if k=="modifvariableleft\n":
                assemblage.write(f" --left {modifvariableleft[0]}")
                for l in modifvariableleft[1:]:
                    variableleft=l
                    assemblage.write(f",{variableleft} ") 
                assemblage.write('\\')  
                assemblage.write("\n")
            else:
                #Remplacement de la variable par les données échantillons reverse
                if k=="modifvariableright\n":
                    assemblage.write(f" --right {modifvariableright[0]}")
                    for m in modifvariableright[1:]:
                        variableright=l
                        assemblage.write(f",{variableright} ") 
                    assemblage.write('\\')  
                    assemblage.write("\n")
                else:
                    #Modification de la variable modifvariable par chemin user
                    assemblage.write(f"scp -r Assemblage {chemin} \n")
                    
   
    


fichier_assemblage_trinity_PE()
