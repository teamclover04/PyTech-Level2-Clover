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

    score_cols = [col for col in df.columns if "score" in col.lower()]

    for col in score_cols:
        if col not in df.columns:
            print(f"Column '{col}' missing.")
            return

    subject_means = df[score_cols].mean()

    plt.figure(figsize=(9, 5))
    bars= plt.bar(subject_means.index, subject_means.values,edgecolor="black",width=0.3)
    colors = ["#D11151", "#6657E8", "#71D63E"]
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    for bar in bars:
        height=bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f"{height:2f}", ha="center", va="bottom",font="Cambria",size=12,weight="bold")

    plt.title("Average Marks Per Subject",font="Cambria",size=16,weight="bold")
    plt.xlabel("Subjects",font="Cambria",size=14,weight="bold")
    plt.ylabel("Average Marks",font="Cambria",size=14,weight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.3)
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