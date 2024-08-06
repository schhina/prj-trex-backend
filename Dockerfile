FROM mongo
RUN apt update
RUN apt install python3 python3-pip -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
ADD requirements.txt /
RUN pip3 install --no-cache-dir -r requirements.txt
ADD main.py ./
ADD edge.py ./
ADD star.py ./
RUN pip3 install flask
ENV FLASK_APP=main.py
RUN pip3 list
CMD ["gunicorn", "main:main()"]