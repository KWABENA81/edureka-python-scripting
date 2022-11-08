# Q1:   Create a python script called googlesearch that provides a command line utility
#       to perform google search. It gives you the top links (search results) of whatever
#       you want to search on google.
import argparse
import google_search

parser = argparse.ArgumentParser(description='Perform CLI Google search')
parser.add_argument(dest='input', metavar='\"search item\"', nargs='+',
                    help='the topic to search in googlesearch', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    args = parser.parse_args()
    results = google_search.search(args.input)
    for res in results:
        print(res)
