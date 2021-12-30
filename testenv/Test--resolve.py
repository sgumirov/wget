#!/usr/bin/env python3
from sys import exit
from test.http_test import HTTPTest
from misc.wget_file import WgetFile

"""
    This test ensures that Wget correctly handles overriding DNS resolution
    for domain name.
"""
############# File Definitions ###############################################
File1 = "dummy"

A_File = WgetFile ("File1", File1)

WGET_OPTIONS = "--resolve=example.com:127.0.0.1"
WGET_URLS = [["File1"]]

Files = [[A_File]]

ExpectedReturnCode = 0
ExpectedDownloadedFiles = [A_File]

################ Pre and Post Test Hooks #####################################
pre_test = {
    "ServerFiles"       : Files,
}
test_options = {
    "WgetCommands"      : WGET_OPTIONS,
    "Urls"              : WGET_URLS
}
post_test = {
    "ExpectedFiles"     : ExpectedDownloadedFiles,
    "ExpectedRetcode"   : ExpectedReturnCode
}

err = HTTPTest (
                pre_hook=pre_test,
                test_params=test_options,
                post_hook=post_test
).begin ()

exit (err)
