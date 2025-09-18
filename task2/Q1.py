print("welcome to GPA Calculator")

name=input("your name:")
print(f"Enter material tags,{name}:")

mat1=int(input("Enter grad 1:"))
mat2=int(input("Enter grad 2:"))
mat3=int(input("Enter grad 3:"))

res=(mat1 + mat2 + mat3)/3

def grad(res):
    if res >=85 and res<=100:
        return "excellent"
    elif res >=70 and res< 85:
        return"very good"
    elif res >= 50 and res<70:
        return"good"
    else :
        return"fail"

print(f"{name},your GPA is:{res:.2f}")
print("your grade is:",grad(res))