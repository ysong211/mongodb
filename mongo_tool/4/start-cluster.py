import subprocess


process = subprocess.Popen("sudo -S mongod -f /home/administrator/mongodb/conf/shard4.conf",
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
stdout, stderr = process.communicate('dy781002!@#' + "\n")
print(stdout)
print(stderr)

process = subprocess.Popen("sudo -S mongod -f /home/administrator/mongodb/conf/shard5.conf",
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
stdout, stderr = process.communicate('dy781002!@#' + "\n")
print(stdout)
print(stderr)

process = subprocess.Popen("sudo -S mongod -f /home/administrator/mongodb/conf/shard6.conf",
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
stdout, stderr = process.communicate('dy781002!@#' + "\n")
print(stdout)
print(stderr)


