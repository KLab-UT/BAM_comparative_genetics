#install.packages("ggplot2",repos = "http://cran.us.r-project.org")
library("ggplot2")

stats <- read.csv("Gene_Proportions.csv")
meanProp <- stats$Mean.Prop
medProp <-stats$Med.Prop

bamA_proportion = 0.9815
tamA_proportion = 0.9889
secY_proportion = 0.9991



hist_plot <-ggplot(stats,aes(x=Mean.Prop)) +
  geom_histogram(aes(fill = Mean.Prop > .9815),
                 binwidth = 0.0015, show.legend = F) +
		 theme_classic() + 
		 scale_color_manual(values = c("gray", "gray")) +  # Change right values to black to bring 
		 scale_fill_manual(values = c("gray", "gray")) +   # shading to values greater than BamA concervancy back
      	         labs(x = "Sequence Conservation", y = "Number of Proteins") +
		 theme(axis.text = element_text(size = 18),  
                 axis.title = element_text(size = 20)) +
  
  # Adding Vertical lines to histogram
  geom_vline(aes(xintercept=bamA_proportion), color = "black") +
  geom_vline(aes(xintercept=tamA_proportion), color = "black")+
  geom_vline(aes(xintercept=secY_proportion),color = "black") +
  
  
  # Labeling vertical lines
  geom_text(aes(x=bamA_proportion,y = 100, label = "BamA")) +
  geom_text(aes(x=tamA_proportion,y = 110, label = "TamA")) +
  geom_text(aes(x=secY_proportion,y = 120, label = "SecY")) 
  
#Make the whole plot grey, 3 labeled black lines
  
  
hist_plot

n <- nrow(subset(stats, Mean.Prop > 0.9815))
prop_greater <- n / nrow(stats)
