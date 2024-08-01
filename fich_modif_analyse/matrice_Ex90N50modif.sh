#!/bin/bash

############################Configuration SLURM#####################
# definir un nom de job
#SBATCH --job-name=trinity
#definir la partition 
#SBATCH -p highmem --nodelist=node27
#SBATCH -o matrice_Ex90N50.txt
#definir le nombre de coeur à utiliser
#SBATCH -c 2
####################################################################

#Programmation de lancement du programme suivant 
sbatch --dependency=afterok:$SLURM_JOB_ID matrice_Ex90N50modif.sh

#Accéder au répertoire
cd /scratch/assemblage_$SLURM_JOB_USER/mapping_abondance/Mapping/

#Chargement des modules
module load singularity/

#Construction de la matrice d'expression
#   Description des options
#       -e: script trinity utilisé pour estimer la matrice d'expression
#       --est_method: programme et méthode d'analyse utilisé
#       --out_prefix: Rajout d'un préfixe dans le nom du fichier en sortie d'analyse
#       --name_sample_by_basedir: nom de la colonne par nom de répertoire
#       --gen_trans_map: fichier de mapping gène-transcription utilisé. Ici aucun. 

singularity exec -e trinityrnaseq.v2.15.1.simg /usr/local/bin/util/abundance_estimates_to_matrix.pl \
    --est_method salmon \
    --out_prefix Trinity_trans \
    --name_sample_by_basedir \
    --gene_trans_map none \
	Bat_M_rep1/quant.sf \
	Bat_M_rep2/quant.sf \
	Bat_F_rep1/quant.sf \
	Bat_F_rep2/quant.sf
#Analyse Ex90N50 et sortie des statistique de Ex90
#   Description des options
#       -e: exécution du programme contenu dans trinity
singularity exec -e trinityrnaseq.v2.15.1.simg /usr/local/bin/util/misc/contig_ExN50_statistic.pl \
    Trinity_trans.isoform.TMM.EXPR.matrix ../../trinity_assemblage/Trinity.fasta transcript | tee ExN50.transcript.stat

#Création plot ExN50
#   Description des options
#       -e: exécution du programme contenu dans trinity
singularity exec -e trinityrnaseq.v2.15.1.simg /usr/local/bin/util/misc/plot_ExN50_statistic.Rscript ExN50.transcript.stat

#Copie des données dans dossier Ex90N50
mkdir Ex90N50
cp ExN50.transcript.stat Ex90N50
cp ExN50.transcript.stat.ExN50_plot.pdf Ex90N50

#Mise du dossier dans Qualite
mv Ex90N50 ../../trinity_assemblage/Qualite

#Transfert du dossier qualité sur le projet
scp -r ../../trinity_assemblage/Qualite /projects/medium/SahelpalmsRNAseq/Sandrine/essai_prog/jeu_assemblage/Assemblage
