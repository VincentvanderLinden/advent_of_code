library(data.table)
library(dplyr)
#Part 1----
pairs <- fread("q04.in", header = F, col.names = c("a", "b"))

magic <- pairs %>%
  rowwise %>%
  mutate(a = list(seq(as.numeric(sub("-.*", "", a)), as.numeric(sub(".*-", "", a)))), 
         b = list(seq(as.numeric(sub("-.*", "", b)), as.numeric(sub(".*-", "", b)))))

#Answer:
sum(mutate(magic, result = all(a %in% b) | all(b %in% a))$result)
#Part 2----
#Answer:
sum(mutate(magic, result = any(a %in% b) | any(b %in% a))$result)
