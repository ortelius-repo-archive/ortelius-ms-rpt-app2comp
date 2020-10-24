# ortelius-ms-rpt-app2comp

A python flask app that maintains the list of countries and there captials and supports CRUD operations around it. 


### API LIST
Four types of APIs are supported at the moment.

#### Add a capital

curl http://localhost:5000/capitals/spain -d "cap=columbia" -X POST -v

#### Delete a capital

curl http://localhost:5000/caplitals/pakistan -X DELETE -v

#### Get a capital

curl http://localhost:5000/capitals/pakistan -X GET -v


#### Get all captials

curl http://localhost:5000/capitals -X GET -v


### Run the app

To run the app locally write \
`$ python app2comp.py`

To dockerize the app \
`$ cd ortelius-ms-rpt-app2comp` \
`$ docker build -t  app2comp:v1 .` \
By default the docker base image servers the app at port 80 we can bind it \
to any port we like, like here it is 5000 \
`$ docker run -it -p 5000:80  app2comp:v1`

