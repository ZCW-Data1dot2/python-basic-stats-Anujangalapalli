from statzcw.basicstat import *
import csv
import pandas as pd


df = pd.read_csv("datazero.csv", usecols=['x', 'y'])
print(zcount(df.x))
print(zmean(df.x))
print(zmedian(df.x))
print(round(zvariance(df.y), 2))

df2 = pd.read_csv("datazero.csv", usecols=['x', 'y'])
print(zcount(df2.x))
print(zstddev(df2.x))
print(zmedian(df2.x))
print(round(zcorr(df2.x,df2.y), 2))


df3 = pd.read_csv("datazero.csv", usecols=['x', 'y'])
print(zcount(df3.x))
print(zmean(df3.x))
print(zmedian(df3.x))
print(round(zvariance(df3.y), 2))


df4 = pd.read_csv("datazero.csv", usecols=['x', 'y'])
print(zcount(df4.x))
print(zstddev(df4.x))
print(zmedian(df4.x))
print(round(zcorr(df4.x,df4.y), 2))
