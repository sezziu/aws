# aws
sg_github_ip_range.py: python script to update EC2 Security Group with Github IP range. It is used in my case to enable push hooks to Jenkins master when all other connections from internet are denied.

"username" and "token" are used because github block connections after a specific number of API query attempts.

Put this script in crontab to check when Github ip range changes.
