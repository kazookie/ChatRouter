[English](https://github.com/kazookie/ChatRouter/blob/master/README.md),
[日本語](https://github.com/kazookie/ChatRouter/blob/master/README.ja.md)
# ChatRouter

ChatRouter is Transfer Twitch comments to text2speech software.

## Developer

### Environment
- python 3.9.13
- node 16.13.2

### Framework and main Libraries
- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue.js](https://vuejs.org/)
- [tmi.js](https://tmijs.com/)
- [axios](https://axios-http.com/)
- [Bulma](https://bulma.io/)

### Build
```
git clone https://github.com/kazookie/ChatRouter.git

# Install python packages
cd app
pip install -r requirements.txt

# Install node packages and build tmi.js
cd assets
node install
cd node_modules/tmi.js
npm install ; npm run build
```

### Run
```
# At app directory
uvicorn main:app --reload
```


## Reference
- [ゆかりねっと](http://www.okayulu.moe/)
- [音声認識 - WangDrive.](https://wangdora.rdy.jp/?plugin/voice_recognition)
- [SimpleVoiceroid2Proxy](https://github.com/SlashNephy/SimpleVoiceroid2Proxy)
- [棒読みちゃん](https://chi.usamimi.info/Program/Application/BouyomiChan/)
