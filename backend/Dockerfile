# 1. Use official lightweight Python image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies (needed for OCR later if required)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements first (better caching)
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy backend code
COPY app ./app

# 7. Expose FastAPI port
EXPOSE 8000

# 8. Start the application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

