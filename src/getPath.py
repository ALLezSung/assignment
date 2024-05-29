from pathlib import Path

class Model:
    '''
    该模型用于遍历文件夹下各个文件的文件名
    
    参数：
        PATH: raw_info文件夹路径
        
    方法：
        getFolders(): 获取raw_info下的文件夹列表
        getFiles(folders): 获取文件夹列表中，每个文件夹下各个文件的文件名
    '''
    tgPATH = Path('raw_info')

    def __init__(self, PATH: str):
        self.tgPATH = Path(PATH)

    def getFolders(self) -> list:
        '''
        获取目标路径下的文件夹列表

        返回：
            dirlist: 文件夹列表
        '''
        try:
            dirlist = [p.name for p in self.tgPATH.iterdir() if p.is_dir()]
            return dirlist
        except Exception as e:
            raise ValueError('请检查文件夹路径是否正确') from e

    def getFiles(self, folders: str | list) -> dict:
        '''
        获取文件夹列表中，每个文件夹下各个文件的路径

        参数：
            folders: 文件夹列表

        返回：
            namesDict: 字典，键为文件夹名，值为该文件夹下各个文件的路径
        '''
        folders = folders if isinstance(folders, list) else [folders]
        namesDict = {}
        limited_suffixs = ('.xlsx', '.xls')  # 限定文件后缀

        for folder in folders:
            folder_path = self.tgPATH / folder
            if folder_path.is_dir():
                files = folder_path.glob('*')
                files = [file for file in files if file.suffix in limited_suffixs]
                files = [str(file) for file in files]  # 将Path对象转换为字符串路径
                namesDict[folder] = files
            else:
                raise ValueError(f'{folder} 不是一个有效的文件夹')

        return namesDict