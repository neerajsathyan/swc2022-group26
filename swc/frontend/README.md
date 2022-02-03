# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### Dockerization of Vue-cli
See [Configuration Reference] (https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html).

To build the Docker image:
```
docker build -t swc/frontend .
```

Run our Vue.js app in a Docker container:
```
docker run -it -p 8080:8080 --rm --name swc-frontend  swc/frontend 
```