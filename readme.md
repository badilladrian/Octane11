# Octane11

## History command

The CLI has a command named history which pulls historical exchange conversions in a date range for a base currency and multiple other currencies. Arguments:

- start: the start date, default today
- end: the end date, default today
- base: the base currency, default USD
- symbol: the list of currency symbols to convert to (space separated), required
- output: the file name to write the output to, optional

It dumps the output in the standard output (or in a file if the argument output is passed) in JSON lines

### History example

```bash
$ ./exrates history --start 2021-02-01 --end 2021-02-02 --base USD --symbol EUR CAD
{"date": "2021-02-01", "base": "USD", "symbol": "CAD", "rate": 1.2805362463}
{"date": "2021-02-01", "base": "USD", "symbol": "EUR", "rate": 0.8275405495}
{"date": "2021-02-02", "base": "USD", "symbol": "CAD", "rate": 1.2804716041}
{"date": "2021-02-02", "base": "USD", "symbol": "EUR", "rate": 0.8302889406}
```

## Convert convert

convert for doing currency conversion. Arguments:

- date: the currency exchange date, default today
- base: the base currency, default USD
- symbol: the currency symbol to convert to, required
- amount: the amount to convert, required

### Convert example

```bash
$ ./exrates convert --date 2021-02-01 --base USD --symbol EUR --amount 50
41.377027475
```
