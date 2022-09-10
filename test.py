import pandas as pd
import numpy as np
from openpyxl import Workbook

a=np.arange(20).reshape(4,5)
b=pd.DataFrame(a)
print("b:\n",b)

print(f'0행 검색: \n {b.loc[0]}')

print(f'0~3행 : \n {b.loc[0:3]}')

print(f'0~1행의 0열 : \n {b.loc[0:1, 0]}')

print(f'모든 행의 0,1열 검색 : \n {b.loc[:,[0,1]]}')