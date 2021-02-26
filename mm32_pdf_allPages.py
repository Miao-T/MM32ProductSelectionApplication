import camelot.io as camelot
import sys


def transform(m):
    # 逆向参数收集，将矩阵中的多个列表转换成多个参数，传给zip
    return list(zip(*m))


def modify_name(name):
    if (name == "W05") | (name == "W06") | (name == "W07") | (name == "L05") | (name == "L06") | (name == "L07"):
        name = name + 'x'
    return name


name = input("Chip Type:")
mm32_list = []
tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages='1-end', copy_text=['v'])
for index in range(tables.n):
    mm32_list += tables[index].data

product_series = []
product_core = []
product_Flash = []
product_RAM = []
product_package = []
product_temp = []
product_result = []

for index in range(len(mm32_list)):
    name = modify_name(name)
    if (mm32_list[index][0] == "MM32" + name):
        product_series.append(mm32_list[index][1])
        product_core.append(mm32_list[index][2])
        product_Flash.append(mm32_list[index][4])
        product_RAM.append(mm32_list[index][5])
        if name[0] == "W":
            product_package.append(mm32_list[index][len(mm32_list[index]) - 4])
            product_temp.append(mm32_list[index][len(mm32_list[index]) - 2])
        else:
            product_package.append(mm32_list[index][len(mm32_list[index]) - 3])
            product_temp.append(mm32_list[index][len(mm32_list[index]) - 1])

product_result.append(product_series)
product_result.append(product_core)
product_result.append(product_Flash)
product_result.append(product_RAM)
product_result.append(product_package)
product_result.append(product_temp)
product_result = transform(product_result)
product_result.insert(0, ['产品系列', '内核信息', 'Flash', 'RAM', '封装', '工作温度'])

if len(product_result) == 1:
    print("Please check the input chip type")
    sys.exit(0)

for index in range(len(product_result)):
    for index2 in range(len(product_result[index])):
        print(product_result[index][index2] + "        ", end="")
    print("")
