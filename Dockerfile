# Use a lightweight and modern Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /fwdbot

# Update system and install git
RUN apt update && apt upgrade -y && \
    apt install -y git && \
    apt clean

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all bot files and start script
COPY . .

# Expose port 8080 for health check (Flask or FastAPI)
EXPOSE 8080

# Start the bot using start.sh
CMD ["bash", "start.sh"]
