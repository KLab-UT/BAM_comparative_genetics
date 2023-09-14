library(ggplot2)

setwd('/Users/r_klabacka/OneDrive - Utah Tech University/KLab/Research/BAM_comparative_genetics')

dat <- read.csv('entero_stats.csv')

ggplot(dat, aes(x=Position, y=Proportion)) + geom_bar(stat="identity")

