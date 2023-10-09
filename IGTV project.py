# %%
import matplotlib.pyplot as plt

# %%
import pandas as pd

# %%
df = pd.read_csv('C:/Users/Francis Mwangi/Downloads/IGTV_DATA.csv')

# %%
df.head()


# %%
print(df)

# %%
df["date"] = pd.to_datetime(df['date'])

# %%
total_views = df["Views"].sum()

# %%
total_likes = df["Likes"].sum()

# %%
total_comments = df["Comments"].sum()

# %%
average_engagement_rate =((df['Likes'] + df['Comments'])  / df['Views'].mean() * 100

# %%
plt.plot (figsize= (10, 5))

# %%
plt.plot (df["date"], df ["Views"], label ="Views", marker = "o")

# %%
plt.plot (df["date"], df ["Likes"], label ="Likes", marker = "o")

# %%
plt.plot (df["date"], df ["Comments"], label ="Comments", marker = "o")

# %%
plt.xlabel("date")

# %%
plt.ylabel("Count")

# %%
plt.title("IGTV Video Engagement Over one month")

# %%
plt.legend()

# %%
plt.grid(True)

# %%
print("Engagement Summary for one Month")

# %%
print(f"Total Views: {total_views}")

# %%
print(f"Total Likes: {total_likes}")

# %%
print(f"Total Comments: {total_comments}")

# %%
print(f"Average Engagement Rate: {average_engangement_rate: .2f}%")

# %%
if total_likes > 1000 and total_comments > 100 and average_engagement_rate > 5.0:

# %%
print("This IGTV product has been successful in the past month.")

# %%
else:

# %%
print("This IGTV product may need improvement to achieve success.")

# %%
plt.show()

# %%


# %%



