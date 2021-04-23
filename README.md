# capstone-project-3900-h16a-victims
A gift shopping website

## Prerequisites

* `python3`should be installed (recommended [Python 3.7.10](https://www.python.org/downloads/release/python-3710/))
* `npm` should be installed

## Installation

### Backend

1. Open the `/backend` folder

   ```shell
   cd backend
   ```

2. Start the backend server

   ```shell
   python3 server.py # Start the server in default port (5000)
   # or
   python3 server.py [PORT NUMBER] # Example: python3 server 6000
   ```

### Fronend

1. Open the `/frontend` folder

   ```shell
   cd frontend
   ```

2. Install all required dependencies

   ```shell
   npm install
   ```

3. After the backend server has been running, start the frontend

   ```shell
   sh run.sh [BACKEND PORT] [FRONTEND PORT]
   ```

   example:

   ```shell
   sh run.sh 5000 3000
   ```

   

