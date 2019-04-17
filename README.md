# Mattermost Bot
This bot returns information below of pythons(one kind of snakes).<br>
* ZooLogicalName
* CommonName
* ReptileDataBasePage
* IMAGE (on Google Search)
## How to build image
    $ docker build --tag=umedocker/mattermost-bot .

## Run
    $ docker run -d --name bot -p 8080:80 -t umedocker/mattermost-bot

## Bot URL
    http://localhost:8080/bot

## Trigger Words
* `real python`
    * bot tells you one kind of pythons at random