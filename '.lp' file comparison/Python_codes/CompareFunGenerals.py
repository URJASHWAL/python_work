pathSpark = r'spark_gen.lp'
pathPy = r'py_gen.lp'

def compare_gen(paths):
    with open(paths, 'r') as f:
        file = f.readlines()
        file_join = "".join(file)
        file_set = set(file_join.split('\n'))
    return file_set

Sp= compare_gen(pathSpark)
Py= compare_gen(pathPy)
count_sp=len(Sp)-1
count_py=len(Py)-1
spset= Sp.difference(Py)
pyset= Py.difference(Sp)
print "Spark Values:",spset,"\n python values:",pyset,"\nSpark count:",count_sp,"\n Python count:",count_py
