import boto3, shutil, subprocess, os
from aws_lambda_powertools import Logger, Tracer

# start logger and tracing of function
logger = Logger()
modules_to_be_patched = [ "boto3" ]
tracer = Tracer(patch_modules = modules_to_be_patched)

# connect to S3 bucket using AWS SDK
s3_bucket_conn = boto3.client("s3")
s3_bucket_name = os.environ['s3_bucket_name']


# run subprocess
@tracer.capture_method(capture_response = True)
def subproc(cmd):

    # run bash command in subprocess
    process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, cwd = '/tmp', text = True)

    # get stdout, stderr and exit code
    stdout, stderr = process.communicate()
    exit_code = process.wait()

    print('cmd ' + str(cmd))
    print('stdout ' + str(stdout))
    print('stderr ' + str(stderr))
    print('exit_code ' + str(exit_code))
    print('')

    return stdout


# download file from S3
@tracer.capture_method(capture_response = True)
def s3_download_file(src, dst):

    print('retrieving s3://' + s3_bucket_name + '/' + src + ' to ' + dst)
    s3_bucket_conn.download_file(s3_bucket_name, src, dst)


# upload file to S3
@tracer.capture_method(capture_response = True)
def s3_upload_file(src, dst):

    print('uploading ' + src + ' to s3://'+ s3_bucket_name + '/' + dst)
    s3_bucket_conn.upload_file(src, s3_bucket_name, dst)


# lambda handler
@logger.inject_lambda_context(log_event = True)
@tracer.capture_lambda_handler(capture_response = True)
def lambda_handler(event, context):

    # get input parameters from event
    cmd         = event['command']
    inputf      = event['input_file']
    outputf     = event['output_file']
    tmpfile     = '/tmp/main.go'

    # download Go file from S3 to /tmp/main.go
    s3_download_file(inputf, tmpfile)

    # run build command
    stdout = subproc(cmd)

    # upload Go artifact to S3 from /tmp/outputcode
    s3_upload_file('/tmp/outputcode', outputf)

    # return build output
    return stdout
