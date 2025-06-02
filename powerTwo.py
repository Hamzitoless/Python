def power(base,exp):
    if(exp==1):
        return base
    else:   
        return base * power(base,exp-1)
#testing the function
    