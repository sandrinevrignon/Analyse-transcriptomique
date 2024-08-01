#!/bin/bash

############################Configuration SLURM#####################
# definir un nom de job
#SBATCH --job-name=trinity
#definir la partition 
#SBATCH -p highmem --nodelist=node27
#SBATCH -o fastqc.txt
#definir le nombre de coeurs à utiliser
#SBATCH -c 2
####################################################################

#Programmation de lancement du programme suivant 
sbatch --dependency=afterok:$SLURM_JOB_ID assemblage_trinitymodif.sh

#Acceder au répertoire
cd /scratch/

#Création d'un répertoire
mkdir assemblage_$SLURM_JOB_USER

#Transfert des données
variablemodif

#Aller dans le répertoire
cd assemblage_$SLURM_JOB_USER

#Chargement des modules
module load FastQC/0.11.9
module load multiqc/1.9

#Fastqc
mkdir Fastqc
fastqc -o Fastqc/ *.fastq

#multiqc
multiqc Fastqc
mv multiqc* Fastqc

#Transfert dans le dossier
modifvariable

