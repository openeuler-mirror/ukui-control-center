%define debug_package %{nil}
Name:           ukui-control-center
Version:        3.0.1
Release:        25
Summary:        utilities to configure the UKUI desktop
License:        GPL-2+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: libmatekbd-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libxklavier-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: libkscreen-qt5-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: dconf-devel
BuildRequires: edid-decode
BuildRequires: redshift
BuildRequires: libmatemixer-devel
BuildRequires: libqtxdg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: libxml2-devel
BuildRequires: libcanberra-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: mate-desktop-devel
BuildRequires: libX11-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbfile-devel
BuildRequires: boost-devel
BuildRequires: libxcb-devel
BuildRequires: qt5-linguist
BuildRequires: polkit-qt5-1-devel
BuildRequires: pam-devel
BuildRequires: systemd-devel

BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-bluez-qt-devel
BuildRequires: opencv
BuildRequires: libddcutil-devel
BuildRequires: upower-devel
BuildRequires: libpwquality-devel
BuildRequires: xorg-x11-server-devel



Requires: dconf
Requires: qt5-qtimageformats
Requires: qt5-qtsvg-devel
Requires: gsettings-qt-devel
Requires: glib2-devel
Requires: libmatekbd-devel
Requires: qt5-qtx11extras-devel
Requires: libxklavier-devel
Requires: kf5-kwindowsystem-devel
Requires: kf5-kwidgetsaddons-devel
Requires: kf5-kconfig-devel
Requires: kf5-kconfigwidgets-devel
Requires: kf5-ki18n-devel
Requires: libkscreen-qt5-devel
Requires: qt5-qtdeclarative-devel
Requires: dconf-devel
Requires: edid-decode
Requires: redshift
Requires: libmatemixer-devel
Requires: libqtxdg-devel
Requires: qt5-qtmultimedia-devel
Requires: libxml2-devel
Requires: network-manager-applet
Requires: libcanberra-devel
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtquickcontrols

Requires: ddcutil
Requires: glib2
Requires: systemd-pam


Recommends: qt5-qtquickcontrols

Suggests: gsettings-desktop-schemas
Suggests: mate-common
Suggests: ukui-power-manager
Suggests: ukui-session-manager
Suggests: ukui-screensaver
Suggests: ukui-settings-daemon
#Suggests: qt5-qtgraphicaleffects

Patch01:Modify-the-icon-displayed-on-the-tray.patch

%description
 The UKUI control center contains configuration applets for the UKUI desktop,
 allowing to set accessibility configuration, desktop fonts, keyboard
 and mouse properties, sound setup, desktop theme and background, user
 interface properties, screen resolution, and other UKUI parameters.

%prep
%setup -q
%patch01 -p1

%build
qmake-qt5
make -j24

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/etc/xdg/autostart/

%post
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/ &> /dev/null ||:

chown root:root /usr/bin/checkuserpwd
chmod u+s /usr/bin/checkuserpwd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/dbus-1/system.d/*
%{_bindir}/launchSysDbus
%{_bindir}/ukui-control-center
%{_libdir}/ukui-control-center/*
%{_datadir}/applications/*
%{_datadir}/dbus-1/system-services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/locale/zh_CN/LC_MESSAGES/*
%{_datadir}/ukui/faces/*
%{_datadir}/ukui-control-center/shell/res/i18n
%{_bindir}/group-manager-server
%{_bindir}/checkuserpwd
%{_bindir}/checkUserPwd
%{_datadir}/polkit-1/actions/org.ukui.groupmanager.policy
%{_sysconfdir}/pam.d/control-center
/lib/systemd/system/ukui-group-manager.service
%{_bindir}/childCheckpwdwithPAM
%{_bindir}/ukui-control-center-session
%{_datadir}/dbus-1/services/org.ukui.ukcc.session.service
%{_datadir}/kylin-user-guide/data/*
%{_datadir}/polkit-1/actions/com.control.center.qt.systemdbus.policy
%{_datadir}/ukui-control-center/shell/res/search.xml


%changelog
* Tue Jun 28 2022 peijiankang <peijiankang@kylinos.cn> - 3.0.1-25
- update about.png for openEuler

* Fri Apr 29 2022 huayadong <huayadong@kylinos.cn> - 3.0.1-24
- Modify the icon displayed on the tray

* Tue Apr 19 2022 pei-jiankang <peijiankang@kylinos.cn> - 3.0.1-23
- modify ukui-control-center install error

* Fri Mar 25 2022 huayadong <huayadong@kylinos.cn> - 3.0.1-22
- The shortcut keys of the same function are combined together

* Thu Oct 28 2021 tanyulong <tanyulong@kylinos.cn> - 3.0.1-21
- fix net sort wifi strength

* Tue Oct 19 2021 peijiankang <peijiankang@kylinos.cn> - 3.0.1-20
- add 0014-modify-the-error-of-ukui-control-center-open.patch

* Thu Sep 16 2021 douyan <douyan@kylinos.cn> - 3.0.1-19
- add fix_user_passwd_valid_issue.patch

* Sat Sep 11 2021 peijiankang <peijiankang@kylinos.cn> - 3.0.1-18
- add 0013-cpuinfo-in-arm-system-is-null.patch

* Mon Sep 6 2021 douyan <douyan@kylinos.cn> - 3.0.1-17
- add fix_user_passwd_valid_time_setting_failed_issue.patch

* Thu Sep 2 2021 douyan <douyan@kylinos.cn> - 3.0.1-16
- fix add group failed issue

* Wed Sep 1 2021 douyan <douyan@kylinos.cn> - 3.0.1-15
- fix arm verion root user open ukui-control-center crash issue

* Thu Jul 29 2021 tanyulong <tanyulong@kylinos.cn> - 3.0.1-14
- solve compile build error

* Fri Jul 16 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-13
- fix failed to view remote desktop

* Tue Jul 13 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-12
- window add title icon

* Mon Jul 12 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-11
- power add sleep function

* Mon Jul 12 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-10
- Added translation using Weblate Tibetan add bo_CN.ts file

* Mon Jul 12 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-9
- fix layout optimization

* Fri Jul 09 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-8
- fix redeclaration of QStringList usergroupList

* Fri Jul 09 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-7
- fix vnc crashed

* Thu Jul 08 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-6
- fix-Group-members-are-not-displayed

* Thu Jul 08 2021 tanyulong<tanyulong@kylinos.cn> - 3.0.1-5
- add-judgment-when-Bluetooth-does-not-exist.patch

* Thu Jan 21 2021 lvhan <lvhan@kylinos.cn> - 3.0.1-4
- fix-blueman-tray-and-groupadd-autologin

* Thu Dec 3 2020 lvhan <lvhan@kylinos.cn> - 3.0.1-3
- fix dialog pop twice after modifying resolution
- fix effects mode not available

* Mon Nov 30 2020 lvhan <lvhan@kylinos.cn> - 3.0.1-2
- fix autologin nopasswdlogin failed
- fix system overview failed

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.0-1+1031

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.0.3-1
- Init package for openEuler
