def dicotonomia_recursiva (tabla, t):
    i = 0
    j = len(tabla)-1
    if i > j:
        return "Ausente"
    else:
        m = (i+j)/2
        if tabla[m] == t:
            return m
        else:
            if tabla[m] < t:
            #Esto implica que tabla[m+1] ≤ t ≤ tabla[j] 
                return dicotonomia_recursiva (tabla[m+1:j], t)
            else:
            #Esto implica que tabla[i] ≤ t ≤ tabla[m–1] 
                return dicotonomia_recursiva (tabla[i:m-1], t)
