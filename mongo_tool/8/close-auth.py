import subprocess
import re,os
path = '/home/administrator/mongodb/conf'
dir = next(os.walk(path))[2]
for file in dir:
    file_path = os.path.join(path,file)
    with open(file_path, "r", encoding="utf-8") as f1, open("%s.bak" % file_path, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub('auth=true', '#auth=true', line))
    os.remove(file_path)
    os.rename("%s.bak" % file_path, file_path)

