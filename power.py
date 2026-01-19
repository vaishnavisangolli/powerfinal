def power(base,exp):
    return base**exp
if __name__=="__main__":
    base=int(input("enter base:"))
    exp=int(input("enter exp:"))
    result=power(base,exp)
    print("power:",result)