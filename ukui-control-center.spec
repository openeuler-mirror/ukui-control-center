%define debug_package %{nil}
Name:           ukui-control-center
Version:        3.1.2
Release:        10
Summary:        utilities to configure the UKUI desktop
License:        GPL-2+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz
Patch01:        0001-fix-compile-error-of-ukui-control-center.patch
Patch02:        0001-modify-version-info-error.patch
Patch03:        0003-fix-power-missing-issue.patch
Patch05:        0005-Fix-the-problem-of-displaying-none-in-the-interface-version-information.patch
Patch07:        0007-modify-icon-theme-not-display.patch
Patch08:        ukui-control-center-3.0.4-fix-invalid-automatic-login.patch
Patch10:        0010-Fix-the-problem-of-scrambled-shortcut-keys.patch
Patch11:	Fix-about-copyright-display-error.patch

BuildRequires: qt5-qtsvg-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: libmatekbd-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libxklavier-devel
BuildRequires: libkscreen-qt5-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: dconf-devel
BuildRequires: libmatemixer-devel
BuildRequires: libxml2-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libX11-devel
BuildRequires: libxkbfile-devel
BuildRequires: boost-devel
BuildRequires: qt5-qttools-devel
BuildRequires: libxcb-devel
BuildRequires: polkit-qt5-1-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libpwquality-devel
BuildRequires: xorg-x11-server-devel
BuildRequires: upower-devel
BuildRequires: pam-devel
BuildRequires: ukui-interface 
BuildRequires: mate-desktop-devel
BuildRequires: libddcutil-devel
BuildRequires: libkylin-chkname-devel
BuildRequires: cups-devel
#compile need  but control is not exist
BuildRequires: kf5-kguiaddons-devel

Requires: dconf
Requires: ukui-search 
Requires: kylin-nm
Requires: ukui-bluetooth
Requires: ukui-media 
Requires: ukui-themes
#install need  but control is not exist
Requires: libkylin-chkname1


Suggests: gsettings-desktop-schemas
Suggests: mate-common
Suggests: ukui-power-manager
Suggests: ukui-session-manager
Suggests: ukui-screensaver
Suggests: ukui-settings-daemon


%description
 The UKUI control center contains configuration applets for the UKUI desktop,
 allowing to set accessibility configuration, desktop fonts, keyboard
 and mouse properties, sound setup, desktop theme and background, user
 interface properties, screen resolution, and other UKUI parameters.

%package -n libukcc-devel
Summary:  libukcc
%description -n libukcc-devel
The UKUI control center contains configuration applets for the UKUI des allowing to set accessibility configuration, desktop fonts, keyboard and mouse properties, sound setup, desktop theme and background, user interface properties, screen resolution, and other UKUI parameters.

%prep
%autosetup -n %{name}-%{version} -p1

%build
qmake-qt5
make -j4

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/etc/xdg/autostart/

%post
set -e
glib-compile-schemas /usr/share/glib-2.0/schemas/ &> /dev/null ||:

chown root:root /usr/bin/checkUserPwd
chmod u+s /usr/bin/checkUserPwd

sed  -i "1iauth    sufficient      pam_succeed_if.so user ingroup nopasswdlogin"   /etc/pam.d/lightdm
groupadd nopasswdlogin &> /dev/null ||:

gsettings set org.ukui.power-manager sleep-computer-battery 0 &> /dev/null ||:
gsettings set org.ukui.power-manager sleep-computer-ac 0 &> /dev/null ||:

%postun
sed  -i "/auth    sufficient      pam_succeed_if.so user ingroup nopasswdlogin/d" /etc/pam.d/lightdm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/dbus-1/system.d/*
%{_sysconfdir}/pam.d/*
/lib/systemd/system/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/dbus-1/system-services/*
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/kylin-user-guide/data/*
%{_datadir}/locale/zh_CN/LC_MESSAGES/*
%{_datadir}/polkit-1/actions/*
%{_datadir}/ukui/faces/*
%{_datadir}/ukui-control-center/shell/res/*
%{_libdir}/ukui-control-center/*
%{_datadir}/lightdm/lightdm.conf.d/95-SeatDefaults.conf

%files -n libukcc-devel
%{_includedir}/ukcc/interface/*.h
%{_includedir}/ukcc/widgets/*.h
%{_libdir}/libukcc*


%changelog
* Mon Feb 27 2023 tanyulong <tanyulong@kylinos.cn> - 3.1.2-10
- Fix about copyright display error

* Tue Feb 7 2023 douyan <douyan@kylinos.cn> - 3.1.2-9
- change power default setting

* Mon Jan 9 2023 peijiankang <peijiankang@kylinos.cn> - 3.1.2-8
- add patch10: 0010-Fix-the-problem-of-scrambled-shortcut-keys.patch

* Fri Dec 30 2022 huayadong <huayadong@kylinos.cn> - 3.1.2-7
- Fix invalid automatic login, fix invalid password free login

* Thu Dec 29 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-6
- modify icon theme not display

* Fri Dec 23 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-5
- add patch5: 0005-Fix-the-problem-of-displaying-none-in-the-interface-version-information.patch

* Thu Dec 15 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-4
- fix power missing issue

* Fri Dec 9 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-3
- add libkylin-chkname1 Requires to fix useradd error

* Fri Dec 9 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-2
- modify version-info error

* Mon Dec 5 2022 peijiankang <peijiankang@kylinos.cn> - 3.1.2-1
- update version to 3.1.2

* Mon Aug 08 2022 tanyulong <tanyulong@kylinos.cn> - 3.0.1-29
- update and modify translations

* Thu Aug 04 2022 tanyulong <tanyulong@kylinos.cn> - 3.0.1-28
- fix and update translation

* Fri Jul 29 2022 tanyulong <tanyulong@kylinos.cn> - 3.0.1-27
- modify displayed size after the installation and download of system update completed

* Thu Jul 28 2022 tanyulong <tanyulong@kylinos.cn> - 3.0.1-26
- add dependency ddcutil to make HDMI brightness adjustment available

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
