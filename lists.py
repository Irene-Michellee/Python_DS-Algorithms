# Accesing elements in a list
list_a = ['phy','chem',1998,2000];
list_b = [1,2,3,4,5,6,7,8,9];
print("list_a[2] is:",list_a[2]);
print(list_b[2:7]);

#updating lists
print("updation");
print(list_a[1]);
list_a[1] = "math";
list_b.append("hello"); #append to add an element to the list
print(list_a);
print(list_b);

#Deleting lists
print("Deletion");
print(list_a[0]);
del list_a[0];
print(list_a);
list_b.remove(4);
print(list_b);

#length
print(len(list_a));
#concatenation
print(list_a + list_b);
#repetition
print(["hi!"]*4);
#iteration
list_c = ["aa",00,"bb",10];
for x in list_c:
    print(x);