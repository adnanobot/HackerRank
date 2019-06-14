"""
    Day 6 of 30 days of coding from hackerrank.com : Let's review

    author : adnanobot
"""

if __name__ == '__main__':
    print("\nPlease enter the no of test cases(from 1 to 10): ")
    T = int(input())

    # check_validity
    if (T >= 1 and T <= 10) is False:
        print("[Error] : Invalid no of inputs.")
    else:
        strings = []
        for i in range(0, T):
            # take the string input
            print("please enter the string %d : " % i)
            strings.append(input())

        for string in strings:
            # chekc the validity of the string
            if (len(string) >= 2 and len(string) <= 10000) is False:
                print("[Error] : String length is not appropriate.")
            else:
                odd_letters = ""
                even_letters = ""
                # loop through the string, character by character
                for i in range(0, len(string)):
                    # check the position
                    # if odd: odd_letters = string[i]
                    if (i % 2) != 0:
                        odd_letters += string[i]
                    else:
                        # else even : even_letters = string[i]
                        even_letters += string[i]

                print(even_letters, odd_letters)
