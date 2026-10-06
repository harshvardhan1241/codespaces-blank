import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race?
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage of people who have a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )

    # 4. Percentage of people with advanced education
    # who make more than 50K
    advanced_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    higher_education_rich = round(
        (
            (df["salary"] == ">50K") &
            advanced_education
        ).sum()
        / advanced_education.sum()
        * 100,
        1
    )

    # 5. Percentage of people without advanced education
    # who make more than 50K
    lower_education = ~advanced_education

    lower_education_rich = round(
        (
            (df["salary"] == ">50K") &
            lower_education
        ).sum()
        / lower_education.sum()
        * 100,
        1
    )

    # 6. Minimum number of hours a person works per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people who work the minimum number
    # of hours and make >50K
    min_workers = df["hours-per-week"] == min_work_hours

    num_min_workers = min_workers.sum()

    rich_percentage = round(
        (
            (df["salary"] == ">50K") &
            min_workers
        ).sum()
        / num_min_workers
        * 100,
        1
    )

    # 8. Country with the highest percentage of people
    # who earn >50K
    country_percentage = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(
        country_percentage.max(),
        1
    )

    # 9. Most popular occupation for people who earn >50K in India
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # Do not modify below this line
    if print_data:
        print("Number of each race:")
        print(race_count)
        print("Average age of men:", average_age_men)
        print(
            "Percentage of people with a Bachelor's degree:",
            percentage_bachelors
        )
        print(
            "Percentage of people with higher education that earn >50K:",
            higher_education_rich
        )
        print(
            "Percentage of people without higher education that earn >50K:",
            lower_education_rich
        )
        print("Min work time:", min_work_hours, "hours/week")
        print(
            "Percentage of rich among people who work minimum hours:",
            rich_percentage
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country,
            highest_earning_country_percentage
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }