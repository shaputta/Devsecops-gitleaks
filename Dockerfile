FROM python:3.10-slim
WORKDIR /app
COPY python_app/ .
RUN pip install flask
ENV PORT=5000
EXPOSE 5000
CMD ["python", "app.py"]