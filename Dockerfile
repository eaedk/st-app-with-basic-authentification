# Streamlit Dockerfile

FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set PYTHONPATH to the root of the project to recognize 'app' as a package
ENV PYTHONPATH=/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the frontend code
COPY . /app

# Expose Streamlit port
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
