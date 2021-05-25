POST /tags accept website url in json format and return task id. Example request:  
{"website": "https://google.com"}  

GET /tags/<task_id> return number of each HTML element or task status if its in progress  

RUN:  
- docker-compose up

- pytest -m webtest  
or simply:  
pytest
