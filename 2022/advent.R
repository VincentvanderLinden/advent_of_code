input <- readr::read_file('/data/users/al9686/rommel/advent/q1.txt')
a <- lapply(lapply(Reduce(sum, lapply(strsplit(input, split = '\\n\\n'), strsplit, '\\n')), as.numeric), sum)
##Q1a----
a[which.max(a)]
##Q1b----
a[order(unlist(a))]

##Q2a----
input <- readr::read_delim('/data/users/al9686/rommel/advent/q2.txt', delim = ' ', col_names = c("action", "reaction"))

score_table <- data.frame (action = c(rep("A", 3), rep("B", 3), rep("C", 3)), 
                           reaction = rep(c("X", "Y", "Z"), 3), 
                           score = c(4, 8, 3, 1, 5, 9, 7, 2, 6 ))
sum(merge(input, score_table)$score)

##Q2b----
input <- readr::read_delim('/data/users/al9686/rommel/advent/q2.txt', delim = ' ', col_names = c("action", "outcome"))
score_table <- data.frame (action = c(rep("A", 3), rep("B", 3), rep("C", 3)), 
                           outcome = rep(c("X", "Y", "Z"), 3), 
                           score = c(3, 4, 8, 1, 5, 9, 2, 6, 7 ))
sum(merge(input, score_table)$score)

##Q3a----

SEKALON <- data.frame( l = c(letters, LETTERS), 
                       n = c(1:52))

ruk <- function(rucksack){
  str1 <- substr(rucksack, 1, nchar(rucksack)/2)
  str2 <- substr(rucksack, nchar(rucksack)/2+1, nchar(rucksack))
  common_letter <- intersect(strsplit(str1, '')[[1]], strsplit(str2, '')[[1]])
  
  return(subset(SEKALON, l == common_letter)$n)
}

a <- sapply(readr::read_table('/data/users/al9686/rommel/advent/q3.txt', col_names = "SJENKIE")$SJENKIE, 
            ruk)

sum(a)

##Q3a----

library(data.table)
library(dplyr)
library(tidyr)
all_sacks <- fread('/data/users/al9686/rommel/advent/q3.txt', header = F, col.names = "rucksack")
all_sacks$rucksack <- strsplit(all_sacks$rucksack, '')
all_sacks %>%
  group_by(grp = ceiling(row_number()/3)) %>%
  summarise(l = Reduce(intersect, as.list(rucksack))) %>%
  ungroup %>%
  inner_join(SEKALON) %>%
  select(n) %>%
  sum


         
##Q4a----
pairs <- fread('/data/users/al9686/rommel/advent/q4.txt', header = F, col.names = c("a", "b"))

magic <- pairs %>%
  rowwise %>%
  mutate(a = list(seq(as.numeric(sub("-.*", "", a)), as.numeric(sub(".*-", "", a)))), 
         b = list(seq(as.numeric(sub("-.*", "", b)), as.numeric(sub(".*-", "", b)))))

sum(mutate(magic, result = all(a %in% b) | all(b %in% a))$result)
##Q4b----
sum(mutate(magic, result = any(a %in% b) | any(b %in% a))$result)


##Q5a----

#     [G]         [P]         [M]    
#     [V]     [M] [W] [S]     [Q]    
#     [N]     [N] [G] [H]     [T] [F]
#     [J]     [W] [V] [Q] [W] [F] [P]
# [C] [H]     [T] [T] [G] [B] [Z] [B]
# [S] [W] [S] [L] [F] [B] [P] [C] [H]
# [G] [M] [Q] [S] [Z] [T] [J] [D] [S]
# [B] [T] [M] [B] [J] [C] [T] [G] [N]
#  1   2   3   4   5   6   7   8   9 

stacks <- list(
  c("B", "G", "S", "C"),
  c("T", "M", "W", "H", "J", "N", "V", "G"),
  c("M", "Q", "S"),
  c("B", "S", "L", "T", "W", "N", "M"),
  c("J", "Z", "F", "T", "V", "G", "W", "P"),
  c("C", "T", "B", "G", "Q", "H", "S"),
  c("T", "J", "P", "B", "W"),
  c("G", "D", "C", "Z", "F", "T", "Q", "M"),
  c("N", "S", "H", "B", "P", "F"))
#move 2 from 4 to 2
instructions <- data.table::fread("/data/users/al9686/rommel/advent/q5.txt", 
                                  header = F,
                                  col.names = c("x", "no_of_boxes", "y", 
                                                "from", "z", "to")
                                  )

for (row in 1:nrow(instructions)){
  for(box in 1:instructions[row,]$no_of_boxes){
    stacks[[instructions[row,]$to]] <- c(stacks[[instructions[row,]$to]], 
                                         tail(stacks[[instructions[row,]$from]], 1))
    stacks[[instructions[row,]$from]] <- head(stacks[[instructions[row,]$from]], 
                                              length(stacks[[instructions[row,]$from]]) -1)
  }
}
#ze answer:
paste0(lapply(stacks, tail, 1), collapse = "")

##Q5b----
for (row in 1:nrow(instructions)){
    stacks[[instructions[row,]$to]] <- c(stacks[[instructions[row,]$to]], 
                                         tail(stacks[[instructions[row,]$from]], 
                                              instructions[row,]$no_of_boxes))
    stacks[[instructions[row,]$from]] <- head(stacks[[instructions[row,]$from]], 
                                              length(stacks[[instructions[row,]$from]]) - 
                                                instructions[row,]$no_of_boxes)
}
#ze answer
paste0(lapply(stacks, tail, 1), collapse = "")

#Q6a----

str <- "nppdvjthqldpwncqszvftbrmjlhg"#readr::read_file("/data/users/al9686/rommel/advent/q6.txt")
input <- strsplit(str,"")[[1]]  

get_marker <- function(input){
  a <- list()
  i <- 1
  
  for(x in input){
    if(i <= 4){
      a <- append(a, x)
      i = i + 1
    }
    else {
      
      if(x %in% a){
        a <- list(x)
        super_i = i + 1
      }
      else {
        a <- append(a, x)
        i = i + 1 
      }
      if(length(a) == 4){
        return(super_i)
      }
    }
    
  }
}
get_marker(input)

