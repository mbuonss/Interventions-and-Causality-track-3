from src.data_loader import DatasetLoader

def main():
    loader = DatasetLoader("data/train_set.json")
    data = loader.load()
    print("Loaded data:", data)


if __name__ == "__main__":
    main()