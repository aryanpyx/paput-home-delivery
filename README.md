# Paput Menorca - Home Delivery (English Version)

[![Netlify Status](https://api.netlify.com/api/v1/badges/bbdf8083-d9d1-4475-b82b-8a8f15cc3b83/deploy-status)](https://paput-home-delievery.netlify.app)

This repository contains the localized English version of the [Paput Menorca website](https://www.paputmenorca.com/). It uses a custom Node.js scraper to download the original Spanish site, followed by a Python post-processing script to replace Spanish text with English translations.

## 🚀 Live Demo

The website is automatically built and deployed on Netlify:
👉 **[paput-home-delievery.netlify.app](https://paput-home-delievery.netlify.app)**

---

## 🛠️ Project Structure

- **`netlify.toml`**: Netlify deployment configuration.
- **`site/www.paputmenorca.com/`**: The core website files downloaded from the source.
  - **`replace.py`**: Python script that runs over the downloaded HTML files to perform translations and text replacements.
  - **`build.sh`**: Bash build script used by Netlify to execute `replace.py` and package the static files into `dist/`.
  - **`build.bat`**: Windows batch file equivalent for local testing.
  - **`dist/`**: The compiled, translated website folder served to users.
- **`scrape.js`**: Node.js script using `website-scraper` to pull the latest version of the site.

---

## 💻 Local Development

### 1. Build and Run the App

Ensure you have Python installed. To build the translation assets locally:

**On Windows:**
Run the batch file in the terminal:
```bash
cd site/www.paputmenorca.com
.\build.bat
```

**On macOS/Linux:**
```bash
cd site/www.paputmenorca.com
chmod +x build.sh
./build.sh
```

This will run the translation script and output the static files to `site/www.paputmenorca.com/dist`.

### 2. Serve Locally

You can serve the build locally using `serve` or any static file server:
```bash
npx serve site/www.paputmenorca.com/dist
```

---

## 📝 Customizing Translations

To add or update translations, open [replace.py](site/www.paputmenorca.com/replace.py) and modify the `replacements` dictionary:

```python
replacements = {
    'CONTÁCTANOS': 'CONTACT US',
    'HACER PEDIDO': 'PLACE ORDER',
    # Add new translations here...
}
```
Once updated, rebuild the project using `build.bat` or `build.sh`.
