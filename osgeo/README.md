Singularity file for compiling a QGIS, GRASS, SAGA-GIS image for running on a GUI.

If you are connecting to a remote host, you can `ssh -X` to open an X11 display on your local.

```

$ ssh -X $USER@<IPADDRESS>

```

Next pull the pre-existing Singularity image from Singularity Hub: 

```

$ singularity pull --name osgeo.simg shub://tyson-swetnam/osgeo-singularity

```

Once you've pulled the image, you can run it on your remote host, and hte X11 will pop QGIS, GRASS, or SAGA on your localhost:

```

$ singularity exec osgeo.simg qgis

```


