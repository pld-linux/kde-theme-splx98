
%define		_name	splx98

Summary:	KDE theme - %{_name}
Summary(pl.UTF-8):   Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	0.2
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.speleoalex.altervista.org/download/%{_name}.tar.gz
# Source0-md5:	19d2ee5b82e6128182713ffb671e8094
URL:		http://www.kde-look.org/content/show.php?content=12598
Requires:	kde-style-%{_name}
Requires:	kde-icons-%{_name}
Requires:	kde-colorscheme-%{_name}
Requires:	kde-wallpaper-%{_name}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Splx98 style resembles an unthemed Windows 98 look and feel.

%description -l pl.UTF-8
Splx98 odwzorowuje wygląd domyślny Windows 98.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl.UTF-8):   Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
Splx98 style resembles an unthemed Windows 98 look and feel.

%description -n kde-style-%{_name} -l pl.UTF-8
Splx98 odwzorowuje wygląd domyślny Windows 98.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl.UTF-8):   Motyw ikon do kde - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
An icon theme that resembles the Windows 98 hicolor icons.

%description -n kde-icons-%{_name} -l pl.UTF-8
Motyw ikon odpowiadający ikonom w Windows 98.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl.UTF-8):   Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
Default Windows 98 color scheme.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Domyślny schemat kolorów Windows 98.

%package -n kde-wallpaper-%{_name}
Summary:	KDE wallpaper - %{_name}
Summary(pl.UTF-8):   Tapeta do KDE - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdelibs

%description -n kde-wallpaper-%{_name}
Wallpapers similar to those distributed with Windows 98/ME.

%description -n kde-wallpaper-%{_name} -l pl.UTF-8
Tapety podobne do dostarczanych z Windows 98/ME.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes

cd $RPM_BUILD_ROOT
%{__tar} xfz %{SOURCE0}
mv -f icons $RPM_BUILD_ROOT%{_datadir}
mv -f wallpapers $RPM_BUILD_ROOT%{_datadir}
mv -f kstyle $RPM_BUILD_ROOT%{_datadir}/apps
mv -f splx98.kcsrc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
rm -rf *.sh
rm -rf *.spec
sed -i -e "s,mdk-hicolor,crystalsvg," $RPM_BUILD_ROOT%{_iconsdir}/splx98/index.desktop
echo "Comment=A clone of the standard Windows 98 icon theme." >> $RPM_BUILD_ROOT%{_iconsdir}/splx98/index.desktop

%post -n kde-style-%{_name}
/sbin/ldconfig
echo "You may have to run kinstalltheme for this theme to become available"
echo "in currently opened sessions."

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kstyle/themes/*.themerc
%{_datadir}/apps/kstyle/pixmaps/*

%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%{_iconsdir}/*

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-wallpaper-%{_name}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*
