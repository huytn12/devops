#!/usr/bin/env python3
from lxml import etree as ET
import sys

orgName = 'origin'
branchName = 'master'
MESSAGE_ERROR_SYNTAX = 'XML Syntax Error, see error_syntax.log'
MESSAGE_ERROR_UNKNOW = 'Unknown error, exiting.'
MESSAGE_ERROR_FORMAT = "Incorrect file format"
MESSAGE_SUCCESS_REPLACE = 'Replace version success'
MESSAGE_FAILED_CHECK = 'Not a Snapshot'

# @author Huy Nguyen
# @description this function for the test devops
def checkVersion(inputPath, outputPath):
    # Parse pom.xml file
    try:
        tree = ET.parse(inputPath)

    # Check if the file is missing or incorrectly formatted
    except OSError:
        return MESSAGE_ERROR_FORMAT

    # Check for XML syntax errors
    except ET.XMLSyntaxError as err:
        # Retrieve the log entries and write it to a file
        with open('error_syntax.log' , 'w') as error_log_file:
            error_log_file.write(str(err.error_log))
        return MESSAGE_ERROR_SYNTAX

    # Unknown error
    except:
        return MESSAGE_ERROR_UNKNOW
    # Get the namespace
    namespace = {'ns':tree.getroot().nsmap[None]}

    # Update version
    version = tree.find('ns:version', namespace)

    # Confirm the version is a snapshot
    if 'SNAPSHOT' not in version.text:
        return MESSAGE_FAILED_CHECK
    else:
        # Replace the version to match the requirement
        version.text = 'ci_' + orgName + '_' + branchName + '-SNAPSHOT'
        # Save the file
        if outputPath != '':
            tree.write(outputPath)
        else:
            tree.write(inputPath)
        return MESSAGE_SUCCESS_REPLACE
