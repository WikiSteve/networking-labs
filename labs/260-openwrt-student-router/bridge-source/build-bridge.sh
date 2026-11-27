#!/bin/sh
# Build on x86-64 Linux with gcc, static libc, OpenWrt ImageBuilder, gzip and qemu-img.
set -eu
builder=$(realpath "${1:?Specify the extracted OpenWrt 25.12.6 x86/64 ImageBuilder directory}")
output=$(realpath -m "${2:?Specify a new output VMDK path}")
[ ! -e "$output" ] || { echo 'Output already exists' >&2; exit 1; }
src=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
cp -R "$src/overlay" "$work/overlay"
mkdir -p "$work/overlay/usr/sbin"
gcc -std=c11 -O2 -Wall -Wextra -Werror -static -s "$src/relay.c" -o "$work/overlay/usr/sbin/portal-relay"
make -C "$builder" image PROFILE=generic ROOTFS_PARTSIZE=48 FILES="$work/overlay"
gzip -dc "$builder/bin/targets/x86/64/openwrt-25.12.6-x86-64-generic-ext4-combined.img.gz" > "$work/bridge.raw"
qemu-img convert -f raw -O vmdk -o subformat=monolithicSparse,adapter_type=ide "$work/bridge.raw" "$output"
