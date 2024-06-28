%global python3_pkgversion 3.11

%define name rdiffweb
%define service_user minarca
%define service_group minarca

Summary: A web interface to rdiff-backup repositories.
Name: %{name}
Version: 2.9.1
Release: 3%{dist}
Source0: %{name}-2.9.1.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Patrik Dufresne <patrik@ikus-soft.com>
Url: https://rdiffweb.org/
BuildRequires: python%{python3_pkgversion} python%{python3_pkgversion}-devel python%{python3_pkgversion}-setuptools python%{python3_pkgversion}-wheel python%{python3_pkgversion}-pip git

%description
RdiffWeb

%prep
%setup -n rdiffweb

%build
python%{python3_pkgversion} setup.py build

%install
python%{python3_pkgversion} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir /opt/minarca -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%files -f INSTALLED_FILES
%defattr(-,root,root)
