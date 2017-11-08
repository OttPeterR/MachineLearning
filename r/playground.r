# run r files like this:
# r < myFile.r --no-save

# r REPL
# q() to quit

# basic variables
# set values with the "<-" operator
a<-5
b<-10
c<-a+b

# vector
# the c command combines elements into a vector
# does not have to be a homogeneous datatype
v <- c(1,2,3)

# lists
# they can hold whatever you want
# does not have to be a homogeneous datatype
# r is 1-indexed, so list1[2] is FALSE
list1 <- list( "this is a list", FALSE, c(1,2,3), 12.34, sin)

# matricies
# only allowed two dimensions and must be rectangular
m = matrix( c(1,2,3,4,5,6), nrow=2, ncol=3, byrow=TRUE)
# results in a matrix like so:
#  1  2  3
#  4  5  6

# arrays
# take note of the dimension parameter, this will output:
# , , 1
#
#      [,1] [,2] [,3] [,4] [,5] [,6]
# [1,]    1    3    5    2    4    1
# [2,]    2    4    1    3    5    2
# 
# , , 2
#
#      [,1] [,2] [,3] [,4] [,5] [,6]
# [1,]    3    5    2    4    1    3
# [2,]    4    1    3    5    2    4
a <- array(c(1,2,3,4,5), dim = c(2,6,2))
