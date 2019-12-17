sudo chmod a+rwx /var/run/docker.sock
sudo chmod a+rwx /var/run/docker.pid

docker build . -t cambot

### Run

```
docker run --device=/dev/video0:/dev/video0 cambot
```