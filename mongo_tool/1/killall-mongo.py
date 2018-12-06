import subprocess

process = subprocess.Popen("sudo -S killall -9 mongod",
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
stdout, stderr = process.communicate('dy781002!@#' + "\n")
print(stdout)
print(stderr)

process = subprocess.Popen("sudo -S killall -9 mongos",
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
stdout, stderr = process.communicate('dy781002!@#' + "\n")
print(stdout)
print(stderr)

