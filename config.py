import os

# Assuming you load environment variables from an .env file
from dotenv import load_dotenv
load_dotenv()

config = {
    "account_email": os.getenv("ACCOUNT_EMAIL", "centurion@mrfuntubbles.co.za"),
    "base_dir_path": os.getenv("BASE_DIR_PATH", r"C:\Users\cyanr\OneDrive\Documents\Centurion_Cashup_Data"),
    "keywords": ["Cashup", "cash up", "Cash up report"],
    "ignore_prefixes": ["RE:", "Re:", "RE", "Re"],
    "start_year": int(os.getenv("START_YEAR", "2024")),
    "start_month": int(os.getenv("START_MONTH", "3")),
}
