# TODO: newt module (currently not handled by configure)
#
# Conditional build:
%bcond_without	png	# build slang without PNG module
%bcond_without	onig	# build slang without Oniguruma module
#
Summary:	Shared library for C like extension language
Summary(de.UTF-8):	Shared Library für eine C-artige Sprache
Summary(es.UTF-8):	Biblioteca compartida para leguaje de extensión semejante a C
Summary(fr.UTF-8):	Bibliothèque partagée pour le langage d'extension C like
Summary(pl.UTF-8):	Biblioteka Slang
Summary(pt_BR.UTF-8):	Biblioteca compartilhada para linguagem de extensão semelhante a C
Summary(ru.UTF-8):	Разделяемая библиотека C-подобного языка расширения S-Lang
Summary(tr.UTF-8):	C benzeri dil için ortak kitaplık
Summary(uk.UTF-8):	Бібліотека спільного користування C-подібної мови розширення S-Lang
Name:		slang
Version:	2.3.2
Release:	3
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.jedsoft.org/releases/slang/%{name}-%{version}.tar.bz2
# Source0-md5:	c2d5a7aa0246627da490be4e399c87cb
Patch0:		%{name}-nodevel.patch
Patch1:		%{name}-remove_unused_terminfo_paths.patch
URL:		http://www.jedsoft.org/slang/
%{?with_png:BuildRequires:	libpng-devel}
%{?with_onig:BuildRequires:	oniguruma-devel}
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
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

%description -l de.UTF-8
Slang (sprich ``sssslang'') ist ein leistungsfähiger stapelbasierter
Interpreter, der eine C-ähnliche Syntax unterstützt. Er kann auf
einfache Weise in ein Programm eingebettet werden, damit dieses
erweiterbar wird. Slang bietet außerdem eine Möglichkeit zum schnellen
Entwickeln und Debuggen der Anwendung, in die er eingebettet ist. Da
Slang C ähnlich ist, können Slang-Vorgänge einfach in C umgeschrieben
werden.

%description -l es.UTF-8
Slang (se pronuncia "sssslang") es un potente interpretador que
soporta C-como sintaxis. Fue escrito en el inicio para ser fácilmente
embutido en un programa para volverlo más extensible. Slang también
nos ofrece una manera de rápidamente desarrollar y depurar
aplicaciones, empotrándolo de manera segura y eficiente. Desde que
slang se parece a C, se hizo fácil recodificar los procedimientos
slang en C, si hace falta.

%description -l fr.UTF-8
slang (prononcez « sssslang ») est un interpréteur puissant offrant
une syntaxe à la C. Il a été conçu au début pour être facilement
intégré dans un programme afin de le rendre extensible. slang offre
aussi le moyen de developper et débugger rapidement l'application
intégrée de façon sûre et efficace. Comme slang ressemble à C, il est
facile de recoder les procédures slang en C si besoin est.

%description -l pl.UTF-8
Slang jest opartą o terminfo biblioteką do obsługi terminali
znakowych, posiadającą wbudowany interpreter języka podobnego
składniowo do C. Na początku był on przeznaczony aby łatwo dał się
osadzać w aplikację i uczynić ją rozszerzoną. Slang zapewnia
mechanizmy ułatwiające szybkie tworzenie rozbudowanych, łatwo
konfigurowalnych aplikacji. Slang również umożliwia proste
prześledzenie ewentualnych błędów w aplikacjach w bezpieczny i wydajny
sposób.

%description -l pt_BR.UTF-8
Slang (pronuncía-se "sssslang") é um poderoso interpretador que
suporta C-como sintaxe. Ele foi escrito no início para ser facilmente
embutido em um programa para torná-lo mais extensível. Slang também
oferece uma maneira de rapidamente desenvolver e depurar aplicações,
embutindo-o de maneira segura e eficiente. Desde que slang
assemelhou-se com C, tornou-se fácil re-codificar os procedimentos
slang em C se necessário.

%description -l ru.UTF-8
Slang - это мощный стековый интерпретатор, поддерживающий C-подобный
синтаксис. С самого начала он разрабатывался так, чтобы его можно было
легко встраивать в программы, делая их расширяемыми. Slang также дает
возможность быстрой разработки и отладки программ посредством
безопасного и эффективного встраивания в эти программы. Так как Slang
напоминает C, то при возникновении такой потребности, можно достаточно
легко перекодировать все процедуры slang в C.

%description -l tr.UTF-8
Slang, C'ye benzer bir yazımı olan, güçlü, yığın-tabanlı bir
yorumlayıcıdır. C'ye benzer olduğundan Slang ile yazılmış kodları C'ye
çevirmek oldukça kolaydır.

%description -l uk.UTF-8
Slang - це потужний стековий інтерпретатор, що підтримує C-подібний
синтаксис. З самого початку він розроблявся так, щоб його можна було
легко вбудовувати в програми, роблячи їх розширюваними. Slang також
дає можливість швидкої розробки та відлагоджування програм завдяки
безпечному та ефективному вбудовуванню в ці програми. Slang нагадує C,
так що, при виникненні такої потреби, можливо досить легко
перекодувати всі процедури Slang в C.

%package libs
Summary:	Shared libraries for slang C like language
Summary(pl.UTF-8):	Biblioteka współdzielona Slang
Group:		Libraries
Conflicts:	slang < 1:2.0.5-1.1

%description libs
Shared libraries for slang C like language

%description libs -l pl.UTF-8
Biblioteka współdzielona Slang.

