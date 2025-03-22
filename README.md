gmail-order-listener/
├── main.py
├── requirements.txt
├── README.md
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app.yaml
├── firebase.json
├── .firebaserc
└── credentials.json (OPTIONAL: only for initial OAuth if needed)# 📬 Gmail Order Listener

Listens to your Gmail inbox for order-related emails and parses them for processing.

## 🚀 One-Click Deploy

[![Deploy to Firebase](https://www.gstatic.com/mobilesdk/210513_mobilesdk/logo/2x/firebase_28dp.png)](https://console.firebase.google.com/project/_/overview?deploy=https://github.com/YOUR_USERNAME/gmail-order-listener)

## 🧰 Stack
- Python
- Google Auth
- Gmail API
- Firebase Hosting (or Google Cloud)

## 🧾 Setup
```bash
pip install -r requirements.txt
python main.py
