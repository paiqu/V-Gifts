# capstone-project-3900-h16a-victims
A gift shopping website

## Prerequisites

* `python3`should be installed (recommended [Python 3.7.10](https://www.python.org/downloads/release/python-3710/))
* `npm` should be installed

## Installation & Usage

### Backend

1. Install `python3` (If you have already installed it, skip this step)

   ```shell
   python3 -m pip install virtualenv
   ```

2. Open the `/backend` folder

   ```shell
   cd backend
   ```

3. Install the required dependencies

   ```shell
   python3 -m pip install -r requirements.txt
   ```

4. Start the backend server

   ```shell
   python3 server.py # start the server in default port (5000)
   # or
   python3 server.py [PORT NUMBER] # example: python3 server 6000
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
   # backend port number need to be same as what's used in the backend server and can not be the same as frontend port number
   ```

   example:

   ```shell
   sh run.sh 5000 3000
   ```

   

