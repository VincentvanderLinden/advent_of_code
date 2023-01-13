library(dplyr)

cubes <- readLines("q18.in") 

#Some data handling
cubes <- sapply(cubes, strsplit, ",") %>%
  do.call(rbind, .) %>%
  matrix(., nrow = length(cubes), ncol = 3) %>%
  as.data.frame(stringsAsFactors = F) 

names(cubes) <- c("x", "y", "z")

#Make numeric
cubes <- cubes %>%
  mutate(across(where(is.character), as.numeric)) 

#Create dataframes of neighbors per direction
#xy
xy_neighbours <- 
  cubes %>%
  inner_join(cubes, 
            by = c("x" = "x", 
                   "y" = "y"), 
            keep = T
  ) %>%
  #Filter neighbors
  filter(z.x == z.y - 1 | z.x == z.y + 1) %>%
  group_by(x.x, y.x, z.x) %>%
  #Count n_neighbors
  summarize(xy_neighbours = n()) %>%
  #Remove suffix
  rename_with(~ gsub(".x", "", .x))
#xz
xz_neighbours <- 
  cubes %>%
  inner_join(cubes, 
            by = c("x" = "x", 
                   "z" = "z"), 
            keep = T
  ) %>%
  #Filter neighbors
  filter(y.x == y.y - 1 | y.x == y.y + 1) %>%
  group_by(x.x, y.x, z.x) %>%
  #Count n_neighbors
  summarize(xz_neighbours = n()) %>%
  #Remove suffix
  rename_with(~ gsub(".x", "", .x))
#yz
yz_neighbours <- 
  cubes %>%
  inner_join(cubes, 
            by = c("y" = "y", 
                   "z" = "z"), 
            keep = T
  ) %>%
  #Filter neighbors
  filter(x.x == x.y - 1 | x.x == x.y + 1) %>%
  group_by(x.x, y.x, z.x) %>%
  #Count n_neighbors
  summarize(yz_neighbours = n()) %>%
  #remove suffix
  rename_with(~ gsub(".x", "", .x))

#Part 1 ----
#Answer:
#Left join all and subtract all neighbors from the 6 possible visible sides: 
cubes %>% 
  left_join(xy_neighbours) %>% 
  left_join(xz_neighbours) %>% 
  left_join(yz_neighbours) %>%
  rowwise %>%
  mutate(sides_visible = 6 - sum(xy_neighbours, xz_neighbours, yz_neighbours, na.rm = T)) %>%
  ungroup %>%
  mutate(is_on_outside = ifelse(x == max(x) | x == min(x) |
                                y == max(y) | y == min(y) |
                                z == max(z) | z == min(z), 
                                1, 0)) %>%
  arrange(x, y, z)
  summarise(answer = sum(sides_visible))