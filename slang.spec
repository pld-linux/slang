# _without_embed - don't build uClibc version
%define		docver  1.4
Summary:	shared library for C like extension language
Summary(de):	Shared Library f�r eine C-artige Sprache
Summary(fr):	Biblioth�que partag�e pour le langage d'extension C like
Summary(pl):	Biblioteka Slang
Summary(tr):	C benzeri dil i�in ortak kitapl�k
Name:		slang
Version:	1.4.5
Release:	2
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://space.mit.edu/pub/davis/slang/v1.4/%{name}-%{version}.tar.bz2
Source1:	ftp://space.mit.edu/pub/davis/slang/v1.4/%{name}%{docver}-doc.tar.gz
Patch0:		%{name}-security.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-nodevel.patch
Patch3:		%{name}-uclibc_ac_fix.patch
Patch4:		%{name}-remove_unused_terminfo_paths.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/slang

%description
Slang (pronounced ``sssslang'') is a powerful stack based interpreter
that supports a C-like syntax. It has been designed from the beginning
to be easily embedded into a program to make it extensible. Slang also
provides a way to quickly develop and debug the application embedding
it in a safe and efficient manner. Since slang resembles C, it is easy
to recode slang procedures in C if the need arises.

%description -l de
Slang (sprich ``sssslang'') ist ein leistungsf�higer stapelbasierter
Interpreter, der eine C-�hnliche Syntax unterst�tzt. Er kann auf
einfache Weise in ein Programm eingebettet werden, damit dieses
erweiterbar wird. Slang bietet au�erdem eine M�glichkeit zum schnellen
Entwickeln und Debuggen der Anwendung, in die er eingebettet ist. Da
Slang C �hnlich ist, k�nnen Slang-Vorg�nge einfach in C umgeschrieben
werden.

%description -l fr
slang (prononcez � sssslang �) est un interpr�teur puissant offrant
une syntaxe � la C. Il a �t� con�u au d�but pour �tre facilement
int�gr� dans un programme afin de le rendre extensible. slang offre
aussi le moyen de developper et d�bugger rapidement l'application
int�gr�e de fa�on s�re et efficace. Comme slang ressemble � C, il est
facile de recoder les proc�dures slang en C si besoin est.

%description -l pl
Slang jest opart� o terminfo bibliotek� do obs�ugi terminali
znakowych, posiadaj�c� wbudowany interpreter j�zyka podobnego
sk�adniowo do C. Na pocz�tku by� on przeznaczony aby �atwo da� si�
osadza� w aplikacj� i uczyni� j� rozszerzon�. Slang zapewnia
mechanizmy u�atwiaj�ce szybkie tworzenie rozbudowanych, �atwo
konfigurowalnych aplikacji. Slang r�wnie� umo�liwia proste
prze�ledzenie ewentualnych b��d�w w aplikacjach w bezpieczny i wydajny
spos�b.

%description -l tr
Slang, C'ye benzer bir yaz�m� olan, g��l�, y���n-tabanl� bir
yorumlay�c�d�r. C'ye benzer oldu�undan Slang ile yaz�lm�� kodlar� C'ye
�evirmek olduk�a kolayd�r.

%package devel
Summary:	header files for slang C like language
Summary(de):	Header-Dateien f�r eine Slangvariante der C-Sprache
Summary(fr):	En-t�tes pour le langage slang
Summary(pl):	Pliki nag��wkowe dla slanga
Summary(tr):	slang dili i�in statik kitapl�k ve ba�l�k dosyalar�
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains header files required to develop slang-based
applications. It also includes documentation to help you write
slang-based apps.

%description devel -l de
Dieses Paket enth�lt Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten
Anwendungen ist enthalten.

%description devel -l fr
Ce paquetage contient les biblioth�ques statiques et les en-t�tes
slang pour d�velopper des applications en slang. Il contient aussi la
documentation pour vous aider � �crire ces applications.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe slang. Znajduje si� tutaj r�wnie�
dokumentacja, kt�ra pomo�e Ci w pisaniu aplikacji pod t� bibliotek�.

%description devel -l tr
Bu paket slang tabanl� uygulamalar geli�tirmek i�in gereken ba�l�k
dosyalar� ve kitapl�klar�n yan�s�ra slang yard�m belgelerini de
i�erir.

%package static
Summary:	slang static library
Summary(pl):	Biblioteka statyczna slang
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the slang static libraries.

%description static -l de
Dieses Paket enth�lt die statischen Libraries.

%description static -l pl
Biblioteka statyczna slang.

%prep
%setup  -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
mv -f autoconf/aclocal.m4 acinclude.m4
mv -f autoconf/configure.in .
aclocal
autoconf
(cd demo
cp -f ../acinclude.m4 .
aclocal
autoconf)
%configure

%{__make} elf ELF_CFLAGS="%{rpmcflags} -fPIC" CC="%{__cc}"
%{__make} all CFLAGS="%{rpmcflags}"
%{__make} -C slsh DL_LIB="-ldl" ARCH="elf" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

%{__make} install install-elf install-links \
	DESTDIR=$RPM_BUILD_ROOT

install slsh/slsh $RPM_BUILD_ROOT%{_bindir}

cp -a modules examples demo src/curses $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf doc/sgml/* doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html doc/*.gz
%attr(755,root,root) %{_libdir}/libslang.so
%{_includedir}
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libslang.a
