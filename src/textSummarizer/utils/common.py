import os
from box.exceptions import  BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and retyurn it
    
    arg: path_to_yaml(str): path like imput
     
    Raise:
       ValueError: if yaml file is empty
        e:empty file
         
     Return:
      ConfigBox: config box objectConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 

@ensure_annotations
def create_directory(path_to_directories: list, verbose=True):
    """create list of directries
    args:
        path_to_directories(list): list of path of directories
        ignore_log (bool,optional): ignore if multiple directries is to be created. Default to False.
        """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path:Path)-> str:
    """get size in kb
    
    Args:
        path(Path): path of the file
    returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} kb"
