FROM python:3.9
RUN apt-get update && \
    apt-get install -y \
    curl \
    sudo \
    wget \
    locales
# locales \
# python3.8 \
# python3-pip \
# python3.8-dev \
# mysql-client \
# mysql-server \
# libgl1-mesa-dev \
# libmysqlclient-dev

# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1 && \
#     update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && \
#     pip3 install --upgrade pip wheel setuptools

RUN pip3 install --upgrade pip wheel setuptools

ARG WORKDIR=/src/

RUN mkdir ${WORKDIR}
WORKDIR ${WORKDIR}
COPY requirements.txt ${WORKDIR}
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", ${HOST}, "--port", ${PORT}, "--reload"]
