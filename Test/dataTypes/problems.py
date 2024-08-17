
student=[{"name":"raju","age":20},
         {"name":"radha","age":22},
         {"name":"balu","age":13},
         {"name":"meera","age":11},
         {"name":"rani","age":19},
         {"name":"meera","age":11},
         {"name":"rani","age":19}]

unique_list= {tuple(d.items())for d in student}
unique_student= [dict(d) for d in unique_list]
print(unique_student)



    
    

