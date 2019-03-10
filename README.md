# gocd-pipeline

- Run server
```
docker run -d -p8153:8153 -p8154:8154 -v $(pwd):/home/go/ gocd/gocd-server:v19.1.0
```

- Go inside server
```
docker exec -it -u go -w /home/go <id> /bin/bash
```

- Start agent
```
docker run -itd -e GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' <server-container-name>):8154/go gocd/gocd-agent-ubuntu-16.04:v19.1.0
```
