import pickle

pentest = {"start": 1, "intermediate": 100, "advance": 1000}

for key, value in pentest.items(): # just print the dictionary value
    print(key, value)

serialization = pickle.dumps(pentest) #we can pass the pentest file into serialization manner
print(serialization)

pentest2 = pickle.loads(serialization) #now we can load the serialized data into new pentest2 variable
print(pentest2)

#with open("pentest.pickle", "wb") as handle: # to create a file such as pentest.pickle and write the serialized data
#   pickle.dump(pentest, handle)

with open("pentest.pickle", "rb") as handle:
    pentest3 = pickle.load(handle)
print(pentest3)