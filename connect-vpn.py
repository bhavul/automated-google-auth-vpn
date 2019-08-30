import pexpect
import subprocess
import configparser
import time

# Author : Bhavul

config = configparser.ConfigParser()
config.read('config.properties')

vpn_connect_command = "sudo openvpn --verb 3 --script-security 2 --config "+config['vpncreds']['VPN_CLIENT_FILE_PATH']

child = pexpect.spawn(vpn_connect_command, timeout = 10)

child.expect('Password*', timeout=5)
child.sendline(config['sudo']['PASSWORD'])

child.expect('Enter Auth Username*', timeout=5)
child.sendline(config['vpncreds']['VPN_USERNAME'])

child.expect('Enter Auth Password*', timeout=5)
child.sendline(config['vpncreds']['VPN_PASSWORD'])

child.expect('CHALLENGE*', timeout=5)

get_gauth_code_cmd = "oathtool -b --now='{now}' --totp {secret}".format(now=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime()), secret=config['googlauth']['VPN_GOOGLE_AUTH_SECRET'])
vcode = subprocess.check_output(get_gauth_code_cmd,shell=True)
print('vcode : {code}'.format(code=vcode))
child.sendline(vcode)

child.setwinsize(400,400)

child.interact()
