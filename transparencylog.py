"""
Copyright (c) 2023 Mario Lins <mario.lins@ins.jku.at>

Licensed under the EUPL, Version 1.2. 
  
You may obtain a copy of the Licence at: 
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""
#!/usr/bin/env python3

import collections
import defusedxml.minidom
import git
import glob
import hashlib
import os
import json
import logging
import requests
import shutil
import tempfile
import zipfile
from argparse import ArgumentParser

from . import _
from . import common
from . import deploy
from .exception import FDroidException


def main():
    global options

    parser = ArgumentParser()
    common.setup_global_opts(parser)
    parser.add_argument("--personalityaddress",
            default="https://ENTER_DEFAULT_IP:PORT/",
                        help=_("Path to the the REST API of the personality"))
    parser.add_argument("--appid",
                        default="com.company.appid",
                        help=_("App ID"))
    parser.add_argument("--version",
                        default="1",
                        help=_("App Version"))
    parser.add_argument("--treeid",
                        default="ENTER_DEFAULT_TREE_ID",
                        help=_("Tree ID"))
    options = parser.parse_args()

    apkfilename = options.appid + '_' + options.version + '.apk'
    apkfile = os.path.join('repo',apkfilename)
    sha256_hash = hashlib.sha256()
    with open(apkfile, 'rb') as f:
        for blk in iter(lambda: f.read(4096),b""):
            sha256_hash.update(blk)
    print(sha256_hash.hexdigest())

    createlogurl = options.personalityaddress + 'Log/AddLogEntry?treeId=' +options.treeid
    logentry = {"applicationId":options.appid,"version":options.version,"signatureData":sha256_hash.hexdigest()}
    
    createloginurl = options.personalityaddress + 'Login/Login'
    logincredentials = {"username": "buildserver", "password":"ENTER_PASSWORD"}
    loginresponse = requests.post(createloginurl,json=logincredentials,verify='PATH_TO_CERTIFICATE')
    #print(loginresponse.json())
    token = loginresponse.json()['token']
    print(token)

    response = requests.post(createlogurl,headers={'Authorization': 'Bearer '+token},json=logentry,verify='PATH_TO_CERTIFICATE')
    print(response)
    print(response.json())
    print(response.status_code)
    print(createlogurl)


