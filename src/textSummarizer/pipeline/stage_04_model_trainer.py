from textSummarizer.config.configuration import configurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = configurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()