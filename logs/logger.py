import logging
from pathlib import Path
LOG_PATH = Path(__file__).parent / "agent.log"
logging.basicConfig(
  filename = LOG_PATH,
  level = logging.INFO
  format = "%(asctime)s [%(levelname)s] %(message)s"
)

def log(message):
  logging.info(message)
