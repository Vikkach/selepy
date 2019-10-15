# selepy
An automation tests framework for writing integrations tests for Electron app. Built on top of Selenium, pyTest

##	UI Test Execution from PyCharm 
### Installation 

1. Install the latest version of Python 3 from https://www.python.org/downloads/.
2. Install virtualenv using command `pip install virtualenv`.
3. Clone this project 
4. Create virtualenv within project root `virtualenv venv`.
5. Activate virtualenv `venv\scripts\activate`.
6. Install python libraries `pip install -r requirements.txt`
7. Create Python tests configuration in PyCharm and select created virtualenv as interpreter
8. Set VERSION of chromedriver (currently working with 2.37)

To run tests set script path in created configuration (e.g. ##your_local_path##\selepy\tests\ui) and set 

## Run from Docker
1. Go to selepy folder
2. Build Docker `docker build -t selepy .`
3. Run tests `docker run -i --rm --user $(id -u):$(id -g) -v $(pwd):/app selepy /app/web_tests_trigger.sh/`