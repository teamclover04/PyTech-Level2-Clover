import pandas as pd
import matplotlib.pyplot as plt

df = None
summary_df = None


def load_dataset():
    global df
    file_path = input("Enter dataset file path: ").strip()

    try:
        df = pd.read_csv(file_path, encoding="latin1")

        if df.empty:
            print("Dataset is empty.")
            return

        print("Dataset loaded successfully.")
        print(df.head())

    except FileNotFoundError:
        print("File not found. Check path.")
    except Exception as e:
        print("Error loading dataset:", e)


def sales_summary():
    global df, summary_df

    if df is None:
        print("Load dataset first.")
        return

    required_columns = ["PRODUCTLINE", "SALES"]

    for col in required_columns:
        if col not in df.columns:
            print(f"Column '{col}' missing in dataset.")
            return

    try:
        summary_df = (
            df.groupby("PRODUCTLINE")["SALES"].sum().reset_index().sort_values(by="SALES", ascending=False))
        print("\nTotal Sales Per Product:")
        print(summary_df)

    except Exception as e:
        print("Processing error:", e)


def plot_sales():
    global summary_df

    if summary_df is None:
        print("Generate summary first.")
        return

    try:
        plt.figure(figsize=(10, 5))
        plt.plot(summary_df["PRODUCTLINE"],summary_df["SALES"], marker="o",color='royalblue',linewidth=2,markersize=7)
        plt.ticklabel_format(style='plain', axis='y')
        offset = max(summary_df["SALES"]) * 0.03
        for x, y in zip(summary_df["PRODUCTLINE"], summary_df["SALES"]):
            plt.text(x, y+ offset, f"{int(y)}",ha='center',va='bottom',fontsize=9,fontweight="bold")
        plt.ylim(0, max(summary_df["SALES"]) * 1.15)    
        plt.title("Sales Trend Per Product",font="Cambria",fontsize=16,fontweight="bold")
        plt.xlabel("Product Line",font="Cambria",fontsize= 14,fontweight="bold")
        plt.ylabel("Total Sales",font="Cambria",fontsize=14,fontweight="bold")
        plt.xticks(rotation=30)
        plt.grid(True, linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Plotting error:", e)


def export_summary():
    global summary_df

    if summary_df is None:
        print("Generate summary first.")
        return

    filename = input("Enter filename (without extension): ").strip()

    if not filename:
        print("Invalid filename.")
        return

    try:
        summary_df.to_csv(f"{filename}.csv", index=False)
        print(f"Summary exported to {filename}.csv")

    except Exception as e:
        print("Export error:", e)