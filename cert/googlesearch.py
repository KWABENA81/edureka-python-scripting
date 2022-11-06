import argparse

import google_search_topic


def search(args):
    # print('line {}', parser.parse_args(args))
    google_search_topic.search(parser.parse_args(args))


parser = argparse.ArgumentParser(description='Perform CLI Google search')
parser.add_argument('strings', metavar='\"The Search Item\"', help='the topic to search in googlesearch', type=str)
parser.add_argument('--search', help='search (default: search google)')
args = parser.parse_args()
# search(args)
# value = args.accumulate(args.string)
print(args)

# print(results)
if __name__ == '__main__':
    args = parser.parse_args()
    print('argument ', args)
    search(args)
    #print(results)
    # args.func(args)  # call the default function
