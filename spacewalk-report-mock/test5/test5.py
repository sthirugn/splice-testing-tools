import os
import sys
import datetime
import yaml

path = os.path.dirname(sys.argv[0])

sys.path.append(path + "/../")

from common import *

fd_splice_export = open('%s/template_splice_export.yaml' % path, 'r')
splice_export = yaml.safe_load(fd_splice_export.read())
fd_splice_export.close()

fd_users = open('%s/template_users.yaml' % path, 'r')
users = yaml.safe_load(fd_users.read())
fd_users.close()


def generate(dirname):
    # 3 weeks back
    initial_date = datetime.datetime.now() - datetime.timedelta(0, 126 * 4 * 3600)
    print_all("%s/step1" % dirname, {'host_guests': [],
                                     'cloned_channels': [],
                                     'users': [users],
                                     'splice_export': []})
    for i in range(0, 41):
        # two systems are doing checkins
        splice_export[0]['last_checkin_time'] = (initial_date + datetime.timedelta(0, i * 4 * 3600)).strftime("%Y-%m-%d %H:%M:%S")
        splice_export[1]['last_checkin_time'] = (initial_date + datetime.timedelta(0, i * 4 * 3600)).strftime("%Y-%m-%d %H:%M:%S")
        print_all("%s/step%i" % (dirname, i + 1), {'host_guests': [],
                                                   'cloned_channels': [],
                                                   'users': [users],
                                                   'splice_export': splice_export})
    for i in range(41, 84):
        # only first system is doing checkin
        splice_export[0]['last_checkin_time'] = (initial_date + datetime.timedelta(0, i * 4 * 3600)).strftime("%Y-%m-%d %H:%M:%S")
        print_all("%s/step%i" % (dirname, i + 1), {'host_guests': [],
                                                   'cloned_channels': [],
                                                   'users': [users],
                                                   'splice_export': splice_export})
    for i in range(84, 125):
        # two systems are doing checkins
        splice_export[0]['last_checkin_time'] = (initial_date + datetime.timedelta(0, i * 4 * 3600)).strftime("%Y-%m-%d %H:%M:%S")
        splice_export[1]['last_checkin_time'] = (initial_date + datetime.timedelta(0, i * 4 * 3600)).strftime("%Y-%m-%d %H:%M:%S")
        print_all("%s/step%i" % (dirname, i + 1), {'host_guests': [],
                                                   'cloned_channels': [],
                                                   'users': [users],
                                                   'splice_export': splice_export})

if len(sys.argv) > 1:
    generate(sys.argv[1])
else:
    generate("./")
