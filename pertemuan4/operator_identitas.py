a = 5
b = 5
print(a is b) #output: TRUE, kenapa? karena python baca b itu berarti manggil a


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)
print(list1 is not list2) #output: FALSE, kenapa? karena LIST itu sifatnya independent atau punya memory sendiri meskipun punya objek yang sama 


tuple1 = (1,2,3)
tuple2 = (1,2,3)
print(tuple1 is tuple2)  
print(tuple1 is not tuple2) #output: TRUE, kenapa? karena TUPLE itu semisal objeknya sama dan variabel nya beda hasilnya tetap True 


list1 = [1, 2, 3]
list2 = list1
list1.append(6)
print(list1, list2)
print(list1 is list2)





