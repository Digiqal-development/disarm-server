# Base image for .NET Core and Python
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
USER root
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

# Install Python 3.11 and necessary libraries
RUN apt-get update && \
    apt-get install -y python3.11 python3.11-dev python3.11-venv build-essential libpython3.11

# Create a virtual environment with the standard library copied
RUN python3.11 -m venv /app/venv --copies

# Upgrade pip inside the virtual environment
RUN /app/venv/bin/pip install --upgrade pip

# Install Python dependencies (e.g., spacy, etc.)
RUN /app/venv/bin/pip install spacy

# Download and install the SpaCy model
RUN /app/venv/bin/python -m spacy download en_core_web_sm

# Set up the environment variables for Python.NET to use the virtual environment
ENV PYTHONPATH="/app/venv/lib/python3.11/site-packages:/app/venv/lib"

# Copy the Console App binaries from the host to the Docker container
COPY ./linux-x64 /app/consoleapp

# Set execute permissions on the console app (if necessary)
RUN chmod +x /app/consoleapp/DisarmPythonResultGenerator

# This stage is used to build the .NET service project
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["Disarm-Server/Disarm-Server.csproj", "Disarm-Server/"]
RUN dotnet restore "./Disarm-Server/Disarm-Server.csproj"
COPY . .
WORKDIR "/src/Disarm-Server"
RUN dotnet build "./Disarm-Server.csproj" -c $BUILD_CONFIGURATION -o /app/build

# Publish the .NET project
FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./Disarm-Server.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

# Final stage for running the .NET and Python components together
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

# Make sure the .NET service executable has the correct permissions (if needed)
RUN chmod +x /app/Disarm-Server.dll

# Set Python environment variables to point to the virtual environment
ENV PYTHONPATH="/app/venv/lib/python3.11/site-packages:/app/venv/lib"

# Entry point to run the .NET service
ENTRYPOINT ["dotnet", "Disarm-Server.dll"]
