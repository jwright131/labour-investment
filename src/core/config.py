from pathlib import Path

APP_TITLE = "Labour Visualizations Dashboard"
APP_ICON = "📊"
APP_LAYOUT = "wide"
APP_CAPTION = "Each chart has its own filters, and the map uses province pie markers."

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

EMPLOYEE_FILE = DATA_DIR / "Employee Count Complete.csv"
VACANCY_FILE = DATA_DIR / "Job Vacancy Complete.csv"
INVESTMENT_FILE = DATA_DIR / "Investment Completed (1).csv"
WAGE_FILE = DATA_DIR / "Wage Completed.csv"
