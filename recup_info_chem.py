#!/usr/bin/env python3

import os,sys,os.path,re

def login():
    
    #Demande de saisie du login pour l'accès au cluster
    print("Bonjour")
    print ("Attention : avant de démarrer l'analyse, merci de vérifier le nom des échantillons : \n\t--> Analyse en single end : echantillon_1.reste.fastq \n\t--> Analyse en paire end: echantillon1_1.reste.fastq et echantillon1_2.reste.fastq ")
    print("\t le _1 correspondra aux échantillons forward et _2 correspondra aux échantillons reverse")
    
    name=input("\nMerci de saisir votre login\n")
    
    return recup_info_chem(name)



def recup_info_chem(name):
    
    #Lecture des éléments dans le dossier présent sur le cluster pour le transcriptome denovo
    chemintranscript=input("Merci de préciser le chemin d'accès aux données pour la création du transcriptome denovo.\nLe chemin est présent sur l'onglet Site distant de Filezilla.\nATTENTION il ne doit contenir que les données à analyser\n")
    #Création d'un fichier récupérant les informations du chemin dans un fichier temporaire texte
    dir=f"ssh {name}@bioinfo-master1.ird.fr 'cd {chemintranscript};infochem=$(ls);touch denovo.txt;for i in $infochem\ndo\n\techo $i >> denovo.txt\ndone'"
    os.system (dir)
    
    #Récupération de ce fichier temporaire
    recup=f"ssh {name}@bioinfo-master1.ird.fr 'cat {chemintranscript}/denovo.txt' >> denovo.txt"
    os.system (recup)
    
    #Lecture des éléments dans le dossier présent sur le cluster pour les données à mapper
    print("\n###########################################################################################")
    chemindonnee=input("Merci de préciser le chemin d'accès aux données pour la création d'analyse.\nLe chemin est présent sur l'onglet Site distant de Filezilla.\nATTENTION il ne doit contenir que les données à analyser\n")
    #Création d'un fichier récupérant les informations du chemin dans un fichier temporaire texte
    dir=f"ssh {name}@bioinfo-master1.ird.fr 'cd {chemindonnee};infochem=$(ls);touch donnees.txt;for i in $infochem\ndo\n\techo $i >> donnees.txt\ndone'"
    os.system (dir)
    
    #Récupération de ce fichier temporaire
    recup=f"ssh {name}@bioinfo-master1.ird.fr 'cat {chemindonnee}/donnees.txt' >> donnees.txt"
    os.system (recup)
    
    #Suppression des fichiers temporaires sur le cluster
    supptranscr=f"ssh {name}@bioinfo-master1.ird.fr 'rm {chemintranscript}/denovo.txt'"
    suppdon=f"ssh {name}@bioinfo-master1.ird.fr 'rm {chemindonnee}/donnees.txt'"
    os.system (supptranscr)
    os.system (suppdon)
    
    #Récupération des chemins pour transferts fichiers et réécriture fichier 
    chemtrans=open('chemtranscrit.txt','w')
    chemtrans.write(chemintranscript)
    chemmapp=open('chemmapp.txt','w')
    chemmapp.write(chemindonnee)

    #Récupération du chemin contenant la base de données pour l'analyse BUSCO
    print("\n###############################################################################")
    BDD=input("Afin de permettre l'analyse BUSCO. Merci de donner le chemin ou se situe la base de données qui permettra l'analyse avec le fichier.\nExemple: home/dataset/liliopsida_odb10\n")
    #Création d'un fichier texte contenant le chemin
    chemBUSCO=open('cheminBUSCOBDD.txt','w')
    chemBUSCO.write(BDD)
    
    
    #Récupération du fichier sample contenant les conditions d'analyse des échantillons
    print('##################################################################################')
    print("Afin de permettre l'analyse de débuter les analyses d'expression différentielle :")
    print("Merci de préparer un fichier texte que vous appellerez sample.txt contenant le nom des échantillons, les répétitions")
    print("Ce fichier devra ressembler à l'exemble ci-dessous pour des données en pair-end:")
    print("\tBat_M\tBat_M_rep1\t/scratch/assemblage_\'votre login\'/Bat457_1.trimmed.fastq\t/scratch/assemblage_\'votre login\'/Bat457_2.trimmed.fastq")
    print("\tBat_M\tBat_M_rep2\t/scratch/assemblage_\'votre login\'/Bat458_1.trimmed.fastq\t/scratch/assemblage_\'votre login\'/Bat458_2.trimmed.fastq")
    print("\tBat_F\tBat_F_rep1\t/scratch/assemblage_\'votre login\'/Bat467_1.trimmed.fastq\t/scratch/assemblage_\'votre login\'/Bat467_2.trimmed.fastq")
    print("\tBat_F\tBat_F_rep2\t/scratch/assemblage_\'votre login\'/Bat468_1.trimmed.fastq\t/scratch/assemblage_\'votre login\'/Bat468_2.trimmed.fastq")
    print("...")
    print("Les données en single end ne contiendront que le chemin des échantillons forward (dans l'exemple Bat457_1.trimmed.fq)")
    print("Attention le fichier ne doit contenir aucune ligne supplémentaire tel qu'une ligne vide ")
    sample=input("\nMerci d'indiquer le chemin où se situe ce fichier sample.txt\n")
    #Création d'un fichier texte contenant le chemin
    sampletxt=open('chemsample.txt','w')
    sampletxt.write(sample)

    #Récupération de ce fichier
    recup=f"ssh {name}@bioinfo-master1.ird.fr 'cat {sample}/sample.txt' >> sample.txt"
    os.system(recup)
    

login() 



