# revision 28908
# category Package
# catalog-ctan /macros/latex/contrib/tabvar
# catalog-date 2013-01-22 17:38:01 +0100
# catalog-license lppl1.3
# catalog-version 1.7
Name:		texlive-tabvar
# previous version had two components (1.61)
Epoch:		1
Version:	1.7
Release:	10
Summary:	Typesetting tables showing variations of functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabvar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabvar.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/tabvar/tabvar.afm
%{_texmfdistdir}/fonts/map/dvips/tabvar/tabvar.map
%{_texmfdistdir}/fonts/tfm/public/tabvar/tabvar.tfm
%{_texmfdistdir}/fonts/type1/public/tabvar/tabvar.pfb
%{_texmfdistdir}/metapost/tabvar/tabvar.mp
%{_texmfdistdir}/tex/latex/tabvar/tabvar.1
%{_texmfdistdir}/tex/latex/tabvar/tabvar.2
%{_texmfdistdir}/tex/latex/tabvar/tabvar.3
%{_texmfdistdir}/tex/latex/tabvar/tabvar.cfg
%{_texmfdistdir}/tex/latex/tabvar/tabvar.sty
%doc %{_texmfdistdir}/doc/latex/tabvar/README
%doc %{_texmfdistdir}/doc/latex/tabvar/demo.pdf
%doc %{_texmfdistdir}/doc/latex/tabvar/demo.tex
%doc %{_texmfdistdir}/doc/latex/tabvar/tabvar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tabvar/tabvar.dtx
%doc %{_texmfdistdir}/source/latex/tabvar/tabvar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts metapost tex doc source %{buildroot}%{_texmfdistdir}
