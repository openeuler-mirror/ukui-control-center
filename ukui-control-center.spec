%define debug_package %{nil}
Name:           ukui-control-center
Version:        3.0.1
Release:        1
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
#BuildRequires: libkscreen
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
#Requires: libkscreen
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

Recommends: qt5-qtquickcontrols

Suggests: gsettings-desktop-schemas
Suggests: mate-common
Suggests: ukui-power-manager
Suggests: ukui-session-manager
Suggests: ukui-screensaver
Suggests: ukui-settings-daemon
#Suggests: qt5-qtgraphicaleffects


%description
 The UKUI control center contains configuration applets for the UKUI desktop,
 allowing to set accessibility configuration, desktop fonts, keyboard
 and mouse properties, sound setup, desktop theme and background, user
 interface properties, screen resolution, and other UKUI parameters.

%prep
%setup -q

%build
qmake-qt5 
make

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

%post
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/

systemctl enable ukui-group-manager.service
systemctl start  ukui-group-manager.service
chown root:root /usr/bin/checkuserpwd
chmod u+s /usr/bin/checkuserpwd

%preun
systemctl disable ukui-group-manager.service
systemctl stop ukui-group-manager.service

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_sysconfdir}/dbus-1/system.d/*
%{_bindir}/launchSysDbus
%{_bindir}/ukui-control-center
#%%{_prefix}/lib/control-center/*
%{_libdir}/ukui-control-center/*
%{_datadir}/applications/*
%{_datadir}/dbus-1/system-services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/locale/zh_CN/LC_MESSAGES/*
%{_datadir}/ukui/faces/*
%{_datadir}/ukui-control-center/shell/res/i18n
%{_sbindir}/group-manager-server
%{_bindir}/checkuserpwd
%{_prefix}/lib/systemd/system/ukui-group-manager.service


%changelog
* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.1-1

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.0.3-1
- Init package for openEuler
