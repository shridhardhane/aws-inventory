import boto3
import botocore
import json
import config
import pprint, operator
import res.utils as utils
import res.glob as glob

# =======================================================================================================================
#
#  Supported services   : CodeStar
#  Unsupported services : CodeCommit, CodeBuild, CodeDeploy, CodePipeline, Cloud9, X-Ray
#
# =======================================================================================================================

#  ------------------------------------------------------------------------
#
#    CodeStar
#
#  ------------------------------------------------------------------------

def get_codestar_inventory(oId):
    """
        Returns codestar details

        :param ownerId: ownerId (AWS account)
        :type ownerId: string

        :return: codestar inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/kms.html
    """ 
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "codestar", 
        aws_region = "all", 
        function_name = "list_projects", 
        key_get = "projects",
        detail_function = "describe_project", 
        key_get_detail = "projectId",
        key_selector = "id"
    )


#
# Hey, doc: we're in a module!
#
#if (__name__ == '__main__'):
#    print('Module => Do not execute')