import config as conf
from getPath import Model
from excelProgram import readExcel
from csvProgram import writeCsv


#从配置文件中读取路径
raw_PATH = conf.raw_PATH
op_PATH = conf.op_PATH

#建立对象
model = Model(raw_PATH)

#第一部分代码
result01 = model.getFiles(model.getFolders())

#第二部分代码
Teams, Persons = readExcel(result01)

#第三部分代码
writeCsv(op_PATH, Teams = Teams, Members = Persons)