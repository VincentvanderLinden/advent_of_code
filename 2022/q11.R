library(dplyr)
library(stringr)
#Part 1----
input <- readLines("q11.in")
input <- data.frame(do.call(rbind,
                            split(input,             
                                  ceiling(seq_along(input) / 7))), stringsAsFactors = F)
colnames(input) <- c("monkey", "starting_items", "operation", "test", "if_true", "if_false", "inspection_count")

input <- input %>%
  mutate(monkey = as.numeric(str_extract(monkey, "\\d+")),
         starting_items = lapply(str_extract_all(starting_items, '\\d+'), as.numeric, warn = F), 
         #Get the equation part, change old * old to **2 operation
         operation = str_replace(str_extract(operation, "(?<== old).*"), " old", "*2"), 
         test = as.numeric(str_extract(test, "\\d+")), 
         if_true = as.numeric(str_extract(if_true, "\\d+")), 
         if_false = as.numeric(str_extract(if_false, "\\d+")), 
         inspection_count = 0)

round <- 1
n_rounds <- 20

while(round <= n_rounds){
  print(round)
  for (row in seq(nrow(input))){
    #Make it easy on myself
    monkey = input[row, ]$monkey
    operation = input[row, ]$operation
    if_true = input[row, ]$if_true
    if_false = input[row, ]$if_false
    test = input[row, ]$test
    counter <- 1
    
    while(length(input[row, ]$starting_items[[1]]) > 0){
      item = input[row, ]$starting_items[[1]][1]
      # print("------------------------------------------------------------------------------------------------")
      # print(paste0("Monkey ", monkey, " is inspecting item ", item))
      #Raise inspection count
      input[row, ]$inspection_count <- input[row, ]$inspection_count + 1
      # print(paste0(monkey, "'s inspection count raised. It stands at ", input[row, ]$inspection_count))
      
      worry_level <- eval(parse(text = paste0(item, operation)))
      # print(paste0("Worry level for item ", item, " changed to: ", worry_level, ". Much wow, many afraid!"))
      worry_level <- floor(worry_level / 3)
      # print(paste0("Monkey gets bored and scratches its ass, worry level is now ", worry_level))
      # print(paste0("Monkey very smart monkey and tries to divide by ", test,
                   # ". The result is ", worry_level/test))
      if((worry_level/test)%%1 == 0){
        # print(paste0("'It's divisible by ", test, 
        #              "!', the monkey exclaimed. I'm going to throw it to monkey ", if_true))
        target_monkey <- if_true
      }
      else {
        # print(paste0("'I can't divide this by ", test, "! OEH OEH AAAH AAAH",  
        #              "!', the monkey exclaimed. I'm going to throw it to monkey ", if_false, 
        #              ". I hate that guy!"))
        target_monkey <- if_false
      }
      
      #Remove own item
      input[row, ]$starting_items[[1]] <- 
        tail(input[row, ]$starting_items[[1]], length(input[row, ]$starting_items[[1]]) - 1)
      
      #Throw that worrying item!
      input[input$monkey == target_monkey,  ]$starting_items[[1]][length(input[input$monkey == target_monkey,  ]$starting_items[[1]]) + 1] <- 
        worry_level
    }
  }
  round = round + 1
}
#Answer: 
input %>%
  top_n(2, wt = inspection_count) %>%
  summarize(monkey_business = prod(inspection_count))


#Part 2----
library(dplyr)
library(stringr)

input <- readLines("q11.in")
input <- data.frame(do.call(rbind,
                            split(input,             
                                  ceiling(seq_along(input) / 7))), stringsAsFactors = F)
colnames(input) <- c("monkey", "starting_items", "operation", "test", "if_true", "if_false", "inspection_count")

input <- input %>%
  mutate(monkey = as.numeric(str_extract(monkey, "\\d+")),
         starting_items = lapply(str_extract_all(starting_items, '\\d+'), as.numeric, warn = F), 
         #Get the equation part, change old * old to **2 operation
         operation = str_replace(str_extract(operation, "(?<== old).*"), " old", "*2"), 
         test = as.numeric(str_extract(test, "\\d+")), 
         if_true = as.numeric(str_extract(if_true, "\\d+")), 
         if_false = as.numeric(str_extract(if_false, "\\d+")), 
         inspection_count = 0)

round <- 1
n_rounds <- 10000
tictoc::tic()
while(round <= n_rounds){
  for (row in seq(nrow(input))){
    #Make it easy on myself
    monkey = input[row, ]$monkey
    operation = input[row, ]$operation
    if_true = input[row, ]$if_true
    if_false = input[row, ]$if_false
    test = input[row, ]$test
    counter <- 1
    
    while(length(input[row, ]$starting_items[[1]]) > 0){
      item = input[row, ]$starting_items[[1]][1]
      
      #Calculate worry_level
      worry_level <- eval(parse(text = paste0(item, operation)))
      
      
      #Keep it small
      worry_level <- ifelse(prod(input$test) < worry_level, 
                            worry_level%%prod(input$test), 
                            worry_level)

      if((worry_level/test)%%1 == 0){
        target_monkey <- if_true
      }
      else {
        target_monkey <- if_false
      }
      
      #Raise inspection count
      input[row, ]$inspection_count <- input[row, ]$inspection_count + 1
      #Remove own item
      input[row, ]$starting_items[[1]] <- 
        tail(input[row, ]$starting_items[[1]], length(input[row, ]$starting_items[[1]]) - 1)
      #Throw that worrying item in a worrying way!
      input[input$monkey == target_monkey,  ]$starting_items[[1]][length(input[input$monkey == target_monkey,  ]$starting_items[[1]]) + 1] <- 
        worry_level
    }
  }
  round = round + 1
}
tictoc::toc()
input %>%
  top_n(2, wt = inspection_count) %>%
  summarize(monkey_business = prod(inspection_count))

