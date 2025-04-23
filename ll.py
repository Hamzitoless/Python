for i in range(30):
    print(i, end='')

def check(num:float) -> None:
    if num <=50.0:
        print(" has passed")
    else:
        print("has not passed")
    return

def check_two(num:float) -> bool:
    if num <=50:
        return True
    else:
        return False

def area(radius: float) -> float:
    return 3.142 * (radius**2)

print(area(7.2))

def sum_i(x:float , y:float) -> float:
    return x + y
def sum_ii(x:float , y:float) -> float:
    return x + y
def sum_iii(x:float , y:float) -> float:
    return x + y
    

check(89.9)
check_two(45.7)

has_passed: bool = check_two(30.2)
print( has_passed)