#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Grantlee editor for KDE PIM applications
Name:		plasma6-grantlee-editor
Version:	24.05.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/grantlee-editor/-/archive/%{gitbranch}/grantlee-editor-%{gitbranchd}.tar.bz2#/grantlee-editor-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/grantlee-editor-%{version}.tar.xz
%endif
Patch0:		grantlee-editor-menus.patch
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KPim6PimCommon)
BuildRequires:	cmake(KPim6MessageViewer)
BuildRequires:	cmake(KPim6GrantleeTheme)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(KF6KIO)
Provides:	grantleeeditor = %{EVRD}

%description
Grantlee editor for KDE PIM applications.

%files -f all.lang
%{_datadir}/applications/org.kde.contactprintthemeeditor.desktop
%{_datadir}/applications/org.kde.contactthemeeditor.desktop
%{_datadir}/applications/org.kde.headerthemeeditor.desktop
%{_bindir}/contactprintthemeeditor
%{_bindir}/contactthemeeditor
%{_bindir}/headerthemeeditor
%{_datadir}/config.kcfg/grantleethemeeditor.kcfg
%{_docdir}/*/*/contactthemeeditor
%{_docdir}/*/*/headerthemeeditor
%{_datadir}/qlogging-categories6/grantleeditor.categories
%{_datadir}/qlogging-categories6/grantleeditor.renamecategories

#----------------------------------------------------------------------------

%define grantleethemeeditor_major 6
%define libgrantleethemeeditor %mklibname grantleethemeeditor %{grantleethemeeditor_major}

%package -n %{libgrantleethemeeditor}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libgrantleethemeeditor}
KDE PIM shared library.

%files -n %{libgrantleethemeeditor}
%{_libdir}/libgrantleethemeeditor.so.%{grantleethemeeditor_major}*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n grantlee-editor-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

rm -rf %{buildroot}%{_libdir}/libgrantleethemeeditor.so

%find_lang contactthemeeditor
%find_lang headerthemeeditor
%find_lang libgrantleethemeeditor
%find_lang contactprintthemeeditor

cat *.lang >all.lang
