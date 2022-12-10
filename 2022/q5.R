input <- readr::read_file("q5.in")

#Split stack and instructions
stack_text <- strsplit(input,"\n\n")[[1]][1]
instructions <- strsplit(input,"\n\n")[[1]][2]

#Preparation----
#Very nasty input handling to deal with this crap: 
#     [G]         [P]         [M]    
#     [V]     [M] [W] [S]     [Q]    
#     [N]     [N] [G] [H]     [T] [F]
#     [J]     [W] [V] [Q] [W] [F] [P]
# [C] [H]     [T] [T] [G] [B] [Z] [B]
# [S] [W] [S] [L] [F] [B] [P] [C] [H]
# [G] [M] [Q] [S] [Z] [T] [J] [D] [S]
# [B] [T] [M] [B] [J] [C] [T] [G] [N]
#  1   2   3   4   5   6   7   8   9 

#Split the stack rows by new line, drop last line
stack_lines <- head(strsplit(stack_text, "\n")[[1]], -1) 
#Add a space at the end to make processing by substring/regex easier
stack_lines <- lapply(stack_lines, paste0, " ")
#Get the letters from all rows by extracting every 4 characters and taking the second character
stack_lines <- lapply(sapply(stack_lines, stringr::str_extract_all, ".{4}"), substr, 2, 2)
#Convert to matrix with ncol boxes and nrow stack lines (every stack has equal length for now)
stack_matrix <- do.call(rbind, stack_lines)
#Replace spaces with NA
stack_matrix[stack_matrix == " "] <- NA
#Convert matrix to list, unname and drop na
stacks <- as.list(as.data.frame(stack_matrix, stringsAsFactors = F)) %>% unname %>% lapply(., na.omit) 
#Finally reverse the vectors to make it easier to popR
stacks <- lapply(stacks, rev)

#Read instructions from second part of input file. fread because why not
instructions <- data.table::fread(text = instructions, 
                                  header = F,
                                  col.names = c("x", "no_of_boxes", "y", 
                                                "from", "z", "to"))
#Part 1----
for (row in 1:nrow(instructions)){
  for(box in 1:instructions[row,]$no_of_boxes){
    stacks[[instructions[row,]$to]] <- c(stacks[[instructions[row,]$to]], 
                                         tail(stacks[[instructions[row,]$from]], 1))
    stacks[[instructions[row,]$from]] <- head(stacks[[instructions[row,]$from]], 
                                              length(stacks[[instructions[row,]$from]]) -1)
  }
}
#Answer:
paste0(lapply(stacks, tail, 1), collapse = "")

##Part 2----
for (row in 1:nrow(instructions)){
  stacks[[instructions[row,]$to]] <- c(stacks[[instructions[row,]$to]], 
                                       tail(stacks[[instructions[row,]$from]], 
                                            instructions[row,]$no_of_boxes))
  stacks[[instructions[row,]$from]] <- head(stacks[[instructions[row,]$from]], 
                                            length(stacks[[instructions[row,]$from]]) - 
                                              instructions[row,]$no_of_boxes)
}
#Answer:
paste0(lapply(stacks, tail, 1), collapse = "")
