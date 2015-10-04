%global with_python3 1

%global pypiname neovim
Name:           python-neovim
Version: 0.0.38
Release:        1%{?dist}
Summary:        Python client for Neovim

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/neovim/python-client
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif #python3

Requires:       python-msgpack
Requires:       python-trollius
Requires:       python-greenlet

%description
Library for scripting Nvim processes through its msgpack-rpc API.

%if 0%{?with_python3}
%package -n python3-neovim
Summary: Python client for Neovim

%description -n python3-neovim
Library for scripting Nvim processes through its msgpack-rpc API.
%endif #python3

%prep
%setup -q

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%{__python2} setup.py build

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%check

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/pynvim
%{python2_sitelib}/neovim
%{python2_sitelib}/%{pypiname}-%{version}-py2.?.egg-info

%if 0%{?with_python3}
%files -n python3-neovim
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/pynvim
%dir %{python3_sitelib}/neovim
%{python3_sitelib}/neovim/*
%{python3_sitelib}/%{pypiname}-%{version}-py3.?.egg-info
%endif

%changelog
