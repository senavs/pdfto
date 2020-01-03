FROM ubuntu:18.04

# where code project will be
RUN mkdir /code
WORKDIR /code

# installing python and poppler
RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools \
        python-poppler \
        poppler-utils  \
    && rm -rf /var/lib/apt/lists/*

# coppying requirements.txt to /code
COPY ./pdfto/requirements.txt /code

# installings python requirements
RUN pip3 install -r requirements.txt

# coppying project to /code
COPY ./pdfto /code

# project environment variables
ENV FLASK_APP 'PDFto'
ENV FLASK_ENVIRONMENT 'development'
ENV FLASK_HOST '0.0.0.0'
ENV FLASK_PORT '9000'
ENV FLASK_DEBUG 1
ENV FLASK_RESTPLUS_VALIDATE 1
ENV FLASK_RESTPLUS_MASK_SWAGGER 0

# exposed port (be careful! if you change FLASK_PORT
# variable, you also have to change here in EXPOSE key)
EXPOSE 9000

# change /code folder permissions
RUN chmod +x -R /code

CMD ["./run.sh"]