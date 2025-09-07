import pickle
file_path = "similarity.pkl"
with open(file_path,"rb") as f:
    data =pickle.load(f)
print(data)