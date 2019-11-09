if __name__ == "__main__":

    import pandas as pd

    data = pd.read_csv("legislators.csv") 


    today = pd.Timestamp.today()

    age = pd.to_datetime(data.birthdate).map(lambda b:
        int(today.year - b.year - ((today.month, today.day) < (b.month, b.day))
    ))

    data.insert(8, 'age', age)


    # First spreadsheet: 
    # All Democrats who are younger than 45 years old 

    democrats = data.loc[
        (data.party == 'D') &
        (data.age <= 45)
    ]

    print(democrats.head())
    democrats.to_excel(
        "young_democrats.xlsx", index=False
    )

    # Second spreadsheet: 
    # All Republicans who have Twitter accounts and YouTube channels

    republicans = data.loc[
        (data.party == 'R') &
        data.youtube_url.notnull() & 
        data.facebook_id.notnull()
    ]

    print(republicans.head())
    republicans.to_excel(
        "tech_savy_republicans.xlsx", index=False
    )

