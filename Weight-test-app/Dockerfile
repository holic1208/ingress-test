FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py .
COPY templates/ templates/

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
