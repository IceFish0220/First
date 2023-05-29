from openpyxl import Workbook
import yfinance as yf
from pandas import read_excel
import matplotlib.pyplot as plt
from datetime import datetime

yf.pdr_override()
nameTicker = '005930.KS'
start = "1990-01-01"
end = "2023-05-29"

downdown = yf.download(nameTicker,start, end)

write_wb = Workbook()
write_ws = write_wb.create_sheet('삼성전자')
write_ws = write_wb.active

downdown.to_excel('E:\\GIHUN\\vsvs\\SEstocks.xlsx')

dataframe = read_excel('E:\\GIHUN\\vsvs\\SEstocks.xlsx')
print(dataframe)

plt.plot(dataframe.Date, dataframe.Close, 'b', label='Samsung Electronics')
plt.show()