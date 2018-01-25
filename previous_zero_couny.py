import pandas as pd

l = [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
i = 0
r = []

for element in l:
    if element != 0:
        i += 1
    else:
        i = 0
    r.append(i)
    
    
result_data_frame = pd.DataFrame({"source":l,"result":r})

print(result_data_frame)
