# Copyright 2014 Michael Rice <michael@michaelrice.org>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import tostring

import requests

from thunderhead.parser import vcenter


def get_all_vcenters(connection):
    """

    :param connection:
    :return:
    """
    connection.command_path = "vcenters"
    extra_headers = {connection.header_key: connection.token}
    url = connection.build_url()
    verify_ssl = connection.verify_ssl
    res = requests.get(url=url, headers=extra_headers, verify=verify_ssl)
    if res.status_code > 210:
        return
    body = res.content
    return vcenter.parse_all_vcenters(body)


def create_vcenter(connection, vcenter):
    """

    :param connection:
    :return:
    """
    connection.command_path = "customers"
    extra_headers = {connection.header_key: connection.token}
    url = connection.build_url()
    verify_ssl = connection.verify_ssl


def get_vcenter(connection, vcenter_id):
    connection.command_path = "vcenter/{0}".format(vcenter_id)
    extra_headers = {connection.header_key: connection.token}
    url = connection.build_url()
    verify_ssl = connection.verify_ssl
    res = requests.get(url=url, headers=extra_headers, verify=verify_ssl)
    if res.status_code > 210:
        return
    body = res.content
    return vcenter.parse_vcenter(body)


def update_vcenter(connection):
    connection.command_path = "customers"
    extra_headers = {connection.header_key: connection.token}
    url = connection.build_url()
    verify_ssl = connection.verify_ssl


def delete_vcenter(connection):
    connection.command_path = "customers"
    extra_headers = {connection.header_key: connection.token}
    url = connection.build_url()
    verify_ssl = connection.verify_ssl


def _build_vcenter(vcenter_info):
    """
    <VC xmlns="http://www.vmware.com/UM">
        <hostname>10.255.79.5</hostname>
        <username>root</username>
        <password>vmware</password>
        <monitor>true</monitor>
    </VC>

    :param vcenter_info:
    :return:
    """
    pass