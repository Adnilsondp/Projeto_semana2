# Imagem oficial do Python versão slim para reduzir o tamanho
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo main.py para o diretório de trabalho
COPY main.py .

# Definir o comando para executar o script Python
CMD ["python", "main.py"]