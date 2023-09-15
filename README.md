# fdroidserver_transparencyextension

This repository contains the transparency extension for F-Droid Build Servers. 

## Add transparency log extension to existing F-Droid server

To enable transparencylog for your f-droid build server instance you have to download the `transparencylog.py` file of this repository and store it in `fdroidserver/fdroidserver/`. This directory contains the available f-droid commands (e.g. deploy, update,...).

The following file has to be adapted:

```shell
    root@fdroidserver:~# cd <PATH_TO_FDROID_REPOSITORY> #e.g. /srv/data/public_repository
    root@fdroidserver:/srv/data/public_repository$ vim ../fdroidserver/fdroidserver/__main__.py
    # Attach the following line to the COMMAND variable:
    ("transparencylog", _("Create new transparency log entry")),
```

## Configuration

Before running the newly added command it is necessary to adapt the `transparencylog.py`file according to your settings.
To update the configuration, open the file in an editor and update the sections marked in the file.

### Authentication

To prevent unauthorized write access on the log, we have implemented a token based authentication scheme. 
To get a token you have to enter valid credentials in the `transparencylog.py` file for the user `buildserver`. 
The credentials should have been defined in the docker configuration of the personality.

### TLS Certificate

In case you are using self-signed TLS certificates, it is neccessary to upload the certificate to the F-Droid Build Server and set it's path in the `transparencylog.py` file. 

## LICENSE

Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
the European Commission - subsequent versions of the EUPL (the "Licence").
You may not use this work except in compliance with the Licence.

**License**: [European Union Public License v1.2](https://joinup.ec.europa.eu/software/page/eupl)
