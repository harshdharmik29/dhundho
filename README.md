# 🛍️ Dhundho

**Saw it in a reel? Find it here.**

🔗 **Live App:** [dhundho.streamlit.app](https://dhundho.streamlit.app/)

Dhundho is an AI-powered tool that helps you find products you spot in Instagram/social media reels. Upload a screenshot, and the AI identifies what's in the image, then generates direct search links across popular Indian e-commerce platforms.

---

## 🚀 Features

- 📸 **Image Upload** — Upload any screenshot from a reel or social media post
- 🤖 **AI Image Captioning** — Uses BLIP (Salesforce) to describe what's in the image
- 🏷️ **Smart Category Detection** — Automatically classifies into Fashion, Electronics, Food, or Home Decor
- 🛒 **Instant Shopping Links** — Get direct search links to:
  - Amazon, Flipkart (always)
  - Myntra, Meesho (fashion)
  - Croma (electronics)
  - Zomato, Swiggy (food)
  - Pepperfry, IKEA (home decor)

---

## 🛠️ Tech Stack

- **Frontend/App**: Streamlit
- **AI Model**: BLIP (Salesforce/blip-image-captioning-base) via Hugging Face Transformers
- **Language**: Python

---

## 📦 Installation & Local Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/dhundho.git
   cd dhundho
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deployment

This app is deployed on [Streamlit Community Cloud](https://share.streamlit.io).

To deploy your own:
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repo, set main file path to `app.py`
5. Click Deploy

---

## 🔮 Future Improvements

- CLIP-based visual similarity search for more accurate product matching
- Affiliate link integration for monetization
- Direct reel/video upload support (not just screenshots)
- Price comparison across platforms

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙋‍♂️ Author

Built by Harsh — ETC student exploring AI/ML applications for everyday problems.
