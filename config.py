from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class to store training parameters. Set this before running the train

    """

    NUM_LABELS: int = 23
    MAX_LEN: int = 64
    TRAIN_BATCH_SIZE: int = 8
    VALID_BATCH_SIZE: int = 4
    EPOCHS: int = 10
    LEARNING_RATE: int = 1e-05

    PRE_TRAINED_MODEL: str = "bert-base-uncased"
    DEVICE: str = "cpu"

    MODEL_DIR: str = "model_files"
    MODEL_NAME: str = "bert-topic-sentiment.bin"
    MODEL_NAME_COLAB: str = "bert-topic-sentiment-colab-final.bin"

    LOSS_FUN: str = "BCE"  # or 'focal'
