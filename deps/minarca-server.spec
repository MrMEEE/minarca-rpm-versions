%global python3_pkgversion 3.11

%define _unpackaged_files_terminate_build 0
%define  debug_package %{nil}
%define _prefix /opt/eda-rpm
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user minarca
%define service_group minarca
%define service_homedir /opt/minarca/server
%define service_logdir /var/log/minarca
%define service_configdir /etc/micarca

Summary: Minarca Backup Server
Name: minarca-server
Version: 6.0.0b3
Release: 17%{dist}
Source0: minarca-server-6.0.0b3.tar.gz
#Patch0: awx-patch.patch-%{version}
License: GPLv3
Group: Backup
URL: https://github.com/ikus060/minarca
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: Minarca
Prefix: %{_prefix}
AutoReqProv: false

#BuildRequires: make python%{python3_pkgversion} python%{python3_pkgversion}-devel nodejs npm gettext git python%{python3_pkgversion}-build rsync libpq libpq-devel 
BuildRequires: git python%{python3_pkgversion} python%{python3_pkgversion}-devel
#BuildRequires: python3.11-poetry


#Requires: python%{python3_pkgversion} nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 
#

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n minarca-server
git checkout -f devel
git checkout -f %{version}
#%patch0 -p0

%build

%install
poetry install -E all --only-root

mkdir -p /var/log/minarca

#pip%{python3_pkgversion} install --root=%{buildroot}/ .

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}
#/usr/bin/gpasswd -a  %{service_user} redis

%post
#if [ ! -f /etc/nginx/nginx.crt ];then
#sscg -q --cert-file /etc/nginx/nginx.crt --cert-key-file /etc/nginx/nginx.key --ca-file /etc/nginx/ca.crt --lifetime 3650 --hostname $HOSTNAME --email root@$HOSTNAME
#fi

%preun

%postun

%clean

%files
%defattr(0644, eda, eda, 0755)
%attr(0755, root, root) /usr/bin/aap-eda-manage
/usr/lib/python3.11/site-packages/aap_eda*


%changelog
* Fri Jun 28 2024 01:14:11 PM CEST +0200 Martin Juhl <m@rtinjuhl.dk> 6.0.0b3
- New version build: 6.0.0b3

