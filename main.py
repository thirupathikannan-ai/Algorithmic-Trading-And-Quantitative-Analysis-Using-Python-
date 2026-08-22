from src.experiment import run_experiment


def main():
    results = run_experiment()

    print("\n===== ALGORITHMIC TRADING RESEARCH =====\n")

    print("Strategy Performance:")
    print(results["performance"].to_string())

    print("\nBest Strategy:")
    print(results["best_strategy"])

    print("\nExperiment completed successfully.")


if __name__ == "__main__":
    main()
