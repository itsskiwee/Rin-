from pathlib import Path

def load_identity():
  identity_path = Path(__file__).parent / "identity.txt"
  return identity_path.read_text()
