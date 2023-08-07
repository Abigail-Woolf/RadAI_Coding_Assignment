# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /RadAI_Coding_Assignment

# Copy the requirements file into the container at /RadAI_Coding_Assignment
COPY requirements.txt /RadAI_Coding_Assignment/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /RadAI_Coding_Assignment
COPY . /RadAI_Coding_Assignment/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
4