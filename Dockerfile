ARG FUNCTION_DIR="/home/app/"

FROM ubuntu:21.04
ENV TZ=Asia/Calcutta
ENV aws_access_key_id=AKIAX4EFR7ZT25UPZUNY
ENV aws_secret_access_key=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

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt install -y python3 python3-pip

COPY requirements.txt .
COPY Speech2txt.py .
COPY test.py .

ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
COPY entry.sh /
RUN chmod 755 /usr/bin/aws-lambda-rie /entry.sh

RUN pip3 install awslambdaric
RUN /usr/bin/python3 -m pip install awslambdaric
RUN /usr/bin/python3 -m pip install -r requirements.txt


RUN /usr/bin/python3 ./test.py

COPY index.py .

ENTRYPOINT [ "/entry.sh" ]
CMD [ "index.handler" ]