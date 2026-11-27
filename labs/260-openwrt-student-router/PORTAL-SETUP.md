# Minion Bridge setup

Use an HTTP server reachable from the Minion Bridge VM through its VMware NAT adapter. The included [sample portal](portal/index.html) is enough to run all of the address, browser and firewall checks in the lab.

On the upstream server, open a terminal in the `portal` folder. If Python 3 is installed, run this command using the server’s actual IPv4 address in place of the example.

```sh
python3 -m http.server 8080 --bind 192.0.2.10
```

`8080` is the listening port. `--bind` selects the interface that the Router PC can reach. Keep this service on your lab’s upstream network. Before opening the VMs, check that the Router PC can open the server address and port in a browser. On Windows, use `py -m http.server` if that is how you start Python 3.

The bridge accepts IPv6 HTTP on its private LAN segment at `[fd00:1ab:5::102]:80`. It starts with the portal disabled. The public VM kit contains the student router and the bridge. Supply your own HTTP portal and its classroom content.

## Set the portal destination

At the Minion Bridge VM console, press Enter. Replace `192.0.2.10` with the HTTP server's IPv4 address and `8080` with its listening port.

```sh
uci set portal.upstream.address='192.0.2.10'
uci set portal.upstream.port='8080'
uci commit portal
/etc/init.d/portal-relay restart
```

The first two commands select the backend. The third saves the settings in `/etc/config/portal`. Restarting the relay applies them. To disable the relay, set the address to an empty string, commit the change, and restart the service.

Connect the bridge's private adapter and the student router's WAN adapter to the same VMware LAN segment. Leave the bridge's upstream adapter on NAT. The student router uses a host-only management network and a separate bench interface on VMnet10. The bench interface starts disconnected so the instructor can verify its physical mapping.

After the student router has IPv6 connectivity, visit `http://minion.lab/` on a client using the router's DNS service. The relay sends the HTTP request, including the original Host header, to the configured portal. Configure the HTTP server to serve that hostname or use a default site. The relay serves HTTP on port 80.

## Rebuild the bridge disk

On an x86-64 Linux build machine, extract [OpenWrt ImageBuilder 25.12.6 for x86/64](https://downloads.openwrt.org/releases/25.12.6/targets/x86/64/). Install its host dependencies along with GCC, static libc development files, gzip, and qemu-img. The build uses the generic BIOS ext4 profile, a 48 MiB root filesystem, and the included OpenWrt overlay.

From the `bridge-source` directory, run the script with the extracted ImageBuilder directory and a new output path. For example:

```sh
./build-bridge.sh ../openwrt-imagebuilder-25.12.6-x86-64.Linux-x86_64 Minion-Bridge.vmdk
```

The script compiles the relay, adds it to the overlay, builds a fresh guest filesystem, and converts the BIOS disk to VMware format. Place the resulting disk beside the kit's Minion-Bridge.vmx file. The VM expects that exact disk filename.
