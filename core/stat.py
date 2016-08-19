#!/usr/bin/env python
# encoding: utf-8
import sys
import argparse
import pstats


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='stat filename', action='store', required=True)
    parser.add_argument('-s', '--sort', help='sort type: cumulative, time', action='append')
    parser.add_argument('-p', '--percent', help='sort type', action='store', default=0.5, type=float)
    parser.add_argument('-d', '--dir', help='show directory', action='store_true')
    return parser


def main():
    args = build_parser().parse_args()
    p = pstats.Stats(args.file)

    sort_keys = args.sort or ('cumulative', 'time')

    if not args.dir:
        p = p.strip_dirs()

    p.sort_stats(*sort_keys).print_stats(args.percent)


if __name__ == '__main__':
    main()
