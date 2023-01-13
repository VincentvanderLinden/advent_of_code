#Cheating the dijkstra shizzle by construction a graph
library(igraph)
library(data.table)
#Read data
p <- readLines("q12.in")
#Split characters
p <- strsplit(p, "")
#Matrix
p <- t(matrix(unlist(p), nrow = max(sapply(p, length))))

#Store S and E position for later
start_coord <- paste(which(p == 'S', arr.ind = T), collapse = ".")
end_coord <- paste(which(p == 'E', arr.ind = T), collapse = ".")
#Make numeric matrix, replacing S with 0 and E with 26 (NB: 27 is wrong :'()
p <- apply(p, c(1, 2), FUN = function(x) {
  if (x %in% letters) {
    res <- which(letters == x)
  }
  else if (x == "S") {
    res <- 0 
  }
  else {
    res <- 26
  }
  return(res)
})

#Gunction to find valid adjacent coordinates per cell
find_adjacent_values <- function(matrix, current_row, current_col){
  #Current coords as string
  cur_coords <- paste(current_row, current_col, sep = ".")
  cur_val <- p[current_row, current_col]
  
  coords <- list()
  
  l <- p[current_row, max(current_col - 1, 1)]
  r <- p[current_row, min(current_col + 1, ncol(p))]
  u <- p[max(current_row - 1, 1), current_col]
  d <- p[min(current_row + 1, nrow(p)), current_col]
  
  if(l <= cur_val + 1) coords <- append(coords, list(c(current_row, max(current_col - 1, 1))))
  if(r <= cur_val + 1) coords <- append(coords, list(c(current_row, min(current_col + 1, ncol(p)))))
  if(u <= cur_val + 1) coords <- append(coords, list(c(max(current_row - 1, 1), current_col)))
  if(d <= cur_val + 1) coords <- append(coords, list(c(min(current_row + 1, nrow(p)), current_col)))
  
  #Dead end: 
  if (length(coords) > 0) {
    #Vector of coords
    found_coords <- apply(do.call(rbind, coords), 1, paste, collapse = ".")  
    #Remove reference to self
    found_coords <- found_coords[!found_coords %in% cur_coords]
    
    #Return dataframe
    return(data.frame(from = rep(cur_coords, length(found_coords)),
                      to = found_coords))
  }
}


coord_df <- data.table(from = NULL, to = NULL)
i <- 1
for (row in 1:nrow(p)){
  for(col in 1:ncol(p)){
    adj_coords <- find_adjacent_values(p, row, col)
    coord_df <- rbind(coord_df, adj_coords)
  } 
}
g <- graph_from_data_frame(coord_df)

#Part 1----
shortest_path <- shortest_paths(g, 
                                from = start_coord, 
                                to = end_coord, 
                                weights = NA)                               
#Answer:
length(shortest_path$vpath[[1]]) - 1

#Part 2----
#Just brute force all a's because the graph is quick
x <- lapply(apply(which(p == 1, arr.ind = T), 1, paste, collapse = "."), 
       function(x) {
         shortest_paths(g, 
                        from = x, 
                        to = end_coord, 
                        weights = NA)$vpath[[1]] 
       })
#Answer:
Reduce(min, lapply(x[sapply(x,length)>0], function(x) {length(x)- 1}))



