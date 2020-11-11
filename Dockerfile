FROM python:3

COPY ./app /app
WORKDIR /app
RUN pip install flask

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["flaskapp.py"]

