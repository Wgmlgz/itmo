# web/Dockerfile
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY web/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code
COPY web/ .

# Build the app
RUN npm run build

# Start the app
CMD ["npm", "run", "preview"]
