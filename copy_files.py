# import json
# import sys
# with open('js_files_file.json') as f:
#     f = (json.load(f))
# for i in f:
#     if not i.endswith(('.js','.jsx','.css','ts','tsx')):
#         print(i)
# li = []
# with open('dir.txt','r',encoding='UTF-8') as f:
#     for line in f:
#         li.append(line.rstrip())
#
# with open('js_files_file.json','w') as f:
#     json.dump(li,f,indent=4)
#
import json
import shutil

with open('js_files_file.json') as f:
    list_files = json.load(f)

index = 0
mapping = {}
from tqdm import tqdm

for file in tqdm(list_files):
    shutil.copy(file, f'js_files/{index}.{file.split(".")[-1]}')
    mapping[index] = file
    index += 1

with open('file_to_index_mapping.json') as f:
    json.dump(mapping, f)
