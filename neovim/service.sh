PKG_VERSION=0.1.2
PKG_DOWNLOAD_URL=https://github.com/neovim/neovim/archive/v${PKG_VERSION}.tar.gz

pkg_prebuild_hook()
{
    sudo dnf -y copr enable mkrawiec/neovim
}

