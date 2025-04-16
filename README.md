# Bedre Skema

Bedre Skema er en desktop applikation, som viser dit lectio skema

## Setup

Bedre Skema gør brug af flere python pakker. For at installere dem alle kør denne kommando i mappen:

```bash
pip install -r installer.txt
```

Desuden skal Bedre Skema have adgang til dine lectio cookies. Dette gøres ved at oprette en .env fil med følgende variabler:

```bash
SESSION_ID=
AUTO_LOGIN_KEY=
```

Disse udfyldes, ved at:
- logge ind på lectio
- inspect
- gå ind på Application tab (google chrome)
- kopiere værdien **ASP.NET_SessionId** og **autologinkeyV2** ind i .env filen

## License

[MIT](https://choosealicense.com/licenses/mit/)