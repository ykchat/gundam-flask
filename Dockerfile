FROM python:2-onbuild

EXPOSE 8080
ENTRYPOINT ["python", "./server.py"]
CMD []
