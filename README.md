# aws

## sg_github_ip_range.py
python script to update EC2 Security Group with Github IP range. It is used in my case to enable push hooks to EC2 Jenkins master when all other connections from internet to this EC2 are denied. **username** and **token** are used because github blocks connections after a specific number of API query attempts.

### Usage ###:

```python sg_github_ip_range.py```

Put this script in crontab to check when Github ip range changes. Ex. every hour:

```0 */1 * * * /home/sg_github_ip_range.py | ts '[%Y-%m-%d %H:%M:%S]' >> /home/sg_github_ip_range.log 2>&1```
