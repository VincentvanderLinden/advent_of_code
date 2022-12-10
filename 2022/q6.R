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