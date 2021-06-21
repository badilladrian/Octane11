# Octane11
Code Challenge - Exchange Rate

The CLI has a command named history which pulls historical exchange conversions in a date range for a base currency and multiple other currencies. Arguments:
start - the start date, default today

end - the end date, default today

base - the base currency, default USD

symbol - the list of currency symbols to convert to (space separated), required

output - the file name to write the output to, optional


- It dumps the output in the standard output (or in a file if the argument output is passed) in JSONlines. An example:

'''
>$./exrates history --start 2021-02-01 --end 2021-02-02 --base USD --symbol EUR CAD
{"date":"2021-02-01", "base":"USD", "symbol":"CAD", "rate":1.2805362463} {"date":"2021-02-01", "base":"USD", "symbol":"EUR", "rate":0.8275405495} {"date":"2021-02-02", "base":"USD", "symbol":"CAD", "rate":1.2804716041} {"date":"2021-02-02", "base":"USD", "symbol":"EUR", "rate":0.8302889406}
'''

# With poetry as package dependency
execute through docker:
@command args1... argsn... args(output optional) 

Example:
history --start 2021-06-01 --end 2021-06-08 --base USD --symbol EUR --output usd_eur.json

convert --date 2021-06-01 --base USD --symbol EUR --amount 10



