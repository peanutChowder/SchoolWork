import pickle

# open("a", "w")

# thing = {1: "A", 2: "B", 3: "C", 4: "D"}
# try:
#     pickling_on = open("thing.pickle", "wb")
# except:
#     print("fail")
# else:

#     pickle.dump(thing, pickling_on)
#     pickling_on.close() 

pickle_off = open("thing.pickle", "rb")
thing = pickle.load(pickle_off)
print(thing)



# import pickle
# emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}
# pickling_on = open("Emp.pickle","wb")
# pickle.dump(emp, pickling_on)
# pickling_on.close()