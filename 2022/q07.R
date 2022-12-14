library(dplyr)
library(stringr)

commands <- readLines("q07.in")

get_file_structure <- function(commands) {
  #Initialize
  file_size <- 0
  file_structure <- data.frame()
  #Add root/ for easier parsing
  current_path <- "root/"
  
  for (command in commands) {
    if (command == "$ cd /") next
    #Keep track of current directory
    if (grepl("\\$ cd ", command)) {
      #Get the path
      dir_name <- sub("\\$ cd ", "", command)
      if (dir_name == "..") {
        #Remove the last dir
        current_path <- sub("(?<=/)\\w*/$", "", current_path, perl = T)
      } else {
        current_path <- paste0(current_path, dir_name, "/")
      }
    }
    #Pick up command lines starting with a digit as these are files
    if (grepl("^\\d+", command)) {
      #Get the file sizes (delete everything after the space)
      file_size <- as.numeric(sub(" .*", "", command))
      #Add file size to current_path
      file_structure <- rbind(file_structure, 
                              data.frame(path = current_path, 
                                         size = file_size))
      #Add records to above directories if we are in a sub directory
      #Check depth
      if (stringr::str_count(current_path, "/") - 1 > 0){
        #Create paths for all above directories (parent paths) of current_path
        for (position in head(str_locate_all(current_path, "/")[[1]][, 1], - 1)) {
          #Add file size to parent paths
          file_structure <- rbind(file_structure, 
                                  data.frame(path = substr(current_path, 1, position), 
                                             size = file_size))
        }
      }
    }
  }
  return(file_structure)
}
#Part 1----
#Answer:
get_file_structure(commands) %>%
  group_by(path) %>%
  summarise(size = sum(size)) %>%
  filter(size <= 1e5) %>%
  summarise(size = sum(size))

#Part 2----
path_structure <- 
  get_file_structure(commands) %>%
  group_by(path) %>%
  summarise(size = sum(size)) 

#Calculate space to free up
total_space <- 7e7
needed_space <- 3e7
space_to_free_up <- 
  abs(
    total_space - 
    path_structure %>%
      filter(path == "root/") %>%
      pull(size) - 
    needed_space)

#Answer:
get_file_structure(commands) %>%
  group_by(path) %>%
  summarise(size = sum(size)) %>%
  filter(size >= space_to_free_up) %>%
  arrange(size) %>%
  top_n(-1) %>%
  select(size)
