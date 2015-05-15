craig = read.csv("C:/Users/Jay/Dropbox/Coding Projects/craigslist/craigTest1.csv")
craig$zipcode = as.factor(craig$zipcode)
lm1 = lm(price ~ beds + size)
lm2 = lm(price ~ beds + size + zipcode, data = craig)
lm3 = lm(price ~ beds + size + zipcode + numPic, data = craig)

#Test example prediction
predict(lm3, newdata = data.frame(beds = '3', size = 1560), type='response')

craig$zipcode = factor(craig$zipcode)
table(craig$zipcode)
craiglm = lm(price ~ beds + size + numPic + baths + zipcode, data = craig)
control = lm(price ~ beds + size, data = craig)
craigLm1 = lm(price ~ beds + size + zipcode + numPic, data = craig1000)
craigLm2 = lm(price ~ beds + size + zipcode, data = craig1000)
craigLm3 = lm(price ~ beds + size + zipcode*numPic, data = craig1000)
craigLm4 = lm(price ~ zipcode + beds*size, data = craig1000)
#Price is 2700
predict(test, newdata = data.frame(beds = 2, size = 1200, contentLen = 5, numPic = 7, baths = 2, zipcode = "98101"), type='response')
#Price is 4500
predict(craigLm1, newdata = data.frame(beds = 2, size = 1430, numPic = 11, zipcode = "98102"), type='response')
#Price is 1950
predict(craigLm1, newdata = data.frame(beds = 3, size = 1320, numPic = 15, zipcode = "98108"), type='response')

listNum = (tail(sort(table(craigClean$zipcode)), 40))
craigClean = craigClean[craigClean$zipcode %in% row.names(listNum),]

craigSeattle = craig[craig$zipcode %in% SeattleCode,]
craigSeattle$zipcode = factor(craigSeattle$zipcode)
table(craigSeattle$zipcode)
craigSeattlelm = lm(price ~ beds + size + numPic + baths + zipcode + contentLen, data = craigSeattle)
craigStand = lm(price ~ beds + size + baths + zipcode, data = craigStand)
summary(craigSeattlelm)
plot(density(resid(craigSeattlelm)))
qqnorm(resid(craigSeattlelm))

SeattleCode <- c("98177", "98133", "98125", "98117", "98103", "98115", 
                 "98107", "98105", "98199", "98119", "98109", "98102", 
                 "98112", "98121", "98101", "98122", "98104", "98134", 
                 "98144", "98116", "98126", "98136", "98106", "98108", 
                 "98118", "98154", "98164", "98174")

lm1CV = cv.lm(df = craigClean, form.lm = craigLm1, m = 2)

#Visualization

craigplot1=craigSeattle[craigSeattle$price < 5500, ]
bw <- diff(range(craigplot1$price)) / (2 * IQR(craigplot1$price) / length(craigplot1$price)^(1/3))
ggplot() + geom_histogram(aes(craigplot1$price), binwidth = bw)

# Aggregate beds together and calculate means
craigGrouping = aggregate(craigSeattle, list(craigSeattle$beds), mean)
craigGrouping = craigGrouping[craigGrouping < 5, ]
ggplot(data=craigGrouping, aes(x=Group.1, y=price, fill=Group.1)) + geom_bar(colour="black", stat="identity") 
  + guides(fill=FALSE) + xlab("Number of Bedrooms") + ylab("Price") + ggtitle("Average Price Per Number of Bedrooms") 
  + ylim(0, 5000)

#Aggregate beds together and calculate medians
craigGrouping = craigGrouping[,c("beds","price")]
craigGrouping = aggregate(craigGrouping, list(craigGrouping$beds), median)
ggplot(data=craigplot3, aes(x=beds, y=price, fill=city)) + 
  geom_bar(stat="identity", position='dodge', colour="black") + 
  scale_fill_manual(values=c("#999999", "#E69F00")) + 
  geom_text(aes(label=price, y = price + 300))
