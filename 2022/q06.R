str <- readr::read_file("q06.in")
input <- strsplit(str,"")[[1]]  

#Part 1----
#Add all characters to a vector. If the unique tail (ooooh, I'm a unicorn!) equals 4, jump out of the loop
get_marker <- function(input, no_of_unique_chars){
  characters <- c()
  loop_counter <- 1
  for(char in input){
    characters <- c(characters, char)
    if (length(unique(tail(characters, no_of_unique_chars))) == no_of_unique_chars) return(loop_counter)
    loop_counter <- loop_counter + 1
  }
}
#Answer:
get_marker(input, 4)

#Part 2-----
#Answer:
get_marker(input, 14)

