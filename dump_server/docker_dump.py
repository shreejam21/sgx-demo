import re
import subprocess

# non-sgx
# sgx-en
def dump_data(secret, container_name):
    sr = subprocess.run(['sudo', 'docker', 'inspect', container_name, '|', 'grep', 'Pid'], capture_output=True)
    file_contents = sr.stdout.decode()

    # with open('pid.txt', 'r') as f:
    #     file_contents = f.read()
    matc = re.findall(": ([0-9]*),", file_contents)
    parent_pid = matc[0]

    sr = subprocess.run(['pstree', '-pg', parent_pid], capture_output=True)
    file_contents = sr.stdout.decode()

    matc = re.findall("\(([0-9]*),", file_contents)

    dump_command = 'sudo gcore '

    for pid in matc:
        dump_command += pid + ' '

    subprocess.run(dump_command.strip().split())

    sr = subprocess.run(f'strings -a core.* | grep {secret.strip()}'.split(), capture_output=True)
    grep_output = sr.stdout.decode()
    
    sr = subprocess.run('strings -a core.*'.split(), capture_output=True)
    file_contents = sr.stdout.decode()
    return file_contents, grep_output
    