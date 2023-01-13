input <- readr::read_file('q01.in')
a <- lapply(lapply(Reduce(sum, lapply(strsplit(input, split = '\\n\\n'), strsplit, '\\n')), as.numeric), sum)

#Part 1----
#Answer:
a[which.max(a)][[1]]

#Part 2----
#Answer:
sum(tail(unlist(a[order(unlist(a))]), 3))
