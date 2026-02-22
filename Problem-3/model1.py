import pandas as pd
import matplotlib.pyplot as plt

df = None


def load_dataset():
    global df

    file_path = input("Enter dataset file path: ").strip()

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            print("Dataset is empty.")
            return

        print("Dataset loaded successfully.")
        print(df.head())

    except FileNotFoundError:
        print("File not found. Check path.")
    except Exception as e:
        print("Error loading dataset:", e)


def calculate_average():
    global df

    if df is None:
        print("Load dataset first.")
        return
    score_cols = [col for col in df.columns if "score" in col.lower()]

    if not score_cols:
        print("No score columns found.")
        return

    df["Average"] = df[score_cols].mean(axis=1)

    print("\nAverage Marks Calculated:")
    print(df[score_cols + ["Average"]].head(100))


def highest_lowest_scorer():
    global df

    if df is None:
        print("Load dataset first.")
        return

    if "Average" not in df.columns:
        print("Calculate average first.")
        return

    highest = df.loc[df["Average"].idxmax()]
    lowest = df.loc[df["Average"].idxmin()]

    print("\nHighest Scorer:")
    print(highest)

    print("\nLowest Scorer:")
    print(lowest)


def plot_bar_chart():
    global df

    if df is None:
        print("Load dataset first.")
        return

    if "gender" not in df.columns:
        print("Gender column not found.")
        return

    score_cols = [col for col in df.columns if "score" in col.lower()]

    gender_avg = df.groupby("gender")[score_cols].mean()

    x = range(len(score_cols))
    width = 0.35

    plt.figure(figsize=(9,5))

    boys = plt.bar([i - width/2 for i in x], gender_avg.loc["male"],width,label="Boys",color="#438BD8",edgecolor="black")

    girls = plt.bar([i + width/2 for i in x],gender_avg.loc["female"],width,label="Girls", color="#D42D68",edgecolor="black")

    for bars in [boys, girls]:
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.1f}", ha="center", va="bottom", fontsize=10,fontweight="bold")

    plt.xticks(x, score_cols)

    plt.title("Average Marks by Gender per Subject",fontname="Cambria",fontsize=16, fontweight="bold")

    plt.xlabel("Subjects", fontname="Cambria", fontsize=14,fontweight="bold")
    plt.ylabel("Average Marks", fontname="Cambria", fontsize=14,fontweight="bold")

    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    def format_coord(x, y):
        subject = list(score_cols)
        index = int(round(x))

        if 0 <= index < len(subject):
            return f"(Subject: {subject[index]}, Marks: {y:.2f})"
        else:
            return f"(Marks: {y:.2f})"

    plt.gca().format_coord = format_coord

    plt.tight_layout()
    plt.show()
def plot_histogram():
    global df

    if df is None:
        print("Load dataset first.")
        return

    if "Average" not in df.columns:
        print("Calculate average first.")
        return

    plt.figure(figsize=(8, 5))
    plt.hist(df["Average"], bins=15,edgecolor="black",color="lightgreen")
    mean_val = df["Average"].mean()
    plt.axvline(mean_val,linestyle="--",linewidth=2)
    plt.title("Distribution of Student Average Marks",font="Cambria",size=16,weight="bold")
    plt.xlabel("Average Marks",font="Cambria",size=14,weight="bold")
    plt.ylabel("Number of Students",font="Cambria",size=14,weight="bold")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

