from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASES = {
    'promo_url': f"sqlite:///{BASE_DIR / 'magnit_promo_db.db'}",
}