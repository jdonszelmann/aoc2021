
print("part 1: {}\npart 2: {}".format(*(lambda f,inp:(f(inp),f([sum(inp[i:i+3]) for i in range(len(inp))])))(lambda lst:len(list(filter(lambda x:x[0]<x[1],zip(lst,lst[1:])))),[int(i)for i in open("input.txt").readlines() if i!=""])))


