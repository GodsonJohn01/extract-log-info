# Write a program to generate number of error, warning and info messages in the log file.

# datetime [level] message
# 2020-11-30T09:43:49Z [error] Config: Interval:10s, Quiet:false, Hostname:"octopilabs", Flush Interval:10s


import re
log_list = [
    '2020-11-30T09:41:10Z [info] Success in plugin: success getting disk io info: open /proc/diskstats: no such file or CASS: Instance Deployment started directory',
    '2020-11-30T09:42:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:43:49Z [info] CASS: Instance Deployment started.',
    '2020-11-30T09:43:49Z [info] Config: Interval:10s, Quiet:false, Hostname:"localhost", Flush Interval:10s.',


    '2020-11-30T09:44:09Z [error] When writing to [http://localhost:8086]: Post "http://localhost:8086": dial tcp 127.0.0.1:8086: connect: connection refused',


    '2020-11-30T09:44:10Z [warning] Error in plugin: warning getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:44:10Z [info] Deploying disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:45:10Z [info] CASS: Instance Deployment configured.',
    '2020-11-30T09:45:10Z [warning] Warning in plugin: error getting disk io info: open /proc/diskstats: no such file or directory.',
    '2020-11-30T09:45:20Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:47:10Z [info] Info in plugin: error getting disk io info: open /proc/diskstats: no such file or directory in Instance Deployment complete in progress',
    '2020-11-30T09:49:10Z [error] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:51:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:54:10Z [info] CASS: Instance Deployment complete.',
    '2020-11-30T09:54:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:55:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',
    '2020-11-30T09:57:10Z [info] Error in plugin: error getting disk io info: open /proc/diskstats: no such file or directory',

]


error_count = 0
warning_count = 0
info_count = 0

for x in log_list:
    error = re.search('\[error]', x)
    if error:
        error_count += 1

    warning = re.search('\[warning]', x)
    if warning:
        warning_count += 1

    info = re.search('\[info]', x)
    if info:
        info_count += 1

print("No of error messages in the log file: ", error_count)
print("No of warning messages in the log file: ", warning_count)
print("No of info messages in the log file: ", info_count)
