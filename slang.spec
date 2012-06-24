Summary:     shared library for C like extension language
Summary(de): Shared Library f�r eine C-artige Sprache 
Summary(fr): Biblioth�que partag�e pour le langage d'extension C like
Summary(tr): C benzeri dil i�in ortak kitapl�k
Name:        slang
Version:     1.2.2
Release:     1
Copyright:   GPL
Group:       Libraries
Source:      ftp://space.mit.edu/pub/davis/slang/%{name}%{version}.tar.gz
Patch0:      slang-1.2.2-security.patch
URL:         ftp://space.mit.edu/pub/davis/slang/
Buildroot:   /tmp/%{name}-%{version}-root

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

%description -l tr
Slang, C'ye benzer bir yaz�m� olan, g��l�, y���n-tabanl� bir yorumlay�c�d�r.
C'ye benzer oldu�undan Slang ile yaz�lm�� kodlar� C'ye �evirmek olduk�a
kolayd�r.

%package devel
Summary:     header files for slang C like language
Summary(de): Header-Dateien f�r eine Slangvariante der C-Sprache 
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package contains header files required to develop slang-based
applications.  It also includes documentation to help you write slang-based
apps.

%description -l de devel
Dieses Paket enth�lt Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten Anwendungen ist
enthalten.

%package static
Summary:     slang static library
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
This package contains the slang static libraries.

%description -l de static
Dieses Paket enth�lt die statischen Libraries.

%prep
%setup -q -n %{name}
%patch0 -p1
chmod +x configure

%build
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr --includedir=/usr/include/slang
make elf
make

%install
rm -rf $RPM_BUILD_ROOT
make install install-elf prefix=$RPM_BUILD_ROOT/usr \
	install_include_dir=$RPM_BUILD_ROOT/usr/include/slang

mv doc/text/* .

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc {cref,cslang,slang,slangfun,changes}.txt
/usr/lib/libslang.so
/usr/include/slang

%files static
%attr(644, root, root) /usr/lib/libslang.a

%changelog
* Fri Aug 28 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.2-1]
- spec rewrited for using Buildroot,
- added %clean section,
- added using %%{name} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added stripping shared libraries,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Fri Jun 26 1998 Alan Cox <alan@redhat.com>
- Swat another hole. Open TERMINFO files as the real uid not the euid.

* Fri Jun 26 1998 Alan Cox <alan@redhat.com>
- There's a hole in my library Dear Red Hat Dear Red Hat
- Squashed an sprintf arbitary length string into a small bufferon error
  bug.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 18 1998 Erik Troan <ewt@redhat.com>
- rebuilt to find terminfo in /usr/share

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 0.99.38 (will it EVER go 1.0???)
- all patches removed (all appear to be in this version)

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
