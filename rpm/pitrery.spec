%global pkgname pitrery
%global confdir %{_sysconfdir}/%{pkgname}
%{!?pkgversion: %global pkgversion 2.1}
%{!?pkgrevision: %global pkgrevision 1}

Name:           %{pkgname}
Version:        %{pkgversion}
Release:        %{pkgrevision}%{?dist}
Summary:        Point-In-Time Recovery tools for PostgreSQL
License:        BSD
Group:          Applications/Databases
URL:            https://github.com/dalibo/pitrery
Source0:        https://dl.dalibo.com/public/pitrery/%{pkgname}-%{version}.tar.gz
Patch1:         pitrery.config.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       bash, rsync

%description
pitrery is set of tools to ease to management of PITR backups and
restores for PostgreSQL.

- Management of WAL segments archiving with compression to hosts
  reachable with SSH
- Automation of the base backup procedure
- Restore to a particular date
- Management of backup retention

%prep
%setup -q
%patch1 -p1

%build
make

%install
make install DESTDIR=%{buildroot}

%files
%config(noreplace) /etc/pitrery/pitrery.conf
/usr/bin/archive_xlog
/usr/bin/pitrery
/usr/bin/restore_xlog
%doc /usr/share/doc/pitrery/COPYRIGHT
%doc /usr/share/doc/pitrery/INSTALL.md
%doc /usr/share/doc/pitrery/UPGRADE.md
%doc /usr/share/doc/pitrery/pitrery.conf
%doc /usr/share/doc/pitrery/CHANGELOG
%doc %{_mandir}/man1/pitrery.1.gz
%doc %{_mandir}/man1/archive_xlog.1.gz
%doc %{_mandir}/man1/restore_xlog.1.gz

%changelog
* Fri Dec 15 2017 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 2.1-1
- Update to 2.1

* Fri Oct 20 2017 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 2.0-1
- Update to 2.0

* Tue May 23 2017 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.13-1
- Update to 1.13

* Fri Nov 18 2016 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.12-1
- Update to 1.12

* Mon Jun 20 2016 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.11-1
- Update to 1.11

* Mon Oct 19 2015 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.10-1
- Update to 1.10

* Fri Oct  9 2015 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.9-1
- Update to 1.9

* Thu Feb 19 2015 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.8-2
- Do not depend on pax, it is no longer the default

* Wed Dec 31 2014 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.8-1
- Update to 1.8

* Sat Apr 19 2014 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.7-1
- Update to 1.7
- Upstream has removed /usr/bin/pitr_mgr

* Tue Feb 18 2014 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.6-1
- Update to 1.6
- store configuration files in /etc/pitrery

* Sun Sep  1 2013 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.5-1
- Update to 1.5

* Mon Jul 15 2013 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.4-1
- Update to 1.4

* Thu May 30 2013 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.3-1
- Update to 1.3

* Fri Apr  5 2013 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.2-1
- Update to 1.2

* Thu Dec 15 2011 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.1-1
- Update to 1.1

* Thu Aug 11 2011 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.0-1
- Update to 1.0

* Mon Aug  8 2011 Nicolas Thauvin <nicolas.thauvin@dalibo.com> - 1.0rc2-1
- New package

