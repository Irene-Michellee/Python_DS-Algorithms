from array import *
arr_1 = array('i',[11,12,13,14,15]);
for x in arr_1:
    print("array:",x);

# Accessing elements
print (arr_1[0]);
print (arr_1[3]);

#Insertion operation
print("insertion");
arr_2 = array('i',[10,20,30,40,50,60]);
arr_2.insert (2,100);
for z in arr_2:
     print(z);

#Deletion operation
print("Deletion");
arr_3 = array('i',[1,2,3,4,5,6,7,8]);
arr_3.remove(7);
for u in arr_3:
    print(u);

#Search Operation
print("search");
arr_4 = array('i',[11,22,33,44,55]);
print(arr_4.index(44));

#Update operation
print("Updation");
arr_5 = array('i',[55,66,77,88,]);
arr_5[0] = 99;
for y in arr_5:
    print(y);