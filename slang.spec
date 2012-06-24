Summary:	Shared library for C like extension language
Summary(de):	Shared Library f�r eine C-artige Sprache
Summary(es):	Biblioteca compartida para leguaje de extensi�n semejante a C
Summary(fr):	Biblioth�que partag�e pour le langage d'extension C like
Summary(pl):	Biblioteka Slang
Summary(pt_BR):	Biblioteca compartilhada para linguagem de extens�o semelhante a C
Summary(ru):	����������� ���������� C-��������� ����� ���������� S-Lang
Summary(tr):	C benzeri dil i�in ortak kitapl�k
Summary(uk):	��̦����� �Ц������ ������������ C-��Ħ��ϧ ���� ���������� S-Lang
Name:		slang
Version:	2.0.5
Release:	1.1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://space.mit.edu/pub/davis/slang/v2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	8b6afa085f76b1be29825f0c470b6cad
Source1:	ftp://space.mit.edu/pub/davis/slang/v2.0/%{name}doc-2.0.4.tar.gz
# Source1-md5:	1c7acca555a4ad1c165048f751e09b02
Patch0:		%{name}-nodevel.patch
Patch1:		%{name}-remove_unused_terminfo_paths.patch
URL:		http://www.s-lang.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	pcre-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	libslang1
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

%description -l es
Slang (se pronuncia "sssslang") es un potente interpretador que
soporta C-como sintaxis. Fue escrito en el inicio para ser f�cilmente
embutido en un programa para volverlo m�s extensible. Slang tambi�n
nos ofrece una manera de r�pidamente desarrollar y depurar
aplicaciones, empotr�ndolo de manera segura y eficiente. Desde que
slang se parece a C, se hizo f�cil recodificar los procedimientos
slang en C, si hace falta.

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

%description -l pt_BR
Slang (pronunc�a-se "sssslang") � um poderoso interpretador que
suporta C-como sintaxe. Ele foi escrito no in�cio para ser facilmente
embutido em um programa para torn�-lo mais extens�vel. Slang tamb�m
oferece uma maneira de rapidamente desenvolver e depurar aplica��es,
embutindo-o de maneira segura e eficiente. Desde que slang
assemelhou-se com C, tornou-se f�cil re-codificar os procedimentos
slang em C se necess�rio.

%description -l ru
Slang - ��� ������ �������� �������������, �������������� C-��������
���������. � ������ ������ �� �������������� ���, ����� ��� ����� ����
����� ���������� � ���������, ����� �� ������������. Slang ����� ����
����������� ������� ���������� � ������� �������� �����������
����������� � ������������ ����������� � ��� ���������. ��� ��� Slang
���������� C, �� ��� ������������� ����� �����������, ����� ����������
����� �������������� ��� ��������� slang � C.

%description -l tr
Slang, C'ye benzer bir yaz�m� olan, g��l�, y���n-tabanl� bir
yorumlay�c�d�r. C'ye benzer oldu�undan Slang ile yaz�lm�� kodlar� C'ye
�evirmek olduk�a kolayd�r.

%description -l uk
Slang - �� �������� �������� �������������, �� Ц�����դ C-��Ħ����
���������. � ������ ������� צ� ����������� ���, ��� ���� ����� ����
����� ����������� � ��������, ������� �� �������������. Slang �����
��� �����צ��� �����ϧ �������� �� צ������������� ������� �������
���������� �� ����������� ������������ � æ ��������. Slang �����դ C,
��� ��, ��� ��������Φ ���ϧ �������, ������� ������ �����
������������ �Ӧ ��������� Slang � C.

%package libs
Summary:	Shared libraries for slang C like language
Summary(pl):	Biblioteka wsp�dzielona Slang
Group:		Libraries

%description libs
Shared libraries for slang C like language

%description libs -l pl
Biblioteka wsp�dzielona Slang.

