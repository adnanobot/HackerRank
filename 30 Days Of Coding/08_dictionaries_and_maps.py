"""
    Day 8 of 30 days of coding from hackerrank.com : Dictonaries and Maps

    author : adnanobot

    Note : ****** for  accepted submission the instructional print commands have
    to be removed.

"""
def saveInPhBook(n):
    # take #n ph book entries - 3 name & ph no "name xxxxxx"
        # save name and no in dictionary format
    phBook = {}
    print("\n\nplease enter <name ph_no>: ")
    for i in range(0, n):
        entry = input().rstrip().split()
        phBook[entry[0]] = entry[1]

    print(phBook)
    return phBook

def takeSearchEntries(phBook):
    # take name queries until the user gives an empty input
        # save the queries
    query = []
    print("\n\nPlease enter search queries: ")
    while True:
        entry = input()
        if entry:
            query.append(entry)
        else:
            break
    print("queries: ", query)
    return query

def searchAndDisplay(queries):
    # search the name in the dictionary
        # if found then print(name=xxx)
        # else : print("Not found")
    print("Search results: ")
    for entry in query:
        if entry in phBook:
            print(entry + "=" + phBook[entry])
        else: print("Not found")

if __name__ == '__main__':
    # Step 1 : take no of entries input <n> from the user
    print("Please enter the no of entries: ")
    n = int(input())

    # Step 2: save entries into phone book
    phBook = saveInPhBook(n)

    # Step 3: save search queries
    query = takeSearchEntries(phBook)

    # Step 4: search and dispay results
    searchAndDisplay(query)
