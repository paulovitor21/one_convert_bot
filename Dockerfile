# Usa imagem oficial Python 3.12 slim
FROM python:3.12-slim

# Instala ffmpeg (necessário para yt-dlp extrair áudio)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia requirements.txt para instalar dependências
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo código para dentro do container
COPY . .

# Expõe a porta (não essencial para polling, mas pode deixar)
EXPOSE 8443

# Comando para rodar o bot
CMD ["python", "bot.py"]
