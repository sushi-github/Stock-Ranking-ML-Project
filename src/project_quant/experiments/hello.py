from pathlib import Path
import yaml

def main():
    # Resolve project root (…/stock-ranking-ml)
    ROOT = Path(__file__).resolve().parents[3]
    config_path = ROOT / "configs" / "base.yaml"

    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    print("Loaded config:")
    print(cfg["project"]["name"])
    print("Tickers:", len(cfg["data"]["universe"]["tickers"]))
    print("Horizon:", cfg["label"]["horizon_days"])
    print(
        "Outer/Inner splits:",
        cfg["validation"]["outer_splits"],
        cfg["validation"]["inner_splits"],
    )

if __name__ == "__main__":
    main()