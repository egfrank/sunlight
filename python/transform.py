import argparse 
import logging

import pandas as pd

def determine_age(birthdate):
    today = pd.Timestamp.today()
    return int(today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)))



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Convert Sunlight csv into two csvs')
    parser.add_argument('csv',
         type=str
    )
    args = parser.parse_args()

    logging.info('Reading CSV: {}'.format(args.csv))
    data = pd.read_csv(args.csv)
    ages = pd.to_datetime(data.birthdate).map(determine_age)

    # First spreadsheet: 
    # All Democrats who are younger than 45 years old 
    logging.info('Producing spreadsheet of all Democrats who are younger than 45 years old')
    democrats = data.loc[
        (data.party == 'D') &
        (ages <= 45)
    ]

    democrats.to_csv(
        "./python/democrats.csv",
        index=False,
        float_format='%g'
    )
    logging.info('Spreadsheet output at ./python/democrats.csv')

    # Second spreadsheet: 
    # All Republicans who have Twitter accounts and YouTube channels

    republicans = data.loc[
        (data.party == 'R') &
        data.youtube_url.notnull() & 
        data.facebook_id.notnull()
    ]
    logging.info('Producing spreadsheet of all Republicans who have Twitter accounts and YouTube channels')
    republicans.to_csv(
        "./python/republicans.csv",
        index=False,
        float_format='%g'
    )
    logging.info('Spreadsheet output at ./python/republicans.csv')

