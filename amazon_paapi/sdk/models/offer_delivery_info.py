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

from .offer_shipping_charge import OfferShippingCharge  # noqa: F401,E501


class OfferDeliveryInfo(object):
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
        'is_amazon_fulfilled': 'bool',
        'is_free_shipping_eligible': 'bool',
        'is_prime_eligible': 'bool',
        'shipping_charges': 'list[OfferShippingCharge]'
    }

    attribute_map = {
        'is_amazon_fulfilled': 'IsAmazonFulfilled',
        'is_free_shipping_eligible': 'IsFreeShippingEligible',
        'is_prime_eligible': 'IsPrimeEligible',
        'shipping_charges': 'ShippingCharges'
    }

    def __init__(self, is_amazon_fulfilled=None, is_free_shipping_eligible=None, is_prime_eligible=None, shipping_charges=None):  # noqa: E501
        """OfferDeliveryInfo - a model defined in Swagger"""  # noqa: E501

        self._is_amazon_fulfilled = None
        self._is_free_shipping_eligible = None
        self._is_prime_eligible = None
        self._shipping_charges = None
        self.discriminator = None

        if is_amazon_fulfilled is not None:
            self.is_amazon_fulfilled = is_amazon_fulfilled
        if is_free_shipping_eligible is not None:
            self.is_free_shipping_eligible = is_free_shipping_eligible
        if is_prime_eligible is not None:
            self.is_prime_eligible = is_prime_eligible
        if shipping_charges is not None:
            self.shipping_charges = shipping_charges

    @property
    def is_amazon_fulfilled(self):
        """Gets the is_amazon_fulfilled of this OfferDeliveryInfo.  # noqa: E501


        :return: The is_amazon_fulfilled of this OfferDeliveryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_amazon_fulfilled

    @is_amazon_fulfilled.setter
    def is_amazon_fulfilled(self, is_amazon_fulfilled):
        """Sets the is_amazon_fulfilled of this OfferDeliveryInfo.


        :param is_amazon_fulfilled: The is_amazon_fulfilled of this OfferDeliveryInfo.  # noqa: E501
        :type: bool
        """

        self._is_amazon_fulfilled = is_amazon_fulfilled

    @property
    def is_free_shipping_eligible(self):
        """Gets the is_free_shipping_eligible of this OfferDeliveryInfo.  # noqa: E501


        :return: The is_free_shipping_eligible of this OfferDeliveryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_free_shipping_eligible

    @is_free_shipping_eligible.setter
    def is_free_shipping_eligible(self, is_free_shipping_eligible):
        """Sets the is_free_shipping_eligible of this OfferDeliveryInfo.


        :param is_free_shipping_eligible: The is_free_shipping_eligible of this OfferDeliveryInfo.  # noqa: E501
        :type: bool
        """

        self._is_free_shipping_eligible = is_free_shipping_eligible

    @property
    def is_prime_eligible(self):
        """Gets the is_prime_eligible of this OfferDeliveryInfo.  # noqa: E501


        :return: The is_prime_eligible of this OfferDeliveryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_prime_eligible

    @is_prime_eligible.setter
    def is_prime_eligible(self, is_prime_eligible):
        """Sets the is_prime_eligible of this OfferDeliveryInfo.


        :param is_prime_eligible: The is_prime_eligible of this OfferDeliveryInfo.  # noqa: E501
        :type: bool
        """

        self._is_prime_eligible = is_prime_eligible

    @property
    def shipping_charges(self):
        """Gets the shipping_charges of this OfferDeliveryInfo.  # noqa: E501


        :return: The shipping_charges of this OfferDeliveryInfo.  # noqa: E501
        :rtype: list[OfferShippingCharge]
        """
        return self._shipping_charges

    @shipping_charges.setter
    def shipping_charges(self, shipping_charges):
        """Sets the shipping_charges of this OfferDeliveryInfo.


        :param shipping_charges: The shipping_charges of this OfferDeliveryInfo.  # noqa: E501
        :type: list[OfferShippingCharge]
        """

        self._shipping_charges = shipping_charges

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
        if issubclass(OfferDeliveryInfo, dict):
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
        if not isinstance(other, OfferDeliveryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
