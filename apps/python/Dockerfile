# Imagem base leve
FROM python:3.14.3-slim-trixie

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências
RUN pip install flask prometheus-flask-exporter

# Copia o código
COPY app.py .

# Expõe a porta da API
EXPOSE 5000

# Comando para rodar
CMD ["python", "app.py"]