# Use the official MongoDB image from Docker Hub
FROM mongo:latest

# Expose the default MongoDB port
EXPOSE 27017

# Set environment variables for MongoDB initialization
ENV MONGO_INITDB_ROOT_USERNAME=${MONGO_INITDB_ROOT_USERNAME}
ENV MONGO_INITDB_ROOT_PASSWORD=${MONGO_INITDB_ROOT_PASSWORD}

# Define a volume for MongoDB data
VOLUME ["/data/db"]

# Default command to run MongoDB
CMD ["mongod"]