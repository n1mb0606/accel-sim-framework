import re

# 입력 파일 경로
input_file = 'overall_stats.csv'
# 출력 파일 경로
output_file = 'overall_stats_conv.csv'

# 파일 읽기
with open(input_file, 'r') as file:
    content = file.read()

data = dict()
seperator = '----------------------------------------------------------------------------------------------------,'
outputs = content.strip(seperator).split(seperator)
print(outputs)

app_list = []
output_list = []

for i,output in enumerate(outputs[1:]):
    output = output.strip()
    lines = output.split('\n')

    if i == 0:
        for line in lines[2:]:
            app_name = line.split('/')[0]
            app_list.append(app_name)
            data[app_name] = {}
    
    else:
        output_name = lines[0].split(',')[0]
        output_name = output_name.split('=')[0].strip('\\s+').strip('\\s*')
        print(output_name)
        output_list.append(output_name)
        for line in lines[2:]:
            app_name = line.split('/')[0]
            value = line.split(',')[-1]
            data[app_name][output_name] = value

result = ''
result += 'output,'

for i, app in enumerate(app_list):
    result += app
    if i != (len(app_list) - 1):
        result += ','
result += '\n'

for output in output_list:
    result += output
    for app in app_list:
        result += ','
        result += data[app][output]
    result += '\n'

# CSV 파일로 출력
with open(output_file, 'w') as file:
    file.write(result)



