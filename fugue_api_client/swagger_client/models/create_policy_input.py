# coding: utf-8

"""
    Fugue API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreatePolicyInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'survey_resource_types': 'list[str]',
        'remediate_resource_types': 'list[str]'
    }

    attribute_map = {
        'survey_resource_types': 'survey_resource_types',
        'remediate_resource_types': 'remediate_resource_types'
    }

    def __init__(self, survey_resource_types=None, remediate_resource_types=None):  # noqa: E501
        """CreatePolicyInput - a model defined in Swagger"""  # noqa: E501

        self._survey_resource_types = None
        self._remediate_resource_types = None
        self.discriminator = None

        if survey_resource_types is not None:
            self.survey_resource_types = survey_resource_types
        if remediate_resource_types is not None:
            self.remediate_resource_types = remediate_resource_types

    @property
    def survey_resource_types(self):
        """Gets the survey_resource_types of this CreatePolicyInput.  # noqa: E501

        List of resource types to be able to survey.  # noqa: E501

        :return: The survey_resource_types of this CreatePolicyInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._survey_resource_types

    @survey_resource_types.setter
    def survey_resource_types(self, survey_resource_types):
        """Sets the survey_resource_types of this CreatePolicyInput.

        List of resource types to be able to survey.  # noqa: E501

        :param survey_resource_types: The survey_resource_types of this CreatePolicyInput.  # noqa: E501
        :type: list[str]
        """

        self._survey_resource_types = survey_resource_types

    @property
    def remediate_resource_types(self):
        """Gets the remediate_resource_types of this CreatePolicyInput.  # noqa: E501

        List of resource types to be able to remediate.  # noqa: E501

        :return: The remediate_resource_types of this CreatePolicyInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._remediate_resource_types

    @remediate_resource_types.setter
    def remediate_resource_types(self, remediate_resource_types):
        """Sets the remediate_resource_types of this CreatePolicyInput.

        List of resource types to be able to remediate.  # noqa: E501

        :param remediate_resource_types: The remediate_resource_types of this CreatePolicyInput.  # noqa: E501
        :type: list[str]
        """

        self._remediate_resource_types = remediate_resource_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatePolicyInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other