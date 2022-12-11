input <- readr::read_delim("q02.in", delim = " ", col_names = c("action", "reaction"))

#Part 1----
score_table <- data.frame(action = c(rep("A", 3), rep("B", 3), rep("C", 3)), 
                          reaction = rep(c("X", "Y", "Z"), 3), 
                          score = c(4, 8, 3, 1, 5, 9, 7, 2, 6 ))
#Answer: 
sum(merge(input, score_table)$score)

#Part 2----
score_table$score <- c(3, 4, 8, 1, 5, 9, 2, 6, 7 )
#Answer:
sum(merge(input, score_table)$score)
