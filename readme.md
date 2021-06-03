go-lambda-pipeline
==================

Build and run your Golang code in S3 using AWS Lambda. This allows you to create a serverless build service that outputs the artifacts to a bucket. 

Deploy the stack using AWS SAM and invoke the Lambda function with the 'event.json' input to build the "hello world" sample. You can customize the event to include any build parameters (such as 'GOOS', 'GOARCH', etc.) or where the input and output files are located.

This is a very initial proof of concept right now, please use it for educational purposes only. 
