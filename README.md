## recsys fast api practice
<hr>

### install 
```bash
$ pip install fastapi # fast api module
$ pip install "uvicorn[standard]" # asgi module
```


### Run 
```bash
$ cd src
$ uvicorn main:app --reload 
```

### docs
```vim
serverhost/docs  #swagger docs
serverhost/redoc # auto docs 
```

### docker build
```bash
$ docker build -t fast-api .
```

### Container Execution
```bash
$ docker run --rm -p 8080:80 fast-api #contianer stop -> container 제거,  8080 포워딩
```

### Docker compose start
```bash
$ docker-compose up
$ docker-compose up --build --force-recreate # rebuild
```


### Requirements

```txt
fastapi==0.95.1
SQLAlchemy==2.0.12
pydantic==1.10.7
boto3==1.25.124
gensim==4.3.1
jwt==1.3.1
decode==0.7.1
```