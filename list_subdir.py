import os
import json

def list_subdirs(directory):
    subdirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    with open('subdirs.txt','w') as f:
        json.dump(subdirs,f,indent=3)
    return subdirs

# Example usage:
directory_path = './repos'
subdirectories = list_subdirs(directory_path)
print("Subdirectories of", directory_path, "are:")
for subdir in subdirectories:
    print(subdir)
