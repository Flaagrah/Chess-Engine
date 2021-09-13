FROM python:3.7
RUN pip install --upgrade pip && \
    pip install numpy==1.19.5 && \
    pip install tensorflow==2.5.0 && \
    pip install chess==1.5.0 && \
    pip install flask==2.0.1 && \
    pip install pgn-parser==1.1.0 && \
    pip install requests==2.26.0

WORKDIR /Docker
COPY . /Docker

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]