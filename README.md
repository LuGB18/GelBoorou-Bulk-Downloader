# GelBoorou Bulk Downloader

A small Python script to bulk-download images from Gelbooru using the XML/API.

Important: This tool downloads content from Gelbooru. Ensure you follow Gelbooru's terms of service and only download content you are allowed to. This project is provided as-is.

Prerequisites
- Python 3.7+
- The following Python packages:
  - requests
  - wget

You can install them with pip:

```powershell
pip install requests wget
```

Usage
1. Place the `GelBoorou_Bulk_Downloader.py` script in a folder.
2. (Optional) Create a `config.json` file with the following structure to avoid entering API credentials each run:

```json
{
  "api_key": "YOUR_API_KEY",
  "user_id": "YOUR_USER_ID"
}
```

3. Run the script:

```powershell
python GelBoorou_Bulk_Downloader.py
```

4. Follow the prompts:
- Enter the limit of posts per page (max 100).
- Enter how many pages to load.
- If no `config.json` is found you'll be asked for `APIKEY` and `USERID` and offered the option to save them.
- Optionally enter tags to filter results (leave blank for no filter).

Files created by the script
- `downloads/` — directory where images are stored as `file<ID>.<ext>`.
- `config.json` — if you choose to save credentials.

License
This repository does not include a license file. Use at your own risk.
