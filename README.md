# Motivational-Bot

A Discord bot that serves motivation quotes. (submission to the CodeHax 2020 hackathon)

## How to run the bot

1. Create `config.yaml`
2. In, `config.yaml`, create this key:

```yaml
token: ""
```

3. Run `./run.sh`

## How to kill the bot

`sudo killall -p docker`

## Commands

`!motivation` _Returns motivational quotes in a rich embed + a motivational GIF_

## Video Script

Everyday, over 100 people die of suicide in the United States. This count has been leveraged by the Coronavirus Pandemic; more specifically, the effects of isolation and quarantine on our minds. September is national suicide prevention month. We hope to assist the cause with Motivational-Bot. It’s a Discord bot that sends users motivational quotes and GIFs. We believe that this bot can help gratify depressed end users and help individuals when they’re in dark times.

### Why did we choose to do this?

2020 has been a hard year for all of us. However, we have a friend that has been hit harder than most by the overwhelming events that occurred this year. He gets bullied and talks about suicide as a joke. We made this bot for him, with love.

### How did we accomplish this?

We used the Discord bot API, python, and a list of quotes + GIF URLs to accomplish this. We DEVOPSified the application by dockerizing it and implementing an automation script that abstracts all of the orchestration, configuration, and running of the bot for us. Our code is beautiful, elegant, and concise. The entire bot is implemented in 25 lines. We’ve formatted everything to the nearest character.
