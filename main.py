import pandas as pd
from pandas import DataFrame


def descriptionToBuySellCategory(description: str):
    if description.startswith('Bought'):
        return 'Buy'
    elif description.startswith('Sold'):
        return 'Sell'
    else:
        return 'Other'


def generateBuySellCategory(df: DataFrame) -> DataFrame:
    df['Type'] = df['DESCRIPTION'].apply(descriptionToBuySellCategory)
    return df


def projectToTracker(df: DataFrame):
    df = generateBuySellCategory(df)
    df['Date'] = df['DATE']
    df['Stock'] = df['SYMBOL']
    df['Transacted Units'] = df['QUANTITY']
    df['Transacted Price (per unit)'] = df['PRICE']
    df = df[df['Type'] != 'Other']
    return df[['Date', 'Type', 'Stock', 'Transacted Units', 'Transacted Price (per unit)']]


if __name__ == '__main__':
    df = pd.read_csv('inputs/transactions.csv', skipfooter=1)
    df = df[['DATE', 'SYMBOL', 'DESCRIPTION', 'QUANTITY', 'PRICE', 'AMOUNT']]
    df = projectToTracker(df)
    df.to_csv('outputs/output_transactions.csv', index=False, header=False)
    print(df.head())


