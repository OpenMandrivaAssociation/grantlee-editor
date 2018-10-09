%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Grantlee editor for KDE PIM applications
Name:		grantlee-editor
Version:	18.08.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5KaddressbookGrantlee)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(KF5KIO)
Provides:	grantleeeditor = %{EVRD}
Conflicts:	contactthemeeditor < 3:17.04.0
Conflicts:	grantleeeditor < 3:17.04.0
Conflicts:	headerthemeeditor < 3:17.04.0
Obsoletes:	contactthemeeditor < 3:17.04.0
Obsoletes:	grantleeeditor < 3:17.04.0
Obsoletes:	headerthemeeditor < 3:17.04.0

%description
Grantlee editor for KDE PIM applications.

%files -f all.lang
%{_kde5_applicationsdir}/org.kde.contactprintthemeeditor.desktop
%{_kde5_applicationsdir}/org.kde.contactthemeeditor.desktop
%{_kde5_applicationsdir}/org.kde.headerthemeeditor.desktop
%{_bindir}/contactprintthemeeditor
%{_bindir}/contactthemeeditor
%{_bindir}/headerthemeeditor
%{_datadir}/config.kcfg/grantleethemeeditor.kcfg
%{_docdir}/*/*/contactthemeeditor
%{_docdir}/*/*/headerthemeeditor
%{_sysconfdir}/xdg/grantleeditor.categories
%{_sysconfdir}/xdg/grantleeditor.renamecategories

#----------------------------------------------------------------------------

%define grantleethemeeditor_major 5
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
%setup -q
%cmake_kde5

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
