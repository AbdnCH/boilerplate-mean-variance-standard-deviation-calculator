import numpy as np

def calculate(list):
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")
    temp = np.array_split(list,3)
    calculations ={
        'mean':[np.mean(temp,axis=0).tolist(),np.mean(temp,axis=1).tolist(),np.mean(temp).tolist()],
        'variance': [np.var(temp,axis=0).tolist(),np.var(temp,axis=1).tolist(),np.var(temp).tolist()],
        'standard deviation': [np.std(temp,axis=0).tolist(),np.std(temp,axis=1).tolist(),np.std(temp).tolist()],
        'max': [np.max(temp,axis=0).tolist(),np.max(temp,axis=1).tolist(),np.max(temp).tolist()],
        'min': [np.min(temp,axis=0).tolist(),np.min(temp,axis=1).tolist(),np.min(temp).tolist()],
        'sum': [np.sum(temp,axis=0).tolist(),np.sum(temp,axis=1).tolist(),np.sum(temp).tolist()],
    }
    
    return calculations