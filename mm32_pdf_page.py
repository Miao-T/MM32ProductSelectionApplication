import camelot.io as camelot
import sys
import fire


def page_selection(name):
    if (name == "F0010") | (name == "F0130"):
        page = 5
    elif (name == "F0270") | (name == "F3270"):
        page = 6
    elif (name == "SPIN0280") | (name == "SPIN_driver_mcu"):
        page = 7
    elif (name == "F003") | (name == "F031") | (name == "F103"):
        page = 8
    elif (name == "SPIN05") | (name == "SPIN25") | (name == "SPIN27"):
        page = 8
    elif (name == "L05") | (name == "L06") | (name == "L07") | (name == "L362") | (name == "L373"):
        page = 9
    elif (name == "W05") | (name == "W06") | (name == "W07") | (name == "W362") | (name == "W373"):
        page = 9
    elif name == "P021":
        page = 9
    else:
        page = -1
    return page


def transform(m):
    # 逆向参数收集，将矩阵中的多个列表转换成多个参数，传给zip
    return list(zip(*m))


def all_function(name):
    page = page_selection(name)
    if page == -1:
        print("Please Check the Input Validity")
        sys.exit(0)
    mm32_list = []
    tables = camelot.read_pdf("Mindmotion product selection manual.pdf", pages=str(page), copy_text=['v'])
    for index in range(tables.n):
        mm32_list += tables[index].data

    product_series = []
    product_core = []
    product_flash = []
    product_RAM = []
    product_package = []
    product_temp = []
    product_result = []

    if (name == "F0270") | (name == "F3270"):
        name = name[0:-1]
    length_name = len(name)

    for index in range(len(mm32_list)):
        if mm32_list[index][1][0:4 + length_name] == "MM32" + name:
            product_series.append(mm32_list[index][1])
            product_core.append(mm32_list[index][2])
            product_flash.append(mm32_list[index][4])
            product_RAM.append(mm32_list[index][5])
            if name[0] == "W":
                product_package.append(mm32_list[index][len(mm32_list[index]) - 4])
                product_temp.append(mm32_list[index][len(mm32_list[index]) - 2])
            else:
                product_package.append(mm32_list[index][len(mm32_list[index]) - 3])
                product_temp.append(mm32_list[index][len(mm32_list[index]) - 1])

    product_result.append(product_series)
    product_result.append(product_core)
    product_result.append(product_flash)
    product_result.append(product_RAM)
    product_result.append(product_package)
    product_result.append(product_temp)
    product_result = transform(product_result)
    product_result.insert(0, ['Product Series', 'Core', 'Flash', 'RAM', 'Package', 'Operation Temp'])

    for index in range(len(product_result)):
        for index2 in range(len(product_result[index])):
            print(product_result[index][index2] + "        ", end="")
        print("")


if __name__ == '__main__':
    fire.Fire(all_function)