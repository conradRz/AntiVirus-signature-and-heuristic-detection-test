import base64
import codecs
import globalVariables
import os

unwantedWindowTitlesSet = {}


def DecryptionTests():

    global unwantedWindowTitlesSet

    if os.path.exists(globalVariables.unwantedWindowTitlesFilePath):
        os.system("attrib +h " + globalVariables.unwantedWindowTitlesFilePath)
        encryptedFileHandle = open(
            globalVariables.unwantedWindowTitlesFilePath, "r")
        encryptedFile = encryptedFileHandle.read()
        encryptedFileHandle.close()

        data = base64.b64decode(encryptedFile)

        unwantedWindowTitlesSet = codecs.decode(
            data.decode(), encoding='rot_13')
        unwantedWindowTitlesSet = set(unwantedWindowTitlesSet.split(","))
    # else:
    #     unwantedWindowTitlesSet = {}
