FROM python:3.9.7-slim-buster

# Set working directory
WORKDIR /app/repo2

# Install required packages
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Ensure ffmpeg is installed
RUN apt install ffmpeg

# Set the cookies file path for the bot
ENV COOKIES_FILE_PATH="/app/repo2/youtube_cookies.txt"

# Run the bot
CMD gunicorn app:app & python3 main.py
