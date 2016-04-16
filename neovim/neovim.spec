Name:           neovim
Version: 0.1.3
Release:        1%{?dist}
License:        Vim
Summary:        Vim's rebirth for the 21st century
Url:            http://neovim.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
# For luarocks
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  ncurses-devel
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  jemalloc-devel
#BuildRequires:  libuv-devel
#BuildRequires:  luajit-devel
#BuildRequires:  lua-devel
#BuildRequires:  lua
#BuildRequires:  lua-lpeg
#BuildRequires:  lua-bitop
#BuildRequires:  lua-msgpack
BuildRequires:  msgpack-devel >= 1.2.0
BuildRequires:  unibilium-devel
BuildRequires:  libtermkey-devel
BuildRequires:  libvterm-devel

%description
Neovim is a project that seeks to aggressively refactor Vim in order to:

* Simplify maintenance and encourage contributions
* Split the work between multiple developers
* Enable the implementation of new/modern user interfaces without any modifications to the core source
* Improve extensibility with a new plugin architecture

%prep
%setup -q

%build
# Bundled lua needed as there is no bitop for lua 5.3
mkdir .deps
pushd .deps
%cmake ../third-party \
    -DUSE_BUNDLED_JEMALLOC=OFF \
    -DUSE_BUNDLED_UNIBILIUM=OFF \
    -DUSE_BUNDLED_LIBTERMKEY=OFF \
    -DUSE_BUNDLED_LIBVTERM=OFF \
    -DUSE_BUNDLED_LIBUV=ON \
    -DUSE_BUNDLED_MSGPACK=OFF \
    -DLUAJIT_USE_BUNDLED=ON \
    -DLUAROCKS_USE_BUNDLED=ON
make %{?_smp_mflags}
popd

mkdir build
pushd build
%cmake .. \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DENABLE_JEMALLOC=ON

make %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=%{buildroot}
popd
%find_lang nvim

%files -f nvim.lang
%defattr(-,root,root)
%{_bindir}/nvim
%{_datadir}/nvim/
%{_datadir}/man/*/*

%changelog
