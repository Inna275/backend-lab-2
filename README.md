# backend-lab-1

This is a basic REST API for Lab 1 of the Backend course.  
It includes a greeting endpoint (`/`) and a healthcheck endpoint (`/healthcheck`).

## How to run

### 1. Access the deployed service
- [Greeting](https://backend-lab-1-3ips.onrender.com)
- [Healthcheck](https://backend-lab-1-3ips.onrender.com/healthcheck)

### 2. Run locally
1. Make sure you have Docker and Docker Compose installed.
   - [Install Docker](https://www.docker.com/get-started)  
   - [Install Docker Compose](https://docs.docker.com/compose/install)
2. Clone the repository:
   ```bash
   git clone https://github.com/Inna275/backend-lab-1.git
   ```
3. Navigate to the project folder:
   ```bash
   cd backend-lab-1
   ```
4. Build and run the containers:
   ```bash
   docker-compose build
   docker-compose up
   ```
5. Access the endpoints:
   - Greeting: http://localhost:8080/
   - Healthcheck: http://localhost:8080/healthcheck
