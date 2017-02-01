import base64


# Gcons pack by  Sarfraz Shoukat CC 3.0 BY
icons_dict = {
    "new_sample": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTguMS4xLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDIzLjQyOSAyMy40MjkiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDIzLjQyOSAyMy40Mjk7IiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iMzJweCIgaGVpZ2h0PSIzMnB4Ij4KPGc+Cgk8Zz4KCQk8cG9seWdvbiBwb2ludHM9IjE2Ljk0NiwwLjY0MyA1LjAxOSwwLjY0MyAwLDUuMTMyIDAsMjIuNzI2IDExLjkzNSwyMi43MjYgMTEuOTM1LDIxLjE0NiAxLjc3NywyMS4xNDYgICAgIDEuNzc3LDYuODUyIDYuOTI2LDYuODUyIDYuOTI2LDIuMjIxIDE1LjE2OSwyLjIyMSAxNS4xNjksNy4xMTEgMTYuOTQ2LDcuMTExICAgIiBmaWxsPSIjMDAwMDAwIi8+CgkJPHBvbHlnb24gcG9pbnRzPSIxNC40MzgsMTQuMzcyIDE0LjQzOCw5LjQ5NSAxOC4yMjQsOS40OTUgMTguMjI0LDE0LjM3MiAyMy40MjksMTQuMzcyIDIzLjQyOSwxNy45MDkgICAgIDE4LjIyNCwxNy45MDkgMTguMjI0LDIyLjc4NiAxNC40MzgsMjIuNzg2IDE0LjQzOCwxNy45MDkgOS4yNDIsMTcuOTA5IDkuMjQyLDE0LjM3MiAgICIgZmlsbD0iIzAwMDAwMCIvPgoJPC9nPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo="}
    

get_icon = lambda x: base64.b64decode(icons_dict[x])