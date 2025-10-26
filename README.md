# GelBoorou Bulk Downloader

A small Python script to bulk-download images from Gelbooru using the XML/API.

**Note:** This tool downloads content from Gelbooru. Make sure you comply with Gelbooru’s Terms of Service and only download content you are permitted to. This project is provided as-is.

---

## Prerequisites

* Python 3.7+
* The following Python packages:

  * `requests`
  * `wget`

Install dependencies with:

```bash
pip install requests wget
```

---

## Usage

1. Place `GelBoorou_Bulk_Downloader.py` in any folder.

2. (Optional) Create a `config.json` file to store your API credentials and avoid entering them each time:

   ```json
   {
     "api_key": "YOUR_API_KEY",
     "user_id": "YOUR_USER_ID"
   }
   ```

3. Run the script:

   ```bash
   python GelBoorou_Bulk_Downloader.py
   ```

4. Follow the prompts:

   * Enter the limit of posts per page (1–100).
   * Enter how many pages to load.
   * If no `config.json` is found, you’ll be asked for your `APIKEY` and `USERID`, and offered to save them.
   * Optionally enter tags to filter results (leave blank for none).

---

## Output

* **`downloads/`** — Folder where all downloaded files are saved as `file<ID>.<ext>`.
* **`config.json`** — Created if you choose to save credentials.
* **`log.json`** — Contains metadata of all downloaded posts (page, file name, and URL).

---

## License

No license is included. Use at your own risk.
