def cube(x) :
    return x * x * x

print(cube(2))

l = [1,2,4,6,8]
# newl =[]
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube,l))
print(newl)

# FILTER
def filter_function(a):
    return a>1

newnewl = list(filter(filter_function , l))
print(newnewl)