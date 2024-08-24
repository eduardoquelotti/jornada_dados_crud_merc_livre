# Use uma imagem base para executar Docker Compose
FROM docker/compose:latest

# Copie o arquivo docker-compose.yml para o container
COPY docker-compose.yml /app/docker-compose.yml

# Defina o diretório de trabalho
WORKDIR /app

# Comando para iniciar o Docker Compose
CMD ["docker-compose", "up"]