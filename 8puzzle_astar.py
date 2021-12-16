def H_n(state, target):
    return sum(x != y for x, y in zip(state, target))      
def F_n(state_with_lvl):
    state, lvl = state_with_lvl
    return H_n(state, target) + lvl 
def astar(src, target, visited_states):
    arr = [[src, 0]]
    c = 0
    while arr:
        c += 1                                                
        min_f_n = min(arr,                                     
                      key=F_n)                                 
        print(min_f_n)                                         
        if min_f_n[0] == target:                               
            return 'Found with {} iterations'.format(c)
        visited_states.append(min_f_n[0])                      
        arr += possible_moves(min_f_n, visited_states)          
        arr.remove(min_f_n)
def possible_moves(state_with_lvl, visited_states): 
    state, lvl = state_with_lvl
    b = state.index(-1)                             
    d=[]                                           
    pos_moves=[]                                    
    if b<=5:                                        
        d.append('d')
    if b>=3 :                                       
        d.append('u')
    if b%3 > 0:                                     
        d.append('l')
    if b%3 < 2:                                      
        d.append('r')
    for i in d:                                     
        temp = gen(state, i, b)                     
        if temp not in visited_states:                                    
            pos_moves.append([temp, lvl+1])          
    return pos_moves                                 
def gen(state, m, b):                               
    temp=state.copy()                               
    if m == 'l':                                    
        temp[b], temp[b-1] = temp[b-1], temp[b]      
    if m == 'r':                                    
        temp[b], temp[b+1] = temp[b+1], temp[b]
    if m == 'u':                                    
        temp[b], temp[b-3] = temp[b-3], temp[b]
    if m =='d':                                     
        temp[b], temp[b+3] = temp[b+3], temp[b]
    return temp                                     
visited = []
src=[1,2,3,-1,4,5,6,7,8]
target=[1,2,3,4,5,-1,6,7,8]          
print(astar(src, target, visited))
