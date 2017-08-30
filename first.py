




movies = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
          ["Graham Chapman",
           ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]],
          "The Life of Brian","The Meanig of Life"]

def print_array (the_list):
    for elem in the_list:
        if isinstance(elem,list):
            print_array(elem)
        else:
            print(elem)

print_array(movies)

"""
if isinstance(movies[1],list):
    print("true")
else:
    print("false")
"""



    
