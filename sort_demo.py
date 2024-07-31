l_list=[20,5,10,3,7]
l_list.sort(key=lambda x:x)
print("asscending order:::\n",l_list)  # ascending order
l_list.sort(key=lambda x:x,reverse=True)
print("descending order:::\n",l_list)  # ascending order

d1=[
    {"eid":102,"ename":"balu","esal":19000},
    {"eid":101,"ename":"arun","esal":21000},
    {"eid":103,"ename":"chandu","esal":17000}
]

d1.sort(key=lambda x:x["eid"])
print("\n",d1)
d1.sort(key=lambda x:x["eid"],reverse=True)
print("\n",d1)

l_str=["kamal","nani","suma","arun","bye"]
l_str.sort(key=lambda x:x)
print("sort\n")
print("\n",l_str)
print("sorted \n")
l_str2=sorted(l_str,key=lambda x:x)
print("\n",l_str2)

l_tuple=[(2,"balu",19),(1,"chandu",13),(3,"arun",27)]
l_t1=sorted(l_tuple,key=lambda x:x)
print("\n",l_t1)
l_t2=sorted(l_tuple,key=lambda x:x[1])
print("\n",l_t2)
l_t3=sorted(l_tuple,key=lambda x:x[2])
print("\n",l_t3)
sub_list=[[10,5,7],[1,2,3,4],[19,26]]
l_s1=sorted(sub_list,key=lambda x:x)
print("\n",l_s1)
l_s2=sorted(sub_list,key=lambda x:x[1])
print("\n",l_s2)
l_s3=sorted(sub_list,key=lambda x:len(x))
print("\n",l_s3)
l_s4=sorted(sub_list,key=lambda x:sum(x))
print("\n",l_s4)





