%global python3_pkgversion 3.11

%define name minarca-server
%define service_user minarca
%define service_group minarca

Summary: Minarca Web Server
Name: %{name}
Version: 6.0.0b3
Release: 2%{dist}
Source0: %{name}-6.0.0b3.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: IKUS Software inc. <support@ikus-soft.com>
Url: https://minarca.org/
BuildRequires: python3.11 python3.11-devel python3.11-setuptools python3.11-wheel python3.11-pip git

%description
Minarca is a self-hosted open source data backup software that allows you to manage your computer and server backups for free from a direct online accessible centralized view of your data with easy retrieval in case of displacement, loss or breakage.

%prep
%setup -n minarca

%build
cd minarca-server
python3.11 setup.py build

%install
cd minarca-server
python3.11 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=../INSTALLED_FILES
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/usr/lib/systemd/system $RPM_BUILD_ROOT/opt/minarca-server/share
cp debian/minarca-server.service $RPM_BUILD_ROOT/usr/lib/systemd/system
cp -a data/etc/minarca $RPM_BUILD_ROOT/etc
mv $RPM_BUILD_ROOT/etc/minarca/sysctl.d $RPM_BUILD_ROOT/etc/
cp minarca_server/minarca.ico minarca_server/minarca_logo.svg $RPM_BUILD_ROOT/opt/minarca-server/share/
ln -s /opt/rdiff-backup-2.0/rdiff-backup-delete $RPM_BUILD_ROOT/opt/minarca-server/bin/rdiff-backup-delete
ln -s /opt/rdiff-backup-2.0/rdiff-backup $RPM_BUILD_ROOT/opt/minarca-server/bin/rdiff-backup
mkdir -p $RPM_BUILD_ROOT/opt/minarca/backups/ $RPM_BUILD_ROOT/var/log/minarca $RPM_BUILD_ROOT/var/lib/minarca

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%files -f INSTALLED_FILES
%defattr(-,minarca,minarca)
/etc/minarca
/opt/minarca-server
%attr(0750,minarca,minarca) /opt/minarca/backups
%attr(0750,minarca,minarca) /var/log/minarca
%attr(0750,minarca,minarca) /var/lib/minarca
%attr(root,root) /usr/lib/systemd/system/minarca-server.service
%attr(root,root) /etc/sysctl.d/00-minarca-server-userns.conf

* Fri Jun 28 2024 10:18:00 PM CEST +0200 Martin Juhl <m@rtinjuhl.dk> 6.0.0b3
- New version build: 6.0.0b3


