FROM registry.access.redhat.com/ubi9/ubi
RUN dnf install -y python3 python3-pip

WORKDIR /app
COPY ./requirements.txt ./app ./
RUN chmod -R ug+rwx /app
RUN python3 -m pip install -r /app/requirements.txt

USER 1001
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
