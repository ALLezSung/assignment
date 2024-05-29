import csv


def writeCsv(path: str, **contents: dict) -> None:
    '''
    将字典列表写入csv文件

    参数：
    path: 文件路径
    contents: 字典列表，字典的键为csv文件名，字典的值为字典列表

    返回：
    无
    '''

    for key, content in contents.items():
        op_path = path + '/' + key + '.csv' #将key作为csv的文件名
        with open(op_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=content[0].keys())
            writer.writeheader()
            writer.writerows(content)

        print(f'{key}写入成功')

    return None

