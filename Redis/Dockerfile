FROM redis:latest

# Expose the Redis port
EXPOSE 6379

# Define a volume to persist Redis data
VOLUME ["/data"]

# Set the default command to run Redis with appendonly enabled
CMD ["redis-server", "--appendonly", "yes"]
