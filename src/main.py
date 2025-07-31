from datetime import datetime
from src.data_structure import Account, Transaction

def main() -> None:
    acct = Account(active=True, available_limit = 1000)

    sample_txn = Transaction(
        merchant="Nu-bank",
        amount = 200,
        time = datetime.now(),
    )

    print("[debug] Before purchase:", acct)
    acct.register(sample_txn)
    print("[debug] After purchase:", acct)

    print("\n Transaction history:")
    for t in acct.history:
        print("  •", t)

if __name__ == "__main__":
    main()