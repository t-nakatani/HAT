FROM pytorch/pytorch:1.9.1-cuda11.1-cudnn8-runtime

COPY requirements.txt setup.py VERSION README.md ./
COPY hat/version.py hat/
RUN pip install -r requirements.txt
RUN python setup.py develop

RUN apt-get update && apt-get update && apt-get install -y libgl1 libglib2.0-0

WORKDIR /work
