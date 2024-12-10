#!/bin/bash

echo "Pulling the latest Docker image..."
docker-compose pull

echo "Restarting the Docker service..."
docker-compose up -d

echo "Deployment complete!"

