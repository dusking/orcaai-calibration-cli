import sys
import logging
import argparse
from typing import List

from calibration import Calibration

logger = logging.getLogger(__name__)


def pose_estimation(args: argparse.Namespace):
    Calibration().run_pose_estimation(args.ship)


def parse_args(argv: List[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity level")

    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser("pose-estimation", help=pose_estimation.__doc__)
    search_parser.set_defaults(command=pose_estimation)
    search_parser.add_argument("--ship", type=str, help="Ship name")

    return parser.parse_args(argv)


def main():
    argv = sys.argv
    args = parse_args(argv[1:])
    logging.basicConfig(
        level=logging.WARNING - (args.verbose * 10),
        format="%(asctime)s %(message)s",
    )
    if args.command:
        return args.command(args)
    else:
        print("No command given, use --help for usage")
        return 1


if __name__ == "__main__":
    sys.exit(main())
