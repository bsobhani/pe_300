def contains_duplicate(L):
    for i in range(len(L)):
        if L[i] in L[:i]:
            return True
    return False

def add_to_list(L):
    Ls = []
    a = L[-1]
    for i in range(4):
        if i==0:
            candidate = L+[(a[0],a[1]+1)]
            #Ls.append(L+[(a[0],a[1]+1)])
            if contains_duplicate(candidate) == False:
                Ls.append(candidate)
            if len(L) == 1:
                return Ls
        if i==1:
            candidate = L+[(a[0],a[1]-1)]
            #Ls.append(L+[(a[0],a[1]-1)])
            if contains_duplicate(candidate) == False:
                Ls.append(candidate)
        if i==2:
            candidate = L+[(a[0]+1,a[1])]
            #Ls.append(L+[(a[0]+1,a[1])])
            if contains_duplicate(candidate) == False:
                Ls.append(candidate)
        if i==3:
            candidate = L+[(a[0]-1,a[1])]
            #Ls.append(L+[(a[0]-1,a[1])])
            if contains_duplicate(candidate) == False:
                Ls.append(candidate)
    return Ls

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5

def elem_lists(N):
    if N==1:
        return [['H'],['P']]
    pel = elem_lists(N-1)
    pelh = [pe + ['H'] for pe in pel] 
    pelp = [pe + ['P'] for pe in pel]
    return pelp + pelh

def calc_distances(L):
    ones = []
    for i in range(len(L)):
        for j in range(i,len(L)):
            if i == j:
                continue
            d = dist(L[i],L[j])
            if d == 1:
                ones.append((i,j))
    return ones

def elem_contact_points(ones,Le):
    count = 0
    for i in range(len(ones)):
        if Le[ones[i][0]] != 'H':
            continue
        if Le[ones[i][0]] == Le[ones[i][1]]:
            count += 1
    return count

L = [(0,0)]
Ls = add_to_list(L)
print(Ls)
def add_to_list2(Ls):
    Ls2 = []
    for i in range(len(Ls)):
        Ls2 += add_to_list(Ls[i])
    return Ls2

list4 = add_to_list2(add_to_list2(Ls))

bad_lists=[]
for i in range(len(list4)):
    if contains_duplicate(list4[i]):
        bad_lists.append(i)
        #print(i,list4[i])

list4 = [list4[i] for i in range(len(list4)) if i not in bad_lists]
print(list4)
#print(calc_distances(list4[0]))
for l in list4:
    #print(len(calc_distances(l)))
    print(elem_contact_points(calc_distances(l),['H','P','H','H']))
print(elem_lists(3))

def good_lists(N):
    Ls = add_to_list(L)
    #list4 = add_to_list2(add_to_list2(Ls))

    for i in range(N-2):
        Ls = add_to_list2(Ls)

    bad_lists=[]
    for i in range(len(Ls)):
        if contains_duplicate(Ls[i]):
            bad_lists.append(i)
            #print(i,list4[i])
    

    Ls = [Ls[i] for i in range(len(Ls)) if i not in bad_lists]

    return Ls

def optimal_sol(N):
    el = elem_lists(N)
    gl = good_lists(N)
    #cd = [calc_distances(l) for l in gl]
    max_sols = []
    for e in el:
        max_sol = 0
        for l in gl:
            sol = elem_contact_points(calc_distances(l),e)
            if sol > max_sol:
                max_sol = sol
        max_sols.append(max_sol)
    return max_sols


#print(good_lists(5))
N=8
for N in range(2,16):
    sos = sum(optimal_sol(N))
    print(N,sos,sos/(2**N))
