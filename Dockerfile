FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY error_analyzer/ ./error_analyzer/
COPY setup.py .

# Install the CLI tool
RUN pip install .

ENTRYPOINT ["error-helper"]
