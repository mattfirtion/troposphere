# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags


class ExternalUrlConfig(AWSProperty):
    """
    `ExternalUrlConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-externalurlconfig.html>`__
    """

    props: PropsDictType = {
        "AccessUrl": (str, True),
        "ApprovedOrigins": ([str], False),
    }


class ApplicationSourceConfig(AWSProperty):
    """
    `ApplicationSourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-applicationsourceconfig.html>`__
    """

    props: PropsDictType = {
        "ExternalUrlConfig": (ExternalUrlConfig, True),
    }


class Application(AWSObject):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html>`__
    """

    resource_type = "AWS::AppIntegrations::Application"

    props: PropsDictType = {
        "ApplicationSourceConfig": (ApplicationSourceConfig, True),
        "Description": (str, True),
        "Name": (str, True),
        "Namespace": (str, False),
        "Permissions": ([str], False),
        "Tags": (Tags, False),
    }


class FileConfiguration(AWSProperty):
    """
    `FileConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html>`__
    """

    props: PropsDictType = {
        "Filters": (dict, False),
        "Folders": ([str], True),
    }


class ScheduleConfig(AWSProperty):
    """
    `ScheduleConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html>`__
    """

    props: PropsDictType = {
        "FirstExecutionFrom": (str, False),
        "Object": (str, False),
        "ScheduleExpression": (str, True),
    }


class DataIntegration(AWSObject):
    """
    `DataIntegration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html>`__
    """

    resource_type = "AWS::AppIntegrations::DataIntegration"

    props: PropsDictType = {
        "Description": (str, False),
        "FileConfiguration": (FileConfiguration, False),
        "KmsKey": (str, True),
        "Name": (str, True),
        "ObjectConfiguration": (dict, False),
        "ScheduleConfig": (ScheduleConfig, False),
        "SourceURI": (str, True),
        "Tags": (Tags, False),
    }


class EventFilter(AWSProperty):
    """
    `EventFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html>`__
    """

    props: PropsDictType = {
        "Source": (str, True),
    }


class EventIntegration(AWSObject):
    """
    `EventIntegration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html>`__
    """

    resource_type = "AWS::AppIntegrations::EventIntegration"

    props: PropsDictType = {
        "Description": (str, False),
        "EventBridgeBus": (str, True),
        "EventFilter": (EventFilter, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
