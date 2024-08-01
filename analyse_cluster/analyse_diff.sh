#!/bin/bash

############################Configuration SLURM#####################
# definir un nom de job
#SBATCH --job-name=trinity
#definir la partition 
#SBATCH -p highmem --nodelist=node27
#SBATCH -o analyse_diff.txt
#definir le nombre de coeurs à utiliser
#SBATCH -c 2
####################################################################

#Programmation de lancement du programme suivant 
sbatch --dependency=afterok:$SLURM_JOB_ID analyse_diffmodif.sh

#Accéder au répertoire
cd /scratch/assemblage_$SLURM_JOB_USER

#Création d'un fichier design.txt ne contenant que le nom des fichiers et les traitements
cut -f1,2 sample.txt > design.txt
#Déplacement de design.txt dans dossier Mapping contenant les analyses
mv design.txt mapping_abondance/Mapping/

#Déplacement dans dossier mapping_abondance
cd mapping_abondance/Mapping

#Création fichier expression
mkdir Expressiondif

#Chargement du module
module load singularity/
#Téléchargement du module
wget https://data.broadinstitute.org/Trinity/TRINITY_SINGULARITY/trinityrnaseq.v2.15.1.simg

#Estimation des seuils pour le comptage et le filtrage des transcrits
#   options utilisées:
#       -e: execution du script présent sur singularity
#       --E_inputs: Type du fichier utilisé 
singularity exec -e trinityrnaseq.v2.15.1.simg /usr/local/bin/util/misc/try_estimate_TPM_filtering_threshold.Rscript --E_inputs Trinity_trans.isoform.TMM.EXPR.matrix.by-transcript.E-inputs 
#Copie du plot obtenu dans le dossier Expressiondif
cp estimate_TPM_threshold.pdf Expressiondif

#Comptage du nombre de transcrits exprimés
#   option utilisée:
#       -e: execution du script présent sur singularity
singularity exec -e trinityrnaseq.v2.15.1.simg /usr/local/bin/util/misc/count_matrix_features_given_MIN_TPM_threshold.pl \
    Trinity_trans.isoform.TPM.not_cross_norm | tee trans_matrix.TPM.not_cross_norm.counts_by_min_TPM

#Création des plot MA et volcano plot
#   options utilisées:
#       -e: execution du script présent sur singularity
#       --matrix: matrice utilisée pour permettre l'analyse
#       --method: methode statistique utilisée (choix entre DeSeq2 et EdgeR)
#       --sample: Correspondance des échantillons en fonction du traitement
singularity exec -e trinityrnaseq.v2.15.1.simg /usr/local/bin/Analysis/DifferentialExpression/run_DE_analysis.pl \
  --matrix Trinity_trans.isoform.counts.matrix \
  --method DESeq2 \
  --samples design.txt

#Transfert dans dossier Expressiondif
mv DESeq* Expressiondif

#Transfert des données issues de l'analyse d'expression différentielle dans Expressiondif
mv Trinity_trans* Expressiondif/

#Transfert du dossier Expressiondif dans le dossier projet
modifvariable

#Suppression des données sur le noeud
cd ../../../
rm -rf assemblage_$SLURM_JOB_USER
