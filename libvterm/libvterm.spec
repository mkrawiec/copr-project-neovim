%define make_flags OPTFLAGS="%{optflags} -std=gnu99" PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

Name:           libvterm
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator
Version: 0.0.0.20151104git0448d8
Release:        1%{?dist}
License:        MIT
Group:          System Environment/Libraries
URL:            https://github.com/neovim/libvterm/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  libtool

%description
An abstract C99 library which implements a VT220 or xterm-like terminal
emulator. It doesn't use any particular graphics toolkit or output system,
instead it invokes callback function pointers that its embedding program should
provide it to draw on its behalf. It avoids calling malloc() during normal
running state, allowing it to be used in embedded kernel situations.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
make %{?_smp_mflags} %{make_flags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags} %{make_flags}
rm -vf %{buildroot}%{_libdir}/libvterm.a


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_bindir}/unterm
%{_bindir}/vterm-ctrl
%{_bindir}/vterm-dump
%doc LICENSE
%{_libdir}/libvterm.so.*


%files devel
%defattr(-,root,root)
%{_includedir}/vterm*.h
%{_libdir}/libvterm.la
%{_libdir}/libvterm.so
%{_libdir}/pkgconfig/vterm.pc


%changelog