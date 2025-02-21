import os

def f(start_path,search_pattern):
    file_or_folder = os.listdir(start_path)
    for ff in file_or_folder:
        new_path = os.path.join(start_path, ff)
        if os.path.isdir(new_path):
            f(start_path=new_path , search_pattern=search_pattern)
        else:
            if search_pattern in ff:
               print(new_path)

print(f(start_path="." , search_pattern=".py"))

test_dict={
    "key1": "value1",
    "key2": "value2",
    "key3":"value3"
   
}



"""
liste= os.listdir(path)

os.path.join(x,y)

os.path.isdir(path) 

os.path.exists(path)

os.makedirs(path)
"""