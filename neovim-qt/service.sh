PKG_VERSION=0.0.0.$(date +%Y%m%d)git0280ff
PKG_DOWNLOAD_URL=https://github.com/equalsraf/neovim-qt/archive/staging.tar.gz

pkg_prebuild_hook()
{
    sudo dnf -y copr enable mkrawiec/neovim
}
