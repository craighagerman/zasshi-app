# Quickstart

How to run this Vue web app
n.b. There are two options for serving:

1. Local development
2. Dockerized Nginx server

## 1. Local development

```bash
  npm run dev
```

## 2. Dockerized Nginx

```bash
  docker-compose up -d
```

### Then...

view web page at `http://localhost:8000/`

---

# Notes on building & running the Docker container

## Build the Docker Container

### First run

```bash
  docker-compose up --build --no-recreate -d
```

### Subsequent runs

From the second time, we can use

```bash
  docker-compose up -d
```

## Build and start the Application

We have a running container, but not the installed or running Vue app.
For that, we need to log into the container and then execute the commands.

log into the container:

```bash
  docker exec -it vite_docker sh

```

and install node packages and then start the app

```bash
  npm i && npm run dev
```
