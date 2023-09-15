"""
** Copyright (C) 2023  Johannes Kepler University Linz, Institute of Networks and Security
** Copyright (C) 2023  CDL Digidow <https://www.digidow.eu/>
**
** Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
** the European Commission - subsequent versions of the EUPL (the "Licence").
** You may not use this work except in compliance with the Licence.
** 
** You should have received a copy of the European Union Public License along
** with this program.  If not, you may obtain a copy of the Licence at:
** <https://joinup.ec.europa.eu/software/page/eupl>
** 
** Unless required by applicable law or agreed to in writing, software
** distributed under the Licence is distributed on an "AS IS" basis,
** WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
** See the Licence for the specific language governing permissions and
** limitations under the Licence.
**
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

    createlogurl = options.personalityaddress + 'LogBuilder/AddLogEntry?treeId=' +options.treeid
    logentry = {"applicationId":options.appid,"version":options.version,"signatureData":sha256_hash.hexdigest()}
    
    createloginurl = options.personalityaddress + 'Login/RequestAccessToken'
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


