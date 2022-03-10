# Jedox confidential
# -------------------------------
#
# Copyright (C) 2006-2021 Jedox AG
# All Rights Reserved.
#
# NOTICE: All information contained herein is, and remains
# the property of Jedox AG and its suppliers, if any.
# The intellectual and technical concepts contained herein are
# proprietary to Jedox AG and its suppliers and may be covered by
# the Federal Republic of Germany, patents in process, and are
# protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Jedox AG.
#
#
# \author Ehsan Saei, Jedox AG, Freiburg, Germany
#

FROM jedox.azurecr.io/centos:7 AS prepare

RUN mkdir /opt/jdx/ \
&& mkdir /opt/jdx/olap \
&& mkdir /opt/jdx/olap/etc \
&& mkdir /opt/jdx/olap/data

ADD palo-Linux-amd64-GPU-full.tar.gz /opt/jdx/olap

ADD svs-Linux-x86_64.tar.gz /opt/jdx/olap

WORKDIR /opt/jdx/olap/

ADD palo.ini.docker /opt/jdx/olap/etc/palo.ini

RUN olap_dir=/opt/jdx/olap \
&& mv $olap_dir/svs-Linux-x86_64 $olap_dir/svs \
&& mv $olap_dir/svs/php.ini.docker $olap_dir/svs/php.ini \
&& mv $olap_dir/usr/bin $olap_dir \
&& mv $olap_dir/Api $olap_dir/api \
&& mv $olap_dir/usr/lib64 $olap_dir/lib64 \
&& rm -R $olap_dir/usr \
&& strip $olap_dir/bin/* $olap_dir/lib64/*.so \
&& ln -s $olap_dir/svs/libPaloSpreadsheetFuncs.so $olap_dir/svs/libPaloSpreadsheetFuncs.so.0 \
&& rm $olap_dir/svs/libboost* \
&& rm $olap_dir/svs/php.ini.linux $olap_dir/svs/palo.ico \
&& chown -R root:root . \
&& chmod 666 $olap_dir/etc/palo.ini

###
###
###
FROM jedox.azurecr.io/centos:7

LABEL maintainer="ehsan.saei@jedox.com"

# http & admin
EXPOSE 7777/tcp \
       7778/tcp

USER daemon
WORKDIR /opt/jdx/olap/
ENV LD_LIBRARY_PATH=/opt/jdx/olap/lib64:/opt/jdx/olap/svs

ENTRYPOINT ["/opt/jdx/olap/bin/palo", "-d", "/opt/jdx/olap/data", "-i",  "/opt/jdx/olap/etc/palo.ini"]

COPY --from=prepare /opt/jdx /opt/jdx
