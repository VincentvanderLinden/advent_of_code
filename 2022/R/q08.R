#Function to create matrix from textfile
matrix_from_txt <- function(txt){
  lines <- readLines(txt)
  #Determine number of columns and rows
  n_cols <- length(lines)
  n_rows <- max(unlist(lapply(lines, nchar)))
  
  #Create tree matrix
  m <- t(matrix(unlist(strsplit(lines, "")), 
                ncol = n_cols, 
                nrow = n_rows))
  class(m) <- "numeric"
  return(m)
}

#Part 1----
forest <- matrix_from_txt("q08.in")  
n_cols <- ncol(forest)
n_rows <- nrow(forest)
#Create result object with invisible (FALSE) trees
visible_forest <- t(matrix(rep(F, n_cols*n_rows), 
                           ncol = n_cols, 
                           nrow = n_rows))

#Loop through matrix                           
for(row in seq(n_rows)){
  for(col in seq(n_cols)){
    #Set perimeter to visible (TRUE)
    if(row %in% c(1, n_rows) | col %in% c(1, n_cols)){
      visible_forest[row, col] <- T
    }
    #Check up, down, left, right respectively for lower values
    else if(max(forest[1:(row-1), col]) < forest[row, col] |
            max(forest[(row+1):n_rows, col]) < forest[row, col] |
            max(forest[row, 1:(col-1)]) < forest[row, col] |
            max(forest[row, (col+1):n_cols]) < forest[row, col]) {
      visible_forest[row, col] <- T
    }
    col <- col + 1
  }
  row <- row + 1
}

#Answer:
sum(visible_forest)

#Part 2----
forest <- matrix_from_txt("q08.in")
class(forest) <- "numeric"
n_cols <- ncol(forest)
n_rows <- nrow(forest)
res <- 0
for(row in seq(n_rows)){
  for(col in seq(n_cols)){
    #Catch perimeters
    if(col %in% c(1, n_cols) | row %in% c(1, n_rows)){
      #Set variables to 0 for perimeters
      if(col == 1)      left <- 0
      if(col == n_cols) right <- 0
      if(row == 1)      up <- 0
      if(row == n_rows) down <- 0
    }
    else {
      #left
      if(any(which(forest[row, 1:(col-1)] >= forest[row, col]))){
        #there be a blocking tree on the left, check which one
        left <- col - max(which(forest[row, 1:(col-1)] >= forest[row, col]))
      }
      else left <- col-1
      #right
      if(any(which(forest[row, (col+1):n_cols] >= forest[row, col]))){
        #there be a blocking tree on the right, check which one
        right <- min(which(forest[row, (col+1):n_cols] >= forest[row, col]))
      }
      else right <- n_cols-col
      #up
      if(any(which(forest[1:(row-1), col] >= forest[row, col]))){
        #there be a blocking tree up from this tree, check which one
        up <- row - max(which(forest[1:(row-1), col] >= forest[row, col]))
      }
      else up <- row-1
      #down
      if(any(which(forest[(row+1):n_rows, col] >= forest[row, col]))){
        #there be a blocking tree down from this tree, check which one
        down <- min(which(forest[(row+1):n_rows, col] >= forest[row, col]))
      }
      else down <- n_rows-row
      #Put the highest product in res
      res <- max(res, left*right*down*up)
    }
    col <- col+1
  }
  row <- row + 1
}
#Answer:
res
