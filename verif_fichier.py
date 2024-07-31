#!/usr/bin/env python3

import os,sys,os.path

def verif_fichier():
    #Définition variable stockage nom fichier
    infook=[]
    infopasok=[]
    infookmap=[]
    infopasokmap=[]
    comptficok=0
    comptficpasok=0
    comptficokmap=0
    comptficpasokmap=0
    
    #Analyse fichier denovo
    #lecture du fichier texte 
    lect=open("denovo.txt","r")
    print("################################Verification des fichiers#########################################")
    print("\nLes éléments présents dans le chemin permettant la création du transcriptome denovo sont:\n")
    for i in lect:
        nom_fic=i.split("\n")
        fichier=nom_fic[0]
        print(fichier)
               
        #Contrôle des fichiers par comptage et analyse de chaque élément
        controle=fichier.split(".")
        if controle[-1]=="fq" or controle[-1]=="fastq" or (controle[-1]=="gz" and controle[-2]=="fq") or (controle[-1]=="gz" and controle[-2]=="fastq"):
            infook.append(fichier)
            comptficok=comptficok+1
        else:  
            infopasok.append(fichier)
            comptficpasok=comptficpasok+1
    
    #Information utilisateur en fonction de l'analyse fichier
    if comptficok>0 and comptficpasok==0:
        print(f"\n{comptficok} fichiers vont être utilisés.\nCes fichiers sont les suivants:\n")
        for j in infook:
            print(f"\t-->{j}")
            lect.close()
        print("\n")
    else:
        if comptficok>0 and comptficpasok>0:
            print(f"\n{comptficok} fichiers peuvent être utilisés.\nCes fichiers sont les suivants:\n")
            for j in infook:
                print(f"\t-->{j}")
            print(f"\nCependant {comptficpasok} éléments ne doivent pas être présents dans le chemin.\nMerci de retirer les éléments suivants:\n")
            for k in infopasok:
                print(f"\t-->{k}")
            print("Merci de relancer l'analyse une fois les fichiers et dossiers non compatibles retirés")
            os.system('rm denovo.txt') 
        else:
            if comptficok==0 and (comptficpasok>0 or comptficpasok==0):           
                print("\nAucun élément ne peut être analysé.\nMerci de vérifier le chemin et relancer l'analyse")
                os.system('rm denovo.txt') 


    #Analyse fichier donnee
    #lecture du fichier texte 
    mapping=open("donnees.txt","r")
    print("\n#########################################################################################")
    print("\nLes éléments présents dans le chemin permettant l'analyse d'expression différentielle sont :\n")
    for i in mapping:
        nom_fic=i.split("\n")
        fichier=nom_fic[0]
        print(fichier)
               
        #Contrôle des fichiers par comptage et analyse de chaque élément
        controle=fichier.split(".")
        if controle[-1]=="fq" or controle[-1]=="fastq" or (controle[-1]=="gz" and controle[-2]=="fq") or (controle[-1]=="gz" and controle[-2]=="fastq"):
            infookmap.append(fichier)
            comptficokmap=comptficokmap+1
        else:  
            infopasokmap.append(fichier)
            comptficpasokmap=comptficpasokmap+1
    
    #Information utilisateur en fonction de l'analyse fichier
    if comptficokmap>0 and comptficpasokmap==0:
        print(f"\n{comptficokmap} fichiers vont être utilisés.\nCes fichiers sont les suivants :\n")
        for j in infookmap:
            print(f"\t-->{j}")
            mapping.close()
    else:
        if comptficokmap>0 and comptficpasokmap>0:
            print(f"\n{comptficokmap} fichiers peuvent être utilisés.\nCes fichiers sont les suivants :\n")
            for j in infookmap:
                print(f"\t-->{j}")
            print(f"\nCependant {comptficpasokmap} éléments ne doivent pas être présents dans le chemin.\nMerci de retirer les éléments suivants :\n")
            for k in infopasokmap:
                print(f"\t-->{k}")
            print("Merci de relancer l'analyse une fois les fichiers et dossiers non compatibles retirés")
            os.system('rm donnees.txt') 
        else:
            if comptficokmap==0 and (comptficpasokmap>0 or comptficpasokmap==0):           
                print("\nAucun élément ne peut être analysé.\nMerci de vérifier le chemin et relancer l'analyse")
                os.system('rm donnees.txt') 
   
verif_fichier()


