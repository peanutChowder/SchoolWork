def return_fold_indices(ti_len, num):
    fold_indices = [[] for i in range(num)]
    increment = ti_len // num 

    if ti_len % num != 0:
        increment += 1

    start = 0
    for i in range(num):
        for j in range(start, ti_len, increment):
            fold_indices[i].append(j)
        
        
        

a = [i for i in range(37)]
print(a)
return_fold_indices(len(a), 2)