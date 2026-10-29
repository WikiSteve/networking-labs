#!/bin/bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Usage: bash ../build-installer.sh GAME_EXECUTABLE_PATH" >&2
    exit 1
fi

game=$1
if [ ! -f "$game" ] || [ ! -x "$game" ]; then
    echo "Error: '$game' must be an executable file in this project." >&2
    exit 1
fi
if [ ! -f LICENSE ]; then
    echo "Error: LICENSE must be in the project folder." >&2
    exit 1
fi
if ! command -v dpkg-deb >/dev/null 2>&1; then
    echo "Error: dpkg-deb is required to build the installer." >&2
    exit 1
fi

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
package="$work/student-game"
mkdir -p "$package/DEBIAN" "$package/usr/bin" "$package/usr/share/doc/student-game"
cp "$game" "$package/usr/bin/student-game"
cp LICENSE "$package/usr/share/doc/student-game/copyright"

cat > "$package/DEBIAN/control" <<EOF
Package: student-game
Version: 1.0
Section: games
Priority: optional
Architecture: $(dpkg --print-architecture)
Depends: libc6, libncurses6, libtinfo6
Maintainer: Student <student@example.invalid>
Description: Student-built terminal game
 A terminal game packaged for the signed game release lab.
EOF

output=../student-game.deb
staged="$work/student-game.deb"
dpkg-deb --root-owner-group --build "$package" "$staged" >/dev/null
mv -f "$staged" "$output"
echo "Built $output"
