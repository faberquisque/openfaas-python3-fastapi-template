# OpenFaas Python3 FastAPI Template

A Python [FastAPI](https://github.com/tiangolo/fastapi) template that make use of the incubator project [of-watchdog](https://github.com/openfaas-incubator/of-watchdog).

Templates available in this repository:
- python3-fastapi


## Downloading the templates
```
$ faas template pull https://github.com/gastonmichel/openfaas-python3-fastapi-template
```

## Using the python3-fastapi templates
Create a new function

```
$ faas new --lang python3-fastapi <fn-name>
```

Build, push, and deploy

```
$ faas up -f <fn-name>.yml
```

Set your OpenFaaS gateway URL. For example:

```
$ OPENFAAS_URL=http://127.0.0.1:8080
```

Test the new function

```
$ curl -X POST $OPENFAAS_URL/function/<fn-name>
```
Get the documentation in openapi.json format

```
$ curl -X GET $OPENFAAS_URL/function/<fn-name>
```

## Usage

### Mandatory FastAPI object 
In the function folder include a file named 'handler.py' and include an 'handle' funcion:
```
def handle(body: RequestModel):
```
Implement a pydantic RequestModel for documentation purposes

Check the template/python3-fastapi/function folder for a minimal example
