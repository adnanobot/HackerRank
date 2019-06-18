"""
    Day 8 of 30 days of coding from hackerrank.com : Dictonaries and Maps

    author : adnanobot

    Note : ****** for  accepted submission the instructional print commands have
    to be removed.

"""
class PhoneBook:
    def __init__(self, no_of_entry):
        self.n = no_of_entry
        self.phBook = {}
        self.query = []

    def saveNewEntry(self):
        # take #n ph book entries - 3 name & ph no "name xxxxxx"
            # save name and no in dictionary format
        print("\n\nplease enter <name ph_no>: ")
        for i in range(0, self.n):
            entry = input().rstrip().split()
            self.phBook[entry[0]] = entry[1]

        print(self.phBook)

    def takeSearchEntries(self):
        # take name queries until the user gives an empty input
            # save the queries
        print("\n\nPlease enter search queries: ")
        while True:
            entry = input()
            if entry:
                self.query.append(entry)
            else:
                break
        print("queries: ", self.query)

    def searchAndDisplay(self):
        # search the name in the dictionary
            # if found then print(name=xxx)
            # else : print("Not found")
        print("\n\nSearch results: ")
        for entry in self.query:
            if entry in self.phBook:
                print(entry + "=" + self.phBook[entry])
            else: print("Not found")

if __name__ == '__main__':
    # Step 1 : take no of entries input <n> from the user
    print("Please enter the no of entries: ")
    n = int(input())

    # create an instance of PhoneBook class
    new_ph_book = PhoneBook(n)

    # Step 2: save entries into phone book
    new_ph_book.saveNewEntry()

    # Step 3: save search queries
    new_ph_book.takeSearchEntries()

    # Step 4: search and dispay results
    new_ph_book.searchAndDisplay()
