import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/sample.csv")

    print(df)

    print(df["Age"] + 1)

    df["Names"] = df["Name"].str.rsplit(n=1)

    print(df)

    print(len(df))

    print(df.columns)

    print(df[["Name", "City"]])

    df[["Name", "City"]].to_csv("data/some_column.csv", index=False)

    print(df.groupby("City").count())

    df = df.drop(["Names", "Name"], axis=1)

    print(df)

    df = df.drop([1], axis=0)

    print(df)

    lookup = pd.DataFrame(
        {
            "City": ["İzmir", "İstanbul", "İstanbul", "İstanbul"],
            "District": ["Menemen", "Avcılar", "Beşiktaş", "Ümraniye"],
        }
    )

    print(lookup)

    print(df.merge(lookup, on=["City"]))

    d = df.merge(lookup, on=["City"]).to_dict("records")
    d2 = df.merge(lookup, on=["City"]).to_dict()

    print(d)
    print(d2)


    lookup # Dataframe
    lookup['City'] # Series
    lookup[['City']] # Dataframe

