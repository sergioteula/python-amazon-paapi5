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

from .single_string_valued_attribute import SingleStringValuedAttribute  # noqa: F401,E501


class ContentRating(object):
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
        'audience_rating': 'SingleStringValuedAttribute'
    }

    attribute_map = {
        'audience_rating': 'AudienceRating'
    }

    def __init__(self, audience_rating=None):  # noqa: E501
        """ContentRating - a model defined in Swagger"""  # noqa: E501

        self._audience_rating = None
        self.discriminator = None

        if audience_rating is not None:
            self.audience_rating = audience_rating

    @property
    def audience_rating(self):
        """Gets the audience_rating of this ContentRating.  # noqa: E501


        :return: The audience_rating of this ContentRating.  # noqa: E501
        :rtype: SingleStringValuedAttribute
        """
        return self._audience_rating

    @audience_rating.setter
    def audience_rating(self, audience_rating):
        """Sets the audience_rating of this ContentRating.


        :param audience_rating: The audience_rating of this ContentRating.  # noqa: E501
        :type: SingleStringValuedAttribute
        """

        self._audience_rating = audience_rating

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
        if issubclass(ContentRating, dict):
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
        if not isinstance(other, ContentRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
