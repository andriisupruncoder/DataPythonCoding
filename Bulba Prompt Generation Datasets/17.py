import subprocess

def run_command(command):
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, error = process.communicate()
  if error:
    print(error)
  else:
    print(output)

run_command("goto")