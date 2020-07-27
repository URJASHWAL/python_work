with open('py_gen.lp', 'r') as f:
    Py = f.readlines()

with open('spark_gen.lp', 'r') as f:
    Sp = f.readlines()

Py1="".join(Py)
Py2=set(Py1.split('\n'))

Sp1="".join(Sp)
Sp2=set(Sp1.split('\n'))
Sp2
count_sp=len(Sp2)-1
count_py=len(Py2)-1
spset= Sp2.difference(Py2)
pyset= Py2.difference(Sp2)
print "Spark Values:",spset,"\n python values:",pyset,"\nSpark count:",count_sp,"\n Python count:",count_py
