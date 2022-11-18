from api import get_list_monthly_summary, get_monthly_summary

if __name__ == "__main__":
    s = get_monthly_summary("Jan", expire=15*60)

    print(s)

    s = get_list_monthly_summary(["Jan","Mar"], expire=15*60)

    print(s)

    s = get_list_monthly_summary(None, expire=15*60)

    print(s)
