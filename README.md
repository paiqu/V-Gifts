# capstone-project-3900-h16a-victims
https://v-gifts.herokuapp.com/
## Prerequisites

* `python3`should be installed (recommended [Python 3.7.10](https://www.python.org/downloads/release/python-3710/))
* `npm` should be installed

## Installation & Usage

### Backend

1. Install `virtualenv` 

   ```shell
   python3 -m pip install virtualenv
   ```

2. Open the `/backend` folder

   ```shell
   cd where/the/project_code/project/backend
   ```

3. Create the virtual environment

   ```shell
   python3 -m venv env
   ```

4. Active the virtual environment 

   ```shell
   source env/bin/activate
   ```

5. Install the required dependencies

   ```shell
   python3 -m pip install -r requirements.txt
   ```

6. Start the backend server

   ```shell
   # remember to active virtual environment every time before run the server (check step 4)
   python3 server.py # start the server in default port (5000)
   # or
   python3 server.py [PORT NUMBER] # example: python3 server 6000
   ```

### Fronend

1. Open the `/frontend` folder

   ```shell
   cd where/the/project_code/project/frontend
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

   

