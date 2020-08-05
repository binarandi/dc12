FROM python:3-onbuild
COPY . /usr/src/app
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
CMD ["python", "app/api.py"]