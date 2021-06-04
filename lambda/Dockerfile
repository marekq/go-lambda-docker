FROM public.ecr.aws/lambda/python:latest

# update yum repo
RUN yum update -y

# install lambda insights logs agent
RUN curl -O https://lambda-insights-extension.s3-ap-northeast-1.amazonaws.com/amazon_linux/lambda-insights-extension.rpm && \
    rpm -U lambda-insights-extension.rpm && \
    rm -f lambda-insights-extension.rpm

# install golang 
RUN yum install golang golang-bin gcc-go -y

# install lambda function app.py requirements 
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# clean yum cache directories to reduce container size
RUN yum clean all && rm -rf /var/cache/yum

# copy lambda code and set cmd entry
COPY main.go .
COPY app.py .

CMD ["app.lambda_handler"]
