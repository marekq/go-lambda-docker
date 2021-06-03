import shutil, subprocess

# run subprocess
def subproc(cmd):
    process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, cwd = '/tmp', text = True)

    stdout, stderr = process.communicate()
    exit_code = process.wait()

    print('cmd ' + str(cmd))
    print('stdout ' + str(stdout))
    print('stderr ' + str(stderr))
    print('exit_code ' + str(exit_code))
    print('')


def lambda_handler(event, context):

    print('event ' + str(event))
    print('')
    cmd = event['command']

    shutil.copy('./main.go', '/tmp/main.go')

    subproc('ls -alFh /tmp')
    subproc(cmd)
    
    subproc('ls -alFh /tmp')

    return 'end'
