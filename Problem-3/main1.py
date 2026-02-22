from model1 import (load_dataset, calculate_average, highest_lowest_scorer, plot_bar_chart, plot_histogram )


def main():
    while True:
        print("\n===== STUDENT MARKS ANALYZER =====")
        print("1. Load Dataset")
        print("2. Calculate Average Marks")
        print("3. Show Highest & Lowest Scorer")
        print("4. Generate Bar Chart")
        print("5. Generate Histogram")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            load_dataset()

        elif choice == "2":
            calculate_average()

        elif choice == "3":
            highest_lowest_scorer()

        elif choice == "4":
            plot_bar_chart()

        elif choice == "5":
            plot_histogram()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Enter number between 1–6.")


if __name__ == "__main__":
    main()
