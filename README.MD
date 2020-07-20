# Endpoint success / failure and TTLB query application

## Usage

This is an application to query endpoint X times per second and log success / failure and TTLB

## Building docker container

The success / failure and TTLB logs are located in /opt/testapp/testerapp.log. Mount this outside the container for them to persist and for easier access to them.
Max log size is 20mb before generating a new log and will keep a max of 10 logs

### Quickstart build / run docker image

Clone project and cd to application directory

Build image:

```docker build --tag testerapp .```

Run image:

Enviroment variables
* EXECUTIONS_PER_SECOND (Optional) = how many times to query the url per second (between 0 and 30), defaults to 10 and will set value to 10 if outside the limits
* TEST_URL (Required): URL to query (set to UTC date/time "API" at http://datewebapp.inmy.coffee/ as an example below)

```docker volume create testerappvolume```

```docker run --restart=always --env "EXECUTIONS_PER_SECOND=20" --env "TEST_URL=http://datewebapp.inmy.coffee/" -v testerappvolume:/opt/testapp/log --name=testerapp -d testerapp```


## License
[MIT](https://choosealicense.com/licenses/mit/)