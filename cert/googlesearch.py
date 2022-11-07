import argparse

import google_search

parser = argparse.ArgumentParser(description='Perform CLI Google search')
parser.add_argument('search_string', metavar='\"The Search Item\"', help='the topic to search in googlesearch',
                    type=str)
args = parser.parse_args()

if __name__ == '__main__':
    args = parser.parse_args()
    results = google_search.search(args.search_string)
    for res in results:
        print(res)
