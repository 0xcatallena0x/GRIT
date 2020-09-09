# GRIT
A tool that is created to gather up disclosed reports in hackerone that is related to a certain vulnerability.

Reminder: After gathering up the links it would save the output to a file


## Usage
```
usage: GRIT.py [-h] -v VULN [-n NUMBEROFREPORTS] [-p SECONDS]

optional arguments:
  -h, --help          show this help message and exit
  -v VULN             The vulnerability that you want to gather h1 reports
  -n NUMBEROFREPORTS  The number of how many reports you want to gather. DEFAULT: 100
  -p SECONDS          How much second/seconds do you want it to wait between HTTP Requests, I
                      highly recommend to set this up so that we can avoid getting banned by
                      google. DEFAULT: 2

```
