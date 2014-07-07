#!/usr/bin/env python
# encoding: utf-8

# License: AGPL v3 - http://www.gnu.org/copyleft/gpl.html 
# Copyright: Christophe Vandeplas <christophe@vandeplas.com>

import argparse
import re
import tempfile
import shutil
# parse the arguments
parser = argparse.ArgumentParser(description='Generates a logstash configuration for a BlueCoat Proxy log.')
parser.add_argument('-c', '--config', default='proxy-bluecoat.conf',
                   help='logstash configuration file to modify (proxy-bluecoat.conf)')
parser.add_argument('-l', '--logfile', required=True,
                   help='log file to read out the log-format')
args = parser.parse_args()

logfile = args.logfile
conffile = args.config
fields_unclean = False
fields = []

try:
    with open(logfile) as f:
        for line in f:
            if line.startswith("#Fields: "):
                fields_str = line[9:]
                fields_unclean = fields_str.strip().split(' ')
                break
except:
    print ("ERROR: Couldn't open the logfile.")
    exit(1)
if not fields_unclean:
    print ("ERROR: Couldn't find the field definition line in the proxy log. Are you sure your logfile contains a '#Fields:' line at the top?")
    exit(1)

# clean up the array and only keep allowed chars
for field in fields_unclean:
    # uniformize the fields: replace all non letters or numbers, lowercase and strip _ at the end
    fields.append(re.sub(r'[^a-z0-9]', '_', field.lower()).strip("_"))
print ("Discovered columns in logfile: {0}".format(', '.join(fields)))
columns_line = '        columns => ["{0}"]\n'.format('", "'.join(fields))

# now build the new configuration (temp)file based on the old one
columns_line_seen = False
with tempfile.NamedTemporaryFile() as tmpf:
    with open(conffile) as f:
        for line in f:
            if 'columns => [' in line:
                columns_line_seen = True
                line = columns_line
            tmpf.write(line)
    if not columns_line_seen:
        print ("ERROR: Couldn't find the columns line in the logstash configuration file.")
        exit(1)
    # copy temp file to original file
    tmpf.seek(0)                       # go back to the start of the tmpfile as we're at the end
    shutil.copy(tmpf.name, conffile)  # copy the new file to the old one 
    print ("\nLogstash configuration file updated.")

