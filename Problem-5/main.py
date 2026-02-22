from model import load_dataset, sales_summary, plot_sales, export_summary


def main():
    while True:
        print("\n===== SALES SUMMARY DASHBOARD =====")
        print("1. Load Dataset")
        print("2. Show Sales Summary")
        print("3. Generate Line Chart")
        print("4. Export Summary Report")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            load_dataset()

        elif choice == "2":
            sales_summary()

        elif choice == "3":
            plot_sales()

        elif choice == "4":
            export_summary()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice...Enter number between 1–5.")


if __name__ == "__main__":
    main()
