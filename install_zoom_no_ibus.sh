#!/bin/sh
set -xe

tmp=$(mktemp -d)
cd "${tmp}"

name='zoom.deb'

wget https://zoom.us/client/latest/zoom_amd64.deb -O "${name}"
dpkg -x "${name}" zoom
dpkg -e "${name}" zoom/DEBIAN

sed -i -E 's/(ibus, |, ibus)//' zoom/DEBIAN/control

dpkg -b zoom "${name}"
sudo dpkg -i "${name}"

rm -rf "${tmp}"
