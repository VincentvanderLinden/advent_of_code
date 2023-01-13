#Data prep for better handling
inst <- readLines("q10.in")
inst <- data.frame(inst, stringsAsFactors = F)
inst$n <- as.numeric(stringr::str_extract(inst$inst, " .*"))
inst$n[is.na(inst$n)] <- 1
inst$inst <- sub(" .*", "", inst$inst)
inst$cycles <- ifelse(inst$inst == "noop", 1, 2)
inst$cycle_sum <- cumsum(inst$cycles)
inst$x_helper <- cumsum(inst$n)


#Part 1----
cycle_no <- 1
X <- 1
sum_signal_strength <- 0

 for (i in 1:nrow(inst)) {
   for (cycle in seq(inst[i,]$cycles)) {
     cycle_no <- cycle_no + 1
     if (cycle == inst[i,]$cycles & inst[i,]$inst != "noop"){ 
       X = X + inst[i,]$n
     }
     print(paste0("cycle ", cycle_no, " complete, X is now ", X))
     if (cycle_no == 20 | cycle_no %% 40 == 20){
       print(paste0("CALCULATING SIGNAL STRENGTH: ", cycle_no * X))
       sum_signal_strength <- sum_signal_strength + cycle_no * X
     }
   }
 }
#Answer:
print(paste0("TOTAL SIGNAL STRENGTH: ", sum_signal_strength))

#Part 2----
cycle_no <- 1
X <- 1
CRT <- c()
for (i in 1:nrow(inst)) {
  for (cycle in seq(inst[i,]$cycles)) {
    CRT <- c(CRT, ifelse(cycle_no >= X & cycle_no <= X+2, "#", "."))
    if (cycle == inst[i,]$cycles & inst[i,]$inst != "noop"){ 
      X = X + inst[i,]$n
    }
    if(cycle_no %% 40 == 0) {
      cycle_no <- 1
    }
    else {
      cycle_no <- cycle_no + 1
    }
    
  }
}
cat(paste(stringr::str_extract_all(paste(CRT, collapse = ""), ".{40}")[[1]], collapse = "\n"))

