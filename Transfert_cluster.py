#!/usr/bin/env python3

import os,sys,os.path

def transfert_cluster():
    #Demande information login user
    print("Les scripts permettant l'analyse vont être transferer sur le cluster\n")
    login=input("Merci de re-saisir votre login\n")
    
    #Transfert des scripts modifiés avec les informations utilisateurs
    transfertfastqc=f"scp fich_modif_analyse/fastqcmodif.sh {login}@bioinfo-master1.ird.fr:/home/{login}"
    os.system(transfertfastqc)
    
    transfertassemblage=f"scp fich_modif_analyse/assemblage_trinitymodif.sh {login}@bioinfo-master1.ird.fr:/home/{login}"
    os.system(transfertassemblage)
    
    transfertmetrique=f"scp fich_modif_analyse/analyse_metriquemodif.sh {login}@bioinfo-master1.ird.fr:/home/{login}"
    os.system(transfertmetrique)
    
    transfertmapping=f"scp fich_modif_analyse/mapping_abondancemodif.sh {login}@bioinfo-master1.ird.fr:/home/{login}"
    os.system(transfertmapping)
    
    transfertmatrice=f"scp fich_modif_analyse/matrice_Ex90N50modif.sh {login}@bioinfo-master1.ird.fr:/home/{login}"
    os.system(transfertmatrice)
    
    transfertanadif=f"scp fich_modif_analyse/analyse_diffmodif.sh {login}@bioinfo-master1.ird.fr:/home/{login}"
    os.system(transfertanadif)
    
    
    #Changement des droits d'accès aux fichiers
    chmodfastqc=f"ssh {login}@bioinfo-master1.ird.fr 'chmod 755 fastqcmodif.sh'"
    os.system(chmodfastqc)
    
    chmodassemblage=f"ssh {login}@bioinfo-master1.ird.fr 'chmod 755 assemblage_trinitymodif.sh'"
    os.system(chmodassemblage)
    
    chmodmetrique=f"ssh {login}@bioinfo-master1.ird.fr 'chmod 755 analyse_metriquemodif.sh'"
    os.system(chmodmetrique)
    
    chmodabondance=f"ssh {login}@bioinfo-master1.ird.fr 'chmod 755 mapping_abondancemodif.sh'"
    os.system(chmodabondance)
    
    chmodmatrice=f"ssh {login}@bioinfo-master1.ird.fr 'chmod 755 matrice_Ex90N50modif.sh'"
    os.system(chmodmatrice)
    
    chmodanadif=f"ssh {login}@bioinfo-master1.ird.fr 'chmod 755 analyse_diffmodif.sh'"
    os.system(chmodanadif)
    
    
    #Suppression des fichiers temporaires créés sur le bureau
    os.system('rm denovo.txt')
    os.system('rm cheminBUSCOBDD.txt')
    os.system('rm chemmapp.txt')
    os.system('rm chemsample.txt')
    os.system('rm chemtranscrit.txt')
    os.system('rm donnees.txt')
    os.system('rm sample.txt')

    #Lancement des analyses sur le cluster
    Lancementanalyse=f"ssh {login}@bioinfo-master1.ird.fr 'sbatch fastqcmodif.sh'"
    os.system(Lancementanalyse)
    print ("Les analyses sont maintenant en cours sur le cluster vous pouvez éteindre votre ordinateur et attendre que les analyses se terminent.")


transfert_cluster ()
    