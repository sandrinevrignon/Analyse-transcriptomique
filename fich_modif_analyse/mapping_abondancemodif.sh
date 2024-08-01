#!/bin/bash

############################Configuration SLURM#####################
# definir un nom de job
#SBATCH --job-name=trinity
#definir la partition 
#SBATCH -p highmem --nodelist=node27
#SBATCH -o mapping_abondance.txt
#definir le nombre de coeur à utiliser
#SBATCH -c 2
####################################################################

#Programmation de lancement du programme suivant 
sbatch --dependency=afterok:$SLURM_JOB_ID mapping_abondancemodif.sh

#Accéder au répertoire
cd /scratch

#Transfert du fichier sample.txt
scp -r /projects/medium/SahelpalmsRNAseq/Sandrine/sample.txt assemblage_$SLURM_JOB_USER/

#Transfert des fichier échantillons à mapper
scp -r /projects/medium/SahelpalmsRNAseq/Sandrine/essai_prog/jeu_map/* assemblage_$SLURM_JOB_USER/

#Accès au dossier
cd assemblage_$SLURM_JOB_USER

#Création du dossier d'analyse
mkdir mapping_abondance
cd mapping_abondance
mkdir Mapping
cd Mapping


#Chargement des modules
module load singularity/

#Installation du module trinity via singularity
wget https://data.broadinstitute.org/Trinity/TRINITY_SINGULARITY/trinityrnaseq.v2.15.1.simg

#Le fichier Trinity.fasta doit toujours être en chmod 755
#Création d'un index de Trinity fasta ainsi que du fichier contenant la
#   options utilisées:
#       -e: execution du script présent sur singularity
#       --transcripts: nom du fichier à indexer et type d'analyse (transcrits ou gène)
#       --seqType: type des données pour l'analyse d'abondance (fastq ou fasta)
#       --samples_file: fichier contenant les conditions d'analyse
#       --est_method: méthode d'analyse de l'abondance de chaque échantillon
#       --trinity_mode: mode d'analyse pour l'indexation
#       --outputdir: sortie des analyses
#       --prep_reference: nom du fichier de sortie regroupant l'ensemble des échantillons
singularity exec -e trinityrnaseq.v2.15.1.simg /usr/local/bin/util/align_and_estimate_abundance.pl --transcripts /scratch/assemblage_$SLURM_JOB_USER/trinity_assemblage/Trinity.fasta --seqType fq --samples_file /scratch/assemblage_$SLURM_JOB_USER/sample.txt --est_method salmon --output_dir /scratch/essai_vrignon/mapping_abondance/Mapping/ --trinity_mode --prep_reference

#Résumé du taux de mapping
grep 'Mapping rate =' */logs/salmon_quant.log >>resumemapping.txt
cd ..
#Transfert du fichier mapping sur le dossier projet
scp -r Mapping /projects/medium/SahelpalmsRNAseq/Sandrine/essai_prog/jeu_assemblage
