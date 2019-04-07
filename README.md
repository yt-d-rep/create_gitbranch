# Mattermost Bot
## How to build image
    $ docker build --tag=umedocker/mattermost-python-bot .

## Run
    $ docker run -d --name bot -p 8080:80 -t umedocker/mattermost-python-bot

## Trigger Words
* `real python`
    * tell you one kind of pythons at random