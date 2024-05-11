# import fileinput
import os
import time
from tqdm import tqdm
import json
def get_directory_size(f):
    total_size = 0
    react_size = 0
    ts_size = 0
    css_size = 0
    s= set()
    with open('big_dirs.txt') as g:
        big_dirs:list = json.load(g)
        big_dirs = set(big_dirs)
    with open('subdirs.txt') as h:
        subdirs = json.load(h)
    index = 0
    node_modules = []
    print(len(subdirs))
    while 1:
        for dirpath, dirnames, filenames in tqdm(os.walk(f'./repos/{subdirs[index]}')):
            if 'node_module' in  dirpath:
                node_modules.append(subdirs[index])
                continue
            # if time.time() - start >60:
            #     big_dirs.append(subdirs[index])
            #
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                temp = os.path.getsize(filepath)
                total_size += temp
                if filepath.endswith(('.js','.jsx','.ts','.tsx','.css')):
                    react_size+= temp
                    f.write(filepath+'\n')
                # elif filepath.endswith('.ts') or filepath.endswith('.tsx'):
                #     ts_size+= temp
                # elif filepath.endswith('.css'):
                #     css_size +=temp
                # else:
                    # pass
                    # s.add(filepath.split('.')[-1])
                    # os.remove(filepath)
                    # try:
                    #     os.remove(filepath)
                    # except:
                    #     pass
        # print(s)
        index +=1
        if index == len(subdirs):
            # print(subdirs[index-1])
            # with open('big_dirs.txt','w') as n:
            #     json.dump(big_dirs,n)
            with open('node_modules.json','w') as nm:
                json.dump(node_modules,nm,indent=4)
            return total_size,ts_size,react_size,css_size

def main():
    try:
        f = open('dir.txt','w',encoding='UTF-8')
        total,ts,react,css = get_directory_size(f)
        size_mb = total / (1024*1024)
        print(f"Size of directory '': ")
        print(f"total megabytes: {size_mb:.2f} MB")
        size_mb = ts / (1024 * 1024)
        # print(f"Size of directory '{directory}':")
        print(f"ts megabytes: {size_mb:.2f} MB")
        size_mb = react / (1024 * 1024)
        # print(f"Size of directory '{directory}':")
        print(f"react megabytes: {size_mb:.2f} MB")
        size_mb = css / (1024 * 1024)
        print(f"css megabytes: {size_mb:.2f} MB")
    except:
        f.close()


if __name__ == "__main__":
    main()
