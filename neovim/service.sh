PKG_VERSION=0.0.0.$(date +%Y%m%d)gitef5ee3
PKG_DOWNLOAD_URL=https://github.com/neovim/neovim/archive/master.zip

pkg_prebuild_hook()
{
    sudo dnf -y copr enable mkrawiec/neovim
}