def addtion(num1:int, num2:int)->int:
    return int(num1)+int(num2)

def alcohol(age:int)->bool:
    if age >= 16:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(alcohol(21))
    print(alcohol(13))