import argparse

import googlesearch


def greet(args):
    #output = '{0}, {1}!'.format(args.greeting, args.name)
    output = '{0}, {1}!'.format(args.searching, args.search)
    googlesearch.search_google(args)
    print({1})


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

googlesearch_parser = subparsers.add_parser('googlesearch')
googlesearch_parser.add_argument('search')  # add the name argument
googlesearch_parser.add_argument('--searching', default='SEARCH')
googlesearch_parser.set_defaults(func=greet)


#print(results)
if __name__ == '__main__':
    args = parser.parse_args()
    print('argument ',args)
    args.func(args)  # call the default function
