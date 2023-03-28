%define name python-flowd
%define version 1.0.0
%define unmangled_version 1.0.0
%define unmangled_version 1.0.0
%define _unpackaged_files_terminate_build 0
%if 0%{?rhel} == 7
  %define dist .el7
%endif
%define release 1%{?dist}

Summary: Flow and Packet Marking Service
Name: %{name}
Version: 1.0.0
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: ASL 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Marian Babik <Marian.Babik@cern.ch>,  <<net-wg-dev@cern.ch>>
Packager: Marian Babik <marian.babik@cern.ch>
Requires: python2-requests python2-psutil systemd-python python-ipaddress
Url: https://github.com/scitags/flowd
BuildRequires: python-setuptools

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{python_sitelib}/*

%config(noreplace) /etc/flowd/flowd.cfg
%attr(755, root, root) /usr/sbin/flowd
/usr/lib/systemd/system/flowd.service

%post
%systemd_post flowd.service

%preun
%systemd_preun flowd.service

%postun
%systemd_postun_with_restart flowd.service
