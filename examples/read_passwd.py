import sys

progname = sys.argv[0]
try:
    _, filename = sys.argv
except ValueError:
    print("Usage: {} <filename>".format(progname))
    sys.exit(1)


f = open("/etc/passwd")

# File format:
# '_dovecot:*:214:6:Dovecot Administrator:/var/empty:/usr/bin/false\n'

for line in f:
    fields = line.split(':')
    username, _, _, _, fullname, _, _ = fields
    print("User name: {}, Full name: {}".format(username, fullname))
