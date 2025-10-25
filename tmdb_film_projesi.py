import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("../veri/tmdb_5000_movies.csv", delimiter=",")
df=df.drop(columns=["homepage","id","keywords","original_language","overview","production_companies","production_countries","revenue",
            "spoken_languages","status","tagline","vote_count","original_title","genres"])

df_clean=df[(df["runtime"]>0) & (df["vote_average"].notna()) & (df["budget"]>0) & (df["popularity"]>0) & (df["release_date"].notna())].copy()

#Finding how runtime affects the average vote
runtime_over_180 = df_clean[df_clean["runtime"] >= 180]
runtime_over_180_mean = runtime_over_180["vote_average"].mean()

runtime_under_180 = df_clean[df_clean["runtime"] < 180]
runtime_under_180_mean = runtime_under_180["vote_average"].mean()

print("Average Vote for Movies Over 180 Minutes: {:.2f}".format(runtime_over_180_mean))
print("Average Vote for Movies Under 180 Minutes: {:.2f}".format(runtime_under_180_mean))

plt.figure(figsize=(10, 6))
plt.scatter(df_clean['runtime'], df_clean['vote_average'],
            alpha=0.6, color='#1f77b4', s=20)

# Critical Threshold: 180 Minutes (Vertical Line)
plt.axvline(x=180, color='r', linestyle='--', linewidth=2, label='180 Minute Threshold')

# Add average vote for movies over threshold as text
plt.text(185, 9.0,
         "Long Movies Avg: {:.2f}".format(runtime_over_180_mean),
         color="r",
         fontsize=10)

# Add average vote for movies under threshold as text
plt.text(10, 9.0,
         "Short Movies Avg: {:.2f}".format(runtime_under_180_mean),
         color='r',
         fontsize=10)

plt.title('Relationship Between Movie Runtime and Average Vote', fontsize=14)
plt.xlabel('Runtime (minutes)', fontsize=12)
plt.ylabel('Average Vote', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, 300)
plt.ylim(0, 10)
plt.legend()
plt.savefig('figure_1.png')
plt.show()

#Finding how budget affects the average vote
budget_threshold = df_clean["budget"].mean()

high_budget = df_clean[df_clean["budget"] >= budget_threshold]
high_budget_vote_average = high_budget["vote_average"].mean()
print("\nThe average vote of those with a budget of 40 million dollars or more: {:.2f}".format(high_budget_vote_average))

low_budget = df_clean[df_clean["budget"] < budget_threshold]
low_budget_vote_average = low_budget["vote_average"].mean()
print("The average vote of those with a budget under 40 million dollars: {:.2f}".format(low_budget_vote_average))

plt.figure(figsize=(8, 6))
plt.bar(["High Budget Movies", "Low Budget Movies"],
        [high_budget_vote_average, low_budget_vote_average],
        color=['skyblue', 'lightcoral'])
plt.title("AVERAGE VOTE BY HIGH/LOW BUDGET")
plt.xlabel("Movie Category")
plt.ylabel("Average Vote")
plt.ylim(5.8, 6.3)
plt.savefig('figure_2.png')
plt.show()

#Finding how popularity affects the average vote
popularity_threshold = df_clean["popularity"].mean()

high_popularity = df_clean[df_clean["popularity"] >= popularity_threshold]
high_popularity_mean = high_popularity["vote_average"].mean()
print("\nAverage vote for high popularity movies: {:.2f}".format(high_popularity_mean))

low_popularity = df_clean[df_clean["popularity"] < popularity_threshold]
low_popularity_mean = low_popularity["vote_average"].mean()
print("Average vote for low popularity movies: {:.2f}".format(low_popularity_mean))

plt.figure(figsize=(10, 6))
plt.bar(
    ["High Popularity Movies", "Low Popularity Movies"],
    [high_popularity_mean, low_popularity_mean],
    color=["powderblue", "sandybrown"]
)
plt.title("AVERAGE VOTE BY POPULARITY")
plt.xlabel("Popularity Category")
plt.ylabel("Average Votes")
plt.ylim(5.5, 6.7)
plt.savefig('figure_3.png')
plt.show()

#Finding how the release date affects the average vote
df_clean["release_date"] = pd.to_datetime(df_clean["release_date"], format="%Y-%m-%d")

before_2000 = df_clean[df_clean["release_date"].dt.year <= 2000]
before_2000_mean = before_2000["vote_average"].mean()
print("\nAverage vote for movies before 2000: {:.2f}".format(before_2000_mean))

between_2000_2009 = df_clean[(df_clean["release_date"].dt.year > 2000) & (df_clean["release_date"].dt.year <= 2009)]
between_2000_2009_mean = between_2000_2009["vote_average"].mean()
print("Average vote for movies between 2000-2009: {:.2f}".format(between_2000_2009_mean))

after_2010 = df_clean[df_clean["release_date"].dt.year >= 2010]
after_2010_mean = after_2010["vote_average"].mean()
print("Average vote for movies after 2010: {:.2f}".format(after_2010_mean))

plt.figure(figsize=(10, 6))
plt.bar(
    ["Movies Before 2000", "Movies 2000-2009", "Movies After 2010"],
    [before_2000_mean, between_2000_2009_mean, after_2010_mean],
    color=["slategray", "seagreen", "goldenrod"]
)
plt.title("AVERAGE VOTE BY RELEASE YEAR")
plt.xlabel("Years")
plt.ylabel("Average Votes")
plt.ylim(5.5, 7.0)
plt.savefig('figure_4.png')
plt.show()