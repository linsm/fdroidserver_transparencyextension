# fdroidserver_transparencyextension

To enable transparencylog for your f-droid build server instance you have to download the transparencylog.py to the fdroidserver/fdroidserver/ directory. This directory contains the available f-droid commands.

The following file has to be adapted:

```shell
    root@fdroidserver:~# cd <PATH_TO_FDROID_REPOSITORY> #e.g. /srv/data/public_repository
    root@fdroidserver:/srv/data/public_repository$ vim ../fdroidserver/fdroidserver/__main__.py
```
Attach the following line to the COMMAND variable:
``("transparencylog", _("Create new transparency log entry")),`

