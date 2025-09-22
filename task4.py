List = ["apple","orange","banana","strawberry","cherry"]
List2 = [1,4,9,5,4,6,8,2,9,4]

print("************************")
print(List)
print("************************")
print(List2)
print("************************")


List2.append(16)
print(List2)

List.extend(["ooooo","ppppp"])
print(List)

List.insert(3,"mmmm")
print(List)



#List2.remove(3)
#print(List2)في هذه الحالة سوف يعطينا error لان 3 غير موجودة داخل القائمة

def remove_list(list):
    if list in List:
        List.remove(list)
        print(f"it has been deleted{list}.")
    else:
        print("non")

print(List2.pop())
print(List2.pop(3))

print(List.clear())

List2.index(9)
print(List2)

def count_list(List , value):
    if value >= 2:
        print(List.count(value))
    else:
        print("not found")
print(count_list(List2,4))
print(count_list(List2,1))

print(List2.sort())

print(List2.sort(reverse=True))


print(List2.copy())
print(List2.append(3))