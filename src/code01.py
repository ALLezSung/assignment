import os


class Model:
    '''
    该模型用于遍历文件夹下各个文件的文件名
    
    参数：
        PATH: raw_info文件夹路径
        
    方法：
        getFolders(): 获取raw_info下的文件夹列表
        getFiles(folders): 获取文件夹列表中，每个文件夹下各个文件的文件名
    '''
    tgPATH = r'raw_info'

    def __init__(self, PATH):
        self.tgPATH = PATH

    def getFolders(self) -> list:
        '''
        获取目标路径下的文件列表

        返回：
            dirlist: 文件列表
        '''
        try:
            dirlist = os.listdir(self.tgPATH)
            return dirlist
        except:
            raise ValueError('请检查文件夹路径是否正确')

    def getFiles(self, folders: str | list) -> dict:
        '''
        获取文件夹列表中，每个文件夹下各个文件的文件路径

        参数：
            folders: 文件夹列表

        返回：
            namesDict: 字典，键为文件夹名，值为该文件夹下各个文件的文件路径
        '''
        
        folders = folders
        #对folders进行修正
        if type(folders) != list:
            if type(folders) == str:
                folders = [folders]
            else:
                raise ValueError('请输入正确的文件夹列表')
        
        namesDict = {}
        limited_suffixs = ('.xlsx', '.xls') #限定文件后缀
        for _ in folders:
            _files = os.listdir(self.tgPATH + '/' + _)
            files = [f for f in _files if f.endswith(limited_suffixs)]
            files = [os.path.join(self.tgPATH, _, f) for f in files]
            namesDict[_] = files

        return namesDict
