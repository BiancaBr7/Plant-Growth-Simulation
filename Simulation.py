import numpy as np
import random
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


class Soil:
    def __init__(self, seed, puffball):
        self.seed = seed
        self.puffball = puffball

column =100
row=100
field=[[Soil([],[]) for c in range(column)]for r in range(row)]

field[0][0].puffball.append(0)

def spread_seed(puff_row,puff_col):
    global field
    total_seed = 2000
    survive_seed = 75/1000*total_seed
    count=0
    while survive_seed!=0 and count<=100:
        random_row = random.randint(max(0,puff_row-9), min(puff_row+9,99))
        random_col = random.randint(max(0,puff_col-9), min(puff_col+9,99))
        if len(field[random_row][random_col].seed)<100:
            field[random_row][random_col].seed.append(0)
            survive_seed-=1
            count=0
        else:
            count+=1
        

def heat(field,T):
    
    data = np.array(field)

    sns.heatmap(data, cmap='viridis')

    plt.title(f"Day {T}")

    plt.savefig(f'Day {T}')

    plt.close()


area=[]

for T in range(25):
    area.append(0)
    time=75
    seed_map=[]
    num_map=[]
    for row in range(100):
        seed_map.append([])
        num_map.append([])
        for col in range(100):
            for puffball in field[row][col].puffball:
                spread_seed(row,col)
                field[row][col].puffball.remove(puffball)
            if T<=13:
                for seed in field[row][col].seed:
                        if seed<75:
                            field[row][col].seed.remove(seed)
                            field[row][col].seed.append(seed+15)
                        else:
                            field[row][col].seed.remove(seed)
                            field[row][col].puffball.append(0)
            if len(field[row][col].seed)+len(field[row][col].puffball)!=0:
                num_map[row].append(len(field[row][col].seed)+len(field[row][col].puffball))
                seed_map[row].append(1)
                
            else:
                seed_map[row].append(0)
                num_map[row].append(0)
        area[T]+=sum(seed_map[row])
    print(f"Day is {(T+1)*15}")
    heat(seed_map,(T+1)*15)
    heat(num_map,f"Num_{(T+1)*15}")
    
print(area)
