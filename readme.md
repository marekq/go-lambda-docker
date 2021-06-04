go-lambda-pipeline
==================

Build and run your Golang code in S3 using AWS Lambda. This allows you to create a serverless build service that outputs the artifacts to a bucket. 

Deploy the stack using AWS SAM and invoke the Lambda function with the 'event.json' input. 

```
{
    "command": "cd /tmp && go build -o outputcode main.go",
    "input_file": "main.go",
    "output_file": "outputcode"
}
```

You should specify the input and output paths for the code based on their S3 prefix paths from the included S3 bucket. You can customize the event to include any build parameters (such as 'GOOS', 'GOARCH', etc.).


This is a very initial proof of concept right now, please use it for educational purposes only. 
