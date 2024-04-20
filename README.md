![image](https://github.com/mrdiamond12312/flask-house-price-predict/assets/102137001/39f33e73-79cb-418b-8b56-39899ccc77e0)

## House Prediction Service
#### Using Py3.9 Flask as driver
This project is to predict house price based on provided information. [Refs here](https://www.kaggle.com/code/tomasmantero/predicting-house-prices-keras-ann)

### Terminal Commands
> [!TIP]
> There are no environment variables needed at the moment!
- Install dependencies
```bash 
make install
```

- Turn on server in development mode
```bash
make run
```

- Run all tasks
```bash
make all
```

### Docker compose
#### Please turn on your docker service (Docker Desktop, etc) beforehand
- Run server in docker environment
```base
make up
```

> [!NOTE]
> The Link provided in description will navigate to a Swagger UI from which you can test the 2 models, which are deployed on [Render](render.com), using a standard instance service, which will need 5-10 minutes to load up if the service is not use for a while.
