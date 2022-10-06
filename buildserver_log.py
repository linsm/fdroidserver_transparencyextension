"""
Copyright (c) 2022 Mario Lins <mario.lins@ins.jku.at>

Licensed under the EUPL, Version 1.2. 
  
You may obtain a copy of the Licence at: 
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

def main():
    global options

    parser = ArgumentParser()
    common.setup_global_opts(parser)
    parser.add_argument("--personalityaddress",
                        default="http://IP_REST_API:PORT/",
                        help=_("Path to the the REST API of the personality"))
    parser.add_argument("--appid",
                        default="com.company.appid",
                        help=_("App ID"))
    parser.add_argument("--version",
                        default="1",
                        help=_("App Version"))
    parser.add_argument("--treeid",
                        default="5253222656226122581",
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
    response = requests.post(createlogurl,json=logentry)
    print(response.json())
    print(response.status_code)
    print(createlogurl)


