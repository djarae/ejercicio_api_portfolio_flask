FROM python:3.11-alpine
COPY . /app
WORKDIR /app
RUN python -m venv venv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["src/app.py"]
