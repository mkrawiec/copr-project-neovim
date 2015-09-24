Name:           neovim-qt
Version: 0.0.0.20150924git311070
Release:        1%{?dist}
Summary:        Neovim RPC and GUI using Qt5

License:        ISC
Url:            https://github.com/equalsraf/neovim-qt
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  msgpack-devel >= 1.2.0
Requires:       neovim

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Qt GUI for Connman with system tray icon. The program provides graphical user
interface to control the connman daemon.

%prep
%setup -q

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DUSE_SYSTEM_MSGPACK=ON ..
make %{?_smp_mflags}

%install
install -D -m 0755 build/bin/nvim-qt %{buildroot}%{_bindir}/nvim-qt
install -D -m 0644 third-party/neovim.png %{buildroot}%{_datadir}/pixmaps/neovim-qt.png
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/neovim-qt.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :

%files
%defattr(-,root,root)
%{_bindir}/nvim-qt
%{_datadir}/applications/neovim-qt.desktop
%{_datadir}/pixmaps/neovim-qt.png

%changelog