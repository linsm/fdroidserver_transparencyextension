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

## Publication

This repository is part of the following publication. 

[M. Lins, R. Mayrhofer, M. Roland, and A. R. Beresford: “Mobile App Distribution Transparency (MADT): Design and evaluation of a system to mitigate necessary trust in mobile app distribution systems”, in Secure IT Systems. 28th Nordic Conference, NordSec 2023, Oslo, Norway, LNCS, vol. 14324/2024, Springer, pp. 185–​203, 2023. https://doi.org/10.1007/978-3-031-47748-5_11](https://doi.org/10.1007/978-3-031-47748-5_11)

## Acknowledgment

This work has been carried out within the scope of Digidow, the Christian Doppler Laboratory for Private Digital Authentication in the Physical World and has partially been supported by the LIT Secure and Correct Systems Lab. 
We gratefully acknowledge financial support by the Austrian Federal Ministry of Labour and Economy, the National Foundation for Research, Technology and Development, the Christian Doppler Research Association, 3 Banken IT GmbH, ekey biometric systems GmbH, Kepler Universitätsklinikum GmbH, NXP Semiconductors Austria GmbH & Co KG, Österreichische Staatsdruckerei GmbH, and the State of Upper Austria.

## LICENSE

Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
the European Commission - subsequent versions of the EUPL (the "Licence").
You may not use this work except in compliance with the Licence.

**License**: [European Union Public License v1.2](https://joinup.ec.europa.eu/software/page/eupl)
