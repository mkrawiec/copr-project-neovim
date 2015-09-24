Name:           libtermkey
Summary:        Library for easy processing of keyboard entry from terminal-based programs
Version: 0.0.0.20150924git90264a
Release:        1%{?dist}
License:        MIT
Group:          System Environment/Libraries
URL:            https://github.com/neovim/libvterm/

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel
BuildRequires:  gcc make glibc-devel pkgconfig libtool

%description
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognise special keys, UTF-8
combining, and so on, with a simple interface.

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
%__make %{?_smp_flags} \
    CFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    LIBDIR="%{_libdir}" \
    INCDIR="%{_includedir}" \
    MANDIR="%{_mandir}"

%install
%__make \
    CFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    LIBDIR="%{_libdir}" \
    INCDIR="%{_includedir}" \
    MANDIR="%{_mandir}" \
    DESTDIR="%{buildroot}" \
    install

rm $RPM_BUILD_ROOT%{_libdir}/*.la


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_libdir}/libtermkey.so.*


%files devel
%defattr(-,root,root)
%{_includedir}/termkey.h
%{_libdir}/libtermkey.so
%{_libdir}/libtermkey.a
%{_libdir}/pkgconfig/termkey.pc
%{_mandir}/man3/termkey*
%{_mandir}/man7/termkey*


%changelog
