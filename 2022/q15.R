#Part 1----
input <- readLines("q15.in")

grid_input <- data.frame(do.call(rbind, lapply(stringr::str_extract_all(input, "-?\\d+"), as.numeric)))
names(grid_input) <- c("sx", "sy", "bx", "by")

#Target row

get_fills_per_row <- function(input, target){
  #browser()
  n_b_on_target <- 
    input %>% 
    filter(by == target) %>% 
    select(bx, by) %>% unique %>% nrow
  
  n_s_on_target <- 
    input %>% 
    filter(sy == target) %>% 
    select(sx, sy) %>% unique %>% nrow
  
  #browser()
  #Dplyr fun
  input %>%
    rowwise %>%
    mutate(
      #Calculate Manhattan distance between signal and beacon
      dist_s_b = dist(rbind(c(sx, sy), c(bx, by)), method = "manhattan"), 
      #Set the target x coordinate (row)
      target = target, 
      #Calculate the distance in rows from the signal
      dist_to_signal_from_target = abs(target - sy)) %>%
    #Only select rows which will affect the target row
    filter((sy >= target & sy - dist_s_b <= target) | (sy <= target & sy + dist_s_b >= target)) %>%
    mutate(
      #Determine how many fills (#) there should be,
      #left and right from the y value of the signal
      n_fills = abs(dist_s_b - dist_to_signal_from_target), 
      #Determine which columns (y) are filled
      target_range_filled = list((sx - n_fills):(sx + n_fills))) %>%
    ungroup %>%
    summarise(answer = length(unique(unlist(target_range_filled))) - n_b_on_target - n_s_on_target)
}
#Answer
tictoc::tic()
get_fills_per_row(grid_input, 2e6)
tictoc::toc()
#0.61 sec elapsed

#Alternative approach using geometry, much faster
#Part 1----
input <- readLines("q15.in")

grid_input <- data.frame(do.call(rbind, lapply(stringr::str_extract_all(input, "-?\\d+"), as.numeric)))
names(grid_input) <- c("sx", "sy", "bx", "by")

library(sf)
library(ggplot2)
library(plotly)

#Create polygons
polys <- 
  grid_input %>%
  rowwise %>%
  mutate(dist_s_b = dist(rbind(c(sx, sy), c(bx, by)), method = "manhattan"), 
         poly = st_sfc(st_polygon(list(
           rbind(c(sx, sy - dist_s_b), 
                 c(sx + dist_s_b, sy), 
                 c(sx, sy + dist_s_b), 
                 c(sx - dist_s_b, sy), 
                 c(sx, sy - dist_s_b)))))) %>%
  st_sf

#Set target
target <- 2e6

#Create intersection line
line <- st_sfc(st_linestring(t(matrix(c(st_bbox(polys)$xmin, target, st_bbox(polys)$xmax, target), ncol = 2))))

#Answer
st_intersection(line, polys) %>% st_union %>% st_length

#bonusplot
ggplot() +
  geom_sf(data = polys, aes(color = "red", fill = "red", alpha = 0.01))  + 
  geom_sf(data = line)



#Part 2----

input <- readLines("q15.in")
grid_input <- data.frame(do.call(rbind, lapply(stringr::str_extract_all(input, "-?\\d+"), as.numeric)))
names(grid_input) <- c("sx", "sy", "bx", "by")

polys <- 
  grid_input %>%
  rowwise %>%
  mutate(dist_s_b = dist(rbind(c(sx, sy), c(bx, by)), method = "manhattan"), 
         poly = st_sfc(st_polygon(list(
           rbind(c(sx, sy - dist_s_b), 
                 c(sx + dist_s_b, sy), 
                 c(sx, sy + dist_s_b), 
                 c(sx - dist_s_b, sy), 
                 c(sx, sy - dist_s_b)))))) %>%
  st_sf

target <- 4e6
bounds <- 
  st_sfc(st_polygon(list(
    rbind(c(0, 0), c(target, 0), c(target, target), c(0, target), c(0,0)))))

# ggplot() +
#   geom_sf(data = polys, aes(color = "red", fill = "red"), alpha = 0.1)  + 
#   geom_sf(data = bounds, aes(alpha = 0), fill = NA)

hole_finder <- st_crop(st_union(polys), bounds) %>% st_coordinates 

#take the second shape in the coordinate list, it will be the hole
hole_coordinates <- st_centroid(st_sfc(st_polygon(list(hole_finder[hole_finder[, "L1"] == 2, 1:2])))) %>% 
  st_coordinates

#Answer: 
hole_coordinates[1] * 4e6 + hole_coordinates[2]


