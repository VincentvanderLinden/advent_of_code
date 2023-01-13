library(data.table)
library(dplyr)
library(tidyr)

##Part 1----
letter_numbers <- data.frame( l = c(letters, LETTERS), 
                              n = c(1:52))

ruk <- function(rucksack){
  str1 <- substr(rucksack, 1, nchar(rucksack)/2)
  str2 <- substr(rucksack, nchar(rucksack)/2+1, nchar(rucksack))
  common_letter <- intersect(strsplit(str1, '')[[1]], strsplit(str2, '')[[1]])
  return(subset(letter_numbers, l == common_letter)$n)
}

#Answer:
sum(sapply(readr::read_table("q03.in", col_names = "SJENKIE")$SJENKIE, ruk))

#Part 2----
all_sacks <- fread("q03.in", header = F, col.names = "rucksack")
all_sacks$rucksack <- strsplit(all_sacks$rucksack, "")
#Answer:
all_sacks %>%
  group_by(grp = ceiling(row_number()/3)) %>%
  summarise(l = Reduce(intersect, as.list(rucksack))) %>%
  ungroup %>%
  inner_join(letter_numbers) %>%
  select(n) %>%
  sum
