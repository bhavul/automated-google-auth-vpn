# Automatic Google Auth VPN Connection Script

If you're using a Mac (although this may work on Linux too), and have OpenVPN setup for yourself which requires Two Factor Authentication using Google Authenticator, then you can use this to automate your connection. 

> Warning : This script requires sudo access

## Installation

#### Pre-requisites

1. **homebrew** : If you've never used `brew` in your terminal, please check here on how to install homebrew.
2. **Python and pip** : If you don't have python/pip, I'd really suggest not to use the script at all. 

#### Instructions to install
1. Install oath-toolkit : `brew install oath-toolkit`
2. Install pexpect for python : `pip install pexpect`
3. Install OpenVpn CLI : `brew install openvpn`
4. Add the following into `~/.bash_profile` : 
```
export PATH=$(brew --prefix openvpn)/sbin:$PATH
```

3. Clone/Download the repo : `git clone https://github.com/bhavul/automated-google-auth-vpn.git`
4. Find your Google Auth VPN Secret Key. It shall be somewhat like this : `GF3H5TRATYRA4MKK`   
NOTE : If you don't have this saved, you will need to contact the people who had set it up for you - the IT Team, or whoever. The first time you set it up, or scan QR Code, it is visible at that time.

5. Open the cloned repository, and open the `config.properties` file in a text editor. Edit and fill each field to your own. Once done, save the file.

You're all done.

## How to use?

1. Open terminal. `cd` into cloned repository
2. Run `connect-vpn.py` using python 3 : 

`python3 connect-vpn.py`

Note that this will occupy one of your terminal and push all the logs in there itself. If you wish to keep this all in background, I suggest to use tmux / screen and launch this there.

You can also push all logs to a file like so : 

`python3 connect-vpn.py > vpn.log 2>&1`


## What's the point of this?

Frankly, this takes away the security that Two factor auth provides. So, I'm not responsible for anything that may happen if you use this script. I just wrote it for automating my workflow. 

