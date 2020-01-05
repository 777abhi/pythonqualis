import pstats, cProfile
 
def f1(n1):
    f= [i**2 for i in range(1,n1)]
    return f
 
def f2(n2):
    g = (x**2 for x in range(1,n2))
    return g
 
cProfile.runctx("f1(n1)", globals(), {'n1':200001}, "Profile1.prof")
cProfile.runctx("f2(n2)", globals(), {'n2':200001}, "Profile2.prof")
 
s1 = pstats.Stats("Profile1.prof")
s1.strip_dirs().sort_stats("time").print_stats()    
 
s2 = pstats.Stats("Profile2.prof")
s2.strip_dirs().sort_stats("time").print_stats()