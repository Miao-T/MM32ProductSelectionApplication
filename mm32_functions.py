import camelot.io as camelot
import os


def transform(m):
    # 逆向参数收集，将矩阵中的多个列表转换成多个参数，传给zip
    return list(zip(*m))


def merge_json():
    filedir ='json'
    #获取当前文件夹中的文件名称列表
    filenames=os.listdir(filedir)
    #打开当前目录下的result.json文件，如果没有则创建
    f=open('json/hhhhhe.json','w')
    #先遍历文件名`在这里插入代码片`
    for filename in filenames:
        filepath = filedir+'/'+filename
        #遍历单个文件，读取行数
        for line in open(filepath):
            f.writelines(line)
            f.write('\n')
    #关闭文件
    f.close()


def create_json():
    if os.path.exists("json/F0010_F0130.json") != 'true':
        tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='5', copy_text=['v'])
        tables[0].to_json("json/F0010_F0130.json")
    if os.path.exists("json/F0270_F3270.json") != 'true':
        tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='6', copy_text=['v'])
        tables[0].to_json("json/F0270_F3270.json")
    if os.path.exists("json/SPIN0280.json") != 'true':
        tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='7', copy_text=['v'])
        tables[0].to_json("json/SPIN0280.json")
    if os.path.exists("json/F003_F031_F103.json") != 'true':
        tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='8', copy_text=['v'])
        tables[0].to_json("json/F003_F031_F103.json")
    if os.path.exists("json/SPIN05_SPIN25_SPIN27.json") != 'true':
        tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='8', copy_text=['v'])
        tables[1].to_json("json/SPIN05_SPIN25_SPIN27.json")
    if os.path.exists("json/L05_L06_L07_L362_L373.json") != 'true':
        tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='9', copy_text=['v'])
        tables[0].to_json("json/L05_L06_L07_L362_L373.json")
    if os.path.exists("json/W05_W06_W07_W362_W373.json") != 'true':
        tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='9', copy_text=['v'])
        tables[1].to_json("json/W05_W06_W07_W362_W373.json")
