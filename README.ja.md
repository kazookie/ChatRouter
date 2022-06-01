# ChatRouter

Twitchのコメントを読み上げソフトに転送します。

## 開発者向け

### 環境
- python 3.9.13
- node 16.13.2

### 使用フレームワークと主なライブラリ
- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue.js](https://vuejs.org/)
- [axios](https://axios-http.com/)
- [Bulma](https://bulma.io/)

### ビルド方法
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

### 実行
```
# At app directory
uvicorn main:app --reload
```

## 参考サイト
- [ゆかりねっと](http://www.okayulu.moe/)
- [音声認識 - WangDrive.](https://wangdora.rdy.jp/?plugin/voice_recognition)
- [SimpleVoiceroid2Proxy](https://github.com/SlashNephy/SimpleVoiceroid2Proxy)
- [棒読みちゃん](https://chi.usamimi.info/Program/Application/BouyomiChan/)