%package devel
Summary:	header files for slang C like language
Summary(de):	Header-Dateien f�r eine Slangvariante der C-Sprache
Summary(es):	Biblioteca y archivos de inclusi�n para slang
Summary(fr):	En-t�tes pour le langage slang
Summary(pl):	Pliki nag��wkowe dla slanga
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para slang
Summary(ru):	���������� � ������ ��� C-��������� ����� S-Lang
Summary(tr):	slang dili i�in statik kitapl�k ve ba�l�k dosyalar�
Summary(uk):	��̦����� �� ������ ��� C-��Ħ��ϧ ���� S-Lang
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	libslang1-devel

%description devel
This package contains header files required to develop slang-based
applications. It also includes documentation to help you write
slang-based apps.

%description devel -l de
Dieses Paket enth�lt Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten
Anwendungen ist enthalten.

%description devel -l es
Este paquete contiene las bibliotecas y archivos de inclusi�n slang,
necesarios al desarrollo de aplicaciones basadas en slang.

%description devel -l fr
Ce paquetage contient les biblioth�ques statiques et les en-t�tes
slang pour d�velopper des applications en slang. Il contient aussi la
documentation pour vous aider � �crire ces applications.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe slang. Znajduje si� tutaj r�wnie�
dokumentacja, kt�ra pomo�e Ci w pisaniu aplikacji pod t� bibliotek�.

%description devel -l pt_BR
Este pacote cont�m as bibliotecas e arquivos de inclus�o slang,
necess�rias ao desenvolvimento de aplica��es baseadas em slang.

%description devel -l ru
���� ����� �������� ���������� � ������, ����������� ��� ����������
��������, ������������ Slang.

%description devel -l tr
Bu paket slang tabanl� uygulamalar geli�tirmek i�in gereken ba�l�k
dosyalar� ve kitapl�klar�n yan�s�ra slang yard�m belgelerini de
i�erir.

%description devel -l uk
��� ����� ͦ����� ¦�̦����� �� ������, ����Ȧ�Φ ��� ��������
�������, �� �������������� Slang.

%package static
Summary:	slang static library
Summary(pl):	Biblioteka statyczna slang
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com slang
Summary(ru):	����������� ���������� ��� C-��������� ����� S-Lang
Summary(uk):	�������� ¦�̦����� ��� C-��Ħ��ϧ ���� S-Lang
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains the slang static libraries.

%description static -l de
Dieses Paket enth�lt die statischen Libraries.

%description static -l pl
Biblioteka statyczna slang.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com slang.

%description static -l ru
���� ����� �������� ����������� ����������, ����������� ��� ����������
��������, ������������ Slang.

%description static -l uk
��� ����� ͦ����� �������� ¦�̦�����, ����Ȧ��� ��� �������� �������,
�� �������������� Slang.

%package png
Summary:	PNG module for Slang
Summary(pl):	Modu� PNG dla Slanga
Group:		Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description png
PNG module for Slang.

%description png -l pl
Modu� PNG dla Slanga.

%package pcre
Summary:	PCRE module for Slang
Summary(pl):	Modu� PCRE dla Slanga
Group:		Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description pcre
PCRE module for Slang.

%description pcre -l pl
Modu� PCRE dla Slanga.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-pcre \
	--with-png

%{__make} elf \
	ELF_CFLAGS="%{rpmcflags} -fPIC"
%{__make} all \
	CFLAGS="%{rpmcflags}"

%{__make} -C slsh \
	DL_LIB="-ldl" \
	ARCH="elf" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -j1 install-elf \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-links \
	DESTDIR=$RPM_BUILD_ROOT

install slsh/slsh $RPM_BUILD_ROOT%{_bindir}

cp -a modules examples demo src/curses $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# help rpmdeps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/v2/modules/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/slsh.rc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/slsh
%{_mandir}/man1/*.1*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/v2
%dir %{_libdir}/%{name}/v2/modules
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/*.so
%attr(755,root,root) %exclude %{_libdir}/%{name}/v2/modules/png-module.so
%attr(755,root,root) %exclude %{_libdir}/%{name}/v2/modules/pcre-module.so

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt doc/text/*.txt
%attr(755,root,root) %{_libdir}/libslang*.so
%{_includedir}
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libslang*.a

%files png
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/png-module.so

%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/pcre-module.so
