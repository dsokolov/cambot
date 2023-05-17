## Coinfig

`bot.properties` file should be like this:

```
[Bot]
token=your_tg_token_here
use_proxy=True|False
proxy=your_proxy_url_here
```

## Docker

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


```
fswebcam -S 10 -l 30 pic_%Y-%m-%d_%H:%M:%S.jpg
```

123