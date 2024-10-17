Name:		texlive-tabvar
# previous version had two components (1.61)
Epoch:		1
Version:	63921
Release:	2
Summary:	Typesetting tables showing variations of functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabvar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package is meant to ease the typesetting of tables
showing variations of functions as they are used in France.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/tabvar
%{_texmfdistdir}/fonts/map/dvips/tabvar
%{_texmfdistdir}/fonts/tfm/public/tabvar
%{_texmfdistdir}/fonts/type1/public/tabvar
%{_texmfdistdir}/metapost/tabvar
%{_texmfdistdir}/tex/latex/tabvar
%doc %{_texmfdistdir}/doc/latex/tabvar
#- source
%doc %{_texmfdistdir}/source/latex/tabvar

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts metapost tex doc source %{buildroot}%{_texmfdistdir}
