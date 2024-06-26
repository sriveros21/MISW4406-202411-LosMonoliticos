FROM python:3.10

# Set the working directory
WORKDIR /app

EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

CMD [ "flask", "--app", "./ArquitecturaHexagonal/PropiedadesdelosAlpes/api", "run", "--host=0.0.0.0"]