%package devel
Summary:	header files for slang C like language
Summary(de.UTF-8):	Header-Dateien für eine Slangvariante der C-Sprache
Summary(es.UTF-8):	Biblioteca y archivos de inclusión para slang
Summary(fr.UTF-8):	En-têtes pour le langage slang
Summary(pl.UTF-8):	Pliki nagłówkowe dla slanga
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para slang
Summary(ru.UTF-8):	Библиотеки и хедеры для C-подобного языка S-Lang
Summary(tr.UTF-8):	slang dili için statik kitaplık ve başlık dosyaları
Summary(uk.UTF-8):	Бібліотеки та хедери для C-подібної мови S-Lang
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	libslang1-devel

%description devel
This package contains header files required to develop slang-based
applications. It also includes documentation to help you write
slang-based apps.

%description devel -l de.UTF-8
Dieses Paket enthält Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten
Anwendungen ist enthalten.

%description devel -l es.UTF-8
Este paquete contiene las bibliotecas y archivos de inclusión slang,
necesarios al desarrollo de aplicaciones basadas en slang.

%description devel -l fr.UTF-8
Ce paquetage contient les bibliothèques statiques et les en-têtes
slang pour développer des applications en slang. Il contient aussi la
documentation pour vous aider à écrire ces applications.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe slang. Znajduje się tutaj również
dokumentacja, która pomoże Ci w pisaniu aplikacji pod tę bibliotekę.

%description devel -l pt_BR.UTF-8
Este pacote contém as bibliotecas e arquivos de inclusão slang,
necessárias ao desenvolvimento de aplicações baseadas em slang.

%description devel -l ru.UTF-8
Этот пакет содержит библиотеки и хедеры, необходимые для разработки
программ, использующих Slang.

%description devel -l tr.UTF-8
Bu paket slang tabanlı uygulamalar geliştirmek için gereken başlık
dosyaları ve kitaplıkların yanısıra slang yardım belgelerini de
içerir.

%description devel -l uk.UTF-8
Цей пакет містить бібліотеки та хедери, необхідні для розробки
програм, що використовують Slang.

%package static
Summary:	slang static library
Summary(pl.UTF-8):	Biblioteka statyczna slang
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com slang
Summary(ru.UTF-8):	Статическая библиотека для C-подобного языка S-Lang
Summary(uk.UTF-8):	Статична бібліотека для C-подібної мови S-Lang
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains the slang static libraries.

%description static -l de.UTF-8
Dieses Paket enthält die statischen Libraries.

%description static -l pl.UTF-8
Biblioteka statyczna slang.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com slang.

%description static -l ru.UTF-8
Этот пакет содержит статическую библиотеку, необходимую для разработки
программ, использующих Slang.

%description static -l uk.UTF-8
Цей пакет містить статичну бібліотеку, необхідну для розробки програм,
що використовують Slang.

%package onig
Summary:	Onig module for Slang
Summary(pl.UTF-8):	Moduł Onig dla Slanga
Group:		Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description onig
Onig module for Slang. It support regular expressions using Oniguruma
library.

%description onig -l pl.UTF-8
Moduł Onig dla Slanga. Obsługuje wyrażenia regularne przy użyciu
biblioteki Oniguruma.

%package png
Summary:	PNG module for Slang
Summary(pl.UTF-8):	Moduł PNG dla Slanga
Group:		Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description png
PNG module for Slang.

%description png -l pl.UTF-8
Moduł PNG dla Slanga.

%package pcre
Summary:	PCRE module for Slang
Summary(pl.UTF-8):	Moduł PCRE dla Slanga
Group:		Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description pcre
PCRE module for Slang.

%description pcre -l pl.UTF-8
Moduł PCRE dla Slanga.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

grep -r '#!.*env slsh' -l examples modules/examples slsh/scripts | xargs %{__sed} -i -e '1 s,#!.*env slsh.*,#!/usr/bin/slsh,'

%build
%configure \
	--with-pcre \
	--with-pcreinc=/usr/include/pcre \
	--with-pcrelib=%{_libdir} \
%if %{with onig}
	--with-onig \
	--with-oniginc=/usr/include \
	--with-oniglib=%{_libdir} \
%else
	--without-onig \
%endif
%if %{with png}
	--with-png \
	--with-pnginc=/usr/include/libpng \
	--with-pnglib=%{_libdir} \
%else
	--without-png \
%endif
	--with-zinc=/usr/include \
	--with-zlib=%{_libdir}

%{__make} -j1 elf \
	ELF_CFLAGS="%{rpmcflags} -fPIC"
%{__make} all \
	CFLAGS="%{rpmcflags}"

%{__make} -C slsh \
	DL_LIB="-ldl" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version}/modules,%{_bindir}}

%{__make} install-all -j1 \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples demo src/curses $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a modules/{cmaps,examples,help,*.sl} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/modules

# help rpmdeps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/v2/modules/*.so

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/{slang,slsh}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc slsh/doc/html/*.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/slsh.rc
%attr(755,root,root) %{_bindir}/slsh
%{_datadir}/slsh
%{_mandir}/man1/slsh.1*

%files libs
%defattr(644,root,root,755)
%doc NEWS README changes.txt
%attr(755,root,root) %{_libdir}/libslang.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libslang.so.2
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/v2
%dir %{_libdir}/%{name}/v2/modules
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/base64-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/chksum-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/csv-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/fcntl-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/fork-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/histogram-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/iconv-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/json-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/rand-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/select-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/slsmg-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/socket-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/stats-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/sysconf-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/termios-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/varray-module.so
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/zlib-module.so

%files devel
%defattr(644,root,root,755)
%doc doc/slangdoc.html doc/*.txt doc/text/*.txt
%attr(755,root,root) %{_libdir}/libslang.so
%{_includedir}
%{_pkgconfigdir}/slang.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libslang.a

%if %{with onig}
%files onig
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/onig-module.so
%endif

%if %{with png}
%files png
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/png-module.so
%endif

%files pcre
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/v2/modules/pcre-module.so
