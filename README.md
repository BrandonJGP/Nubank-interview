This is a challenge made by nu bank. 
This project will simulate a bank account with the following data structure.
Transaction:
    merchant: str
    amount: int
    time: datetime

Account:
    active: bool
    available_limit: int
    history: List[Transaction] = field(default_factory=list)


# 1. Clone / copy files, then:
python -m venv .venv && source .venv/bin/activate    # optional but neat
pip install -r requirements.txt

# 2. Execute the sample script
python -m src.main

# 3. Run the test suite 
pytest -q
