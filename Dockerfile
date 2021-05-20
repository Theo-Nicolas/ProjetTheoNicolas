#Import python 3.8
FROM python:3.8-buster

EXPOSE 8501

#Define the directory of the application
WORKDIR /app


COPY requirements.txt ./
# Run the command to install python packages
RUN pip install -r requirements.txt
# Copy the file to the Docker image
COPY . .
CMD ["python", "app.py"]

