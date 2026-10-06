import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Years from the first year through 2050
    years = pd.Series(
        range(df["Year"].min(), 2051)
    )

    plt.plot(
        years,
        slope * years + intercept,
        label="Line of best fit"
    )

    # Second line of best fit using data from 2000 onward
    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, _, _, _ = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = pd.Series(
        range(2000, 2051)
    )

    plt.plot(
        years_recent,
        slope_recent * years_recent + intercept_recent,
        label="Line of best fit since 2000"
    )

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig("sea_level_plot.png")

    return plt.gca()