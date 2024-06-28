%define name minarca-server
%define version 6.0.0b3
%define unmangled_version 6.0.0b3
%define release 1

Summary: Minarca Web Server
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: IKUS Software inc. <support@ikus-soft.com>
Url: https://minarca.org/
BuildRequires: python3.11 python3.11-devel python3.11-setuptools python3.11-wheel python3.11-pip

%description
Minarca is a self-hosted open source data backup software that allows you to manage your computer and server backups for free from a direct online accessible centralized view of your data with easy retrieval in case of displacement, loss or breakage.

%prep
%setup -n minarca

%build
cd minarca-server
python3.11 setup.py build

%install
cd minarca-server
python3.11 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
