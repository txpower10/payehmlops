# Base image with Python
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    git \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install Python dependencies including PyTorch
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install other required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

