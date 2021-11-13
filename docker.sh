#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp views.py tempdir/.
cp -r templates/* tempdir/templates/.
cp requirements.txt tempdir/.

echo "FROM python" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates" >> tempdir/Dockerfile
echo "COPY requirements.txt /home/myapp/" >> tempdir/Dockerfile
echo "RUN pip install -r/home/myapp/requirements.txt" >> tempdir/Dockerfile
echo "EXPOSE 8000" >> tempdir/Dockerfile
echo "CMD python/home/myapp/views.py" >> tempdir/Dockerfile

cd tempdir
docker build -t views .
docker run -t -d -p 8000:8000 --name breakoutrunning main
docker ps -a