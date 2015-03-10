### ABRAHAM MATHEW
### BN PRESENTATION
### DATA^3 CONFERENCE

## SET WORKING DIRECTORY
setwd("/Users/abraham.mathew/Other_Projects/BN_in_R/")

## IMPORT DATA
pth = "/Users/abraham.mathew/Other_Projects/BN_in_R/Data"
dat = read.csv(file.path(pth, "Tinder_Data.csv"))

## EXPLORE DATA:
str(dat)
head(dat, 10)
tail(dat)

## RECODE VARIABLE:
dat$Age[dat$Age <= 21] <- "18 to 21"
dat$Age[dat$Age >= 22 & dat$Age <= 26] <- "22 to 26"
dat$Age[dat$Age >= 27 & dat$Age <= 30] <- "27 to 30"
dat$Age[dat$Age >= 31] <- "31+"

## CHANGE VARIABLE MODE:
dat$Age <- as.factor(dat$Age)
dat$Pictures <- as.factor(dat$Pictures)
dat$Shared_Interest <- as.factor(ifelse(dat$Shared_Interest == 0, 0, 1))

## LEARN NETWORK STRUCTURE
library(bnlearn)
net <- hc(dat)
plot(net)
modelstring(net)
net

## HIGHLIGHT 'PICTURES' NODE AND RELATED ARCS 
plot(net, highlight = "Pictures")
## HIGHLIGHT 'PICTURES' NODE AND ITS MARKOV BLANKET
plot(net, highlight = c("Pictures", mb(net, "Pictures")))

##  ESTIMATE PARAMETERS (probability distribution)
fitted <- bn.fit(net, dat)
fitted

## HOW WELL DOES THE NETWORK FIT THE DATA
score(net, dat)

# STRENGTH OF THE ARCS
arc.strength(net, dat)

## CONDITIONAL PROBABILITY QUERIES
cpquery(fitted, (Liked_You=="Y"), TRUE)
cpquery(fitted, (Liked_You=="N"), TRUE)
cpquery(fitted, (Liked_You=="N"), (Pictures=="3" & Text=="N"))
cpquery(fitted, (Liked_You=="N"), (Pictures=="3" & Text=="Y"))

## EXAMPLE:
Train <- sample(1:nrow(dat), ceiling(nrow(dat)*2/3), replace=FALSE)
net = hc(dat[Train,])
plot(net)
fitted = bn.fit(net, dat[Train,])
fitted
pred = predict(fitted$Liked_You, dat[-Train,])  
cbind(pred, dat[-Train, "Liked_You"])    
accuracy <- table(pred, dat[-Train, "Liked_You"])
accuracy
sum(diag(accuracy))/sum(accuracy)



