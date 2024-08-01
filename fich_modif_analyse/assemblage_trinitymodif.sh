#!/bin/bash

############################Configuration SLURM#####################
# definir un nom de job
#SBATCH --job-name=trinity
#definir la partition 
#SBATCH -p highmem --nodelist=node27
#SBATCH -o assemblage_trinity.txt
#definir le nombre de coeurs à utiliser
#SBATCH -c 2
####################################################################

#Programmation de lancement du programme suivant 
sbatch --dependency=afterok:$SLURM_JOB_ID analyse_metriquemodif.sh

#Accéder au répertoire
cd /scratch/assemblage_$SLURM_JOB_USER

#Chargement du module
module load trinityrnaseq/2.5.1 
module load samtools/1.9
module load bowtie2/2.3.4.1

#Lancement programme
    #option seqType:Type de fichier à analyser fq/
    #max_memory: Mémoire max à utilisé 50G/ 
    #normalize_by_read_set: Normalisation individuelle de chaque paire limité à 200, puis combination finale des lectures normalisés individuelles/
    #left: Séquençage forward/ right: Séquençage reverse/
    #output: nom du fichier de sortie doit contenir le mot trinity

Trinity --seqType fq --max_memory 50G --normalize_by_read_set \
 --left Bat457_1_trimmed.fastq\
 --right Bat457_2_trimmed.fastq\
 --output trinity_assemblage

#Autorisation des fichiers à mettre obligatoirement en public lecture, écriture
chmod 777 trinity_assemblage
cd trinity_assemblage
#Changer les autorisations pour la suite des analyses
chmod 755 Trinity.fasta

#Création des fichiers à transférer
mkdir Assemblage
cd Assemblage
mkdir Données
cd ..
cp Trinity.fasta Assemblage/Données
mkdir Qualite
cp Trinity.timing Qualite

#Transfert du transcriptome denovo
scp -r Assemblage /projects/medium/SahelpalmsRNAseq/Sandrine/essai_prog/jeu_assemblage 

