import re

# line = "Jan 19 09:46:51 ubuntu anacron[2275]: Updated timestamp for job `cron.weekly' to 2014-01-19"

regex = "^(?P<month>\S+) (?P<day>\d+) (?P<time>\d\d:\d\d:\d\d) (?P<message>.+)"

for line in open("/var/log/syslog"):
    match = re.match(regex, line)
    if match:
        fields = match.groupdict()
        print fields["time"]
