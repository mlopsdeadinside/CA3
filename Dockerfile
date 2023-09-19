FROM python
ENV USERNAME=raheimeen
RUN mkdir -p /home/dockerdemo

EXPOSE 5000
WORKDIR /home/dockerdemo
RUN pip install -r requirements.txt
CMD ["python", "test_hello.py"]
