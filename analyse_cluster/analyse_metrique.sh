#!/bin/bash

############################Configuration SLURM#####################
# definir un nom de job
#SBATCH --job-name=trinity
#definir la partition 
#SBATCH -p highmem --nodelist=node27
#SBATCH -o analyse_metrique.txt
#definir le nombre de coeurs à utiliser
#SBATCH -c 2
####################################################################

#Programmation de lancement du programme suivant 
sbatch --dependency=afterok:$SLURM_JOB_ID mapping_abondancemodif.sh

#Accéder au répertoire
cd /scratch/assemblage_$SLURM_JOB_USER

###################################Analyse N50##########################################################

#Chargement du module
module load trinityrnaseq/2.5.1 
module load samtools/1.9
module load bowtie2/2.3.4.1

#Récupération du chemin d'accès au script présent dans le programme trinity
path_to_trinity=/usr/local/bioinfo/trinityrnaseq-2.8.5/

#Lancement du script afin d'obtenir les résultats de l'analyse N50 dans trinityStats.txt
$path_to_trinity/util/TrinityStats.pl /scratch/assemblage_$SLURM_JOB_USER/trinity_assemblage/Trinity.fasta > trinityStats.txt

#Mettre le fichier dans le dossier qualité
mv trinityStats.txt trinity_assemblage/Qualite/
cd trinity_assemblage


#Déchargement des modules
module purge

#################################Analyse BUSCO##############################################

#Chargement du module
module load busco/5.5.0

#Création d'un dossier
mkdir busco
cd busco
cd ..

#Récupération de la base de données
modifvariable

#Lancement de l'analyse
variablemodif

#déplacement du dossier dans le dossier qualité
cd busco
mv busco_resultat ../Qualite


