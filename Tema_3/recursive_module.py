def full_sum(el):
    sum = 0
    for i in range(0,el+1):
        sum += i
    return sum

def even_element_sum(el):
    ev_sum = 0
    for i in range(0,el+1):
       if(i%2==0):
           ev_sum += i
    return ev_sum

def uneven_element_sum(el):
    un_sum = 0
    for i in range(0,el+1):
        if(i%2!=0):
            un_sum += i
    return un_sum