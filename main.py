from pathlib import Path
from data_loading import get_dataset

dataset_dir = Path("data")
train_dir = dataset_dir / "training_set"
test_dir = dataset_dir / "test_set"

train_ds = get_dataset(train_dir)
test_ds = get_dataset(test_dir)

image_batch, label_batch = next(iter(train_ds))
