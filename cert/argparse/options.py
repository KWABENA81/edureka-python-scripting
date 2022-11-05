import argparse

import googlesearch


def greet(args):
    #output = '{0}, {1}!'.format(args.greeting, args.name)
    output = '{0}, {1}!'.format(args.searching, args.search)
    print(output)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

googlesearch_parser = subparsers.add_parser('googlesearch')
googlesearch_parser.add_argument('search')  # add the name argument
googlesearch_parser.add_argument('--searching', default='SEARCH')
googlesearch_parser.set_defaults(func=greet)

#googlesearch.search_google('nollywood')

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function
