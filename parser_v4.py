import json
from pprint import pprint
def write_json(dictionary):
    with open("roz.json", "w", encoding= " utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent= 4)
   
def parser(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    decanat = {}

    for line in lines:
        if len(line) > 2:
            if ")" in line[1]:
                split_line = line[3:].split(",")
                village = split_line[0]
                decanat[village] = {}
                decanat[village]["церква"] = split_line[1]
                print(village)
            elif ")" in line[2]:
                split_line = line[4:].split(",")
                village = split_line[0]
                decanat[village] = {}
                decanat[village]["церква"] = split_line[1]
            elif ":" in line:

                line_split = line.split(":")
                pprint(line_split)
                decanat[village][line_split[0]] = line_split[1].replace("\n", '')
                pprint(line_split)
                pprint(decanat[village][line_split[0]])


    #write_json(decanat)
    return decanat


def parse_line(rubric_info: str):
    """
    formates line into list of lists to
    find data with ease
    """
    info = []
    line_without_semis = rubric_info.split(";")
    for semi in line_without_semis:
        line_without_comas = semi.split(",")
        for info_bit in line_without_comas:
            info_bit = info_bit.strip("\n")
            info_bit = info_bit.strip(".")
            info_bit_split = info_bit.split(" ")
            info.append(info_bit_split)
    return info

def parse_dict(decanat: dict)->dict:
    """
    parses dict
    key -> subkey -> info ->
    parse info
    :param dict decanat:

    :return dict
    
    """
    decanat_pure = decanat
    for village in decanat:
        for village_info in decanat[village]:
            #pprint(village_info)
            info = parse_line(decanat[village][village_info])
            if village_info == "Надає":
                pass
            elif village_info == "Завідатель":
                pass
            elif village_info == "Душ":
                decanat_pure[village][village_info] = {}
                for i in info:
                    i_len = len(i)
                    if i_len < 3:
                        decanat_pure[village][village_info][i[1]] = 0
                    elif "костел" or 'кост.' in i:
                        decanat_pure[village][village_info]["клер."] = " ".join(i[1:])
                    else:
                        pprint(i)
                        decanat_pure[village][village_info][i[1]] = int(i[2].replace(".",''))
                    pprint(i)
            elif village_info == "Дот.":
                decanat_pure[village][village_info] = {}
                
                for i in info:
                    building_type_key = i[1]
                    if building_type_key.isnumeric():
                        building_type_key = "undef."
                    decanat_pure[village][village_info][building_type_key] = {}
                    if building_type_key == "буд.":
                        decanat_pure[village][village_info][building_type_key] = i[2]
                    if "ha" in i:
                        #pprint(building_type_key)
                        line_index =  i.index("ha") - 1
                        ha = i[line_index]
                        try:
                            decanat_pure[village][village_info][building_type_key]["ha"] = int(ha)
                        except ValueError:
                            pass
                    if "a" in i:
                        #building_type_key = info_bit_split[1]
                        #pprint(building_type_key)
                        line_index =  i.index("a") - 1
                        a = i[line_index]
                        try:
                            decanat_pure[village][village_info][building_type_key]["a"] = int(a)
                        except ValueError:
                            pass
                    if "m2" in i:
                        #building_type_key = info_bit_split[1]
                        #pprint(building_type_key)
                        line_index =  i.index("m2") - 1
                        m2 = i[line_index]
                        try:
                            decanat_pure[village][village_info][building_type_key]["m2"] = int(m2)
                        except ValueError:
                            pass
            elif village_info == "Шк.":
                decanat_pure[village][village_info] = {}
                for i in info:
                    pprint(i)
                pass
            elif village_info == "Стар.":
                pass
            elif village_info == "Завідує":
                pass
            elif village_info == "Парох":
                pass
    write_json(decanat_pure)
    return decanat_pure
decanat = parser("wrks_with_parser\\file4.txt")
decanat_pure = parse_dict(decanat)
pprint(decanat_pure)