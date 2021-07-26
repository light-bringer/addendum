## Install dependencies
 -  if you use PipEnv then run : `pipenv sync` or `pipenv install`
 -  if you use pip and requirements.txt file : `pip install -r requirements.txt`



## Command Line Code 
  # Command line execution
  Execute : `python -m adder_api 1 2 3`
  # Test Cases
  Run : `python -m unittest`


## API 
  # FastAPI API
  Run : `gunicorn -w 4 -k uvicorn.workers.UvicornWorker  adder_api.api:app --bind 0.0.0.0:8000` or `uvicorn adder_api.api:app --bind 0.0.0.0:8000`

## Docker 
Run : `docker-compose up`

- #  APIDOC
http://localhost:8000/docs