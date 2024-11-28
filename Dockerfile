# Step 1: Use an official Python base image
FROM python:3.9-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy dependency files to container
COPY requirements.txt /app/

# Step 4: Install Necessary Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all Django project code into the container
COPY . /app

# Step 6: Expose port 8000, which Django runs on by default
EXPOSE 8000

# Step 7: Command to Start Django Development Server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
