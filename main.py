from textSummarizer.pipeline.stage_01_data_ingestion import DataIntegrationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Integration Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion =DataIntegrationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e