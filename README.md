## recsys fast api practice
<hr>

### setup
<br>

#### install 
```bash
$ pip install fastapi # fast api module
$ pip install "uvicorn[standard]" # asgi module
```


#### Run 
```bash
$ cd src
$ uvicorn main:app --reload 
```

#### docs
```vim
serverhost/docs  #swagger docs
serverhost/redoc # auto docs 
```

#### docker build
```bash
$ docker build -t fast-api .
```

#### Container Execution
```bash
$ docker run -rm -p 8080:80 fast-api #contianer stop -> container 제거,  8080 포워딩
```

