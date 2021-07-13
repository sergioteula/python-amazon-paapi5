# coding: utf-8

"""
  Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.

  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

      http://www.apache.org/licenses/LICENSE-2.0

  or in the "license" file accompanying this file. This file is distributed
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
  express or implied. See the License for the specific language governing
  permissions and limitations under the License.
"""


"""
    ProductAdvertisingAPI

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from .image_size import ImageSize  # noqa: F401,E501


class ImageType(object):
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
        'small': 'ImageSize',
        'medium': 'ImageSize',
        'large': 'ImageSize'
    }

    attribute_map = {
        'small': 'Small',
        'medium': 'Medium',
        'large': 'Large'
    }

    def __init__(self, small=None, medium=None, large=None):  # noqa: E501
        """ImageType - a model defined in Swagger"""  # noqa: E501

        self._small = None
        self._medium = None
        self._large = None
        self.discriminator = None

        if small is not None:
            self.small = small
        if medium is not None:
            self.medium = medium
        if large is not None:
            self.large = large

    @property
    def small(self):
        """Gets the small of this ImageType.  # noqa: E501


        :return: The small of this ImageType.  # noqa: E501
        :rtype: ImageSize
        """
        return self._small

    @small.setter
    def small(self, small):
        """Sets the small of this ImageType.


        :param small: The small of this ImageType.  # noqa: E501
        :type: ImageSize
        """

        self._small = small

    @property
    def medium(self):
        """Gets the medium of this ImageType.  # noqa: E501


        :return: The medium of this ImageType.  # noqa: E501
        :rtype: ImageSize
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this ImageType.


        :param medium: The medium of this ImageType.  # noqa: E501
        :type: ImageSize
        """

        self._medium = medium

    @property
    def large(self):
        """Gets the large of this ImageType.  # noqa: E501


        :return: The large of this ImageType.  # noqa: E501
        :rtype: ImageSize
        """
        return self._large

    @large.setter
    def large(self, large):
        """Sets the large of this ImageType.


        :param large: The large of this ImageType.  # noqa: E501
        :type: ImageSize
        """

        self._large = large

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
        if issubclass(ImageType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
