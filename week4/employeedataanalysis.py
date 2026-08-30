import sys
import argparse
import pandas as pd


# ---- COLUMN MAPPING ----
# Kaggle employee datasets use different column names depending on the source.
# Update these if your CSV's headers don't match.
DEPARTMENT_COL = "department"
SALARY_COL = "salary"


def load_data(csv_path):
    """Load employee data using Pandas."""
    print(f"Loading data from: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df):,} rows and {len(df.columns)} columns.")
    return df


def validate_columns(df):
    """Check that the expected columns exist, with a helpful error if not."""
    missing = [c for c in (DEPARTMENT_COL, SALARY_COL) if c not in df.columns]
    if missing:
        raise KeyError(
            f"Missing expected column(s): {missing}\n"
            f"Available columns: {list(df.columns)}\n"
            f"Update DEPARTMENT_COL / SALARY_COL at the top of this script "
            f"to match your CSV's actual headers."
        )


def calculate_average_salary(df):
    """Return the overall average salary."""
    return df[SALARY_COL].mean()


def calculate_department_count(df):
    """Return a Series of employee counts per department."""
    return df[DEPARTMENT_COL].value_counts()


def calculate_average_salary_by_department(df):
    """Return a Series of average salary per department."""
    return df.groupby(DEPARTMENT_COL)[SALARY_COL].mean().sort_values(ascending=False)


def filter_above_threshold(df, threshold):
    """Return only employees earning above the given salary threshold."""
    return df[df[SALARY_COL] > threshold]


def main():
    parser = argparse.ArgumentParser(description="Employee Data Analysis")
    parser.add_argument("csv_path", nargs="?", help="Path to the employee CSV file")
    parser.add_argument(
        "--threshold", type=float, default=None,
        help="Salary threshold for filtering (default: overall average salary)"
    )
    parser.add_argument(
        "--output", default="employees_above_threshold.csv",
        help="Output CSV filename (default: employees_above_threshold.csv)"
    )
    args = parser.parse_args()

    csv_path = args.csv_path or input("Enter path to employee CSV file: ").strip()

    df = load_data(csv_path)
    validate_columns(df)

    # --- Average salary ---
    avg_salary = calculate_average_salary(df)
    print(f"\nAverage Salary (all employees): {avg_salary:,.2f}")

    # --- Department count ---
    dept_counts = calculate_department_count(df)
    print("\n--- Employee Count by Department ---")
    for dept, count in dept_counts.items():
        print(f"{dept:<25}{count:>6}")

    # --- Average salary by department (bonus insight) ---
    dept_avg_salary = calculate_average_salary_by_department(df)
    print("\n--- Average Salary by Department ---")
    for dept, avg in dept_avg_salary.items():
        print(f"{dept:<25}{avg:>15,.2f}")

    # --- Filter by threshold ---
    threshold = args.threshold if args.threshold is not None else avg_salary
    filtered = filter_above_threshold(df, threshold)
    print(f"\nEmployees earning above {threshold:,.2f}: {len(filtered):,} "
          f"out of {len(df):,} ({len(filtered) / len(df) * 100:.1f}%)")

    # --- Export results ---
    filtered.to_csv(args.output, index=False)
    print(f"\nFiltered results exported to: {args.output}")

    # Also export summary stats to a second CSV for convenience
    summary_path = "employee_summary.csv"
    summary_df = pd.DataFrame({
        "department": dept_counts.index,
        "employee_count": dept_counts.values,
        "average_salary": dept_avg_salary.reindex(dept_counts.index).values,
    })
    summary_df.to_csv(summary_path, index=False)
    print(f"Department summary exported to: {summary_path}")


if __name__ == "__main__":
    main()