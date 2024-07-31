#!/usr/bin/env python3

#Importation des modules 
import os,sys,os.path
import subprocess
os.system("clear")


def execution():
    import recup_info_chem
    import verif_fichier
    if os.path.exists("donnees.txt") and os.path.exists("denovo.txt"):
        import verif_transcrit_analyse
        import Transfert_cluster
           
    

execution()
