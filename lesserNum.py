def lesser_of_even_num(a,b):
    
    if a%2==0 and b%2==0:
       return min(a,b)
        
    else:
        return max(a,b)


final_num = lesser_of_even_num(4,2)
print(final_num)
