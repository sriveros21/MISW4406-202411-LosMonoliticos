FROM python:3.10

EXPOSE 5000/tcp

COPY auditorias-requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r auditorias-requirements.txt

# Copy the rest of the application code
COPY . .

CMD [ "flask", "auditorias.main:app", "./ArquitecturaHexagonal/PropiedadesdelosAlpes/auditoria/api", "run", "--host=0.0.0.0"]