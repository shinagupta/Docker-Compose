FROM python
Workdir /myapp
COPY ./app.py .
RUN pip install pymysql
RUN pip install cryptography
CMD ["python", "app.py"]
