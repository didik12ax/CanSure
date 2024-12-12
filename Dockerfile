FROM python:3.9-slim

# Install dependencies sistem yang diperlukan untuk OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy file requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy aplikasi dan model
COPY app.py .
COPY modelbest.pt .

# Expose port Flask
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "app.py"]
