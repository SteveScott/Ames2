# -*- coding: utf-8 -*-
import os
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd

#
#@click.command()
#@click.argument('input_filepath', type=click.Path(exists=True))
#@click.argument('output_filepath', type=click.Path())
#def main(input_filepath, output_filepath):
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    """ configuration """
    working_directory = os.path.dirname(os.path.realpath(__file__))
    root_directory = Path(__file__).resolve().parents[2]
    test_data_path = os.path.join(root_directory, os.path.join('data','raw', 'test1.csv'))
    train_data_path = os.path.join(root_directory, os.path.join('data', 'raw', 'train1.csv'))
    
    input_filepath = os.path.join(root_directory, os.path.join('data', 'raw'))
    output_filepath = os.path.join(root_directory, os.path.join('data', 'processed'))
    """ end configuration """
    
    
    test_dataframe = pd.read_csv(test_data_path)
    train_dataframe = pd.read_csv(train_data_path)
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files


    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
