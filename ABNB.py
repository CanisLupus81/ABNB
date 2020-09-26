import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import descartes
from shapely.geometry import Point, Polygon
import numpy as np
df = pd.read_csv("AB_NYC_2019.csv")
df.loc[df["neighbourhood_group"]=="Manhattan"
mean_for_man=df.groupby("neighbourhood_group").mean()['price']
type(mean_for_man.head())
mean_for_man.to_frame()
ax=mean_for_man.plot.bar(y="price", rot=0)
ax.set_xlabel("NYC Boroughs")
ax.set_ylabel("Average Price")
ax.set_title("Average Price for Airbnb in NYC")
plt.savefig("Avg_ABNB.png")
graphing=df.drop_duplicates(subset="host_name", keep=False, inplace=False)
z=graphing.loc[graphing["neighbourhood_group"]=="Manhattan"]
street_map=gpd.read_file("nyu-2451-34522-geojson.json")
fig,ax=plt.subplots(figsize=(15,15))
street_map.plot(ax=ax)
geometry=[Point(xy) for xy in zip(z["longitude"], z["latitude"])]
geometry[:3]
geo_df=gpd.GeoDataFrame(z,geometry=geometry)
geo_df.head(100)
fig,ax=plt.subplots(figsize=(15,15))
street_map.plot(ax=ax,alpha=0.4,color="grey")
geo_df[geo_df["price"]<=200].plot(ax=ax,markersize=10,color="red",marker="o", label="ABNB under $200")
geo_df[geo_df["price"]>200].plot(ax=ax,markersize=12,color="blue",marker="^",label="ABNB $200-$400")
geo_df[geo_df["price"]>400].plot(ax=ax,markersize=15,color="yellow",marker="x",label="ABNB $400+")
plt.legend(prop={'size':15})
plt.savefig("ABNB_Manhattan.png")
