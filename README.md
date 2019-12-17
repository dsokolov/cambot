### Misc

sudo chmod a+rwx /var/run/docker.sock
sudo chmod a+rwx /var/run/docker.pid

### Build

docker build . -t cambot

### Save container
```
docker save --output cambot.tar cambot
```

### Load container
```
docker load --input cambot.tar
```


### Run

```
docker run --device=/dev/video0:/dev/video0 cambot
```

