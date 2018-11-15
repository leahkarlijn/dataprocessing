import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

input_csv = "input.csv"
GDP = 'GDP ($ per capita) dollars'
IM = 'Infant mortality (per 1000 births)'

def clean():
    df = pd.read_csv(input_csv)
    df = df.dropna()
    df = df[df[GDP] != 'unknown']
    return df

def get_std(dataframe):
    df[GDP] = df[GDP].str.strip(' dollars')
    df[GDP] = pd.to_numeric(df[GDP])
    std = df[GDP].std()

def histo(dataframe):
    df2 = df[np.abs(df[GDP]-df[GDP].mean()) <= (3*df[GDP].std())]
    hist = df2[GDP].hist(bins=50)
    plt.xlabel('GDP (dollars)')
    plt.ylabel('std')
    plt.title('GPD histo')

def boxplot(dataframe):
    IM_list = []
    box_list = []
    for x in df[IM]:
        if ',' in x:
            x = x.replace(',', '.')
            x = float(x)
            IM_list.append(x)
        else:
            x = float(x)
            IM_list.append(x)
    IMp = np.array(IM_list)
    minimum = min(IM_list)
    box_list.append(minimum)
    firstq = np.percentile(IMp, 25)
    box_list.append(firstq)
    median = np.median(IMp)
    box_list.append(median)
    thirdq = np.percentile(IMp, 75)
    box_list.append(thirdq)
    maximum = max(IM_list)
    box_list.append(maximum)

    plt.boxplot(box_list)

def json(dataframe):
    df2 = df[['Country', 'Region', 'Pop. Density (per sq. mi.)', GDP, IM]]
    outfile = open('Final.json','w')
    outfile.write(df2.to_json(orient='index'))
    print(outfile)
    outfile.close()

if __name__ == '__main__':
    df = clean()
    std = get_std(df)
    histo = histo(df)
    box = boxplot(df)
    json = json(df)
