#!/usr/bin/env python3

import os,sys,os.path

def verif_analyse():
    #Définition variable stockage nom fichier
    analyseSE=0
    analysePE=0

    #lecture du fichier texte
    lect=open("denovo.txt","r")
    for i in lect:      
        #Definition des répétitions
        cut=i.split("_")
        repetition=cut[1]
        if repetition == "1":
            analyseSE=analyseSE+1
        else:
            if repetition=="2":
                analysePE=analysePE+1
            else:
                print("Merci de vérifier le nom des fichiers, puis relancer l'analyse")
                os.system('rm denovo.txt')
                os.system('rm cheminBUSCOBDD.txt')
                os.system('rm chemmapp.txt')
                os.system('rm chemsample.txt')
                os.system('rm chemtranscrit.txt')
                os.system('rm donnees.txt')
                os.system('rm sample.txt')
                
        
        #Lancement des analyses
    if analysePE>0 and analyseSE==0:
        import fichier_analyse_qualite
        import fichier_assemblage_trinity_SE 
        import fichier_analyse_metrique
        import fichier_mapping_abondance
        import fichier_matrice_Ex90N50
        import fichier_analyse_diff
    else:
        if analyseSE>0 and analysePE>0 and analysePE==analyseSE:
            import fichier_analyse_qualite
            import fichier_assemblage_trinity_PE
            import fichier_analyse_metrique
            import fichier_mapping_abondance
            import fichier_matrice_Ex90N50
            import fichier_analyse_diff
        else:
            print("Aucune analyse ne peut être lancer.\nMerci de vérifier qu'il ne manque pas un fichier à analyser")
            os.system('rm denovo.txt')
            os.system('rm cheminBUSCOBDD.txt')
            os.system('rm chemmapp.txt')
            os.system('rm chemsample.txt')
            os.system('rm chemtranscrit.txt')
            os.system('rm donnees.txt')
            os.system('rm sample.txt')
        
        
        
verif_analyse()
