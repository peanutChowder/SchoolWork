import pickle 

# emp = {1: "A", 2: "B", 3: "C"}
# pickling_on = open("Emp.pickle", "wb")
# pickle.dump(emp, pickling_on)
# pickling_on.close()
data = """8003 7d71 0028 4b01 5801 0000 0041 7101
4b02 5801 0000 0042 7102 4b03 5801 0000
0043 7103 752e """

pickle.loads(data)
print(emp)