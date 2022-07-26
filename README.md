# Vending Machine

It's microservice with fastapi rabbitmq and mariadb in docker

# How to run this project
step1: Install docker and docker-compose 

step2: run docker-compose up --build -d 

step3: Let's go!!! You can see order service api in localhost:8000 and stock service in localhost:5000

# How to deploy

you can setup nginx in docker or docker-compose and mount it to docker.sock in example docker-compose file let see below 

version: '2'
services:
  nginx-proxy:
    image: jwilder/nginx-proxy:alpine
    container_name: nginx-proxy
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - vhost:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - certs:/etc/nginx/certs:ro
      - dhparam:/etc/nginx/dhparam
      - /var/run/docker.sock:/tmp/docker.sock:ro

  letsencrypt:
    image: jrcs/letsencrypt-nginx-proxy-companion
    container_name: nginx-proxy-lets
    volumes_from:
      - nginx-proxy
    volumes:
      - certs:/etc/nginx/certs:rw
      - /var/run/docker.sock:/var/run/docker.sock:ro
    depends_on:
      - nginx-proxy
      
volumes:
  vhost:
  html:
  certs:
  dhparam:

networks:
  default:
    external:
      name:
        webproxy
