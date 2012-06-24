%define		docver	1.4
Summary:    	shared library for C like extension language
Summary(de):	Shared Library f�r eine C-artige Sprache 
Summary(fr):	Biblioth�que partag�e pour le langage d'extension C like
Summary(pl):	Biblioteka Slang
Summary(tr):	C benzeri dil i�in ortak kitapl�k
Name:      	slang
Version:   	1.3.9
Release:     	1
Serial:		1
Copyright:   	GPL
Group:       	Libraries
Group(pl):	Biblioteki
Source0:	ftp://space.mit.edu/pub/davis/slang/%{name}-%{version}.tar.gz
Source1:      	ftp://space.mit.edu/pub/davis/slang/%{name}%{docver}-doc.tar.gz
Patch0:		slang-security.patch
Patch1:		slang-keypad.1.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Slang (pronounced ``sssslang'') is a powerful stack based interpreter that
supports a C-like syntax.  It has been designed from the beginning to be
easily embedded into a program to make it extensible. Slang also provides a
way to quickly develop and debug the application embedding it in a safe and
efficient manner.  Since slang resembles C, it is easy to recode slang
procedures in C if the need arises.

%description -l de
Slang (sprich ``sssslang'') ist ein leistungsf�higer stapelbasierter Interpreter,
der eine C-�hnliche Syntax unterst�tzt. Er kann auf einfache Weise in ein
Programm eingebettet werden, damit dieses erweiterbar wird. Slang bietet
au�erdem eine M�glichkeit zum schnellen Entwickeln und Debuggen der 
Anwendung, in die er eingebettet ist. Da Slang C �hnlich ist, k�nnen
Slang-Vorg�nge einfach in C umgeschrieben werden.

%description -l fr
slang (prononcez � sssslang �) est un interpr�teur puissant offrant une
syntaxe � la C. Il a �t� con�u au d�but pour �tre facilement int�gr� dans
un programme afin de le rendre extensible. slang offre aussi le moyen de
developper et d�bugger rapidement l'application int�gr�e de fa�on s�re et
efficace. Comme slang ressemble � C, il est facile de recoder les proc�dures
slang en C si besoin est.

%description -l pl
Slang jest opart� o terminfo bibliotek� do obs�ugi terminali znakowych,
posiadaj�c� wbudowany interpreter j�zyka podobnego sk�adniowo do C.
Na pocz�tku by� on przeznaczony aby �atwo da� si� osadza� w aplikacj� i
uczyni� j� rozszerzon�. Slang zapewnia mechanizmy u�atwiaj�ce szybkie
tworzenie rozbudowanych, �atwo konfigurowalnych aplikacji. Slang r�wnie�
umo�liwia proste prze�ledzenie ewentualnych b��d�w w aplikacjach w
bezpieczny i wydajny spos�b.

%description -l tr
Slang, C'ye benzer bir yaz�m� olan, g��l�, y���n-tabanl� bir yorumlay�c�d�r.
C'ye benzer oldu�undan Slang ile yaz�lm�� kodlar� C'ye �evirmek olduk�a
kolayd�r.

%package devel
Summary:   	header files for slang C like language
Summary(de):	Header-Dateien f�r eine Slangvariante der C-Sprache 
Summary(fr):	En-t�tes pour le langage slang
Summary(pl):	Pliki nag��wkowe dla slanga
Summary(tr):	slang dili i�in statik kitapl�k ve ba�l�k dosyalar�
Group:       	Development/Libraries
Group(pl):   	Programowanie/Biblioteki
Requires:    	%{name} = %{version}

%description devel
This package contains header files required to develop slang-based
applications.  It also includes documentation to help you write slang-based
apps.

%description -l de devel
Dieses Paket enth�lt Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten Anwendungen ist
enthalten.

%description -l pl devel
Pakiet ten zawiera pliki nag��wkowe slang. Znajduje si� tutaj
r�wnie� dokumentacja, kt�ra pomo�e Ci w pisaniu aplikacji pod
ta bibliotek�.

%description -l fr devel
Ce paquetage contient les biblioth�ques statiques et les en-t�tes
slang pour d�velopper des applications en slang. Il contient aussi
la documentation pour vous aider � �crire ces applications.

%description -l tr devel
Bu paket slang tabanl� uygulamalar geli�tirmek i�in gereken ba�l�k dosyalar�
ve kitapl�klar�n yan�s�ra slang yard�m belgelerini de i�erir.

%package static
Summary:     	slang static library
Summary(pl): 	Biblioteka statyczna slang
Group:       	Development/Libraries
Group(pl):   	Programowanie/Biblioteki
Requires:    	%{name}-devel = %{version}

%description static
This package contains the slang static libraries.

%description -l de static
Dieses Paket enth�lt die statischen Libraries.

%description -l pl static
Biblioteka statyczna slang.

%prep
%setup  -q -a1
%patch0 -p1
%patch1 -p1 

%build
LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--includedir=%{_includedir}/slang
	
make elf ELF_CFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS"
make all ELF_CFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS"
cd slsh
make DL_LIB="-ldl" ARCH="elf"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/src/examples/slang,%{_bindir}}

make install install-elf install-links \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	install_include_dir=$RPM_BUILD_ROOT%{_includedir}/slang
	
install -s slsh/slsh $RPM_BUILD_ROOT%{_bindir} 

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

cp -a modules examples demo src/curses $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

gzip -9fn doc/sgml/* doc/*.txt 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/sgml/* doc/*.txt*

%attr(755,root,root) %{_libdir}/libslang.so
%{_includedir}/slang

%{_prefix}/src/examples/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libslang.a
