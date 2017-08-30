




movies = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
          ["Graham Chapman",
           ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]],
          "The Life of Brian","The Meanig of Life"]

def print_array(the_list,indent=False,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_array(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(each_item)

print_array(movies,True)

"""
if isinstance(movies[1],list):
    print("true")
else:
    print("false")
"""






    
