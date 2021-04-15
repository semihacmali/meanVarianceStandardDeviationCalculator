import numpy as np

def calculate(ls):
    
    msg = 'List must contain nine numbers.'    
    nLs = np.array(ls)
    try:
        nLs = nLs.reshape((3,3))
    except:
        raise ValueError(msg)

    calculations = dict()
    meanLs = []
    varLs = []
    sdLs = []
    maxLs = []
    minLs = []
    sumLs = []
    #calculation mean values
    meanLs.append(nLs.mean(axis = 0).tolist())
    meanLs.append(nLs.mean(axis = 1).tolist())
    meanLs.append(nLs.mean())
    
    
    #calcualtion variance values
    varLs.append(nLs.var(axis = 0).tolist())
    varLs.append(nLs.var(axis = 1).tolist())
    varLs.append(nLs.var())
   
    #calculation standart deviation values
    sdLs.append(nLs.std(axis = 0).tolist())
    sdLs.append(nLs.std(axis = 1).tolist())
    sdLs.append(nLs.std())
    
    #max values
    maxLs.append(nLs.max(axis = 0).tolist())
    maxLs.append(nLs.max(axis = 1).tolist())
    maxLs.append(nLs.max())
    
    #min
    minLs.append(nLs.min(axis = 0).tolist())
    minLs.append(nLs.min(axis = 1).tolist())
    minLs.append(nLs.min())
    
    #sum
    sumLs.append(nLs.sum(axis = 0).tolist())
    sumLs.append(nLs.sum(axis = 1).tolist())
    sumLs.append(nLs.sum())
    
    calculations = {
        'mean' : meanLs,
        'variance' : varLs,
        'standard deviation': sdLs,
        'max' : maxLs,
        'min' : minLs,
        'sum' : sumLs
        }
    return calculations