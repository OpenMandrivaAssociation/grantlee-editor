Summary:	Grantlee editor for KDE PIM applications
Name:		grantlee-editor
Version:	17.04.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5KaddressbookGrantlee)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5SyntaxHighlighting)
Provides:	grantleeeditor = %{EVRD}
Conflicts:	contactthemeeditor < 3:17.04.0
Conflicts:	grantleeeditor < 3:17.04.0
Conflicts:	headerthemeeditor < 3:17.04.0
Obsoletes:	contactthemeeditor < 3:17.04.0
Obsoletes:	grantleeeditor < 3:17.04.0
Obsoletes:	headerthemeeditor < 3:17.04.0

%description
Grantlee editor for KDE PIM applications.

%files
%{_kde5_applicationsdir}/org.kde.contactprintthemeeditor.desktop
%{_kde5_applicationsdir}/org.kde.contactthemeeditor.desktop
%{_kde5_applicationsdir}/org.kde.headerthemeeditor.desktop
%{_kde5_bindir}/contactprintthemeeditor
%{_kde5_bindir}/contactthemeeditor
%{_kde5_bindir}/headerthemeeditor
%{_kde5_datadir}/config.kcfg/grantleethemeeditor.kcfg
%{_kde5_docdir}/*/*/contactthemeeditor
%{_kde5_docdir}/*/*/headerthemeeditor
%{_kde5_sysconfdir}/xdg/grantleeditor.categories
%{_kde5_sysconfdir}/xdg/grantleeditor.renamecategories

#----------------------------------------------------------------------------

%define grantleethemeeditor_major 5
%define libgrantleethemeeditor %mklibname grantleethemeeditor %{grantleethemeeditor_major}

%package -n %{libgrantleethemeeditor}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libgrantleethemeeditor}
KDE PIM shared library.

%files -n %{libgrantleethemeeditor}
%{_kde5_libdir}/libgrantleethemeeditor.so.%{grantleethemeeditor_major}*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

rm -rf %{buildroot}%{_kde5_libdir}/libgrantleethemeeditor.so
