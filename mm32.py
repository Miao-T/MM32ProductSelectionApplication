import sys
import json

product_list = []
headList = ["Num","PartNO.","Core","Flash","RAM","Package","OperationTemp"]
gLen = 15
filename = "json/MM32SeriesTable.json"


def modify_name(name):
    if (name == "W05") | (name == "W06") | (name == "W07") | (name == "L05") | (name == "L06") | (name == "L07"):
        name = name + 'x'
    return name


def is_chinese(ch):
    if '\u4e00' <= ch <= '\u9fa5':
        return True
    else:
        return False


def len_str(string):
    count = 0
    for line in string:
        if is_chinese(line):
            count = count + 2
        else:
            count = count + 1
    return count


def search_json(name):
    name = modify_name(name)

    with open(filename) as f:
        pop_data = json.load(f)

    i = 0
    for pop_dict in pop_data:
        if pop_dict['Series'] == "MM32" + name :
            i = i + 1
            num_str = str(i) + "."
            partNO_str = pop_dict['PartNO']
            core_str = pop_dict['Core']
            flash_str = pop_dict['Flash']
            RAM_str = pop_dict['RAM']
            package_str = pop_dict['Package']
            temp_str = pop_dict['OperationTemp']
            product_dict = {
                "Num": num_str,
                "PartNO": partNO_str,
                "Core": core_str,
                "Flash": flash_str,
                "RAM": RAM_str,
                "Package": package_str,
                "Temp": temp_str
            }
            product_list.append(product_dict)


def show_result():
    name = input("Please Input the Chip Type:")
    search_json(name)
    if len(product_list) == 0:
        print("Please Check the Input Chip Type")
        sys.exit(0)
    head_str = "".join([x + " " * (gLen - len_str(x)) for x in headList])
    print(head_str)
    print("=" * 110)
    for product_dict in product_list:
        line_list = [product_dict["Num"], product_dict["PartNO"], product_dict["Core"], product_dict["Flash"], product_dict["RAM"], product_dict["Package"], product_dict["Temp"]]
        line_str = "".join([x + " " * (gLen - len_str(x)) for x in line_list])
        print(line_str)


if __name__ == '__main__':
    show_result()
    # fire.Fire(show_result)
