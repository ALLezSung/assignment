import conf
import code01
import code02
import code03


#从配置文件中读取路径
raw_PATH = conf.raw_PATH
op_PATH = conf.op_PATH

#建立对象
model = code01.Model(raw_PATH)

#第一部分代码
result01 = model.getFiles(model.getFolders())

#第二部分代码
Teams, Persons = code02.readExcel(result01)

#第三部分代码
code03.writeCsv(op_PATH, Teams = Teams, Members = Persons)
