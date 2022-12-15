#Starting over :'(
library(data.table)
library(ggplot2)

#Helper function to plot the knots
plt_knots <- function(knots){
  lwr_x <- min(c(knots$x, -5))
  upr_x <- max(c(knots$x, 5))
  lwr_y <- min(c(knots$y, -5))
  upr_y <- max(c(knots$y, 5))
  
  p <- ggplot(data = knots[order(-knot)]) +
    geom_label(aes(x = x, y = y, label = knot), fill = "white") +
    scale_x_continuous(breaks = seq(lwr_x, upr_x, by = 1)) +
    scale_y_continuous(breaks = seq(lwr_y, upr_y, by = 1)) +
    expand_limits(x = c(lwr_x, upr_x), 
                  y = c(lwr_y, upr_y)) +
    theme(panel.grid.minor = element_blank()) + 
    theme(axis.ticks=element_blank(),
          axis.title.x=element_blank(),
          axis.title.y=element_blank(),
          legend.position="none",
          #panel.background=element_blank(),
          panel.border=element_blank(),
          panel.grid.minor=element_blank(),
          plot.background=element_blank()
    )
}

#Function to move the head
move_head <- function(dir){
  knots[knot == "H", `:=`(x = fcase(dir == "L", x-1, 
                                    dir == "R", x+1, 
                                    default = x),
                          y = fcase(dir == "D", y-1, 
                                    dir == "U", y+1, 
                                    default = y))]
}

#Function to move the knots
move_knot <- function(knot, dir, n_knots){
  prv_knot <- knot - 1
  #Get difference to previous knot
  coord_diff <- knots[prv_knot, .(x, y)] - 
                knots[knot, .(x, y)]
  #If previous knot is two steps away: 
  if(any(abs(coord_diff) == 2)){
    knots[knot, `:=`(x = fcase(#Diagonal move of previous knot, move to same column:
                               coord_diff$x > 0, x+1, 
                               coord_diff$x < 0, x-1, 
                               default = x),
                     y = fcase(#Diagonal move of previous knot, move to same column:
                               coord_diff$y > 0, y+1, 
                               coord_diff$y < 0, y-1, 
                               default = y))]
    # Store knot positions
    if(knot == n_knots + 2){
      #mwuhaha <<-
      knot_result <<- unique(c(knot_result, list(c(knots[knot]$x, knots[knot]$y))))
    }
  }
}

move_snake <- function(instructions, knots, n_knots) {
  for (row in 1:nrow(instructions)){
    dir <- instructions[row]$dir
    n <- instructions[row]$n
    print(paste0("Executing row ", row))
    for(step in seq(n)){
      move_head(dir)
      for(knot in c(3:(2+n_knots))){
        move_knot(knot, dir, n_knots)
      }
    }
    # ggsave(plt_knots(knots),
    #        filename = paste0("q09_gif/000000", ifelse(row<10, paste0("000", row), 
    #                                                   ifelse(row< 100, paste0("00", row), 
    #                                                   ifelse(row<1000, paste0("0", row), 
    #                                                   row))), ".png"), 
    #        dpi = 72)
  }
}

#Part 1 & 2--

instructions <- data.table::fread("q09.in", col.names = c("dir", "n"), 
                                  stringsAsFactors = F, 
                                  colClasses = list(character = 1, numeric = 2))
knots <- data.table(knot = c("S", "H", c(paste0("K", 1:9))), 
                              x = rep(0, 11), 
                              y = rep(0, 11))


#Answer 1:
#result will be filled from functions with <<-
knot_result <- list()
move_snake(instructions, knots, 1)
length(knot_result)
#Answer 2:
knot_result <- list()
move_snake(instructions, knots, 9)
length(knot_result)

#Bonus animation----
#(enable the ggsave line on line 75 first and create a directory q09_gif in your working directory)
#Then get a cup of coffee

# library(magick, lib.loc = "/data/workspace/dime/pkg_prd/") #You won't need the lib.loc
# library(magrittr)
# list.files(path = 'q09_gif/', pattern = '*.png', full.names = TRUE) %>% 
#   image_read() %>% # reads each path file
#   image_join() %>% # joins image
#   image_animate(fps = 25) %>% # animates, can opt for number of loops
#   image_write("q09.gif")
