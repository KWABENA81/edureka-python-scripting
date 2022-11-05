try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    query = "Geeksforgeeks"

    for i in search(query, tld="co.in", num=15, stop=5, pause=2):
        print(i)
