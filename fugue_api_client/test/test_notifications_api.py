# coding: utf-8

"""
    Fugue API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.notifications_api import NotificationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.notifications_api.NotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_notification(self):
        """Test case for create_notification

        Creates a new notification.  # noqa: E501
        """
        pass

    def test_delete_notification(self):
        """Test case for delete_notification

        Deletes a notification.  # noqa: E501
        """
        pass

    def test_list_notifications(self):
        """Test case for list_notifications

        Lists details for all notifications.  # noqa: E501
        """
        pass

    def test_update_notification(self):
        """Test case for update_notification

        Updates an existing notification.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()