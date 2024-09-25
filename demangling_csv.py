
input_file = 'overall2_kern.csv'
input_dict_files = ['mobilenet_kern_list.csv','resnet_kern_list.csv', 'vgg_kern_list.csv', 'vit_kern_list.csv' ]

# 출력 파일 경로
output_file = 'overall_stats_conv.csv'

dem_dict = {}
# 파일 읽기
for input_dict_file in input_dict_files:
    with open(input_dict_file, 'r') as file:
        dict_lines = file.readlines()


    for line in dict_lines[1:]:
        eles = line.split(',')

        found = 0
        stidx = 0
        concat_str = ''
        csv_line = list()
        

        for ele in eles:
            if concat_str != '':
                concat_str += ','
            if found:
                if ele[-1] == '"':
                    concat_str += ele[:-1]
                    csv_line.append(concat_str)
                    concat_str = ''
                    found = 0
                else:
                    concat_str += ele
            else:
                if ele[0] == '"':
                    concat_str += ele[1:]
                    found = 1
                else:
                    concat_str += ele
                    csv_line.append(concat_str)
                    concat_str = ''
                
        dem_dict[csv_line[7]] = csv_line[9]

with open(input_file, 'r') as file:
    lines = file.readlines()


with open(output_file, 'w+') as file:
    pre_appname = ''
    header = lines[2]
    for line in lines:
        outline = line
        mangle_name = line.split(',')[0].split('-')[-1]
        appname = line.split(',')[0].split('/')[0]

        if pre_appname.split('.')[-1] == 'sh' and appname.split('.')[-1] == 'sh' and pre_appname != appname:
            file.writelines('\n' + header)
        pre_appname = appname

        if mangle_name in dem_dict:

            demangle_name = dem_dict[mangle_name] + '"'
            rep = line.replace(mangle_name, demangle_name)
            outline = '"' + rep
        file.writelines(outline)


