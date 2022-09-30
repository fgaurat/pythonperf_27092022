#!/usr/bin/env python
import sys
import os
from pysnmp.hlapi import *


# snmpsimd.py --cache-dir=./cache --data-dir=./data --variation-modules-dir=./variation --v3-only --v3-user=XYZ2008 --v3-auth-key=XYZpassword --v3-auth-proto=MD5 --v3-priv-key=XYZpassword --v3-priv-proto=DES --agent-udpv4-endpoint=10.161.175.245:10001

def main():
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('demo.snmplabs.com', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

if __name__ == '__main__':
    main()