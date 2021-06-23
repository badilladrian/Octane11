""" CLI to pulls historical exchange conversions in a date range
for a base currency and multiple other currencies """
import argparse
import datetime
import json
import logging

import requests

TODAY = datetime.date.today().isoformat()
BASE_URL = "https://api.frankfurter.app"


def config_logger(handler, filename=""):
    """configures a logger"""
    if handler == "FileHandler":
        _handler = getattr(logging, handler)(filename, "w")
    if handler == "StreamHandler":
        _handler = getattr(logging, handler)()
    _handler.setFormatter(logging.Formatter("%(message)s"))
    _logger = logging.getLogger(f"{__name__}-{handler}")
    _logger.addHandler(_handler)
    _logger.setLevel(logging.INFO)
    return _logger


STREAM_LOGGER = config_logger("StreamHandler")


def history(start, end, base, symbol, output):
    """pulls historical exchange conversions in a date range for
    a base currency and multiple other currencies"""
    payload = {"from": base, "to": ",".join(symbol)}
    try:
        response = requests.get(f"{BASE_URL}/{start}..{end}", params=payload)
    except RequestException as exception:
        STREAM_LOGGER.error(exception)
        return
    rates = response.json().get("rates")
    entries = []
    for _date in rates:
        for _symbol in rates[_date]:
            entry = {
                "date": _date,
                "base": base,
                "symbol": _symbol,
                "rate": rates[_date][_symbol],
            }
            entries.append(json.dumps(entry))

    to_string = lambda e: "\n".join(entries)
    if len(output):
        FILE_LOGGER = config_logger("FileHandler", output)
        FILE_LOGGER.info(to_string(entries))
    else:
        STREAM_LOGGER.info(to_string(entries))
    return entries


def convert(date, base, symbol, amount):
    """currency conversion"""
    payload = {"amount": amount, "from": base, "to": symbol}
    response = requests.get(f"{BASE_URL}/{date}", params=payload)
    result = response.json().get("rates").get(symbol)
    STREAM_LOGGER.info(result)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="exrates")
    subparsers = parser.add_subparsers(dest="command", required=True, help="available commands")

    history_parser = subparsers.add_parser(
        "history",
        help="""pulls historical exchange conversions in a date range for"""
        """ a base currency and multiple other currencies""",
    )
    history_parser.add_argument("--start", default=TODAY, help="the start date, default today.")
    history_parser.add_argument("--end", default=TODAY, help="the end date, default today.")
    history_parser.add_argument("--base", default="USD", help="the base currency, default USD.")
    history_parser.add_argument(
        "--symbol",
        nargs="*",
        required=True,
        help="the list of currency symbols to convert to(space separated).",
    )
    history_parser.add_argument("--output", default="", help="the filename to write the output to.")

    convert_parser = subparsers.add_parser("convert", help="currency conversion")
    convert_parser.add_argument("--date", default=TODAY, help="the currency exchange date, default today.")
    convert_parser.add_argument("--base", default="USD", help="the base currency, default USD.")
    convert_parser.add_argument("--symbol", required=True, help="the currency symbol to convert to.")
    convert_parser.add_argument("--amount", type=float, required=True, help="the amount to convert.")

    args = parser.parse_args()

    result = ""
    if args.command == "history":
        history(args.start, args.end, args.base, args.symbol, args.output)
    if args.command == "convert":
        convert(args.date, args.base, args.symbol, args.amount)
