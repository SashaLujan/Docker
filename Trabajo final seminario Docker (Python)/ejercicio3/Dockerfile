FROM python:3
EXPOSE 5000
WORKDIR /myapp/
COPY . /myapp/
RUN pip install -r requirements.txt
CMD python hello.py

# docker build .
# docker run -p 5000:5000 IMAGE[:tag]
# ej: docker run -p 5000:5000 41c5fe511fc9