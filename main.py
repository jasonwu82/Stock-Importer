import pandas as pd


def descriptionToBuySellCategory(description: str):
    print(description)
    if description.startswith('Bought'):
        return 'Buy'
    elif description.startswith('Sold'):
        return 'Sell'
    else:
        return 'Other'


def generateBuySellCategory(df):
    df['type'] = df['DESCRIPTION'].apply(descriptionToBuySellCategory)
    return df


if __name__ == '__main__':
    data = pd.read_csv('inputs/transactions.csv', skipfooter=1)
    data = generateBuySellCategory(data)
    print(data.head())


